import numpy as np

# Calculate BMI for 5 people using lists and numpy arrays
height = [1.73, 1.68, 1.71, 1.89, 1.79]
weight = [65.4, 59.2, 63.6, 88.4, 68.7]
bmi = []

for i in range(len(height)):
    bmi.append((weight[i] / height[i] ** 2))
print(bmi)

# Convert lists to numpu arrays and perform element-by-element division
np_height = np.array(height)
np_weight = np.array(weight)
np_bmi = np_weight / np_height ** 2

print(np_bmi)
print(np_bmi[2])        # Access item at position 2
print(np_bmi > 21.5)    # Return ndarray of Booleans reflecting element satisfying condition
print(np_bmi[np_bmi > 21.5])

print(np_height + 10)

baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

# Create a 2D numpy array from baseball: np_baseball
np_baseball =np.array(baseball)
# Print out the type of np_baseball
print(type(np_baseball))
# Print out the shape of np_baseball
print(np_baseball.shape)

np_mat = np.array([[1, 2],
                   [3, 4],
                   [5, 6]])
print(np_mat * 2)
print(np_mat + np.array([10, 10]))
print(np_mat + np_mat)
print(np_mat * np.array([10, 1]))


x = [1, 4, 8, 10, 12]
y = [3, 6, 7, 1, 78]
print(np.mean(x))
print(np.median(x))
xy_np = np.array([[x],[y]])
print(np.mean(xy_np))
print(np.median(xy_np))

a = np.matrix([[1,1],[2,2],[3,3]])
print(a)
print(type(a))
print(a.T)

b = np.array([[1,1],[2,2],[3,3]])
print(b)
print(type(b))
print(b.T)

c = np.matrix([[4, 5], [3, 10]])
d = c.I
print(d)
print(np.dot(c,d)           # The identity matrix
