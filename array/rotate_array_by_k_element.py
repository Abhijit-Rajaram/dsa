from typing import List

def bruteForce(array: List[int], k: int) -> List[int]:
    array_size = len(array)

    if array_size == k:
        return array
    
    if k > array_size:
        k = k % array_size

    temp: List[int] = array[:k]

    for i in range(k,array_size):
        array[i-k] = array[i]

    for i in range(0, k):
        array[array_size - k + i] = temp[i]
    return array


def optimalSolution(array: List[int], k: int) -> List[int]:
    array_size = len(array)

    if array_size == k:
        return array
    
    if k > array_size:
        k = k % array_size
    
    def reverse(array: List[int], start: int, end: int):
        left: int = start
        right: int = end

        while right > left:
            array[left], array[right] = array[right], array[left]
            left = left + 1
            right = right - 1
    
    reverse(array=array,start=0, end=k-1)
    reverse(array=array,start=k, end=array_size-1)
    reverse(array=array, start=0, end=array_size - 1)

    return array

if __name__ == "__main__":
    array: List[int] = [1,2,3,4,5,6,7]
    k: int = 3
    
    array_one: List[int] = array.copy()
    print(array,bruteForce(array=array_one,k=k))

    array_two: List[int] = array.copy()
    print(array,optimalSolution(array=array_two,k=k))
