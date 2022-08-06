import numpy as np


def _change_position(input, position_1, position_2):
    """
    It swaps the values of two elements in a list
    
    :param input: the list of characters to be permuted
    :param position_1: The position of the first character to swap
    :param position_2: the position of the element to be moved
    """
    temp = input[position_1]
    input[position_1] = input[position_2]
    input[position_2] = temp


def bubble_sort(input, number_elements):
    """
    For each element in the list, compare it to the next element and swap them if the next element is
    smaller
    
    :param input: the list of numbers to be sorted
    :param number_elements: The number of elements in the input array
    :return: The input array is being returned.
    """
    for j in range(number_elements):
        for i in range(0, number_elements - j - 1):
            if input[i] > input[i + 1]:
                _change_position(input, i, i + 1)
    return input


if __name__ == "__main__":
    example = [1, 30, 25, 12, 20, 2, 4, 7]
    print("This is an example for insertion sort algorithm")
    print("Initial array:")
    print(example)
    print("Running...")
    bubble_sort(example, len(example))
    print("Sorted array:")
    print(example)
