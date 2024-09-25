def merge_sort(arr):
    def sort(low, high):
        if high - low < 2:
            return 

        mid = (low + high)//2
        sort(low, mid)
        sort(mid, high)
        merge(low, mid, high)

    
    def merge(low, mid, high):
        temp = []
        left, right = low, mid

        while left < mid and right < high:
            if arr[left] < arr[right]:
                temp.append(arr[left])
                left += 1

            else:
                temp.append(arr[right])
                right += 1

        while left < mid:
            temp.append(arr[left])
            left += 1

        while right < high:
            temp.append(arr[right])
            right += 1

        for i in range(low, high):
            arr[i] = temp[i -low]

        
    return sort(0, len(arr))


s=[3,5,2,9,10,14,4,8] 
merge_sort(s) 
print(s)
