import pyautogui
import time


def donwload():
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
   

def main():
    total_documents = 514
    block_size = 30
    pause_between_blocks = 10  # segundos

    pyautogui.alert("O programa vai começar")
    pyautogui.PAUSE = 2

    counter = 1

    for _ in range(0, total_documents, block_size):
        for _ in range(min(block_size, total_documents - _)):
            donwload()
            
        time.sleep(pause_between_blocks)

    pyautogui.alert("O programa terminou")

if __name__ == "__main__":
    main()
