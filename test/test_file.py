import pytest
from fibonacci.fibonacci import fibonacci
'''
fibonacci
n=0 -> '0'
n=1 -> '1'
n=2 -> '1'
n=3 -> '2'
n=4 -> '3'
n=5 -> '5'
n=6 -> '8'
n=7 -> '13'
'''
def test_one():
    actual= fibonacci(1)
    excepted= 1
    assert actual == excepted
    
def test_two():
    actual= fibonacci(0)
    excepted= 0
    assert actual == excepted
    
def test_three():
      actual= fibonacci(3)
      excepted= 2
      assert actual == excepted
      
def test_four():
      actual= fibonacci(4)
      excepted= 3
      assert actual == excepted
      
def test_five():
      actual= fibonacci(5)
      excepted= 5
      assert actual == excepted
      
def test_six():
      actual= fibonacci(6)
      excepted= 8
      assert actual == excepted
      
def test_string():
      actual= fibonacci("7")
      excepted= "please enter a number"
      assert actual == excepted