'''Nested loops over the same data cause quadratic growth: 0(n square)'''
def print_pairs(arr):
    for i in arr:
        for j in arr:
            print(f"{i}, {j}")

arr = [1, 2, 3]

print_pairs(arr)