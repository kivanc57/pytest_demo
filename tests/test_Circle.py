import math
import source.shapes as shapes


class TestCircle:

  """
  setup_method and teardown_method:
    They are initialized before each test, they print test object

  Execution:
    pytest -s {test_script}
  """
  
  def setup_method(self, method):
    print(f"\nSetting up -> {method}")
    self.circle = shapes.Circle(10)

  def teardown_method(self, method):
    print(f"Tearing down -> {method}")
    del self.circle


  def test_area(self):
    # assert self.circle.area() == (math.pi * self.circle.radius) ** 2
    result = self.circle.area()
    expected = (math.pi * self.circle.radius) ** 2
    assert result == expected

  def test_perimeter(self):
    # assert self.circle.perimeter() == (math.pi * self.radius) * 2
    result = self.circle.perimeter()
    expected = (math.pi * self.circle.radius) * 2
    assert result == expected

  def test_not_same_area_rectangle(self, test_rectangle):
    assert self.circle.area() != test_rectangle.area()
