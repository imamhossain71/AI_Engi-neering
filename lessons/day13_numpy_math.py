import numpy as np

# Sample array
arr = np.array([10, 20, 30, 40, 50])

print("------ Array ------")
print(arr)

# 1. Basic Math Operations
print("\n------ Math Operations ------")
print("Add 5:", arr + 5)
print("Multiply by 2:", arr * 2)
print("Square:", arr ** 2)

# 2. Statistics
print("\n------ Statistics ------")
print("Mean:", np.mean(arr))
print("Median:", np.median(arr))
print("Standard Deviation:", np.std(arr))
print("Variance:", np.var(arr))
print("Min:", np.min(arr))
print("Max:", np.max(arr))

# 3. 2D Array (Matrix)
matrix = np.array([[1,2],[3,4]])
print("\n------ Matrix ------")
print(matrix)

# Matrix Transpose
print("\nTranspose:\n", matrix.T)

# Matrix Multiplication
matrix2 = np.array([[5,6],[7,8]])
print("\nMatrix Multiplication:\n", np.dot(matrix, matrix2))

# Determinant
print("\nDeterminant:", np.linalg.det(matrix))

# Inverse Matrix
print("\nInverse:\n", np.linalg.inv(matrix))

# Eigenvalues & Eigenvectors
values, vectors = np.linalg.eig(matrix)
print("\nEigenvalues:", values)
print("Eigenvectors:\n", vectors)
# ---------------- Task 1: Statistics ----------------
print("------ Task 1: Statistics ------")
arr = np.random.randint(10, 100, size=20)  # 20 random integers between 10 and 100
print("Array:", arr)

print("Mean:", np.mean(arr))
print("Median:", np.median(arr))
print("Variance:", np.var(arr))
print("Standard Deviation:", np.std(arr))
print("Min:", np.min(arr))
print("Max:", np.max(arr))
print("Range:", np.max(arr) - np.min(arr))


# ---------------- Task 2: Matrix Operations ----------------
print("\n------ Task 2: Matrix Operations ------")
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
print("Matrix A:\n", A)

# Transpose
print("Transpose of A:\n", A.T)

# Another 3x3 matrix
B = np.array([[9, 8, 7],
              [6, 5, 4],
              [3, 2, 1]])
print("Matrix B:\n", B)

# Multiplication
print("Matrix Multiplication (A x B):\n", np.dot(A, B))

# Determinant (Note: det of A will be 0 since it's singular)
print("Determinant of A:", np.linalg.det(A))

# To show inverse, let's use a non-singular matrix
C = np.array([[2, 1, 1],
              [1, 3, 2],
              [1, 0, 0]])
print("Matrix C:\n", C)
print("Determinant of C:", np.linalg.det(C))
print("Inverse of C:\n", np.linalg.inv(C))


# ---------------- Task 3: Eigenvalues & Eigenvectors ----------------
print("\n------ Task 3: Eigenvalues & Eigenvectors ------")
values, vectors = np.linalg.eig(C)
print("Eigenvalues:", values)
print("Eigenvectors:\n", vectors)


# ---------------- Task 4: Solve Linear Equations ----------------
print("\n------ Task 4: Solve Linear Equations ------")
A = np.array([[2, 1],
              [1, 3]])
b = np.array([8, 13])

solution = np.linalg.solve(A, b)
print("Solution of Ax = b:", solution)