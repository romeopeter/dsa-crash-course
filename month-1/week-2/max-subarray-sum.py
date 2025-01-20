"""Find the maximum sum of a sub-array size of K"""

def max_subarray_sum(arr, k):
    n = len(arr)
    if n < k:
        return None  # Not enough element

    max_sum = current_sum = sum(arr[:k])

    for i in range(k, n):
        current_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, current_sum)

    return max_sum

arr = [2, 1, 5, 1, 3, 2]

print(max_subarray_sum(arr, 3)) # Output: 9 (5+1+3)

