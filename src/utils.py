import math
from random import randint


def distance(p1, p2):
    return math.sqrt(sum((p1[i] - p2[i]) ** 2 for i in range(len(p1))))


def min2(lst):
    return min(filter(lambda x: x is not None, lst)) if any(lst) else None


def generate_dots(num=100, x=100, dim=3):
    return [tuple([randint(-x, x) for _i in range(dim)]) for _j in range(num)]
