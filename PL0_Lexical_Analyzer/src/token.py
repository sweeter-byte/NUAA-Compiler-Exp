"""
Token Class Definition
Represents a lexical unit (Token)
"""


class Token:
    """
    Token Class: Represents a single token in the source program
    
    return(code, value)
    
    Attributes:
        type (str): Token type (code)
        value: Token value (value)
        line (int): Line number
        column (int): Column number
    """
    
    def __init__(self, token_type, value, line, column):
        """
        Initialize a Token
        
        :param token_type: Token type (from TokenType class)
        :param value: Token value (identifier name, integer value, operator symbol, etc.)
        :param line: Line number (starting from 1)
        :param column: Column number (starting from 1)
        """
        self.type = token_type
        self.value = value
        self.line = line
        self.column = column
    
    def __str__(self):
        """
        String representation of the Token
        Format: <type, value, line, column>
        """
        return f"<{self.type}, {self.value}, line{self.line}, column{self.column}>"
    
    def __repr__(self):
        """
        Debug representation of the Token
        """
        return self.__str__()
    
    def __eq__(self, other):
        """
        Check if two Tokens are equal
        """
        if not isinstance(other, Token):
            return False
        return (self.type == other.type and 
                self.value == other.value and
                self.line == other.line and
                self.column == other.column)
    
    def to_dict(self):
        """
        Convert Token to dictionary format
        Facilitates JSON serialization
        
        :return: Token in dictionary format
        """
        return {
            'type': self.type,
            'value': self.value,
            'line': self.line,
            'column': self.column
        }
    
    def to_tuple(self):
        """
        Convert Token to tuple format
        
        :return: (type, value, line, column)
        """
        return (self.type, self.value, self.line, self.column)
    
    @classmethod
    def from_dict(cls, data):
        """
        Create a Token object from a dictionary
        
        :param data: Dictionary containing Token information
        :return: Token object
        """
        return cls(
            token_type=data['type'],
            value=data['value'],
            line=data['line'],
            column=data['column']
        )