"""
LEGB
L - local
E - enclosing
G - global
B - built-in
"""


scope = 'global'


def test_func():
    scope = 'enclosing'

    def inner_func():
        scope = 'local'
        print(scope)

    inner_func()

test_func()