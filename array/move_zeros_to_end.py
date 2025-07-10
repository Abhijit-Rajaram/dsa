from typing import List

def bruteForce(array: List[int]) -> List[int]:
    temp: List[int] = []
    no_of_zeroes = 0
    array_size: int = len(array)

    for i in range(array_size):
        if array[i] != 0:
            temp.append(array[i])
        else:
            no_of_zeroes += 1

    if no_of_zeroes == 0:
        return array
    
    for i in range(no_of_zeroes):
        temp.append(0)
    
    for i in range(array_size):
        array[i] = temp[i]

    return array


def optimalSolution(array: List[int]) -> List[int]:
    array_size: int = len(array)

    left: int = 0
    right: int = 1

    while right < array_size:
        if array[left] != 0:
            left += 1
            right += 1
            continue

        if array[left] == 0 and array[right] == 0:
            right += 1
            continue

        
        array[right], array[left] = array[left], array[right]
        right += 1
        left += 1

    return array


if __name__ == "__main__":
    array: List[int] = [1,2,0,3,0,0,4,5,0,6,7]
    k: int = 3
    
    array_one: List[int] = array.copy()
    print(array,bruteForce(array=array_one))

    array_two: List[int] = array.copy()
    print(array,optimalSolution(array=array_two))
