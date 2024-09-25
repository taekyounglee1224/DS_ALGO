def partition(S, p, q):
    pivot = S[p]

    low = p + 1
    high = q

    while low <= high:
        while S[low] < pivot:
            low += 1

        while S[high] > pivot:
            high -= 1

        if low <= high:
            temp = S[low]
            S[low] = S[high]
            S[high] = temp

    temp = S[p]
    S[p] = S[high]
    S[high] = temp

    return high

def quick_sort(S, left, right):
    if left <= right:
        pivot = partition(S, left, right)

        quick_sort(S, left, pivot - 1)
        quick_sort(S, pivot + 1, right)

    
s=[3,5,2,9,10,14,4,8] 
quick_sort(s, 0, len(s)-1)
print(s)


