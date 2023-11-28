import pyautogui
import time

# Função de cliques para downloads
def download():
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

# Contador de downloads
numero_de_downloads = 515
pyautogui.alert("O programa ja vai começar")
            
# Loop para realizar os downloads
for i in range(1, numero_de_downloads + 1):
    download()
    print(f"Download {i} concluído.")
pyautogui("Fim do programa")
