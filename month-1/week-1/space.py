''' Measures the additional memory the algorithm uses relative to input size.'''
def create_matrix(n):
    # Creates n x n matrix
    return [[0] * n for _ in range(n)]

# 
print(create_matrix(3))