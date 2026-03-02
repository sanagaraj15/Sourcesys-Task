import numpy as np

def create_matrix():
    matrix = np.array([[5, 10, 15],
                       [20, 25, 30],
                       [35, 40, 45]])
    return matrix


def calculate_sums(matrix):
    row_sum = np.sum(matrix, axis=1)
    col_sum = np.sum(matrix, axis=0)
    return row_sum, col_sum


def find_statistics(matrix):
    mean = np.mean(matrix)
    maximum = np.max(matrix)
    minimum = np.min(matrix)
    std_dev = np.std(matrix)
    return mean, maximum, minimum, std_dev


def multiply_matrix(matrix):
    return np.dot(matrix, matrix)


def transpose_matrix(matrix):
    return matrix.T


def filter_values(matrix):
    return matrix[matrix > 20]


def main():
    print("===== NUMPY FUNCTION PROGRAM =====\n")

    matrix = create_matrix()
    print("Original Matrix:\n", matrix)

    row_sum, col_sum = calculate_sums(matrix)
    print("\nRow-wise Sum:", row_sum)
    print("Column-wise Sum:", col_sum)

    mean, maximum, minimum, std_dev = find_statistics(matrix)
    print("\nMean:", mean)
    print("Max:", maximum)
    print("Min:", minimum)
    print("Standard Deviation:", std_dev)

    print("\nMatrix Multiplication:\n", multiply_matrix(matrix))
    print("\nTranspose:\n", transpose_matrix(matrix))

    print("\nFiltered Values (>20):", filter_values(matrix))

    print("\n===== PROGRAM COMPLETED =====")


if __name__ == "__main__":
    main()