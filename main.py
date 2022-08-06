from sort.selection_sort import selection_sort
from sort.insertion_sort import insertion_sort
from sort.bubble_sort import bubble_sort
import sys
from time import time

def main():

    print("----- Sort Algorithms -----")
    input_array = input('Inserting array:\nExample: 1, 2, 4\n')
    try:
        li = list(input_array.split(','))
        input_list = [int(x) for x in li]
    except:
        print("That was no valid array.")

    print("---------------------------")
    print("Available algorithms:")
    print("a) Selection Sort")
    print("b) Insertion Sort")
    print("c) Bubble Sort")
    print("---------------------------")
    select_alg = input("Select one:\n")

    print(time())
    init_time = time()
   
    if select_alg == 'a':
        sorted_list = selection_sort(input_list, len(input_list))
    elif select_alg == 'b':
        sorted_list = insertion_sort(input_list, len(input_list))
    elif select_alg == 'c':
        sorted_list = bubble_sort(input_list, len(input_list))
    else:
        print("Invalid option")
        exit()

    print(time())
    end_time = time()

    print("------ Sorted Array: ------")
    print(sorted_list)
    print("----- Execution time: -----")
    print(end_time - init_time, "seconds.")

if __name__ == '__main__':
    main()