"""
Token Type Definitions
Defines all token types and keyword table for the PL/0 language
"""


class TokenType:
    """
    Token Type Enumeration
    Each token has a unique type identifier
    """
    
    # Keywords (1-15)
    PROGRAM = 'PROGRAM'          # program
    CONST = 'CONST'              # const
    VAR = 'VAR'                  # var
    PROCEDURE = 'PROCEDURE'      # procedure
    BEGIN = 'BEGIN'              # begin
    END = 'END'                  # end
    IF = 'IF'                    # if
    THEN = 'THEN'                # then
    ELSE = 'ELSE'                # else
    WHILE = 'WHILE'              # while
    DO = 'DO'                    # do
    CALL = 'CALL'                # call
    READ = 'READ'                # read
    WRITE = 'WRITE'              # write
    ODD = 'ODD'                  # odd
    
    # Identifiers and Constants (16-17)
    ID = 'ID'                    # Identifier
    INT = 'INT'                  # Integer constant
    
    # Arithmetic Operators (18-21)
    PLUS = 'PLUS'                # +
    MINUS = 'MINUS'              # -
    TIMES = 'TIMES'              # *
    DIVIDE = 'DIVIDE'            # /
    
    # Relational Operators (22-27)
    EQ = 'EQ'                    # =
    NEQ = 'NEQ'                  # <>
    LT = 'LT'                    # <
    LEQ = 'LEQ'                  # <=
    GT = 'GT'                    # >
    GEQ = 'GEQ'                  # >=
    
    # Delimiters (28-32)
    LPAREN = 'LPAREN'            # (
    RPAREN = 'RPAREN'            # )
    SEMICOLON = 'SEMICOLON'      # ;
    COMMA = 'COMMA'              # ,
    ASSIGN = 'ASSIGN'            # :=
    
    # Special Tokens
    EOF = 'EOF'                  # End of file
    ERROR = 'ERROR'              # Error token


# Reserve Table
KEYWORDS = {
    'program': TokenType.PROGRAM,
    'const': TokenType.CONST,
    'var': TokenType.VAR,
    'procedure': TokenType.PROCEDURE,
    'begin': TokenType.BEGIN,
    'end': TokenType.END,
    'if': TokenType.IF,
    'then': TokenType.THEN,
    'else': TokenType.ELSE,
    'while': TokenType.WHILE,
    'do': TokenType.DO,
    'call': TokenType.CALL,
    'read': TokenType.READ,
    'write': TokenType.WRITE,
    'odd': TokenType.ODD
}


# Token Type Descriptions in Chinese (for output)
TOKEN_DESCRIPTIONS = {
    # Keywords
    TokenType.PROGRAM: 'Keyword-Program',
    TokenType.CONST: 'Keyword-Constant',
    TokenType.VAR: 'Keyword-Variable',
    TokenType.PROCEDURE: 'Keyword-Procedure',
    TokenType.BEGIN: 'Keyword-Begin',
    TokenType.END: 'Keyword-End',
    TokenType.IF: 'Keyword-If',
    TokenType.THEN: 'Keyword-Then',
    TokenType.ELSE: 'Keyword-Else',
    TokenType.WHILE: 'Keyword-While',
    TokenType.DO: 'Keyword-Do',
    TokenType.CALL: 'Keyword-Call',
    TokenType.READ: 'Keyword-Read',
    TokenType.WRITE: 'Keyword-Write',
    TokenType.ODD: 'Keyword-Odd',
    
    # Identifiers and Constants
    TokenType.ID: 'Identifier',
    TokenType.INT: 'Integer',
    
    # Operators
    TokenType.PLUS: 'Plus',
    TokenType.MINUS: 'Minus',
    TokenType.TIMES: 'Times',
    TokenType.DIVIDE: 'Divide',
    
    # Relational Operators
    TokenType.EQ: 'Equal',
    TokenType.NEQ: 'Not Equal',
    TokenType.LT: 'Less Than',
    TokenType.LEQ: 'Less Than or Equal',
    TokenType.GT: 'Greater Than',
    TokenType.GEQ: 'Greater Than or Equal',
    
    # Delimiters
    TokenType.LPAREN: 'Left Parenthesis',
    TokenType.RPAREN: 'Right Parenthesis',
    TokenType.SEMICOLON: 'Semicolon',
    TokenType.COMMA: 'Comma',
    TokenType.ASSIGN: 'Assignment',
    
    # Special
    TokenType.EOF: 'End of File',
    TokenType.ERROR: 'Error'
}


def get_token_description(token_type):
    """
    Get the Chinese description of a token type
    
    :param token_type: Token type
    :return: Chinese description string
    """
    return TOKEN_DESCRIPTIONS.get(token_type, 'Unknown Type')