import pytest
import source.shapes as shapes

@pytest.mark.parametrize("side_length, expected_area", [(5, 25), (4, 16), (9, 81)])
# Marked as: parametrize
# Use to give multiple parameters
# In this case: expected_area
def test_multiple_square_areas(side_length, expected_area):
  assert shapes.Square(side_length).area() == expected_area

@pytest.mark.parametrize("side_length, expected_perimeter", [(3, 12), (4, 16), (5, 20)])
# Marked as: parametrize
# Use to give multiple parameters
# In this case: expected_perimeter
def test_multiple_parameters(side_length, expected_perimeter):
  assert shapes.Square(side_length).perimeter() == expected_perimeter
