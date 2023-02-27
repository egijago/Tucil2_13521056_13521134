from random import randint
import math

def min2(lst):
    return min(filter(lambda x: x is not None, lst)) if any(lst) else None

def generate_dots(num = 100, x = 100, dim = 3):
    return [tuple([randint(-x, x) for _i in range (dim)]) for _j in range (num)]


def closest_pair_brute(points):
    global brute
    if (len(points) <= 1):
        return None, None, None

    min_point1, min_point2, min = points[0], points[1], distance(points[0], points[1])
    for i in range (len(points)):
        for j in range (i + 1, len(points), 1):
            point1 = points[i]
            point2 = points[j]
            brute += 1
            temp = distance(point1, point2)
            if (temp < min) :
                min = temp  
                min_point1, min_point2 = point1, point2

    return min_point1, min_point2, min

def distance(p1, p2):
    return math.sqrt(sum((p1[i]-p2[i])**2 for i in range(len(p1))))

def closest_pair_strip(
    points: list[tuple[int]], delta: float, dimension: int
) -> tuple[tuple[int], tuple[int], float]:
    global dnq

    midIdx: int = len(points) // 2
    median: float = (
        points[midIdx - 1][dimension - 1] + points[midIdx][dimension - 1]
    ) / 2
    stripPoints: list[tuple[int]] = [
        point for point in points if abs(median - point[dimension - 1]) < delta
    ]

    if dimension == 2:
        sortedPoints = sorted(stripPoints, key=lambda x: x[0])

        stripPoint1: tuple = None
        stripPoint2: tuple = None
        stripDelta: float = None

        # TODO: check number of iterations
        for i in range(len(sortedPoints)):
            for j in range(i + 1, len(sortedPoints)):
                if sortedPoints[j][0] - sortedPoints[i][0] >= delta:
                    break
                dist = distance(sortedPoints[i], sortedPoints[j])
                dnq += 1
                if stripDelta == None or dist < stripDelta:
                    stripPoint1, stripPoint2, stripDelta = (
                        sortedPoints[i],
                        sortedPoints[j],
                        dist,
                    )

        if stripDelta != None:
            return stripPoint1, stripPoint2, stripDelta
        else:
            return None, None, None
    else:
        return closest_pair(stripPoints, dimension - 1)


def closest_pair(
    points: list[tuple[int]], dimension: int
) -> tuple[tuple[int], tuple[int], float]:
    global dnq, brute

    if len(points) <= 3:
        dnq += sum(i + 1 for i in range(len(points)))
        brute -= sum(i + 1 for i in range(len(points)))
        return closest_pair_brute(points)

    sortedPoints: list[tuple[int]] = sorted(points, key=lambda x: x[dimension - 1])

    midIdx: int = len(points) // 2
    leftPoints: list[tuple[int]] = sortedPoints[0:midIdx]
    rightPoints: list[tuple[int]] = sortedPoints[midIdx : len(sortedPoints)]

    leftPoint1, leftPoint2, leftDelta = closest_pair(leftPoints, dimension)

    rightPoint1, rightPoint2, rightDelta = closest_pair(rightPoints, dimension)

    delta = min(leftDelta, rightDelta)

    stripPoint1, stripPoint2, stripDelta = closest_pair_strip(
        sortedPoints, delta, dimension
    )

    if stripDelta != None:
        delta = min(delta, stripDelta)

    if delta == leftDelta:
        return leftPoint1, leftPoint2, leftDelta
    elif delta == rightDelta:
        return rightPoint1, rightPoint2, rightDelta
    elif stripDelta != None and delta == stripDelta:
        return stripPoint1, stripPoint2, stripDelta


brute = 0
dnq = 0
def testing(iter = 100): 
    global brute, dnq
    brute = 0
    dnq = 0
    count = 0
    for _ in range (iter):
        points = generate_dots(dim = 3)
        if closest_pair_brute(points)[2] != closest_pair(points)[2]:
            count +=1
    print(count, brute, dnq)

if __name__ == "__main__" :
    testing(100)