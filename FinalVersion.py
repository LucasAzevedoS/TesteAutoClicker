import pyautogui
import time

## selecionar primeira caixa e dar 3 tabs a partir da inicialização do programa

## Função de clicks para downloads
def donwload():
    pyautogui.press("tab")
    time.sleep(0.5)
    pyautogui.press("tab")
    time.sleep(0.5)
    pyautogui.press("tab")
    time.sleep(0.5)
    pyautogui.press("tab")
    time.sleep(0.5)
    pyautogui.press("space")
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
    pyautogui.press("space")
    time.sleep(0.5)
   
## função principal do programa, total de documento e divisão em blocos
def main():
    total_documents = 50
    block_size = 40
    pause_between_blocks = 10  # segundos

    pyautogui.alert("O programa vai começar")
    pyautogui.PAUSE = 2

    counter = 1

## loop para download dos documentos
    for _ in range(0, total_documents, block_size):
        for _ in range(min(block_size, total_documents - _)):
            donwload()
            
        time.sleep(pause_between_blocks)

    pyautogui.alert("O programa terminou")

## chamada da função principal
if __name__ == "__main__":
    main()