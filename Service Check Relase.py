import pyautogui
import time
from datetime import datetime


def find_and_click(image_path, confidence=0.7):
    location = pyautogui.locateOnScreen(image_path, confidence=confidence)
    if location:
        pyautogui.click(*pyautogui.center(location))
        return True
    return False


def send_whatsapp_message(counter):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = f"*TEST SERVICO EN PLATAFORMA*\nFecha y hora: {current_time}\nNumero de Notificaciones: {counter}"
    pyautogui.typewrite(message)
    pyautogui.press('enter')



counter = 0
while True:
    time.sleep(1)
    try:
        no_ace_image = pyautogui.locateOnScreen('Resources/noace.png', confidence=0.7)
        if no_ace_image:
            print(pyautogui.center(no_ace_image))

            if find_and_click('Resources/WhatsAppLogo.png'):
                counter += 1
                send_whatsapp_message(counter)
                find_and_click('Resources/ListaDeServicios.png')
                time.sleep(60)

    except pyautogui.ImageNotFoundException:
        time.sleep(0.1)