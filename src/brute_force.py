from collections.abc import Callable


def closest_pair_brute(
    points: list[tuple[int]],
    getEuclideanDistance: Callable[[tuple[int], tuple[int]], float],
):
    if len(points) <= 1:
        return None, None

    min_points = []
    min = None

    for i in range(len(points)):
        for j in range(i + 1, len(points), 1):
            point1 = points[i]
            point2 = points[j]
            temp = getEuclideanDistance(point1, point2)
            if min == None or temp < min:
                min = temp
                min_points = [(point1, point2)]
            elif min != None and temp == min:
                min_points.append((point1, point2))

    return min_points, min
