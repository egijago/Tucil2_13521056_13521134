from collections.abc import Callable
from sorting import quicksort


def closest_pair_strip(
    points: list[tuple[int]],
    delta: float,
    dimension: int,
    getEuclideanDistance: Callable[[tuple[int], tuple[int]], float],
) -> tuple[tuple[int], tuple[int], float]:
    midIdx: int = len(points) // 2
    median: float = (
        points[midIdx - 1][dimension - 1] + points[midIdx][dimension - 1]
    ) / 2
    stripPoints: list[tuple[int]] = [
        point for point in points if abs(median - point[dimension - 1]) < delta
    ]

    if dimension == 2:
        quicksort(stripPoints, 0, len(stripPoints) - 1, 0)

        stripPoint1: tuple = None
        stripPoint2: tuple = None
        stripDelta: float = None

        for i in range(len(stripPoints)):
            for j in range(i + 1, len(stripPoints)):
                if stripPoints[j][0] - stripPoints[i][0] >= delta:
                    break
                dist = getEuclideanDistance(stripPoints[i], stripPoints[j])
                if stripDelta == None or dist < stripDelta:
                    stripPoint1, stripPoint2, stripDelta = (
                        stripPoints[i],
                        stripPoints[j],
                        dist,
                    )

        if stripDelta != None:
            return stripPoint1, stripPoint2, stripDelta
        else:
            return None, None, None
    else:
        return closest_pair(stripPoints, dimension - 1, getEuclideanDistance)


def closest_pair(
    points: list[tuple[int]],
    dimension: int,
    getEuclideanDistance: Callable[[tuple[int], tuple[int]], float],
) -> tuple[tuple[int], tuple[int], float]:
    if len(points) == 1:
        return None, None, None
    if len(points) <= 3:
        point1 = None
        point2 = None
        delta = None
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                dist = getEuclideanDistance(points[i], points[j])
                if delta == None or dist < delta:
                    point1, point2, delta = points[i], points[j], dist

        return point1, point2, delta

    quicksort(points, 0, len(points) - 1, dimension - 1)

    midIdx: int = len(points) // 2
    leftPoints: list[tuple[int]] = points[:midIdx]
    rightPoints: list[tuple[int]] = points[midIdx:]

    leftPoint1, leftPoint2, leftDelta = closest_pair(
        leftPoints, dimension, getEuclideanDistance
    )
    rightPoint1, rightPoint2, rightDelta = closest_pair(
        rightPoints, dimension, getEuclideanDistance
    )

    delta = min(leftDelta, rightDelta)

    stripPoint1, stripPoint2, stripDelta = closest_pair_strip(
        points, delta, dimension, getEuclideanDistance
    )

    if stripDelta != None:
        delta = min(delta, stripDelta)

    if delta == leftDelta:
        return leftPoint1, leftPoint2, leftDelta
    elif delta == rightDelta:
        return rightPoint1, rightPoint2, rightDelta
    elif stripDelta != None and delta == stripDelta:
        return stripPoint1, stripPoint2, stripDelta
