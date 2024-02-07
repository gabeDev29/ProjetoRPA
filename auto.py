#Passo 1: Abrir o navegador.
import pyautogui
import time
#pyautogui.click -> para clicar em algum local.
#pyautogui.write -> para escrever algo.
#pyautogui.press -> para pressionar uma tecla.
#pyautogui.hotkey -> para atalhos (Exemplo: CRTL + C, CRTL + V)
#pyautogui.position -> determinar a posição do eixo X e Y do incone do mouse.
pyautogui.PAUSE = 0.5
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
#Passo 2: Abrir o site da empresa.
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(1)
#Passo 3: Fazer o login no site da empresa.
pyautogui.click(x=455, y=368)
pyautogui.write("gabrieldiaz@empresa.com.br")
pyautogui.press("tab")
pyautogui.write("password")
pyautogui.press("tab")
pyautogui.press("enter")
#Passo 4: Cadastrar os produtos da empresa.
import pandas as pd
tabela = pd.read_csv("produtos.csv")
print(tabela)
time.sleep(1)
for linha in tabela.index:
    pyautogui.click(x=456, y=258)
    #codigo
    pyautogui.write(tabela.loc[linha, "codigo"])
    pyautogui.press("tab")
    #marca
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")
    #tipo
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")
    #categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    #preco_unitario
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    #custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    #obs
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
            pyautogui.write(obs)
    #enviar produto
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(5000)
#Passo 5: Refazer as tarefas em Looping.