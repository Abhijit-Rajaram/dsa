from typing import List

def brute_force(array: List[int], target: int) -> List[int]:
    """Brute Force O(n^2)"""
    if len(array) < 2:
        return [-1, -1]
    
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] + array[j] == target:
                return [i, j]
    return [-1, -1]

def optimized(array: List[int], target: int) -> List[int]:
    ...
    my_dict = {}
    for i in range(len(array)):
        current = target - array[i]
        if current in my_dict:
            return [my_dict[current], i]
        my_dict[array[i]] = i
    return [-1,-1]

if __name__ == "__main__":
    given_array: List[int] = [2,7,11,15]
    target: int = 22

    array_one: List[int] = given_array.copy()
    print(brute_force(array=array_one, target= target))

    array_two: List[int] = given_array.copy()
    print(optimized(array=array_two, target= target))
