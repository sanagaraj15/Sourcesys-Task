import numpy as np

def main():
    print("===== NUMPY 2D ARRAY PROGRAM =====\n")

    matrix = np.array([[10, 20, 30],
                       [40, 50, 60],
                       [70, 80, 90]])

    print("Original Matrix:\n", matrix)

    print("\nRow-wise Sum:", np.sum(matrix, axis=1))
    print("Column-wise Sum:", np.sum(matrix, axis=0))

    matrix2 = np.array([[1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9]])

    print("\nSecond Matrix:\n", matrix2)
    print("Addition:\n", matrix + matrix2)

    print("\nMatrix Multiplication:\n", np.dot(matrix, matrix2))

    print("\nTranspose of Matrix:\n", matrix.T)

    print("\nMaximum Value:", np.max(matrix))
    print("Minimum Value:", np.min(matrix))

    print("\nDeterminant:", np.linalg.det(matrix))

    print("\nValues greater than 50:", matrix[matrix > 50])

    print("\nMean:", np.mean(matrix))
    print("Standard Deviation:", np.std(matrix))

    print("\n===== PROGRAM COMPLETED =====")

if __name__ == "__main__":
    main()