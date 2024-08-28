import re

X = 0
Y = 0
direction = 90
movement = []
arrow_location = []


def calculate_movement():
    global X, Y, direction
    print("Please provide movement:")
    movement = input()
    movement_main = re.findall(r'\D+', movement)
    movement_step = re.findall(r'\d+', movement) 
    movement_step = list(map(int, movement_step))

    for step, item in zip(movement_step, movement_main):
        
        if 'R' in item:
            for i in range(item.count('R')):
                direction = int(direction) + 90


        if 'L' in item:
            for j in range(item.count('L')):
                direction = int(direction) - 90

        if type(step) is int:
            
            if direction == 90:
                X = X
                Y = Y + step
                arrow_direction = "North"

            if direction == 180:
                X = X + step
                Y = Y
                arrow_direction = "East"

            if direction == 270 or direction == -90:
                X = X
                Y = Y - step
                arrow_direction = "South"

            if direction == 0 or direction == -180:
                X = X - step
                Y = Y
                arrow_direction = "West"

    print("X :" + str(X), "Y :" + str(Y), "Direction :" + str(arrow_direction))


calculate_movement()