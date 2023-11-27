import pyautogui
import time


def donwload(counter):
    pyautogui.press("tab")
    time.sleep(0.5)
    pyautogui.press("tab")
    time.sleep(0.5)
    pyautogui.press("tab")
    time.sleep(0.5)
    pyautogui.press("tab")
    time.sleep(0.5)
    pyautogui.press("tab")
    time.sleep(0.5)
    pyautogui.press("enter")
    time.sleep(0.5)
    pyautogui.press("tab")
    time.sleep(0.5)
    pyautogui.press("tab")
    time.sleep(0.5) 
    pyautogui.press("tab")
    time.sleep(0.5)
    pyautogui.press("tab")
    time.sleep(0.5)
    pyautogui.press('space')
    pyautogui.press("tab")                  
    time.sleep(0.5)
    pyautogui.press("enter")
    time.sleep(0.5)
    pyautogui.alert(f"Download concluído para o documento {counter}")
counter = 1
pyautogui.alert("O programa vai começar")
pyautogui.PAUSE = 2


for i in range(1):
    donwload()
    time.sleep(0.5)
time.sleep(0.5)

pyautogui.alert("O programa Terminou")
