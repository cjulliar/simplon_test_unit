import pytest
import source.shapes as shapes
import math

class TestCircle:
    def setup_method(self, method):
        self.circle = shapes.Circle(10)
        # print(f"setting up {method}")

    def test_area(self):
        assert self.circle.area() == math.pi * self.circle.radius ** 2

    def test_perimeter(self):
        assert self.circle.perimeter() == math.pi * self.circle.radius * 2




def test_area(my_rectangle):
    assert my_rectangle.area() == 4 * 5

def test_perimeter(my_rectangle):
    assert my_rectangle.perimeter() == 4 * 2 + 5 * 2

def test_eq(my_rectangle, other_rectangle):
    assert my_rectangle == other_rectangle 

def test_wrong_eq(my_rectangle, wrong_rectangle):
    assert my_rectangle != wrong_rectangle 



class TestRectangleAndCircle:
    def setup_method(self, method):
        self.circle = shapes.Circle(10)
        self.rectangle = shapes.Rectangle(length=4, width = 5)

    def test_not_the_same_area(self):
        assert self.circle.area() != self.rectangle.area()


def test_area(rectangle_factory):
    my_rect = rectangle_factory(4, 5)
    assert my_rect.area() == 4 * 5


@pytest.mark.skip(reason="broken")
def test_skip():
    result= mf.add(3, 1)
    assert result == 4

@pytest.mark.xfail(reason="broken")
def test_xfail():
    result= mf.add(3, 1)
    assert result == 4

