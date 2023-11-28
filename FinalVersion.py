import pyautogui
import time

## Função de cliques para downloads
def download():
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

## Função principal do programa, total de documentos e divisão em blocos
def main():
    total_documents = 515
    block_size = 100   

    pyautogui.alert("O programa vai começar")
    pyautogui.PAUSE = 1     

    ## Loop para download dos documentos
    for _ in range(0, total_documents, block_size):
        for _ in range(min(block_size, total_documents - _)):
            download()

    pyautogui.alert("O programa terminou")

## Chamada da função principal
if __name__ == "__main__":
    main()
    