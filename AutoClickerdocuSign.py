import pyautogui
import time

time.sleep(5)
## Função para mover o mouse para uma posição específica
def moveMouse(x, y):
    pyautogui.moveTo(x, y)

def clickBaixar():
    moveMouse(1760, 421)
    pyautogui.click(1760, 421)
    time.sleep(2)

    pyautogui.click(687, 599)
    time.sleep(2)

    pyautogui.click(716, 682)
    time.sleep(2)

    moveMouse(1760, 421)
    time.sleep(2)

# Número total de repetições
total_repetitions = 520

# Loop principal
for i in range(total_repetitions):
    
    # Alternar entre -240 e -235 a cada iteração (mudando o valor de scroll_value a cada iteração entre número impares e pares)
    if i % 2 == 0:
        scroll_values = [-240, -230]
    else:
        scroll_values = [-230, -240]
    # Loop para rolar a página para baixo e para cima
    for scroll_value in scroll_values:
        # Chamar clickBaixar a cada rolagem
        clickBaixar()

        # Rolar a página para baixo ou para cima
        pyautogui.scroll(scroll_value)

        # Agora, mova o mouse para uma posição fixa após cada rolagem
        moveMouse(1760, 421)
        time.sleep(2)

pyautogui.alert("O programa acabou")
