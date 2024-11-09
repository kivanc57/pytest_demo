import time
import pytest
import source.functions as functions

"""
Execution: pytest {test_script}
"""

def test_add():
  result = functions.add(number_one=1, number_two=4)
  assert result == 5

def test_add_strings():
  result = functions.add(number_one="I like ", number_two="burgers")
  assert result == "I like burgers"

def test_divide():
  result = functions.divide(number_one=10, number_two=5)
  assert result == 2

def test_divide_by_zero():
  with pytest.raises(ZeroDivisionError):
    functions.divide(number_one=10, number_two=0)


"""
These are examples of marking with pytest
Execution:
  pytest -m {slow}
"""
@pytest.mark.slow
# Marked as: 'slow'
# This function is slow
def test_very_slow():
  time.sleep(5)
  assert functions.divide(number_one=10, number_two=5) == 2


@pytest.mark.skip(reason="This feature is currently broken")
# Marked as: 'skip'
# This function will be skipped
def test_add():
  assert functions.add(number_one=1, number_two=2) == 3


@pytest.mark.xfail(reason="We know we cannot divide by zero")
# Marked as: 'xfail'
# This function is broken
def test_divide_by_zero_broken():
  functions.divide(number_one=4, number_two=0)
