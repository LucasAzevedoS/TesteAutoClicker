import pyautogui
import time

def tab():
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.alert(f"Download concluído para o documento {counter}")


pyautogui.alert("O programa ja vai iniciar")
pyautogui.press("alt", "tab")
time.sleep(1)

for _ in range():
    tab()

pyautogui.alert("O programa foi encerrado")