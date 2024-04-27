import random

# Open the output file
with open('output.txt', 'w') as f:
    # Generate random readings
    for i in range(500):  # Generate 500 readings
        x = random.randint(647, 652)  # Random x-coordinate
        y = i  # Incrementing y-coordinate
        a = 0  # Fixed third reading
        print(x, file=f)
        print(y, file=f)
        print(a, file=f)
    
    for j in range(500):  # Generate 500 readings
        x = random.randint(347, 352)  # Random x-coordinate
        y = j  # Incrementing y-coordinate
        a = 0  # Fixed third reading
        print(x, file=f)
        print(y, file=f)
        print(a, file=f)