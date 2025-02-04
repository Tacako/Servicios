import pyautogui
import time
from datetime import datetime


def find_and_click(image_path, confidence=0.7):
    location = pyautogui.locateOnScreen(image_path, confidence=confidence)
    if location:
        pyautogui.click(*pyautogui.center(location))
        return True
    return False


def send_whatsapp_message():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = f"*SERVICIO EN PLATAFORMA*"
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
    # Coordenadas iniciales
    start_x, start_y = 792, 253
    # Coordenadas finales
    end_x, end_y = 1569, 815
    pyautogui.moveTo(start_x, start_y)
    time.sleep(1)
    pyautogui.mouseDown()
    pyautogui.moveTo(end_x, end_y)
    pyautogui.mouseUp()
    time.sleep(1)

while True:
    try:
        no_ace_image = pyautogui.locateOnScreen('Resources/noace.png', confidence= 0.7)
        if no_ace_image:
            find_and_click('Resources/noace.png')
            time.sleep(4)
            pyautogui.scroll(10)
            take_screen_shoot()
            if find_and_click('Resources/WhatsApp.png'):
                send_whatsapp_message()
                find_and_click('Resources/ListaDeServicios.png')
                pyautogui.hotkey('alt', 'left')
                time.sleep(50.4)
    except pyautogui.ImageNotFoundException:
        pass