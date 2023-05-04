import pytest
from series.series import fibonacci
from series.series import lucus
from series.series import sum
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
#fibonacci test
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
    
    
#lucus test 
def test_one():
      actual= lucus(0)
      excepted= 2
      assert actual == excepted
      
def test_two():
      actual= lucus(1)
      excepted= 1
      assert actual == excepted
      
def test_three():
      actual= lucus(2)
      excepted= 3
      assert actual == excepted
      
def test_string():
      actual= lucus("4")
      excepted= "please enter a number"
      assert actual == excepted 


# sum test
def test_one():
      actual= sum(7)
      excepted= 13
      assert actual == excepted
      
def test_two():
      actual= sum(6,2,1)
      excepted= 18
      assert actual == excepted
      
def test_three():
      actual= sum(5,0,0)
      excepted=15 
      assert actual == excepted
      
def test_string():
      actual= sum("4")
      excepted= "please enter all integer number"
      assert actual == excepted 