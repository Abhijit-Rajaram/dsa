from typing import List

def merge(array: list[int], low: int, mid: int, high: int):
    temp: List[int] = []

    left: int = low
    right: int = mid + 1

    while left <= mid and right <= high:
        if array[left] < array[right]:
            temp.append(array[left])
            left += 1
        else:
            temp.append(array[right])
            right += 1
    while left <= mid:
        temp.append(array[left])
        left += 1
    while right <= high:
        temp.append(array[right])
        right += 1
   
    for i in range(len(temp)):
        array[i + low] = temp[i]
    

def mergeSort(array: List[int], low: int, high: int):
    if low == high:
        return
    mid: int = (low + high)//2
    mergeSort(array,low,mid)
    mergeSort(array,mid+1,high)
    merge(array, low, mid, high)


if __name__ == "__main__":
    array: List[int] = [4,6,8,2,3,7,1]
    n: int = len(array)
    print("Original Array",array)
    mergeSort(array,0,n-1)
    print("Sorted Array",array)
