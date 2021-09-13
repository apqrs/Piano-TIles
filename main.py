import keyboard
# import ray
import pyautogui
import time
from threading import Thread




def main():
    a,b,c,d = get_coordinates()

    # ray.get([check1.remote(), check2.remote(), check3.remote(), check4.remote()])
    Thread(target= check1, args=(a,)).start()
    Thread(target= check2, args=(b,)).start()
    Thread(target= check3, args=(c,)).start()
    Thread(target= check4, args=(d,)).start()

    print()
    print("Program started")


def get_coordinates(n=4):
    points = []

    print("Getting corrdinates..")
    print("Move your curson to the first tile and press 'd'")
    while True:
        if keyboard.is_pressed("a"):
            points +=[pyautogui.position()]
            time.sleep(2)
            print(f"Capture a point at {points[-1]} {pyautogui.pixel(points[-1][0],points[-1][1])}")
        if len(points) == n:
            break
    return points

# ray.init()

# @ray.remote
def check1(point):
    a,b = point
    while True:
        
        if pyautogui.pixel(a,b)[0] < 10 and pyautogui.pixel(a,b)[1] < 10 and pyautogui.pixel(a,b)[2] < 10:
            pyautogui.click(a,b)
        # time.sleep(1)

        if keyboard.is_pressed("q"):
            exit()

# @ray.remote
def check2(point):
    a,b = point
    while True:
        
        if pyautogui.pixel(a,b)[0] < 10 and pyautogui.pixel(a,b)[1] < 10 and pyautogui.pixel(a,b)[2] < 10:
            pyautogui.click(a,b)
         # time.sleep(1)

        if keyboard.is_pressed("q"):
            exit()

# @ray.remote
def check3(point):
    a,b = point
    while True:
        
        if pyautogui.pixel(a,b)[0] < 10 and pyautogui.pixel(a,b)[1] < 10 and pyautogui.pixel(a,b)[2] < 10:
            pyautogui.click(a,b)
         # time.sleep(1)

        if keyboard.is_pressed("q"):
            exit()

# @ray.remote
def check4(point):
    a,b = point
    while True:
        
        if pyautogui.pixel(a,b)[0] < 10 and pyautogui.pixel(a,b)[1] < 10 and pyautogui.pixel(a,b)[2] < 10:
            pyautogui.click(a,b)
         # time.sleep(1)

        if keyboard.is_pressed("q"):
            exit()



if __name__=="__main__":
    main()