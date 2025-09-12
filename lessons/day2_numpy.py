# Day 2 – NumPy Practice
import numpy as np  
# numpy import 

# 1️⃣ Array creation
arr1 = np.array([1, 2, 3, 4, 5])
print("1D Array:", arr1)
# 1D array 

arr2 = np.array([[1,2,3],[4,5,6]])
print("2D Array:\n", arr2)
# 2D array 
arr4 = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print("3D Array:\n", arr4)

# 2️⃣ Array attributes
print("Shape of arr2:", arr2.shape) # (rows, columns)
print("Data type of arr2:", arr2.dtype)
print("Number of dimensions:", arr2.ndim)
print("Total elements:", arr2.size)

# 3️⃣ Array operations
arr3 = np.array([10, 20, 30, 40])
print("Original array:", arr3)
print("Add 5:", arr3 + 5)
print("Multiply by 2:", arr3 * 2)
print("Square:", arr3 ** 2)

# 4️⃣ Indexing & Slicing
print("First element:", arr1[0])
print("Last two elements:", arr1[-2:])
print("2D array first row:", arr2[0, :])
print("2D array last column:", arr2[:, -1])

# 5️⃣ Useful functions
print("Zeros:", np.zeros(5))      # 5 zeros
print("Ones:", np.ones((2,3)))    # 2x3 ones
print("Arange:", np.arange(0, 10, 2)) # 0 to 10 step 2
print("Linspace:", np.linspace(0,1,5)) # 5 points between 0 and 1
#homework
array= np.array([5,10,15,20,25])
print("Array:", array*3)
array2=np.array([[1,2,3],[5,6,7]])
print("Array2 first column:", array2[:,0])
array3=np.random.randint(1,50,5)
print("Random Array:", array3)




