"""
PL/0 Lexical Analyzer Core Implementation
Implemented using the loop-branch method
"""

from token_type import TokenType, KEYWORDS
from token import Token


class PL0Lexer:
    """
    PL/0 Lexical Analyzer
    
    Functions:
    1. Reads PL/0 source program
    2. Identifies all tokens (keywords, identifiers, constants, operators, delimiters)
    3. Detects lexical errors
    4. Outputs token sequence to a file
    """
    
    def __init__(self, source_code):
        """
        Initialize the lexical analyzer
        
        :param source_code: PL/0 source program string
        """
        self.source = source_code       # Source code
        self.pos = 0                    # Current position pointer
        self.line = 1                   # Current line number
        self.column = 0                 # Current column number
        self.current_char = None        # Current character
        self.tokens = []                # Token list
        self.errors = []                # Error list
        
        # Read the first character
        self.get_char()
    
    # GetChar()
    
    def get_char(self):
        """
        GetChar() - Read the next character
        
        Functions:
        1. Reads the next character
        2. Updates the position pointer
        3. Updates line and column numbers
        """
        if self.pos < len(self.source):
            self.current_char = self.source[self.pos]
            self.pos += 1
            self.column += 1
            
            # If newline is encountered, increment line number and reset column
            if self.current_char == '\n':
                self.line += 1
                self.column = 0
        else:
            self.current_char = None  # End of file
        
        return self.current_char
    
    def peek(self, offset=1):
        """
        Look ahead at a character without moving the position pointer
        
        :param offset: Look-ahead offset
        :return: The character seen, or None if out of range
        """
        peek_pos = self.pos + offset - 1
        if peek_pos < len(self.source):
            return self.source[peek_pos]
        return None
    
    # Helper judgment methods
    
    def is_letter(self, char):
        """Check if the character is a letter"""
        return char is not None and char.isalpha()
    
    def is_digit(self, char):
        """Check if the character is a digit"""
        return char is not None and char.isdigit()
    
    def is_whitespace(self, char):
        """Check if the character is a whitespace (space, tab, newline, etc.)"""
        return char is not None and char.isspace()
    
    # Error handling
    
    def add_error(self, message, line, column):
        """
        Record a lexical error
        
        :param message: Error message
        :param line: Line where the error occurred
        :param column: Column where the error occurred
        """
        error_msg = f"Lexical error (line {line}, column {column}): {message}"
        self.errors.append(error_msg)
    
    # Skip whitespace and comments
    
    def skip_whitespace(self):
        """Skip whitespace characters (space, tab, newline, etc.)"""
        while self.is_whitespace(self.current_char):
            self.get_char()
    
    def skip_comment(self):
        """
        Skip comments
        Supports two comment formats:
        1. {comment content}
        2. (*comment content*)
        """
        # Handle {comment}
        if self.current_char == '{':
            start_line = self.line
            start_column = self.column
            self.get_char()  # Skip {
            
            while self.current_char and self.current_char != '}':
                self.get_char()
            
            if self.current_char == '}':
                self.get_char()  # Skip }
            else:
                self.add_error("Unclosed comment, missing '}'", start_line, start_column)
        
        # Handle (*comment*)
        elif self.current_char == '(' and self.peek() == '*':
            start_line = self.line
            start_column = self.column
            self.get_char()  # Skip (
            self.get_char()  # Skip *
            
            while self.current_char:
                if self.current_char == '*' and self.peek() == ')':
                    self.get_char()  # Skip *
                    self.get_char()  # Skip )
                    break
                self.get_char()
            else:
                self.add_error("Unclosed comment, missing '*)'", start_line, start_column)
    
    # Identify identifiers or keywords (corresponding to Figure 3.4(a))
    
    def scan_identifier(self, start_line, start_column):
        """
        Identify identifiers or keywords
        
        State transition diagram:
        State 1 (start) --letter--> State 2 (accept)
        State 2 --letter|digit--> State 2 (loop)
        State 2 --other--> End
        
        :param start_line: Starting line number
        :param start_column: Starting column number
        :return: Token object
        """
        token_str = ''
        
        # Read sequence of letters and digits
        while self.is_letter(self.current_char) or self.is_digit(self.current_char):
            token_str += self.current_char
            self.get_char()
        
        # Reserve table lookup: Check if it is a keyword
        token_str_lower = token_str.lower()
        if token_str_lower in KEYWORDS:
            # It is a keyword, return keyword Token
            token_type = KEYWORDS[token_str_lower]
            return Token(token_type, token_str, start_line, start_column)
        else:
            # It is an identifier, return ID Token
            # Corresponds to InsertId(strToken) on page 45 of the textbook
            return Token(TokenType.ID, token_str, start_line, start_column)
    
    # Identify integers (corresponding to Figure 3.4(a))
    
    def scan_number(self, start_line, start_column):
        """
        Identify integer constants
        
        State transition diagram:
        State 1 (start) --digit--> State 2 (accept)
        State 2 --digit--> State 2 (loop)
        State 2 --other--> End
        
        :param start_line: Starting line number
        :param start_column: Starting column number
        :return: Token object or error Token
        """
        num_str = ''
        
        # Read sequence of digits
        while self.is_digit(self.current_char):
            num_str += self.current_char
            self.get_char()
        
        # Error check: A letter cannot follow a number directly
        if self.is_letter(self.current_char):
            error_str = num_str
            # Read all subsequent alphanumeric characters
            while self.is_letter(self.current_char) or self.is_digit(self.current_char):
                error_str += self.current_char
                self.get_char()
            
            self.add_error(f"Letter cannot directly follow a number: {error_str}", start_line, start_column)
            return Token(TokenType.ERROR, error_str, start_line, start_column)
        
        # Normal case: Convert to integer and return
        # InsertConst(strToken)
        int_value = int(num_str)
        return Token(TokenType.INT, int_value, start_line, start_column)
    
    # Identify operators and delimiters
    
    def scan_operator(self, start_line, start_column):
        """
        Identify operators and delimiters
        
        Handles:
        1. Single-character operators: + - * / = ( ) ; ,
        2. Two-character operators: := <> <= >=
        
        :param start_line: Starting line number
        :param start_column: Starting column number
        :return: Token object
        """
        char = self.current_char
        
        # Handle := (assignment operator)
        if char == ':':
            self.get_char()
            if self.current_char == '=':
                self.get_char()
                return Token(TokenType.ASSIGN, ':=', start_line, start_column)
            else:
                # Error: Standalone : is invalid
                self.add_error(f"Illegal character ':', expected ':='", start_line, start_column)
                return Token(TokenType.ERROR, ':', start_line, start_column)
        
        # Handle < <= <>
        elif char == '<':
            self.get_char()
            if self.current_char == '=':
                self.get_char()
                return Token(TokenType.LEQ, '<=', start_line, start_column)
            elif self.current_char == '>':
                self.get_char()
                return Token(TokenType.NEQ, '<>', start_line, start_column)
            else:
                return Token(TokenType.LT, '<', start_line, start_column)
        
        # Handle > >=
        elif char == '>':
            self.get_char()
            if self.current_char == '=':
                self.get_char()
                return Token(TokenType.GEQ, '>=', start_line, start_column)
            else:
                return Token(TokenType.GT, '>', start_line, start_column)
        
        # Handle single-character operators and delimiters
        single_char_tokens = {
            '+': TokenType.PLUS,
            '-': TokenType.MINUS,
            '*': TokenType.TIMES,
            '/': TokenType.DIVIDE,
            '=': TokenType.EQ,
            '(': TokenType.LPAREN,
            ')': TokenType.RPAREN,
            ';': TokenType.SEMICOLON,
            ',': TokenType.COMMA
        }
        
        if char in single_char_tokens:
            self.get_char()
            return Token(single_char_tokens[char], char, start_line, start_column)
        
        # Unrecognized character
        self.add_error(f"Illegal character: '{char}'", start_line, start_column)
        self.get_char()
        return Token(TokenType.ERROR, char, start_line, start_column)
    
    # Get the next token (main loop)
    
    def get_next_token(self):
        """
        Get the next token
        
        1. GetChar()
        2. Skip whitespace and comments
        3. Process based on character type:
           - Letter: scan_identifier()
           - Digit: scan_number()
           - Other: scan_operator()
        4. Return Token
        
        :return: Token object
        """
        while self.current_char:
            # Skip whitespace characters
            if self.is_whitespace(self.current_char):
                self.skip_whitespace()
                continue
            
            # Skip comments
            if self.current_char == '{' or (self.current_char == '(' and self.peek() == '*'):
                self.skip_comment()
                continue
            
            # Record token starting position
            start_line = self.line
            start_column = self.column
            
            # Identify identifier or keyword
            if self.is_letter(self.current_char):
                return self.scan_identifier(start_line, start_column)
            
            # Identify number
            if self.is_digit(self.current_char):
                return self.scan_number(start_line, start_column)
            
            # Identify operators and delimiters
            return self.scan_operator(start_line, start_column)
        
        # End of file
        return Token(TokenType.EOF, None, self.line, self.column)
    
    # Perform lexical analysis on the entire source code
    
    def tokenize(self):
        """
        Perform lexical analysis on the entire source code
        Generate the complete token sequence
        
        :return: Token list
        """
        self.tokens = []
        while True:
            token = self.get_next_token()
            self.tokens.append(token)
            if token.type == TokenType.EOF:
                break
        return self.tokens
    
    # Output to file
    
    def output_to_file(self, filename='tokens.txt'):
        """
        Output the token sequence to an intermediate file
        
        :param filename: Output file name
        """
        with open(filename, 'w', encoding='utf-8') as f:
            # Header
            f.write("=" * 80 + "\n")
            f.write("PL/0 Lexical Analysis Results\n")
            f.write("=" * 80 + "\n\n")
            
            # Token list
            f.write(f"{'Index':<6} {'Line':<6} {'Column':<6} {'Type':<15} {'Value':<20}\n")
            f.write("-" * 80 + "\n")
            
            for idx, token in enumerate(self.tokens, 1):
                if token.type != TokenType.EOF:
                    f.write(f"{idx:<6} {token.line:<6} {token.column:<6} "
                           f"{token.type:<15} {str(token.value):<20}\n")
            
            f.write("\n" + "=" * 80 + "\n")
            
            # Error information
            if self.errors:
                f.write("\nError List:\n")
                f.write("-" * 80 + "\n")
                for error in self.errors:
                    f.write(error + "\n")
                f.write(f"\nFound {len(self.errors)} errors in total.\n")
            else:
                f.write("\nLexical analysis completed, no errors.\n")
            
            f.write("\n" + "=" * 80 + "\n")
    
    # Statistical information
    
    def get_statistics(self):
        """
        Get lexical analysis statistics
        
        :return: Statistics dictionary
        """
        stats = {
            'total_tokens': len(self.tokens) - 1,  # Exclude EOF
            'keywords': 0,
            'identifiers': 0,
            'integers': 0,
            'operators': 0,
            'delimiters': 0,
            'errors': len(self.errors)
        }
        
        for token in self.tokens:
            if token.type in [TokenType.PROGRAM, TokenType.CONST, TokenType.VAR, 
                            TokenType.PROCEDURE, TokenType.BEGIN, TokenType.END,
                            TokenType.IF, TokenType.THEN, TokenType.ELSE,
                            TokenType.WHILE, TokenType.DO, TokenType.CALL,
                            TokenType.READ, TokenType.WRITE, TokenType.ODD]:
                stats['keywords'] += 1
            elif token.type == TokenType.ID:
                stats['identifiers'] += 1
            elif token.type == TokenType.INT:
                stats['integers'] += 1
            elif token.type in [TokenType.PLUS, TokenType.MINUS, TokenType.TIMES, 
                              TokenType.DIVIDE, TokenType.EQ, TokenType.NEQ,
                              TokenType.LT, TokenType.LEQ, TokenType.GT, TokenType.GEQ,
                              TokenType.ASSIGN]:
                stats['operators'] += 1
            elif token.type in [TokenType.LPAREN, TokenType.RPAREN, 
                              TokenType.SEMICOLON, TokenType.COMMA]:
                stats['delimiters'] += 1
        
        return stats