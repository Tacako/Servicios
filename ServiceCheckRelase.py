import pyautogui
import time
from datetime import datetime


def find_and_click(image_path, confidence=0.7, timeout=5, check_change=None):
    start_time = time.time()
    while time.time() - start_time < timeout:
        location = pyautogui.locateOnScreen(image_path, confidence=confidence)
        if location:
            pyautogui.click(*pyautogui.center(location))
            time.sleep(2)
            if check_change:
                if verify_screen(check_change):
                    return True
        time.sleep(0.5)
    return False


def verify_screen(image_path, confidence=0.7, timeout=5):
    start_time = time.time()
    while time.time() - start_time < timeout:
        if pyautogui.locateOnScreen(image_path, confidence=confidence):
            return True
        time.sleep(0.5)
    return False


def send_whatsapp_message():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = "*SERVICIO EN PLATAFORMA*"
    pyautogui.typewrite(message)
    pyautogui.hotkey('alt', 'enter')
    message = f"Fecha y hora: {current_time}"
    pyautogui.typewrite(message)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(2)


def take_screen_shoot():
    pyautogui.hotkey('win', 'shift', 's')
    start_x, start_y = 516, 264
    end_x, end_y = 1000, 728
    pyautogui.moveTo(start_x, start_y)
    time.sleep(1)
    pyautogui.mouseDown()
    pyautogui.moveTo(end_x, end_y)
    pyautogui.mouseUp()
    time.sleep(1)


while True:
    try:
        if pyautogui.locateOnScreen('Resources/noace.png', confidence=0.7):
            print("Intentando abrir servicio...")
            if find_and_click('Resources/noace.png', check_change='Resources/noaceOpen.png'):
                time.sleep(1)
                pyautogui.scroll(1000)
                take_screen_shoot()
            if find_and_click('Resources/WhatsApp.png', check_change='Resources/WhatsAppOpen.png'):
                send_whatsapp_message()
            if find_and_click('Resources/ListaDeServicios.png', check_change='Resources/ListaDeServiciosOpen.png'):
                pyautogui.hotkey('alt', 'left')
                time.sleep(49.4)

    except pyautogui.ImageNotFoundException:
        pass
