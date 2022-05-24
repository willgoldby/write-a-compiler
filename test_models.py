# test_models.py
#
# Within the bowels of your compiler, you need to represent programs
# as a data structure.  Sometimes this is known as an "Abstract Syntax
# Tree" or AST.  In this file, you will manually encode some simple
# Wabbit programs using the data model you're creating in the file
# wabbit/model.py
#
# The purpose of this is two-fold:
#
#   1. Make sure you understand the internal data structures
#      used by the compiler. You will need this to do everything else.
#
#   2. Have some program structures that you can use for later testing,
#      debugging, and experimentation.
#
# This file is broken into sections. Follow the instructions for
# each part.  Parts of this file might be referenced in later
# parts of the project.  Plan to have a lot of discussion.
#
# Also, these examples don't cover every possible language feature.
# More exhaustive testing becomes easier once you have the parser
# working.

from wabbit.model import *
from wabbit.program import Program

# ----------------------------------------------------------------------
# A simple Expression
#
# This one is given to you as an example. You might need to adapt it
# according to the names/classes you defined in wabbit/model.py.

print("--- Simple Expression")

# Programs are provided by a user as "source code" text
expr = Program("2 + 3 * 4")

# Programs are represented by a data structure.  For example:
expr.model  = BinOp(Op('+'), Integer('2'),
                         BinOp(Op('*'), Integer('3'), Integer('4')))

# The following operation tries to turn the model representation back into
# source code.  It's defined in the file wabbit/model.py.

# Uncomment:
print(to_source(expr))

# ----------------------------------------------------------------------
# Program 1: Printing
#
# Encode the following program which tests printing and evaluates some
# simple expressions using Wabbit's core math operators.
#

print('--- Program 1')

program1 = Program("""
    print 2;
    print 2 + 3;
    print -2 + 3;
    print 2 + 3 * -4;
    print (2 + 3) * -4;
    print 2.0 - 3.0 / -4.0;
""")

program1.model = [
    PrintStatement(Integer('2')),
    PrintStatement(BinOp(Op('+'), Integer('2'), Integer('3')))]
    

print(to_source(program1))

# ----------------------------------------------------------------------
# Program 2: Variable and constant declarations. 
#            Expressions and assignment.
#
# Encode the following statements.

print('--- Program 2')

program2 = Program("""
    const pi = 3.14159;
    const tau = 2.0 * pi;
    var radius = 4.0;
    var perimeter float;
    perimeter = tau * radius;
    print perimeter;    // Should produce 25.13272
""")

program2.model = None

print(to_source(program2))

# ----------------------------------------------------------------------
# Program 3: Relations.  You have to be able to compare values.

print('--- Program 3')

program3 = Program('''
    // Each statement below prints "true"
    print 1 == 1;
    print 0 < 1;
    print 0 < 1 < 2;
    print true || (1/0 == 0);
''')

program3.model = None
# print(to_source(program3))

# ----------------------------------------------------------------------
# Program 4: Conditionals.  This program prints out the minimum
# value of two variables.

print('--- Program 4')

program4 = Program('''
    var a int = 2;
    var b int = 3;
    var minval int;
    if a < b {
        minval = a;
    } else {
        minval = b;
    }
    print minval;   // Should print 2
''')

program4.model = None
# print(to_source(program4))

# ----------------------------------------------------------------------
# Program 5: Loops.  This program prints out the first 10 factorials.

print('--- Program 5')

program5 = Program('''
    const n = 10;
    var x int = 1;
    var fact int = 1;

    while x < n {
        fact = fact * x;
        x = x + 1;
        print fact;
    }
''')

program5.model = None
# print(to_source(program5))

# -----------------------------------------------------------------------------
# Program 6: Break/continue.  This program changes loop control flow

print('--- Program 6')

program6 = Program('''
    var n = 0;
    while true {
        if n == 2 {
            print n;
            break;
        } else {
            n = n + 1;
            continue;
        }
        n = n - 1;   // Should never execute
    }
''')
program6.model = None
# print(to_source(program6))

# ----------------------------------------------------------------------
# Program 7: Compound Expressions.  This program swaps the values of
# two variables using a single expression.
#
# A compound expression is a series of statements/expressions enclosed
# in { ... }.  The value of a compound expression is the value represented
# by the last operation. 

print('--- Program 7')

program7 = Program('''
    var x = 37;
    var y = 42;
    x = { var t = y; y = x; t; };  // Compound expression (value is "t")
    print x;   // Prints 42
    print y;   // Prints 37
''')

program7.model = None

# print(to_source(program7))

# ----------------------------------------------------------------------
# Program 8: Functions.  This program tests the basics of function
# calls and returns.  For this, you're going top need to have a number
# features in your model including:
#
#     1. Function definitions.
#     2. Function application (calling a function)
#     3. The return statement.
#

print('--- Program 8')

program8 = Program('''
func add(x int, y int) int {
    return x + y;
}

var result = add(2, 3);
print result;
''')

program8.model = None
# print(to_source(program8))

