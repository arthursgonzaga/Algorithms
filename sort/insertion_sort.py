import numpy as np

def insertion_sort(input, number_elements):
    for n in range(number_elements):
        analysis_number = n
        while(analysis_number > 0 and input[analysis_number] < input[analysis_number-1]):
            _change_position(input, analysis_number, analysis_number-1)
            analysis_number -= 1
        
    return input

def _change_position(input, position_1, position_2):
    first_value = input[position_1]
    second_value = input[position_2]

    input[position_2] = first_value
    input[position_1] = second_value    

    return None

if __name__ == '__main__':
    example = [1, 30, 25, 12]
    print("This is an example for insertion sort algorithm")
    print("Initial array:")
    print(example)
    print("Running...")
    insertion_sort(example, len(example))
    print("Sorted array:")
    print(example)
