import pyautogui
import time

def baixarArquivo():
    time.sleep(1)
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.press("space")
    time.sleep(1)
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(2)

pyautogui.alert("O programa vai começar")

# Definir o número total de repetições
total_repeticoes = 515

# Loop para realizar os downloads
for i in range(1, total_repeticoes + 1):
    baixarArquivo()
    if i % 15 == 0 and i != total_repeticoes:
        pyautogui.alert("Pausa de 15 segundos. Por favor, não toque no teclado ou mouse.")
        time.sleep(15)

pyautogui.alert("O programa acabou")
        