for i in range(5):
    print("hello world")
for value in [1,3,5,7,9]:
    print (value)
for i in range(1,10,2):
    print(i)
import random
colors = ["red", "blue", "yellow", "green", "purple"]
for i in range(3):
    colors.append(random.choice(colors))
    print(colors)
import random
colors = []
for i in range(15):
    colors.append(random.choice(["red", "blue", "yellow", "green", "purple", "orange", "pink",]))
for color in colors:
    print(color)