'''Check if a list contains duplicates and analyze its complexity.'''
def has_duplicates(arr):
    seen = set()
    for num in arr:
        if(num in seen):
            return True
        seen.add(num)
    return False

# Example
print(has_duplicates([1, 2, 3, 4, 5]))  # False
print(has_duplicates([1, 2, 3, 4, 1]))  # True