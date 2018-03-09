# Import the Numpy package and give it the alias np
import numpy as np

my_array1 = np.array([1, 2, 3])
my_array2 = np.array([[2,1],[7,4],[5,2],[6,3]])
my_array3 = np.array([3, 3, 3])

print(my_array1)
print(my_array1.shape)
print(my_array1.sum())
print(type(my_array1))

print(my_array2)
print(my_array2.shape)
print(my_array2.sum())
print(type(my_array2))
print(type(my_array2.shape))

# Calculate sum of 2 vectors
print(my_array1 + my_array3)
# Calculate dot multiplication of 2 vectors
print(my_array1 * my_array3)

print(np.random.rand(5))
print(np.random.rand(3,2))

print("\n\n")
print("Generating a normal distribution of random numbers")
mu = int(input("Enter a mean: "))
std = int(input("Enter a standard deviation: "))
lgt = int(input("How many numbers would you like in the series?"))
normal_array = np.random.normal(mu, std, lgt)
print(normal_array)

print("\n\n")
print("Calculating mean and median")

sample = [3, 75, 98, 2, 10, 3, 14, 99, 44, 25, 31, 100, 356, 4, 23, 55, 327, 64, 6, 20]

mean = np.mean(sample)
median = np.median(sample)

print(f"Mean: {mean}. Median: {median}")

print(np.mean(my_array1))
print(np.mean(my_array2))
print(np.median(my_array2))
print(np.mean(normal_array))
print(np.median(normal_array))
