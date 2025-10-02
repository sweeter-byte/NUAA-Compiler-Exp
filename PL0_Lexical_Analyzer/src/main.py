"""
PL/0 Lexical Analyzer Main Program
Provides a command-line interface
"""

import sys
import os
from lexer import PL0Lexer
from token_type import TokenType


def print_header():
    """Print the program title"""
    print("=" * 80)
    print(" " * 28 + "PL/0 Lexical Analyzer")
    print("=" * 80)


def print_usage():
    """Print usage instructions"""
    print("\nUsage:")
    print("  python main.py <source_file_path> [output_file_path]")
    print("\nExamples:")
    print("  python main.py ../tests/test_cases/test1_basic.pl0")
    print("  python main.py ../tests/test_cases/test1_basic.pl0 ../output/result.txt")
    print("\nNotes:")
    print("  - Source file path: Required parameter, PL/0 source program file")
    print("  - Output file path: Optional parameter, token sequence output file (defaults to output/ directory)")


def read_source_file(filepath):
    """
    Read the source program file
    
    :param filepath: File path
    :return: Source code string, returns None on failure
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"\n Error: File '{filepath}' does not exist!")
        return None
    except Exception as e:
        print(f"\n Error: Failed to read file - {e}")
        return None


def print_source_code(source_code):
    """Print the source program"""
    print("\n Source Code Content:")
    print("-" * 80)
    
    # Add line numbers
    lines = source_code.split('\n')
    for i, line in enumerate(lines, 1):
        print(f"{i:3d} | {line}")
    
    print("-" * 80)


def print_tokens(tokens):
    """Print the token list"""
    print(f"\n Identified {len(tokens)-1} Tokens:\n")
    print(f"{'Index':<6} {'Line':<6} {'Column':<6} {'Type':<15} {'Value':<20}")
    print("-" * 80)
    
    for idx, token in enumerate(tokens, 1):
        if token.type != TokenType.EOF:
            value_str = str(token.value)
            if len(value_str) > 20:
                value_str = value_str[:17] + "..."
            print(f"{idx:<6} {token.line:<6} {token.column:<6} "
                  f"{token.type:<15} {value_str:<20}")


def print_statistics(stats):
    """Print statistical information"""
    print("\n Statistical Information:")
    print("-" * 80)
    print(f"  Total Tokens:    {stats['total_tokens']}")
    print(f"  Keywords:       {stats['keywords']}")
    print(f"  Identifiers:    {stats['identifiers']}")
    print(f"  Integers:       {stats['integers']}")
    print(f"  Operators:      {stats['operators']}")
    print(f"  Delimiters:     {stats['delimiters']}")
    print(f"  Errors:         {stats['errors']}")
    print("-" * 80)


def print_errors(errors):
    """Print error information"""
    if errors:
        print(f"\n Found {len(errors)} Errors:")
        print("-" * 80)
        for error in errors:
            print(f"  {error}")
        print("-" * 80)
    else:
        print("\n Lexical analysis completed, no errors.")


def main():
    """Main function"""
    # Print title
    print_header()
    
    # Check command-line arguments
    if len(sys.argv) < 2:
        print_usage()
        return 1
    
    input_file = sys.argv[1]
    
    # Determine output file path
    if len(sys.argv) >= 3:
        output_file = sys.argv[2]
    else:
        # Default output file: output/source_filename_tokens.txt
        base_name = os.path.splitext(os.path.basename(input_file))[0]
        output_dir = os.path.join(os.path.dirname(__file__), '..', 'output')
        output_file = os.path.join(output_dir, f"{base_name}_tokens.txt")
    
    # Read source program
    print(f"\n Reading source file: {input_file}")
    source_code = read_source_file(input_file)
    
    if source_code is None:
        return 1
    
    # Display source program
    print_source_code(source_code)
    
    # Create lexical analyzer
    print("\n Starting lexical analysis...")
    lexer = PL0Lexer(source_code)
    
    # Perform lexical analysis
    tokens = lexer.tokenize()
    
    # Display token list
    print_tokens(tokens)
    
    # Display statistical information
    stats = lexer.get_statistics()
    print_statistics(stats)
    
    # Display error information
    print_errors(lexer.errors)
    
    # Output to file
    try:
        # Ensure output directory exists
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        
        lexer.output_to_file(output_file)
        print(f"\n Results have been output to file: {output_file}")
    except Exception as e:
        print(f"\n Failed to output file: {e}")
        return 1
    
    # Return status code
    print("\n" + "=" * 80)
    if lexer.errors:
        print(f"  Lexical analysis completed, but found {len(lexer.errors)} errors")
        return 1
    else:
        print("  Lexical analysis successfully completed!")
        return 0


if __name__ == "__main__":
    sys.exit(main())