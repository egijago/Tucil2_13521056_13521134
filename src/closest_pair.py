from divide_conquer import closest_pair
from brute_force import closest_pair_brute
from utils import generate_dots
import timeit


def testing(iter=100):
    dim = 5
    points = generate_dots(dim=dim, num=10000, x=)

    dnc_start = timeit.default_timer()
    dnc = closest_pair(points, dim)
    dnc_stop = timeit.default_timer()

    bf_start = timeit.default_timer()
    bf = closest_pair_brute(points)
    bf_stop = timeit.default_timer()

    if bf[2] != dnc[2]:
        print("incorrect")

    print(f"dnc time: {dnc_stop - dnc_start}")
    print(f"bf time: {bf_stop - bf_start}")


if __name__ == "__main__":
    testing(100)
