import pyautogui

import time

pyautogui.alert("O código vai começar. Não utilize nada do computador até o código finalizar!")

pyautogui.PAUSE = 0.5

# Abrir o Google Drive no computador

pyautogui.press("winleft")

pyautogui.write("chrome")

pyautogui.press("enter")

time.sleep(2)

pyautogui.write("https://account.docusign.com/")

pyautogui.press("enter")
time.sleep(1)
#localizar login
pyautogui.moveTo(870,481)
pyautogui.write("lucas.a.souza@hotmail.com")
pyautogui.press("enter")
time.sleep(1)
pyautogui.write("Lucas30092004")
pyautogui.press("enter")

# Esperar alguns segundos

time.sleep(5)

pyautogui.alert("O código foi finalizado. Você já pode utilizar o computador!")