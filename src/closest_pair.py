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

def closest_pair(points, counter = 0):
    global dnq, brute
    n = len(points)

    # base case / conquer
    if n <= 3:
        dnq += sum(i+1 for i in range(n))
        brute -= sum(i+1 for i in range(n))
        return closest_pair_brute(points)
    dimension = len(points[0])

    # divide
    sorted_points = sorted(points, key = lambda point: point[counter])

    mid = n // 2
    left_half = sorted_points[:mid]
    right_half = sorted_points[mid:]
    
    # solve each half recursively
    left_point1, left_point2, left_delta = closest_pair(left_half)
    right_point1, right_point2, right_delta = closest_pair(right_half)
    delta = min2([left_delta, right_delta])

    if delta == left_delta:
        point1 = left_point1
        point2 = left_point2  
    else:
        point1 = right_point1
        point2 = right_point2

    div_axis = sorted_points[mid][counter] if n % 2 == counter else (sorted_points[mid - 1][counter] + sorted_points[mid - 1][counter])/2
    # stripe
    if dimension - counter == 3 : 

        left_stripe = [point for point in left_half if abs(point[counter] - div_axis) < delta]
        right_stripe = [point for point in right_half if abs(point[counter] - div_axis) < delta]
        # check for closest pairs within stripes
        for i in range(len(left_stripe)):
            right_stripe_to_check = [point for point in right_stripe if abs(point[dimension - 1] - left_stripe[i][dimension - 1]) < delta] # only interested if d + 1 distance within 2*delta
            for j in range(len(right_stripe_to_check)):
                dnq += 1
                d = distance(left_stripe[i], right_stripe_to_check[j])
                if d < delta:
                    point1, point2, delta = left_stripe[i], right_stripe_to_check[j], d
        return point1, point2, delta
    else: 
        stripe = [point for point in sorted_points if abs(point[counter] - div_axis) < delta]
        stripe_point1, stripe_point2, stripe_delta = closest_pair(stripe, counter + 1)
        return stripe_point1, stripe_point2, stripe_delta if stripe_delta < delta else point1, point2, delta


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