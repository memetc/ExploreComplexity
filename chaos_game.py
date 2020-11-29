# Chaos Game
# 
#
# memetc
import matplotlib.pyplot as plt
import random

# Direction points are (5,5) - (15,25) -(25,5)
direction_point1= (5,5)
direction_point2= (15,25)
direction_point3= (25,5)
current_location = (10,10)
print(tuple(map(lambda i: i / 2, direction_point2)))
def move(current, direction):
    rep = tuple(map(lambda i, j: i - j, direction, current))
    rep = tuple(map(lambda i: i / 2, rep))
    rep = tuple(map(lambda i, j: i + j, rep, current))
    return rep

iteration = 0
x_coordinates = [current_location[0]]
y_coordinates = [current_location[1]]
plt.scatter(x_coordinates, y_coordinates)
while(iteration != 1000):
    iteration +=1
    direction = random.random()
    if(direction <= 0.33):
        current_location = move(current_location,direction_point1)
    elif(direction <= 0.66):
        current_location = move(current_location, direction_point2)
    else:
        current_location = move(current_location,direction_point3)

    x_coordinates.append(current_location[0])
    y_coordinates.append(current_location[1])
    plt.scatter(x_coordinates, y_coordinates)
    # plt.show(block=False)
    plt.pause(0.25)
    # plt.close()
plt.show(block=False)