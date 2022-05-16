# interp.py
#
# In order to write a compiler for a programming language, it helps to
# have some kind of understanding of how programs written in the
# programming language are actually supposed to work. A language is
# more than just "syntax" or a data model.  There have to be some kind
# of semantics that describe what happens when a program in the
# language executes.
#
# One way to specify the semantics is to write a so-called
# "definitional interpreter" that directly executes the data
# model. This might seem like cheating--after all, our final goal is
# not to write an interpreter, but a compiler. However, if you can't
# write an interpreter, chances are you can't write a compiler either.
# So, the purpose of doing this is to pin down fine details as well as
# our overall understanding of what needs to happen when programs run.
# Writing an interpreter will also help understand things that are
# *NOT* supposed to happen (i.e., programming errors).
#
# The process of writing an interpreter is mostly straightforward.
# You'll write a top-level function called "interpret()". 
# For each class in the model.py file, you'll then write a 
# a conditional check and some code that executes the model:
#
#    def interpret(node, context):
#        ...
#        if isinstance(node, ModelClass):
#            # Execute "node" in the environment "context"
#            ...
#            return (result_type, result_value)
#        ...
#   
# The input to the interpret() will be an object from model.py (node)
# along with an object respresenting the execution environment
# (context).  In executing the node, the environment might be
# modified (for example, when executing assignment expressions,
# making variable definitions, etc.).  The return result will
# consist of a type along with a value.   These types and values
# are from Wabbit, not Python.   For example, a result might 
# look like ('int', 34) or ('float', 3.4).
#
# In addition to executing the code, you should try to check for
# as many programming errors as possible.   For example, Wabbit
# does NOT allow mixed-type operations (e.g., 2 + 3.5 is a type
# error).   If you encounter an error, have your interpreter
# stop with a RuntimeError exception.  Better yet, have it produce
# a nice error message that indicates exactly what's wrong.
#
# For testing, try running your interpreter on the models you
# created in the test_models.py file.   Verify that their output
# is what you expect it to be.   Later, when you have written
# a parser, you should continue to check your interpreter against
# various programs in the tests/Programs/ directory.
#
# The most difficult parts of writing the interpreter concern
# unusual control flow.  For example, the handling of "break"
# and "continue" statements inside a while loop. 
#
# The handling of function calls is tricky.  For functions,
# you need to worry about the delicate matter of variable scoping.
# Specifically, each call to a function needs to create a new
# environment in which local variables created inside that function
# can live.  Moreover, the function still needs to be able to
# access variables defined in the global scope. To do this,
# you'll probably need multiple dictionaries.  You'll need to
# link those dictionaries together in some manner.

from .model import *

# Class representing the execution environment of the interpreter.
class Context:
    def __init__(self):
        self.env = { }          # Storage of variables
    
# Top level function that interprets an entire program. It creates the
# initial environment that's used for storing variables.
def interpret_program(program):
    # Make the initial environment (a dict).  The environment is
    # where you will create and store variables.
    context = Context()
    return interpret_node(program.model, context)


# Internal function to interpret a node in the environment.  You need
# to expand to cover all of the node classes in the model.py file. 
def interpret_node(node, context):
    if isinstance(node, Integer):
        return ('int', node.value)     # All values should be tagged a type

    elif isinstance(node, Float):
        return ('float', node.value)

    elif isinstance(node, BinOp):
        # Note: all values are tagged with a Wabbit type.
        # See the code for "Integer" and "Float" above.
        # Knowing the type is essential for type-checking.
        left_type, left_value = interpret_node(node.left, context)
        right_type, right_value = interpret_node(node.right, context)
        if left_type != right_type:
            raise RuntimeError("Type error in binary operator")
        if left_type in {'int', 'float'}:
            if node.op == '+':
                return (left_type, left_value + right_value)
            elif node.op == '-':
                return (left_type, left_value - right_value)
            ...
        raise RuntimeError(f"Unsupported operation {node.op}")
            
    elif isinstance(node, PrintStatement):
        valuetype, value = interpret_node(node.value, context)
        # The type is useful if you need to carry out special processing.
        if valuetype == 'char':
            print(value, end='')
        elif valuetype == 'bool':
            print('true' if value else 'false')
        else:
            print(value)
        
    # Expand to check for different node types
    else:
        raise RuntimeError(f"Can't interpret {node}")
                             
                             

        
        
        
