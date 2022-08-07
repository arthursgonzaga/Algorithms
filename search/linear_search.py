import numpy as np

def linear_search(input, number_elements, search_term):
    """
    It takes an array, the number of elements in the array, and a search term, and returns the index of
    the search term in the array, or None if the search term is not in the array
    
    :param input: the list of numbers to search through
    :param number_elements: The number of elements in the input array
    :param search_term: The value you're looking for
    :return: The index of the search term.
    """
    for i in range(number_elements):
        if input[i] == search_term:
            return i
    return None

if __name__ == "__main__":
    example = [1, 30, 25, 12, 20, 2, 4, 7]
    search_number = 13
    print("This is an example for linear search algorithm")
    print("Initial array:")
    print(example)
    print("Looking for number:", search_number)
    print("Running...")
    result = linear_search(example, len(example), search_number)
    print("Position on array:")
    print(result)
