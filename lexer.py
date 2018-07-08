import ply.lex as lex

reserved = {
    'INPUT': 'INPUT',
    'OUTPUT': 'OUTPUT',
    'GOTO': 'GOTO'
}

tokens = [
             # Literals (identifier, float constant, string constant)
             'ID', 'NUMBER', 'STRING',

             # Operators (+,-,*,/,%,^)
             'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'MODULO', 'POW',

             # Assignment (=)
             'EQUALS',

             # Delimeters ( ) ;
             'LPAREN', 'RPAREN',

             'SEMI',
         ] + list(reserved.values())

t_ignore = ' \t'


def t_ID(t):  # Yes i Know this violated PEP8 but its neaded to work with PLY
    r"""[a-zA-Z_][a-zA-Z_0-9]*"""
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
    return t


t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MODULO = r'%'
t_POW = r'\^'

t_EQUALS = r'='

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_SEMI = r';'

t_INPUT = r'INPUT'
t_OUTPUT = r'OUTPUT'
t_GOTO = r'GOTO'

t_ignore_COMMENT = r'\#.*'


def t_NUMBER(t):  # Yes i Know this violated PEP8 but its neaded to work with PLY
    r"""[0-9]+(\.[0-9]+)?"""
    t.value = float(t.value)
    return t


def t_STRING(t):  # Yes i Know this violated PEP8 but its neaded to work with PLY
    r"""\"([^\\\n]|(\\.))*?\\"""  # I think this is right ...
    t.value = t.value[1:-1]
    return t


def t_newline(t):
    r"""\n+"""
    t.lexer.lineno += len(t.value)


def t_error(t):
    print("Illegal character '%s'" % t.value[0])


lexer = lex.lex()