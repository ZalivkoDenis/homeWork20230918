# ШАГ. Д/з по сроку 18/09/2023 © Денис Заливко


NORM_WHEEL = 4
NORM_HULL = 1
NORM_PERSON = 2


def cars(wheels: int, hulls: int, persons: int) -> int:
    """
    Возвращает количество машинок, которые можно собрать из деталей.
    Одна машинка: 4 колеса, 1 корпус и 2 фигурки человечков внутри.
    :param wheels: Количество колёс.
    :param hulls: Количество корпусов
    :param persons: Количество фигурок человечков
    :return: Количество машинок, которые можно собрать из деталей
    """
    return min(wheels // NORM_WHEEL, hulls // NORM_HULL, persons // NORM_PERSON)


def median(some_list: list[int]) -> float:
    """
    Функция, которая принимает отсортированный список чисел и возвращает медиану.
    Если число дробное, то округляется до десятых.
    :param some_list: Список чисел.
    :return: Медиана.
    """
    analyze_list: list[int] = sorted(some_list)
    n = len(analyze_list)
    if n < 1:
        raise ValueError('List must have elements')
    elif n == 1:
        return analyze_list[n]
    elif n % 2:
        return analyze_list[n // 2]
    else:
        return round((analyze_list[n // 2] + analyze_list[n // 2 - 1]) / 2, 1)

# Testing started at 1:46 ...
# Launching pytest with arguments D:\PROJECTS\PYTHON\homeWork20230918\test_main.py --no-header --no-summary -q in D:\PROJECTS\PYTHON\homeWork20230918
#
# ============================= test session starts =============================
# collecting ... collected 2 items
#
# test_main.py::test_cars PASSED                                           [ 50%]
# test_main.py::test_median PASSED                                         [100%]
#
# ============================== 2 passed in 0.01s ==============================
#
# Process finished with exit code 0
