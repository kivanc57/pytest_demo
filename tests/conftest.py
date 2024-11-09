# conftest.py --> Script to define global variables
# Do not abuse it to avoid overloadings

import pytest
import source.shapes as shapes

@pytest.fixture
# This is a doceration to create a test instance
def test_rectangle():
  return shapes.Rectangle(length=10, width=20)

@pytest.fixture
# This a another test instance
def other_triangle():
  return shapes.Rectangle(length=5, width=6)
