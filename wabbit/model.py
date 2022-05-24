# model.py
#
# This file defines the data model for Wabbit programs.  The data
# model is a data structure that represents the contents of a program
# as objects, not text.  Sometimes this structure is known as an
# "abstract syntax tree" or AST.  However, the model is not
# necessarily a direct representation of the syntax of the language.
# So, we'll prefer to think of it as a more generic data model
# instead.
#
# To do this, you need to identify the different "elements" that make
# up a program and encode them into classes.  To do this, it may be
# useful to slightly "underthink" the problem. To illustrate, suppose
# you wanted to encode the idea of "assigning a value."  Assignment
# involves a location (the left hand side) and a value like this:
#
#         location = expression;
#
# To represent this idea, maybe you make a class with just those parts:
#
#     class Assignment:
#         def __init__(self, location, expression):
#             self.location = location
#             self.expression = expression
#
# Alternatively, maybe you elect to store the information in a tuple:
#
#    def Assignment(location, expression):
#        return ('assignment', location, expression)
#
# What are "location" and "expression"?  Does it matter? Maybe
# not. All you know is that an assignment operator definitely requires
# both of those parts.  DON'T OVERTHINK IT.  Further details will be
# filled in as the project evolves.
# 
# Work on this file in conjunction with the top-level
# "test_models.py" file.  Go look at that file and see what program
# samples are provided.  Then, figure out what those programs look
# like in terms of data structures.
#
# There is no "right" solution to this part of the project other than
# the fact that a program has to be represented as some kind of data
# structure that's not "text."   You could use classes. You could use 
# tuples. You could make a bunch of nested dictionaries like JSON. 
# The key point: it must be a data structure.
#
# Starting out, I'd advise against making this file too fancy. Just
# use basic data structures. You can add usability enhancements later.
# -----------------------------------------------------------------------------

# The following classes are used for the expression example in test_models.py.
# Feel free to modify as appropriate.  You don't even have to use classes
# if you want to go in a different direction with it.

class Node:
    pass

class Expression(Node):
    pass

class Statement(Node):
    pass

class Integer(Expression):
    '''
    Example: 42
    '''
    def __init__(self, value):
        assert isinstance(value, str), value
        self.value = value

    def __repr__(self):
        return f'Integer({self.value})'

class Float(Expression):
    '''
    Example: 3.0
    '''
    def __init(self, value):
        assert isinstance(value, str), value
        self.value = value

    def __repr__(self):
        return f'Float({self.value})'

class Bool(Expression):
    '''
    Example: false, true
    '''
    def __init__(self, value):
        assert value in {'true', 'false'}, value
        self.value = value

    def __repr__(self):
        return f'Bool({self.value})'
    
class Op:
    '''
    Example: *, +, -. /
    '''
    def __init__(self,symbol):
        self.symbol = symbol
    
    def __repr__(self):
        return f'Op({self.symbol})'

class BinOp:
    '''
    Example: left + right
    '''
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

    def __repr__(self):
        return f'BinOp({self.op}, {self.left}, {self.right})'

class UnaryOp:
    '''
    Example: -operand
    '''
    def __init__(self, op, operand):
        self.op = op
        self.operand = operand
    
    def __repr__(self):
        return f'UnaryOp({self.op}, {self.operand})'

class PrintStatement:
    '''
    Example: print 2
    '''
    def __init__(self, value):
        self.value = value  
    def __repr__(self):
        return f'PrintStatement({self.value})'


# -----------------------------------------------------------------------------
# Debugging function to convert a model back into source code (for easier viewing)
#
# Special challenge: Write this function in a way so that it produces
# the output code with nice formatting such as having different indentation
# levels in "if" and "while" statements.

def to_source(program):
    # Top-level function that makes source from a Program instance.
    return node_as_source(program.model)

def node_as_source(node):
    # Low-level function that makes source from different kinds of model nodes.
    if isinstance(node, Integer):
        return str(node.value)
    
    elif isinstance(node, Op):
        return str(node.symbol)

    elif isinstance(node, BinOp):
        return f'{node_as_source(node.left)} {node_as_source(node.op)} {node_as_source(node.right)}'

    elif isinstance(node, UnaryOp):
        return f'{node_as_source(node.op)}{node_as_source(node.operand)}'

    elif isinstance(node, PrintStatement):
        return f'{node_as_source(node.value)}'
    
    elif isinstance(node, list):
        return ''.join(node_as_source(n) for n in node)

    else:
        raise RuntimeError(f"Can't convert {node} to source")



    
