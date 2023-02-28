import math
from random import randint


def generate_dots(num=100, x=100, dim=3):
    return [[randint(-x, x) for _i in range(dim)] for _j in range(num)]


def distance(p1, p2):
    return math.sqrt(sum((p1[i] - p2[i]) ** 2 for i in range(len(p1))))


def appendPairsIfNotIn(
    target: list[tuple[tuple, tuple]], pairs: list[tuple[tuple, tuple]]
):
    toAdd = []
    for pair in pairs:
        found = False
        for tgt in target:
            if (tgt[0] == pair[0] and tgt[1] == pair[1]) or (
                tgt[0] == pair[1] and tgt[1] == pair[0]
            ):
                found = True
        if not found:
            toAdd.append(pair)

    target.extend(toAdd)


class DistFuncCounter:
    def __init__(self):
        self.count = 0

    def getEuclideanDistance(self, p1, p2):
        self.count += 1
        return distance(p1, p2)
