import numpy as np

# Zeros and Ones
a = np.zeros((3, 3))   # 3x3 matrix full of zeros
b = np.ones((2, 4))    # 2x4 matrix full of ones

# Identity matrix
c = np.eye(4)          # 4x4 identity matrix

# Random numbers
d = np.random.rand(3, 3)    # Uniform distribution (0 to 1)
e = np.random.randn(3, 3)   # Normal distribution (mean=0, std=1)

print("Zeros:\n", a)
print("Ones:\n", b)
print("Identity:\n", c)
print("Random Uniform:\n", d)
print("Random Normal:\n", e)
arr = np.arange(1, 11)   # [1,2,...10]

# Slicing
print(arr[2:7])    # elements 3rd to 7th
print(arr[::-1])   # reverse array

# Boolean indexing
print(arr[arr > 5])   # all elements greater than 5
x = np.array([1, 2, 3])
y = np.array([10])

print(x + y)   # [11, 12, 13]
data = np.array([2, 4, 6, 8, 10])

print("Sum:", np.sum(data))
print("Mean:", np.mean(data))
print("Standard Deviation:", np.std(data))
print("Variance:", np.var(data))
print("Max:", np.max(data))
print("Min:", np.min(data))
arr = np.arange(1, 13)   # 1 to 12
print("Original:", arr)

reshaped = arr.reshape(3, 4)   # 3 rows, 4 columns
print("Reshaped:\n", reshaped)

flattened = reshaped.flatten()
print("Flattened:", flattened)
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

# Horizontal and Vertical stacking
h_stack = np.hstack((a, b))
v_stack = np.vstack((a, b))

print("Horizontal Stack:\n", h_stack)
print("Vertical Stack:\n", v_stack)

# Splitting
arr = np.arange(1, 13).reshape(3, 4)
print("Original Array:\n", arr)

split = np.hsplit(arr, 2)   # split into 2 parts column-wise
print("Split Array Part 1:\n", split[0])
print("Split Array Part 2:\n", split[1])
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Matrix multiplication
print("Matrix Multiplication:\n", np.dot(A, B))

# Determinant
print("Determinant of A:", np.linalg.det(A))

# Inverse
print("Inverse of A:\n", np.linalg.inv(A))
