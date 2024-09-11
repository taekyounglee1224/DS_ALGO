def binary_search(data, item, low, high):

    location = -1   # Initialize with -1
    while low <= high and location == -1:
        mid = (low + high) // 2     # Integer division to get the middle index

        if item == data[mid]:
            location = mid  # Set location to the index where the item is found

        elif item < data[mid]:
            high = mid - 1  # Narrow the search to the left half

        else:
            low = mid + 1  # Narrow the search to the right half

    return location

data = [1,3,5,6,7,9,10,14,17,19] 
n=10 
location = binary_search(data,17,0,n-1) 
print(location)
