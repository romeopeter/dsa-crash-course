'''The number of operation (time) grows linearly with input size: 0(n)'''
def sum_element(arr):
    total = 0

    for num in arr:
        total += num

    return total

arr = [1, 2, 3, 4, 5]

print(sum_element(arr))