 #automação de cadastro de produtos de um LInk externo

import pyautogui
import time

# pyautogui.write -> comomando para escrever texto em Python
# pyautogui.press -> comando para apertar 1 tecla em Python
# pyautogui.click -> comando para clicar em algum lugar da tela em Python
# pyautogui.hotkey -> comando de combinação de teclas em Python
pyautogui.PAUSE = 0.4

# abrir o navegador (chrome, Firefoz, Safira, Opera, ou o que voce usa) em Python
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

# entrar no link (Entra no Link da Hashtag)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)


# Passo 2: Fazer login no Link externo
# selecionar o campo de email na tela do Windows
pyautogui.click(x=685, y=451)
# escrever o seu email 
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab") # passando pro próximo campo
pyautogui.write("sua senha")
pyautogui.click(x=955, y=638) # clique no botao de login
time.sleep(3)

# Passo 3: Importar a base de produtos pra cadastrar fornecido pelo criador (site)
import pandas as pd

tabela = pd.read_csv("produtos.csv")

print(tabela)

# Passo 4: Cadastrar um produto da tabela csv
for linha in tabela.index:
    # clicar no campo de código
    pyautogui.click(x=653, y=294)
    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"]
    # preencher o campo
    pyautogui.write(str(codigo))
    # passar para o proximo campo
    pyautogui.press("tab")
    # preencher o campo
    pyautogui.write(str(tabela.loc[linha, 'marca']))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, 'tipo']))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") # cadastra o produto (botao enviar)
    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)
    # Passo 5: Repetir o processo de cadastro até o fim do ciclo
