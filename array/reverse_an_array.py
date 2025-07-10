from typing import List

def reverse_array_inplace(array: List[int]) -> List[int]:
    """
    Reverses the array in-place using the two-pointer approach.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    left, right = 0, len(array) - 1
    while left < right:
        array[left], array[right] = array[right], array[left]
        left += 1
        right -= 1
    return array


def reverse_array_using_recursive(array: List[int], left: int, right: int) -> List[int]:
    """
    Reverses the array in-place using recursion.
    Time Complexity: O(n)
    Space Complexity: O(n) due to recursion stack
    """
    if left >= right:
        return array
    array[left], array[right] = array[right], array[left]
    return reverse_array_using_recursive(array, left + 1, right - 1)


def reverse_array_using_slicing(array: List[int]) -> List[int]:
    """
    Reverses the array using Python's slicing.
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    return array[::-1]


# 4. List Comprehension with range()
def reverse_array_using_list_comprehension(array: List[int]) -> List[int]:
    """
    Reverses the array using list comprehension and range().
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    return [array[i] for i in range(len(array) - 1, -1, -1)]


if __name__ == "__main__":
    original_array: List[int] = [1, 2, 3, 4, 5]

    print("Original Array:", original_array)

    # Make copies since some methods reverse in-place
    array1 = original_array.copy()
    array2 = original_array.copy()
    array3 = original_array.copy()
    array4 = original_array.copy()

    print("Iterative Reverse         : ", reverse_array_inplace(array1))
    print("Recursive Reverse         : ", reverse_array_using_recursive(array2, 0, len(array2) - 1))
    print("Slicing Reverse           : ", reverse_array_using_slicing(array3))
    print("List Comprehension Reverse: ", reverse_array_using_list_comprehension(array4))
