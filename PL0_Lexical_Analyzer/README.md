# PL/0 Lexical Analyzer

## Project Introduction
This project implements a lexical analyzer for the PL/0 language, completed using the loop-branch method.

## Functional Features
- Recognizes 15 keywords (program, const, var, procedure, begin, end, if, then, else, while, do, call, read, write, odd)
- Recognizes identifiers and integer constants
- Recognizes all operators (+, -, *, /, =, <>, <, <=, >, >=)
- Recognizes delimiters ((, ), ;, ,, :=)
- Error detection and precise positioning (line number, column number)
- Outputs token sequence to an intermediate file

## Environment Requirements
- Python 3.6 or higher
- No additional dependency packages required

## Running Method

### Method 1: Using Command Line Arguments
```bash
cd src
python main.py ../tests/test_cases/test1_basic.pl0
```

### Method 2: Interactive Execution
```bash
cd src
python main.py
# Then follow the prompts to enter the file path
```

## File Description
```text
├── README.md                   # This file
├── src/                        # Source code
│   ├── token_type.py           # Token type definitions
│   ├── token.py                # Token class
│   ├── lexer.py                # Lexical analyzer
│   └── main.py                 # Main program
├── tests/                      # Test directory
│   └── test_cases/             # Test cases
└── output/                     # Output results
```

## Test Cases
- **test1_basic.pl0**: Basic functionality test
- **test2_expression.pl0**: Expression test
- **test3_procedure.pl0**: Procedure declaration test
- **test4_error.pl0**: Error detection test
- **test5_complex.pl0**: Complex program test

## Output Format
The lexical analyzer will generate a token sequence file containing the following information:
- Sequence number
- Line number
- Column number
- Token type
- Token value

## Error Handling
The program can detect the following lexical errors:
1. Illegal characters
2. Letter immediately following a number
3. Standalone colon (should be :=)
4. Unclosed comment

## Author Information
- Name: Ran Maoyin
- Student ID: 162350107
- Class: 1623001
- Date: October 2, 2025

## References
- Compiler Principles Textbook, pages 45-46
- PL/0 Language BNF Description
