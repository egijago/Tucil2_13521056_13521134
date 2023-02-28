import math
from random import randint


def generate_dots(num=100, x=100, dim=3):
    return [[randint(-x, x) for _i in range(dim)] for _j in range(num)]


def distance(p1, p2):
    return math.sqrt(sum((p1[i] - p2[i]) ** 2 for i in range(len(p1))))


class DistFuncCounter:
    def __init__(self):
        self.count = 0

    def getEuclideanDistance(self, p1, p2):
        self.count += 1
        return distance(p1, p2)
