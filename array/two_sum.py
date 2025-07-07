from typing import List

def brute_force(array: List[int]):
    max_profit: int = 0
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            if array[j] - array[i] > max_profit:
                max_profit = array[j] - array[i]
    return max_profit

def optimized(array: List[int]):
    max_value = min_value = array[0]
    pointer: int = 1

    max_profit: int = 0

    while pointer < len(array):
        if max_value < array[pointer]:
            max_value = array[pointer]
            max_profit = max(max_profit, max_value - min_value)
        if min_value > array[pointer]:
            min_value = max_value = array[pointer]
        pointer += 1
    return max_profit

if __name__ == "__main__":
    given_array: List[int] = [7,1,5,3,6,4,15]

    array_one: List[int] = given_array.copy()
    print(brute_force(array=array_one))

    array_two: List[int] = given_array.copy()
    print(optimized(array=array_two))
