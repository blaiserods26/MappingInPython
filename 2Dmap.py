import matplotlib.pyplot as plt
arr = [[0]*1000 for i in range(1000)]
a = 0
print("Welcome to 2D Mapping with Python where you can make a 2D map using simple x and y co-ordinates ")
print("Enter the co-ordinates x and y and a the value for the counter 'a' which should not be 1 until all the readings are over.")
while(a!=1):
    x = int(input())
    y = int(input())
    a = int(input())
    arr[x][y] = 1
print(arr)    

plt.imshow(arr, cmap='binary')

plt.xlabel('X-direction')
plt.ylabel('Y-direction')
plt.title("2D MAP")

plt.show()
