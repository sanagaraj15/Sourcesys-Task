import numpy as np

def main():
    print("===== NUMPY LARGE OPERATIONS PROGRAM =====\n")

    print("1. Creating Arrays")
    arr1 = np.arange(1, 21)
    arr2 = np.linspace(10, 50, 20)

    print("Array 1:", arr1)
    print("Array 2:", arr2)

    print("\n2. Reshaping Arrays")
    matrix1 = arr1.reshape(4, 5)
    matrix2 = arr2.reshape(4, 5)

    print("Matrix 1:\n", matrix1)
    print("Matrix 2:\n", matrix2)

    print("\n3. Arithmetic Operations")
    print("Addition:\n", matrix1 + matrix2)
    print("Subtraction:\n", matrix2 - matrix1)
    print("Multiplication:\n", matrix1 * matrix2)
    print("Division:\n", matrix2 / matrix1)

    print("\n4. Statistical Operations")
    print("Mean:", np.mean(matrix1))
    print("Median:", np.median(matrix1))
    print("Standard Deviation:", np.std(matrix1))
    print("Sum:", np.sum(matrix1))
    print("Column-wise Sum:", np.sum(matrix1, axis=0))
    print("Row-wise Sum:", np.sum(matrix1, axis=1))

    print("\n5. Matrix Operations")
    A = np.random.randint(1, 10, (3, 3))
    B = np.random.randint(1, 10, (3, 3))

    print("Matrix A:\n", A)
    print("Matrix B:\n", B)

    print("Matrix Multiplication:\n", np.dot(A, B))
    print("Transpose of A:\n", A.T)
    print("Determinant of A:", np.linalg.det(A))
    print("Inverse of A:\n", np.linalg.inv(A))

    print("\n6. Broadcasting Example")
    vector = np.array([1, 2, 3, 4, 5])
    print("Vector:", vector)
    print("Matrix1 + Vector:\n", matrix1 + vector)

    print("\n7. Filtering Values > 10")
    filtered = matrix1[matrix1 > 10]
    print(filtered)

    print("\n8. Random Data Analysis")
    random_data = np.random.normal(loc=50, scale=10, size=1000)
    print("Random Data Mean:", np.mean(random_data))
    print("Random Data Max:", np.max(random_data))
    print("Random Data Min:", np.min(random_data))

    print("\n===== PROGRAM COMPLETED =====")


if __name__ == "__main__":
    main()