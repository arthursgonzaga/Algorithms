import numpy as np

def selection_sort(input, number_elements):
    for n in range(number_elements):
        smallest_number = _get_smallest_number(input, n, number_elements)
        _change_position(input, n, smallest_number)
        
    return input

def _get_smallest_number(input, initial_number, end_number):
    smallest_number = initial_number
    for n in range(initial_number, end_number):
        if input[n] < input[smallest_number]:
            smallest_number = n
        else:
            pass
    return smallest_number

def _change_position(input, position_1, position_2):
    first_value = input[position_1]
    second_value = input[position_2]

    input[position_2] = first_value
    input[position_1] = second_value    

    return None

if __name__ == '__main__':
    example = [1, 30, 25, 12]
    print("This is an example for selection sort algorithm")
    print("Initial array:")
    print(example)
    print("Running...")
    selection_sort(example, len(example))
    print("Sorted array:")
    print(example)
