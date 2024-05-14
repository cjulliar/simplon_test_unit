import pytest
import source.shapes as shapes

@pytest.fixture
def other_rectangle():
    return shapes.Rectangle(4, 5)

@pytest.fixture
def wrong_rectangle():
    return shapes.Rectangle(42, 5)

@pytest.fixture
def my_rectangle():
    return shapes.Rectangle(4, 5)

@pytest.fixture
def rectangle_factory():
    def the_rectangle(length, width):
        return shapes.Rectangle(length=length, width=width)
    return the_rectangle


@pytest.fixture
def my_circle():
    return shapes.Circle(10)