import time
from datetime import datetime
import cv2
import numpy as np
import pyautogui


def find_image_on_screen(image_path2, confidence=0.8):
    screen = pyautogui.screenshot()
    screen = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2BGR)
    template = cv2.imread(image_path2, cv2.IMREAD_UNCHANGED)
    result = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if max_val >= confidence:
        return max_loc
    return None


def main(image_path, target_position, target_position1, wait_time=1):
    counter = 0

    while True:
        image_location = find_image_on_screen(image_path)
        if image_location:
            # Incrementa el contador
            counter += 1

            # Genera el mensaje
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            message = f"*TEST SERVICO EN PLATAFORMA*\nFecha y hora: {current_time}\nNumero de Notificaciones: {counter}"

            # Guarda la posición actual del mouse
            current_mouse_pos = pyautogui.position()

            # Mueve el mouse a la posición deseada y haz clic
            pyautogui.moveTo(target_positionWep[0], target_positionWep[1])
            pyautogui.click()

            pyautogui.moveTo(target_position2Mess[0], target_position2Mess[1])
            pyautogui.click()

            # Oprime Ctrl + V para pegar el mensaje
            pyautogui.typewrite(message)

            pyautogui.moveTo(target_position1Send[0], target_position1Send[1])
            pyautogui.click()

            # Regresa el mouse a la posición original
            pyautogui.moveTo(current_mouse_pos)

            # Espera un tiempo antes de volver a buscar la imagen
            time.sleep(wait_time)


if __name__ == "__main__":
    # Ruta de la imagen a buscar
    image_path = "Resources/noace.png"

    # Posición en la pantalla donde se hará el clic
    target_positionWep = (-182, 185)  # Reemplaza x e y con las coordenadas específicas

    target_position1Send = (-40, 1039)

    target_position2Mess = (-404, 1044)

    # Tiempo de espera entre cada chequeo en segundos
    wait_time = 60

    main(image_path, target_positionWep, target_position1Send,  wait_time)