import pyautogui
import time

pyautogui.alert("O código vai começar. Não utilize esse computador")
pyautogui.pause = 0.5
pyautogui.moveTo(862.395)
time.sleep(1)
pyautogui.click()
pyautogui.write("https://drive.google.com")
time.sleep(2)
pyautogui.press("enter")
                
pyautogui.alert('O código foi finalizado. Você já pode utilizar o computador!')