# parse.py
#
# Wabbit parser.  The parser needs to construct the data model or an
# abstract syntax tree from text input.  The precise format of Wabbit
# source code is described by a grammar.  The grammar for Wabbit can
# be found in the document docs/Wabbit-Specification.md.
#
# For our purposes, however, it may be easier to work from syntax
# diagrams which can be found in the document docs/WabbitSyntax.pdf.
#
# Our plan for writing the parser is going to proceed in two phases.
#
# Phase 1:  Statements
# --------------------
# In phase 1, we will write all of the parsing code for statements.
# However, we'll restrict expression parsing to only work with a
# single integer value.  Here are examples of statements we'll
# parse in this phase:
#
#      break;
#      continue;
#      print 1;
#      const x = 1;
#      var x int;
#      if 1 { print 2; } else { print 3; }
#      while 1 { print 2; }
#      1;             
#
# Again, expressions will restricted to a single integer value in this
# first part.
#
# Phase 2: Expressions
# --------------------
# One you have everything in phase 1 working, we'll work on expression
# parsing.  Expression parsing is probably the most difficult part of
# writing the parser because expressions need to capture precedence
# rules from math class.  For example, how is the following expression
# parsed?
#
#           2 + 3 * 4 < 30 / 6 - 7
#
# There are essentially different parsing "levels".  For example, to
# evaluate this expression, multiplication and division go first:
#
#            2 + (3 * 4) < (30 / 6) - 7
#            2 + 12 < 5 - 7
#
# Addition and subtraction then go next:
#
#            (2 + 12) < (5 - 7)
#              14     <   -2
#
# The relation goes last, producing false in this example.
# To make this work, each level of precedence is going to get its
# own parsing rule.
#
# It should be noted that assignment is also an expression.
#
#            x = 2 + 3;
#
# The value of an assignment is the right hand side.  So, statements
# such as this are legal:
#
#            print x = 2 + 3;     // Prints 5, assigns to x.
#
# Assignments can also be chained:
#
#            x = y = 2 + 3;
#
# This is to be interpreted as meaning the following:
#
#            x = (y = 2 + 3);
#
# A plan for testing
# ------------------
# At first, it's going to be difficult to make substantial
# progress.  You'll need to focus on isolated simple statements
# and work your way up to more complicated things as you
# expand to more Wabbit features.
#
# The directory tests/Parser contains a series of parsing tests
# arranged in order of difficulty.  Each test file also contains
# some implementation notes to help guide you.  Thus, start here
# and work your way up to more complicated tests.
#
# Eventually, you should be able to parse programs in the
# test_models.py file.   At this point, you're well on your
# way to parsing real programs.   The directory tests/Programs
# contains actual Wabbit programs that you can try.
#
# If you're feeling lucky, modify your interpreter to read source
# code, parse it, and run it.   Try your interpreter by running
# it on various programs in the tests/Programs directory.


from .model import *
from .tokenize import tokenize

# Top-level function that runs everything.  You'll need to modify
# this part to integrate with your tokenizer and representation of
# source code.  Also,
def parse_program(program):
    tokens = tokenize(program)
    # One challenge. How do you encapsulate the token stream in a way that
    # it can be used to write the rest of the parser?  What do you pass
    # as an argument to the various functions below?
    program.model = parse_source()
    return program.model

def parse_source():
    # Code this to recognize any Wabbit program and return the model.
    # How do you modify this to parse multiple statements?
    model = statement()
    expect('EOF')
    return model

def parse_statement():
    # Parse any Wabbit statement.  How do you modify this to recognize more
    # than one statement kind?
    return parse_break_statement()

def parse_break_statement():
    # Example of parsing a simple statement (pseudocode).  You work left-to-right
    # over the expected tokens and return a model node upon success.
    expect('BREAK')
    expect('SEMI')
    return BreakStatement()

def parse_expression():
    # For phase 1, only make this recognize integers.
    tok = expect('INTEGER')      # Pseudocode
    return Integer(tok.value)    # Pseudocode (adjust to your model)

    # For phase 2, expand this to cover more complex expression types

# Example of a main program
def parse_file(filename):
    from .program import Program
    program = Program.from_file(filename)
    parse_program(program)
    return program

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        raise SystemExit('Usage: python3 -m wabbit.parse filename')
    program = parse_file(sys.argv[1])
    print(program.model)


