import pytest
import source.shapes as shapes

@pytest.mark.parametrize("side_lenght, expected_area", [(3, 9), (5, 25), (9, 81)])
def test_multiple_square_areas(side_lenght, expected_area):
    assert shapes.Square(side_lenght).area() == expected_area

