import main


def test_cars():
    assert main.cars(2, 48, 76) == 0
    assert main.cars(43, 15, 87) == 10
    assert main.cars(88, 37, 17) == 8


def test_median():
    assert main.median([1, 2, 4, 5, 6, 8, 8, 8, 10]) == 6
    assert main.median([2, 2, 6, 8, 8, 10, 10]) == 8
    assert main.median([1, 2, 2, 4, 7, 8, 9, 10]) == 5.5
