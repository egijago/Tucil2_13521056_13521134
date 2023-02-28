from utils import distance


def closest_pair_brute(points):
    if len(points) <= 1:
        return None, None, None

    min_point1 = None
    min_point2 = None
    min = None

    for i in range(len(points)):
        for j in range(i + 1, len(points), 1):
            point1 = points[i]
            point2 = points[j]
            temp = distance(point1, point2)
            if min == None or temp < min:
                min = temp
                min_point1, min_point2 = point1, point2

    return min_point1, min_point2, min
