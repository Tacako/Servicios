import pyautogui
import time
from datetime import datetime


def find_and_click(image_path, confidence=0.8):
    location = pyautogui.locateOnScreen(image_path, confidence=confidence)
    if location:
        pyautogui.click(*pyautogui.center(location))
        return True
    return False

def handle_login():
    if find_and_click('Resources/Login.png') or find_and_click('Resources/LoginCaducado.png'):
        time.sleep(2)
        find_and_click('Resources/Confirm.png')
        time.sleep(2)
        find_and_click('Resources/Seguimineto.png')
    elif find_and_click('Resources/Indicadores.png'):
        find_and_click('Resources/Seguimineto.png')

counter = 0
while True:
    time.sleep(1)
    try:
            handle_login()
    except pyautogui.ImageNotFoundException:
        time.sleep(0.1)