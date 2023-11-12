import re

# 定义词法规则
token_specification = [
    ('NUMBER',   r'\d+'),           # Integer
    ('IDENT',    r'[A-Za-z]+'),     # Identifiers
    ('OPERATOR', r'[+\-*/]'),       # Arithmetic Operators
    ('RESERVED', r'if|else|while'), # Reserved Words
    ('SEPARATOR', r'[;(),]'),       # Separators
    ('SKIP',     r'[ \t]'),         # Skip over spaces and tabs
    ('MISMATCH', r'.'),             # Any other character
]

# 将规则编译成正则表达式
token_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)

# 词法分析函数
def lex(code):
    for mo in re.finditer(token_regex, code):
        kind = mo.lastgroup
        value = mo.group()
        if kind == 'NUMBER':
            value = int(value)  # Convert to integer
        elif kind == 'SKIP':
            continue  # Skip whitespace
        elif kind == 'MISMATCH':
            raise RuntimeError(f'Illegal character {value}')
        print(f'{kind}: {value}')

# 测试代码
source_code = 'if x + 4 > y while 23'
lex(source_code)
