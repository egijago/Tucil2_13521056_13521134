from divide_conquer import closest_pair
from brute_force import closest_pair_brute
from utils import generate_dots, DistFuncCounter
import timeit


def testing(iter=100):
    dim = 3
    points = generate_dots(dim=dim, num=1000)

    bf_counter = DistFuncCounter()
    bf_start = timeit.default_timer()
    bf = closest_pair_brute(points, bf_counter.getEuclideanDistance)
    bf_stop = timeit.default_timer()

    dnc_counter = DistFuncCounter()
    dnc_start = timeit.default_timer()
    dnc = closest_pair(points, dim, dnc_counter.getEuclideanDistance)
    dnc_stop = timeit.default_timer()

    if bf[2] != dnc[2]:
        print("incorrect")

    print(f"dnc time: {dnc_stop - dnc_start}")
    print(f"dnc count: {dnc_counter.count}")
    print(f"bf time: {bf_stop - bf_start}")
    print(f"bf count: {bf_counter.count}")


if __name__ == "__main__":
    testing(100)
