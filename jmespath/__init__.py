from jmespath import parser
from jmespath.visitor import Options

__version__ = '0.10.0'


def compile(expression):
    return parser.Parser().parse(expression)


def search(expression, data, options=None):
    return parser.Parser().parse(expression).search(data, options=options)
