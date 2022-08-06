import numpy as np


def selection_sort(input, number_elements):
    """
    "For each element in the list, find the smallest number and swap it with the current element."
    
    The first thing we do is loop through the list. We start at the first element and go to the last
    element
    
    :param input: the list of numbers to be sorted
    :param number_elements: The number of elements in the input array
    :return: The input array is being returned.
    """
    for n in range(number_elements):
        smallest_number = _get_smallest_number(input, n, number_elements)
        _change_position(input, n, smallest_number)

    return input


def _get_smallest_number(input, initial_number, end_number):
    """
    It takes an array, an initial number, and an end number, and returns the index of the smallest
    number in the array between the initial and end numbers
    
    :param input: the list of numbers
    :param initial_number: the first number in the range of numbers to be searched
    :param end_number: the number of elements in the list
    :return: The index of the smallest number in the list.
    """
    smallest_number = initial_number
    for n in range(initial_number, end_number):
        if input[n] < input[smallest_number]:
            smallest_number = n
        else:
            pass
    return smallest_number


def _change_position(input, position_1, position_2):
    """
    It takes in a list, two positions in that list, and swaps the values at those positions
    
    :param input: the list of numbers
    :param position_1: The position of the first value to swap
    :param position_2: the position of the first value to swap
    :return: None
    """
    first_value = input[position_1]
    second_value = input[position_2]

    input[position_2] = first_value
    input[position_1] = second_value

    return None


if __name__ == "__main__":
    example = [1, 30, 25, 12]
    print("This is an example for selection sort algorithm")
    print("Initial array:")
    print(example)
    print("Running...")
    selection_sort(example, len(example))
    print("Sorted array:")
    print(example)
