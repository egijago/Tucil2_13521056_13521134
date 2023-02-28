from brute_force import *
from closest_pair import *
from divide_conquer import *
from utils import *
from IO import *
import matplotlib.pyplot as plt
import platform



def welcome_text():
    print("""
   _____  _                         _     _____        _       
  / ____|| |                       | |   |  __ \      (_)      
 | |     | |  ___   ___   ___  ___ | |_  | |__) |__ _  _  _ __ 
 | |     | | / _ \ / __| / _ \/ __|| __| |  ___// _` || || '__|
 | |____ | || (_) |\__ \|  __/\__ \| |_  | |   | (_| || || |   
  \_____||_| \___/ |___/ \___||___/ \__| |_|    \__,_||_||_|        

    """)


def menu_text():
    print("================================MENU================================")
    print()
    print("1. Generate random           ")
    print("2. Import from file          ")
    print("3. Exit                      ")
    print()
    print("====================================================================")
    
def space(n=3):
    for _ in range (n):
        print()

def visualize(points, solution):


    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for point in points:
        if point not in solution:
            ax.scatter(point[0], point[1], point[2], c='b', marker='o') 

    for point in solution:
        ax.scatter(point[0], point[1], point[2], c='r', marker='o') 
    
    for point in solution:
        ax.plot([solution[0][0], solution[1][0]], [solution[0][1], solution[1][1]], [solution[0][2], solution[1][2]], c='k')
        
    ax.set_xlabel('x axis')
    ax.set_ylabel('y axis')
    ax.set_zlabel('z axis')

    plt.show()


def compute(points):
    space(1)

    bf_counter = DistFuncCounter()
    bf_start = timeit.default_timer()
    bf = closest_pair_brute(points, bf_counter.getEuclideanDistance)
    bf_stop = timeit.default_timer()

    dim = len(points[0])
    dnc_counter = DistFuncCounter()
    dnc_start = timeit.default_timer()
    dnc = closest_pair(points, dim, dnc_counter.getEuclideanDistance)
    dnc_stop = timeit.default_timer()

    print("==============================SOLUTION==============================")
    print()
    print(f"Closest pair                           : {dnc[0]}, {dnc[1]}")
    print(f"Closest distance                       : {dnc[2]}")
    print()
    print("=============================STATISTICS=============================")
    print(f"DNQ execution time                     : {(dnc_stop - dnc_start)*1000} ms")
    print(f"DNQ distance computation count         : {dnc_counter.count}")
    print(f"Brute-force execution time             : {(bf_stop - bf_start)*1000} ms")
    print(f"Brute-forcedistance computation count  : {bf_counter.count}")
    print()
    print(f"Running on: {platform.processor()}")
    
    if dim == 3:
        cc = str(input("Do you want to visualize (y/n)? "))
        if cc == 'y':
            visualize(points, [dnc[0], dnc[1]])
            


def main():
    welcome_text()
    while (True):
        menu_text()
        choice = int(input("> "))

        if choice == 1: 
            num = int(input("Enter the number of points (n >= 2)    : "))

            if num  <= 1:
                print("Please enter a number >= 2")
                continue

            dim = int(input("Enter the number of dimensions (d>=1)  : "))

            if dim  < 1:
                print("Please enter a number >= 1")
                continue

            x = int(input("Enter the range of randomized value    : "))
            points = generate_dots(num, x, dim)
            compute(points)

        elif choice == 2:
            path = str(input("Enter the txt file path                   : "))
            try : 
                points = read_from_file(path)
                print(points)
                compute(points)
            except: 
                print("File not found or out of format")

        elif choice == 3:
            print("Bye-bye~")
            exit(0)

        else :
            print("Masukan salah, harap masukkan (1-3)")
        
if __name__ == "__main__":
    main()
