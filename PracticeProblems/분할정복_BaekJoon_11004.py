N, K = map(int, input().split())
arr = list(map(int, input().split()))

def swap(i,j):

    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def quicksort(start, end, k):

    left = start
    right = end

    pivot = arr[(start + end) // 2 ]

    while left <= right:
        while arr[left] < pivot:
            left += 1

        while arr[right] > pivot:
            right -= 1

        if left <= right:
            swap(left, right)

            left += 1
            right -= 1
    
    if start <= k <= right:
        quicksort(start, right, k)

    if left <= k <= end:
        quicksort(left, end, k)

quicksort(0, N-1, K-1)
print(arr[K-1])
            