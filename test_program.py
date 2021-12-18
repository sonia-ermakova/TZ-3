import random
from functools import reduce
from datetime import datetime
from program import minimum, maximum, addition, multiplication, read_file, data


def test_minimum():
    assert minimum(data) == min(data)


def test_maximum():
    assert maximum(data) == max(data)


def test_addition():
    assert addition(data) == sum(data)


def test_multiplication():
    assert multiplication(data) == reduce(lambda m, n: m*n, data)


def test_speed():
    start_1 = datetime.now()
    read_file()
    minimum(data[:5])
    maximum(data[:5])
    addition(data[:5])
    multiplication(data[:5])
    end_1 = datetime.now()
    time_1 = end_1 - start_1
    start_2 = datetime.now()
    read_file()
    minimum(data)
    maximum(data)
    addition(data)
    multiplication(data)
    end_2 = datetime.now()
    time_2 = end_2 - start_2
    assert time_1 < time_2


def test_speed_minimum():
    start_1 = datetime.now()
    minimum(data)
    end_1 = datetime.now()
    time_1 = end_1 - start_1
    start_2 = datetime.now()
    minimum(data[:5])
    end_2 = datetime.now()
    time_2 = end_2 - start_2
    assert time_2 < time_1
