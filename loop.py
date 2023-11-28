import pyautogui
import time

## Função de cliques para downloads
def download():
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.press("tab")      
    time.sleep(2)
    pyautogui.press("space")
    time.sleep(1.5)
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.press("tab")
    time.sleep(1) 
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.press("tab")
    time.sleep(2)
    pyautogui.press('space')
    time.sleep(1.5)
    pyautogui.press("tab")                  
    time.sleep(2)
    pyautogui.press("space")
    time.sleep(1.5)

pyautogui.alert("O programa vai começar")
# Repetir a função download 515 vezes
for _ in range(515):
    download()
pyautogui.alert("O programa terminou")