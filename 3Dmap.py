import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create a figure and a 3D Axes
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

print("Welcome to 3D Mapping with Python where you can make a 3D map using simple x, y and z co-ordinates ")
print("Enter the coordinates x, y, and z along with a value for the counter 'a' which should not be 1 until all the readings are over.")

# input data
a = 0
while(a!=1):
    x = int(input())
    y = int(input())
    z = int(input())
    a = int(input())
    ax.scatter(x, y, z, color='black')

plt.show()
