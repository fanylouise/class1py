import pyautogui
import time
import pandas
print(pandas. __version__)

pyautogui.PAUSE = 0.5

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(3)

pyautogui.click(x=1138, y=373)
pyautogui.hotkey("ctrl", "a")
pyautogui.write("nana5656@gmail.com")

pyautogui.click(x=2532, y=904)

pyautogui.hotkey("ctrl", "a")
pyautogui.write("nana5656")


pyautogui.click(x=957, y=530)
time.sleep(3)


tabela = pandas.read_csv("produtos.csv")


for linha in tabela.index:
    #codigo
    pyautogui.click(x=1078, y=257)
    str(tabela.loc[linha, "codigo"])
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    #marca
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    #tipo
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    #categoria
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    #preco_unitario
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    #custo
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    #obs
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))

    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(6000)

#2:08:06