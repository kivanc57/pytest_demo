def test_area(test_rectangle):
  assert test_rectangle.area() == 10 * 20

def test_perimeter(test_rectangle):
  assert test_rectangle.perimeter() == (10 + 20) * 2

def test_not_equal(test_rectangle, other_triangle):
  assert test_rectangle != other_triangle
