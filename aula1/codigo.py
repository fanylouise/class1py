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

