from sort.selection_sort import selection_sort
from sort.insertion_sort import insertion_sort
import sys

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
    print("---------------------------")
    select_alg = input("Select one:\n")
   
    if select_alg == 'a':
        sorted_list = selection_sort(input_list, len(input_list))
    elif select_alg == 'b':
        sorted_list = insertion_sort(input_list, len(input_list))
    else:
        print("Invalid option")
        exit()

    print("------ Sorted Array: ------")
    print(sorted_list)

if __name__ == '__main__':
    main()