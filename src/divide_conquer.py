from collections.abc import Callable
from sorting import quicksort
from utils import appendPairsIfNotIn


def closest_pair_strip(
    points: list[tuple[int]],
    delta: float,
    dimension: int,
    getEuclideanDistance: Callable[[tuple[int], tuple[int]], float],
) -> tuple[list[tuple[tuple, tuple]], float]:
    midIdx: int = len(points) // 2
    median: float = (
        points[midIdx - 1][dimension - 1] + points[midIdx][dimension - 1]
    ) / 2
    stripPoints: list[tuple[int]] = [
        point for point in points if abs(median - point[dimension - 1]) < delta
    ]

    if dimension == 2:
        quicksort(stripPoints, 0, len(stripPoints) - 1, 0)

        min_strip_points = []
        stripDelta: float = None

        for i in range(len(stripPoints)):
            for j in range(i + 1, len(stripPoints)):
                if stripPoints[j][0] - stripPoints[i][0] >= delta:
                    break
                dist = getEuclideanDistance(stripPoints[i], stripPoints[j])
                if stripDelta == None or dist < stripDelta:
                    min_strip_points = [(stripPoints[i], stripPoints[j])]
                    stripDelta = dist
                elif stripDelta != None and dist == stripDelta:
                    min_strip_points.append((stripPoints[i], stripPoints[j]))

        if stripDelta != None:
            return min_strip_points, stripDelta
        else:
            return None, None
    else:
        return closest_pair(stripPoints, dimension - 1, getEuclideanDistance)


def closest_pair(
    points: list[tuple[int]],
    dimension: int,
    getEuclideanDistance: Callable[[tuple[int], tuple[int]], float],
) -> tuple[list[tuple[tuple, tuple]], float]:
    if len(points) == 1:
        return None, None
    if len(points) <= 3:
        min_points = []
        delta = None
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                dist = getEuclideanDistance(points[i], points[j])
                if delta == None or dist < delta:
                    min_points = [(points[i], points[j])]
                    delta = dist
                elif delta != None and dist == delta:
                    min_points.append((points[i], points[j]))

        return min_points, delta

    quicksort(points, 0, len(points) - 1, dimension - 1)

    midIdx: int = len(points) // 2
    leftPoints: list[tuple[int]] = points[:midIdx]
    rightPoints: list[tuple[int]] = points[midIdx:]

    left_points, leftDelta = closest_pair(leftPoints, dimension, getEuclideanDistance)
    right_points, rightDelta = closest_pair(
        rightPoints, dimension, getEuclideanDistance
    )

    delta = min(leftDelta, rightDelta)

    strip_points, stripDelta = closest_pair_strip(
        points, delta, dimension, getEuclideanDistance
    )

    if stripDelta != None:
        delta = min(delta, stripDelta)

    min_points = []
    if delta == leftDelta:
        min_points.extend(left_points)
    if delta == rightDelta:
        min_points.extend(right_points)
    if stripDelta != None and delta == stripDelta:
        appendPairsIfNotIn(min_points, strip_points)

    return min_points, delta
