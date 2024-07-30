import sys

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    arr_left = merge_sort(arr[:mid])
    arr_right = merge_sort(arr[mid:])

    return merge(arr_left, arr_right)


def merge(left, right):
    sorted_arr = []
    idx1, idx2 = 0, 0

    while idx1 < len(left) and idx2 < len(right):
        if left[idx1] <= right[idx2]:
            sorted_arr.append(left[idx1])
            idx1 += 1
        else:
            sorted_arr.append(right[idx2])
            idx2 += 1
    
    while idx1 < len(left):
        sorted_arr.append(left[idx1])
        idx1 += 1

    return sorted_arr

N = int(input())
A = []

for i in range(N):
    A.append(int(input()))

sorted_A = merge_sort(A)

for idx in sorted_A:
    print(idx)