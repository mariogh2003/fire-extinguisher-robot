from utils.brick import EV3ColorSensor, wait_ready_sensors, Motor
from time import sleep
from normalize import *
from normalize_test import *
from path_finder import *

user_input = input("Enter coordinates: ")

input_list = user_input.split(',')

coordinate_tuples = []
letters = []

for i in range(0, len(input_list), 3):
    x, y, letter = int(input_list[i]), int(input_list[i + 1]), input_list[i + 2]
    coordinate_tuples.append((x, y))
    letters.append(letter)

motorR = Motor("A")
motorL = Motor("D")
motorB = Motor("B")
motorC = Motor("C")

COLOR_SENSOR_R = EV3ColorSensor(1)
COLOR_SENSOR_L = EV3ColorSensor(2)

current = (0, 0)
direction = "North"
on_green = False

cube_color = {'A': 'Blue', 'B': 'Yellow', 'C': 'Purple', 'D': 'Red', 'E': 'Orange', 'F': 'Green'}

wait_ready_sensors(True)  # Input True to see what the robot is trying to initialize! False to be silent.

print(current)


def go_straight():
    global coordinate_list, current, direction, on_green

    while True:
        color_data_R = COLOR_SENSOR_R.get_value()
        color_data_L = COLOR_SENSOR_L.get_value()

        if color_data_R is not None:  # If None is given, then data collection failed that time
            color_data_R.pop()
            RR, GR, BR = color_data_R

        if color_data_L is not None:  # If None is given, then data collection failed that time
            color_data_L.pop()
            RL, GL, BL = color_data_L

        if check_if_table_left(RL, GL, BL) and check_if_table_right(RR, GR, BR):
            motorR.set_power(-50)
            motorL.set_power(-55)
            on_green = False

        else:
            if check_if_green_left(RL, GL, BL) or check_if_green_right(RR, GR, BR):
                if not on_green:
                    update_coord()
                    on_green = True
                    motorR.set_power(0)
                    motorL.set_power(0)
                    break
                else:
                    motorR.set_power(-55)
                    motorL.set_power(-60)


            elif not check_if_table_left(RL, GL, BL):
                motorR.set_power(-20)
                motorL.set_power(0)
                on_green = False


            elif not check_if_table_right(RR, GR, BR):
                motorR.set_power(0)
                motorL.set_power(-20)
                on_green = False

        sleep(0.01)


def turn_right():
    global direction

    color_data_L = COLOR_SENSOR_L.get_value()

    if color_data_L is not None:  # If None is given, then data collection failed that time
        color_data_L.pop()
        RL, GL, BL = color_data_L

    while not (check_if_blue_left(RL, GL, BL) or check_if_red_left(RL, GL, BL)):
        color_data_L = COLOR_SENSOR_L.get_value()

        if color_data_L is not None:  # If None is given, then data collection failed that time
            color_data_L.pop()
            RL, GL, BL = color_data_L
        motorR.set_power(0)
        motorL.set_power(-55)
        sleep(0.01)

    if direction == "North" or direction == "NorthEast":
        direction = "East"
    elif direction == "South":
        direction = "West"
    elif direction == "West":
        direction = "North"
    elif direction == "East":
        direction = "South"

    motorR.set_power(0)
    motorL.set_power(0)
    print(direction)


def turn_left():
    global direction

    color_data_R = COLOR_SENSOR_R.get_value()

    if color_data_R is not None:  # If None is given, then data collection failed that time
        color_data_R.pop()
        RR, GR, BR = color_data_R

    while not (check_if_blue_right(RR, GR, BR) or check_if_red_right(RR, GR, BR)):
        color_data_R = COLOR_SENSOR_R.get_value()

        if color_data_R is not None:  # If None is given, then data collection failed that time
            color_data_R.pop()
            RR, GR, BR = color_data_R
        motorR.set_power(-55)
        motorL.set_power(0)
        sleep(0.01)

    if direction == "North":
        direction = "West"
    elif direction == "South":
        direction = "East"
    elif direction == "West":
        direction = "South"
    elif direction == "East" or direction == "NorthEast":
        direction = "North"

    motorR.set_power(0)
    motorL.set_power(0)
    print(direction)


def turn_around():
    global direction

    motorR.set_power(20)
    motorL.set_power(23)
    sleep(1.5)

    color_data_R = COLOR_SENSOR_R.get_value()

    if color_data_R is not None:  # If None is given, then data collection failed that time
        color_data_R.pop()
        RR, GR, BR = color_data_R
    
    motorR.set_power(-25)
    motorL.set_power(25)
    sleep(1)

    while not (check_if_blue_right(RR, GR, BR) or check_if_red_right(RR, GR, BR)):
        color_data_R = COLOR_SENSOR_R.get_value()

        if color_data_R is not None:  # If None is given, then data collection failed that time
            color_data_R.pop()
            RR, GR, BR = color_data_R
            
        motorR.set_power(-25)
        motorL.set_power(25)
            
        sleep(0.03)

    if direction == "North":
        direction = "South"
    elif direction == "South":
        direction = "North"
    elif direction == "West":
        direction = "East"
    elif direction == "East":
        direction = "West"

    motorR.set_power(0)
    motorL.set_power(0)
    print(direction)


def update_coord():
    global current
    x, y = current
    new_x = x
    new_y = y
    if direction == "North":
        new_y += 1
    if direction == "South":
        new_y -= 1
    if direction == "West":
        new_x -= 1
    if direction == "East":
        new_x += 1
    new_current = (new_x, new_y)
    current = new_current


def moveTo(target_coordinate, current_coordinate):
    target_x = target_coordinate[0]
    target_y = target_coordinate[1]

    current_x = current_coordinate[0]
    current_y = current_coordinate[1]

    if target_y > current_y:
        while not direction == "North":
            if direction == "West":
                turn_right()
            elif direction == "East":
                turn_left()
            elif direction == "South":
                turn_around()
    elif target_y < current_y:
        while not direction == "South":
            if direction == "East":
                turn_right()
            elif direction == "West":
                turn_left()
            elif direction == "North":
                turn_around()
    elif target_x > current_x:
        while not direction == "East":
            if direction == "North":
                turn_right()
            elif direction == "South":
                turn_left()
            elif direction == "West":
                turn_around()
    elif target_x < current_x:
        while not direction == "West":
            if direction == "South":
                turn_right()
            elif direction == "North":
                turn_left()
            elif direction == "East":
                turn_around()
    go_straight()
    print(current)


def move_tray(a, b, c, d):
    motorC.set_limits(a, b)
    motorC.set_position_relative(c)
    sleep(2)
    move_piston()
    sleep(1)
    motorC.set_position_relative(d)
    sleep(2)
    motorC.set_power(0)


def choose_cube(s):
    if s == 'A':
        move_tray(0, 0, 0, 0)

    elif s == 'D':
        move_tray(35, 360, -120, 120)

    elif s == 'F':
        move_tray(35, 365, -210, 210)

    elif s == 'C':
        move_tray(35, 360, -310, 310)

    elif s == 'B':
        move_tray(35, 360, -390, 390)

    elif s == 'E':
        move_tray(35, 360, -470, 470)


def move_piston():
    motorB.set_position_relative(360)
    sleep(1)
    motorB.set_power(0)


try:
    target = coordinate_tuples
    coordinate_list = generate_coordinate_list(target[0], target[1], target[2])

    print(coordinate_list)

    if coordinate_list[0] == (1, 0):
        color_data_L = COLOR_SENSOR_L.get_value()

        if color_data_L is not None:  # If None is given, then data collection failed that time
            color_data_L.pop()
            RL, GL, BL = color_data_L

        while not (check_if_red_left(RL, GL, BL)):
            color_data_L = COLOR_SENSOR_L.get_value()

            if color_data_L is not None:  # If None is given, then data collection failed that time
                color_data_L.pop()
                RL, GL, BL = color_data_L
            motorR.set_power(15)
            motorL.set_power(-25)
            sleep(0.01)

    for coords in coordinate_list:
        moveTo(coords, current)
        if current in target:
            index = target.index(current)
            motorR.set_power(0)
            motorL.set_power(0)
            sleep(0.2)
            motorR.set_power(20)
            motorL.set_power(24)
            sleep(0.4)
            motorR.set_power(0)
            motorL.set_power(0)
            sleep(0.2)
            choose_cube(letters[index])
        
    if direction == "West":
        turn_right()
        motorR.set_power(20)
        motorL.set_power(23)
        sleep(1)
        motorR.set_power(0)
        motorL.set_power(0)
        
    elif direction == "South":
        turn_around()
        go_straight()
        sleep(0.5)
        motorR.set_power(20)
        motorL.set_power(23)
        sleep(3.7)
        motorR.set_power(0)
        motorL.set_power(0)


except KeyboardInterrupt:
    motorR.set_power(0)
    motorL.set_power(0)