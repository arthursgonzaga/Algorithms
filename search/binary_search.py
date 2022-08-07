import numpy as np

def binary_search(input, low, high, search_term):
    low_term = low
    high_term = high
    mid_term = int((low_term + high_term) / 2)

    if low_term > high_term:
        return None

    if input[mid_term] == search_term:
        return mid_term
    elif input[mid_term] < search_term:
        low_term = mid_term + 1
        return binary_search(input, low=low_term, high=high_term, search_term=search_term)
    else:
        high_term = mid_term - 1
        return binary_search(input, low=low_term, high=high_term, search_term=search_term)

if __name__ == "__main__":
    print("For this algorithm the array has to be sorted")
    example = [1, 2, 4, 6, 13, 20, 22, 30]
    search_number = 4
    print("This is an example for binary search algorithm")
    print("Initial array:")
    print(example)
    print("Looking for number:", search_number)
    print("Running...")
    result = binary_search(example, 0, len(example), search_number)
    print("Position on array:")
    print(result)
