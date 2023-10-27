#'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs',
#'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii',
#'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable',
#'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans',
#'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition',
#'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate',
#'upper', 'zfill']
age=42
name='Daniel'
#print(dir('my_string'))
print('my_name'.title())
print('my_string'.upper())
print('my name is {}, my name is {}'.format(name,age))
print(f'my name is {name}, my name is {name}')
print('C_leg_system_GRP'.split('_'))
name_of_object=['C','color','system','GRP']
print('_'.join(name_of_object))
