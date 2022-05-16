# tokenize.py
#
# The role of a tokenizer is to turn raw text into symbols known as
# tokens.  A token consists of a type and a value.  For example, the
# text "123" is represented as the token ('INTEGER', '123').
#
# The following set of tokens are defined. The suggested name of the
# token is on the left. An example of matching text is on the right.
#
# Reserved Keywords:
#     CONST   : 'const'
#     VAR     : 'var'  
#     PRINT   : 'print'
#     BREAK   : 'break'
#     CONTINUE: 'continue'
#     IF      : 'if'
#     ELSE    : 'else'
#     WHILE   : 'while'
#     FUNC    : 'func'
#     RETURN  : 'return'
#     TRUE    : 'true'
#     FALSE   : 'false'
#
# Identifiers/Names
#     NAME    : Text starting with a letter or '_', followed by any number
#               number of letters, digits, or underscores.
#               Examples:  'abc' 'ABC' 'abc123' '_abc' 'a_b_c'
#
# Literals:
#     INTEGER :  123   (decimal)
#
#     FLOAT   : 1.234
#
#     CHAR    : 'a'     (a single character - byte)
#               '\n'    (newline)
#
# Operators:
#     PLUS     : '+'
#     MINUS    : '-'
#     TIMES    : '*'
#     DIVIDE   : '/'
#     LT       : '<'
#     LE       : '<='
#     GT       : '>'
#     GE       : '>='
#     EQ       : '=='
#     NE       : '!='
#     LAND     : '&&'     (logical and, not bitwise)
#     LOR      : '||'     (logical or, not bitwise)
#     LNOT     : '!'      (logical not, not bitwise)
#    
# Miscellaneous Symbols
#     ASSIGN   : '='
#     SEMI     : ';'
#     LPAREN   : '('
#     RPAREN   : ')'
#     LBRACE   : '{'
#     RBRACE   : '}'
#     COMMA    : ','
#
# Comments:  To be ignored
#      //             Skips the rest of the line
#      /* ... */      Skips a block (no nesting allowed)
#
# Errors: Your lexer may optionally recognize and report errors
# related to bad characters, unterminated comments, and other problems.
# ----------------------------------------------------------------------

# Class that represents a token
class Token:
    def __init__(self, type, value, lineno, index):
        self.type = type
        self.value = value
        self.lineno = lineno   
        self.index = index

    def __repr__(self):
        return f'Token({self.type!r}, {self.value!r}, {self.lineno}, {self.index})'

# High level function that takes an input program and turns it into
# tokens.  This might be a natural place to use some kind of generator
# function or iterator.

def tokenize(program):
    lineno = 1
    n = 0
    text = program.source
    while n < len(text):
        ...
        # Emit tokens using yield
        ...
        print(f'{lineno}: Illegal character {text[n]!r}')
        n += 1
        
    # Emit an EOF token at the end to signal end of input
    yield Token('EOF', 'EOF', lineno, n)

# Main program to test on input files
def main(filename):
    from .program import Program
    program = Program.from_file(filename)
    for tok in tokenize(program):
        print(tok)

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python3 -m wabbit.tokenize filename")
    main(sys.argv[1])

    
            
        

            
    
