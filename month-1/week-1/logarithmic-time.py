'''Number of operation increases slowly in respect to input size increase: 0(log n)

Often occurs in divide-and-conquer algorithmic, like binary search'''
def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if (arr[mid] == target):
            return target
        elif (arr[mid] < target):
            low = mid + 1
        else:
            high = mid - 1
    
    return -1

arr = [1, 3, 5, 7, 9]
print(binary_search(arr, 5))