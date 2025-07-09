import numpy as np

def matrix_mul():
    n = int(input("Enter size of matrix: "))
    A = [list(map(float, input().split())) for _ in range(n)]
    A = np.array(A)

    m = int(input("Enter power m: "))
    A_power_m = np.linalg.matrix_power(A, m)
    return(A_power_m)


print(matrix_mul())
