
from typing import NamedTuple
import re
import re



class Token(NamedTuple):
    # If u don't know what a class is think of this as a struct with 4 variables inside it.
    type: str
    value: str
    line: int
    column: int

keyword = {'return' : 'keyword that returns a value from a block'}
keyword_keys = keyword.keys()
keywords = {
    "auto",
    "bool",
    "break",
    "case",
    "catch",
    "char",
    "word",
    "class",
    "const",
    "continue",
    "delete",
    "do",
    "double",
    "else",
    "enum",
    "false",
    "float",
    "for",
    "goto",
    "if",
    "#include",
    "int",
    "long",
    "namespace",
    "not",
    "or",
    "private",
    "protected",
    "public",
    "return",
    "short",
    "signed",
    "sizeof",
    "static",
    "struct",
    "switch",
    "true",
    "try",
    "unsigned",
    "void",
    "while",
    }
delimiter = {';':'terminator symbol semicolon (;)'}
delimiter_keys = delimiter.keys()

blocks = {'{' : 'Blocked Statement Body Open', '}':'Blocked Statement Body Closed'}
block_keys = blocks.keys()

def tokenize(code):
    # ToDo:add the rest of the keywords;
    keywords_cpp = {'auto', 'break', 'case', 'char',
                    'const', 'continue', 'default', 'do',
                    'double', 'else', 'enum', 'extern',
                    'float', 'for', 'goto', 'if',
                    'int', 'long', 'register', 'return',
                    'short', 'signed', 'sizeof', 'static',
                    'struct', 'switch', 'typedef', 'union',
                    'unsigned', 'void', 'volatile', 'while','cin','cout','vectror'}
    keyword = {'while' : 'while'}
    keyword_keys = keyword.keys()
    # each element in the token_specification list is a named tuple that represents a possible token
    token_specification = [
        # ToDo: Check this example then complete the rest of the tokens.
        # I use a namedtuple in here. It's like a normal tuple but with named fields.
        # So i can get the values using names.
        ('assignment_operator', r'=|(/=)|\*=|-=|\+='),
    ('letter_', r'A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z|M…|Z|a|b|c|x|y|m|….|z|_' ),
    ('digit', r'0|1|2….|9' ),
    ('digits', r'10|11|12….|10000000' ),
        #('identifier', r'(letter_|digit)*' ),
    ('unary_operator',r'\+|-|\*|&'),
    #('')
    ('identifiers', r'[a-zA-Z_a-zA-Z][a-zA-Z0-9_]'),
    ('logical_operator',r'\&&|!|\|{2}'),
    #('logical_operator',r'\||')
    
    
    
    
              # assignment-operator identifier
    ]

    # This creates a regular expression that contains all the expressions u wrote in the token_specification list.
    # it uses the property that the regular expression a|b will get either a or b .
    # The syntax uses an idea called list comprehension to create a one line code.
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    #keyword='|'.join('(?P<%s>%s)' % pair for pair in keywords_cpp )
    line_num = 1
    line_start = 0
    # This for loop iterates over all the found matches in the input code and then creates a token for each match.
    # The finditer method can be found in the python documentation linked in the Task page.
    
    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup
        value = mo.group()
        column = mo.start() - line_start
        # These lines give an example on some processing done to found tokens.
        # U can ignore them if u want.

        # if kind == 'NUMBER':
        #     value = float(value) if '.' in value else int(value)
        # elif kind == 'ID' and value in keywords_cpp:
        #     kind = value
        # elif kind == 'NEWLINE':
        #     line_start = mo.end()
        #     line_num += 1
        #     continue
        # elif kind == 'SKIP':
        #     continue
        # elif kind == 'MISMATCH':
        #     raise RuntimeError(f'{value!r} unexpected on line {line_num}')


# The yield statement is part f a concept called generators in python.
        yield Token(kind, value, line_num, column)


    
f = open(r'C:\Users\laptop store\Documents\c_iti\day9.txt')
i=f.read()
statements='''
     while(x=1){
       = total*=total+11&1
     o_=a}
   
   '''  
program =  i.split('\n')
program =  i.split('\n')


def main():
    # ToDo: U have to add the file handling logic in here and then pass the code to the tokenize() function.
    for token in tokenize(i):
        print(token)


if name == 'main':
    main()
    for line in program:
        count=0
        count = count+1
    
     
        tokens = line.split(' ')
        
        for token in tokens:
        
      if token in keyword_keys:
        print( keyword[token])
