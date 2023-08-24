from .. import db
from main.models.example_model import Example

def foo():
    return 'bar'

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fib(n-2) + fib(n-1)
    
def get_all_examples():
    example = Example.query.order_by(Example.id).all()
    
    return example
    