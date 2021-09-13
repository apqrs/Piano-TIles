import keyboard
import ray
import pyautogui
import time

def get_coordinates(n):
    points = []

    print("Getting corrdinates..")
    print("Move your curson to the first tile and press 'd'")
    while True:
        if keyboard.is_pressed("a"):
            points +=[pyautogui.position()]
            time.sleep(2)
            print(f"Capture a point at {points[-1]}")
        if len(points) == n:
            break
    return points

print(get_coordinates(4))