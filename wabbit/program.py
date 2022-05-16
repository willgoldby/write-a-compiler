# program.py
#
# The input to a compiler is a "Program".  However, compilers are
# complex creatures, consisting of many stages and complex data
# structures.  A central problem is simply keeping everything
# organized.  One way to handle this is to organize everything under a
# top-level "Program" object of some sort.  The program can be a
# container of everything interesting--source code, the model, error
# messages, generated code, and so forth.
#
# We'll use this Program class as the central object that gets
# passed around between different parts of the compiler.  In
# the project, you'll see functions like "tokenize_program",
# "parse_program", "check_program", etc.  These all expect to
# take the Program object as input. 
#
# You can choose to leave this class simple as shown.  However, as
# your compiler evolves, you might want to expand some of its
# functionality--especially as it relates to advanced features such as
# error handling.
        
class Program:
    def __init__(self, source:str):
        self.source = source   
        self.model = None
        self.have_errors = False

    def error_message(self, message:str):
        # Helper method to issue an error message
        print(message)
        self.have_errors = True

    @classmethod
    def from_file(cls, filename:str):
        # Alternate constructor to create from a file
        with open(self.filename) as file:
            return cls(file.read())
