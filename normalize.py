from utils.brick import  EV3ColorSensor, wait_ready_sensors, reset_brick
from time import sleep
from math import sqrt
import threading


COLOR_SENSOR_R = EV3ColorSensor(1)
COLOR_SENSOR_L = EV3ColorSensor(2)


wait_ready_sensors(True) # Input True to see what the robot is trying to initialize! False to be silent.


def normalize(R, G, B):
    sum_values = R + G + B
    
    v1 = R / sum_values
    v2 = G / sum_values
    v3 = B / sum_values
    
    return v1,v2,v3
       
def check_if_red_right(R, G, B):
    v1 = 0.789
    v2 = 0.123
    v3 = 0.088
    
    std1 = 0.1
    std2 = 0.1
    std3 = 0.1
    
    v1n, v2n, v3n = normalize(R, G, B)
    
    if v1 <= v1n + std1 and v1 >= v1n - std1 and v2 <= v2n + std2 and v2 >= v2n - std2 and v3 <= v3n + std3 and v3 >= v3n - std3:
        return True
    else:
        return False

def check_if_blue_right(R, G, B):
    v1 = 0.284
    v2 = 0.289
    v3 = 0.427
    
    std1 = 0.1
    std2 = 0.1
    std3 = 0.1
    
    v1n, v2n, v3n = normalize(R, G, B)
    
    if v1 <= v1n + std1 and v1 >= v1n - std1 and v2 <= v2n + std2 and v2 >= v2n - std2 and v3 <= v3n + std3 and v3 >= v3n - std3:
        return True
    else:
        return False

def check_if_green_right(R, G, B):
    v1 = 0.234
    v2 = 0.517
    v3 = 0.249
    
    std1 = 0.1
    std2 = 0.1
    std3 = 0.1
    
    v1n, v2n, v3n = normalize(R, G, B)
    
    if v1 <= v1n + std1 and v1 >= v1n - std1 and v2 <= v2n + std2 and v2 >= v2n - std2 and v3 <= v3n + std3 and v3 >= v3n - std3:
        return True
    else:
        return False


 
def check_if_table_right(R, G, B):
    v1 = 0.538
    v2 = 0.287
    v3 = 0.176
    
    std1 = 0.07
    std2 = 0.07
    std3 = 0.07
    
    v1n, v2n, v3n = normalize(R, G, B)
    
    if v1 <= v1n + std1 and v1 >= v1n - std1 and v2 <= v2n + std2 and v2 >= v2n - std2 and v3 <= v3n + std3 and v3 >= v3n - std3:
        return True
    else:
        return False 

def check_if_red_left(R, G, B):
    v1 = 0.771
    v2 = 0.144
    v3 = 0.084
    
    std1 = 0.1
    std2 = 0.1
    std3 = 0.1
    
    v1n, v2n, v3n = normalize(R, G, B)
    
    if v1 <= v1n + std1 and v1 >= v1n - std1 and v2 <= v2n + std2 and v2 >= v2n - std2 and v3 <= v3n + std3 and v3 >= v3n - std3:
        return True
    else:
        return False

def check_if_blue_left(R, G, B):
    v1 = 0.255
    v2 = 0.380
    v3 = 0.365
    
    std1 = 0.1
    std2 = 0.1
    std3 = 0.1
    
    v1n, v2n, v3n = normalize(R, G, B)
    
    if v1 <= v1n + std1 and v1 >= v1n - std1 and v2 <= v2n + std2 and v2 >= v2n - std2 and v3 <= v3n + std3 and v3 >= v3n - std3:
        return True
    else:
        return False

def check_if_green_left(R, G, B):
    v1 = 0.202
    v2 = 0.586
    v3 = 0.212
    
    std1 = 0.1
    std2 = 0.1
    std3 = 0.1
    
    v1n, v2n, v3n = normalize(R, G, B)
    
    if v1 <= v1n + std1 and v1 >= v1n - std1 and v2 <= v2n + std2 and v2 >= v2n - std2 and v3 <= v3n + std3 and v3 >= v3n - std3:
        return True
    else:
        return False

 
def check_if_table_left(R, G, B):
    v1 = 0.514
    v2 = 0.344
    v3 = 0.142
    
    std1 = 0.07
    std2 = 0.07
    std3 = 0.07
    
    v1n, v2n, v3n = normalize(R, G, B)
    
    if v1 <= v1n + std1 and v1 >= v1n - std1 and v2 <= v2n + std2 and v2 >= v2n - std2 and v3 <= v3n + std3 and v3 >= v3n - std3:
        return True
    else:
        return False