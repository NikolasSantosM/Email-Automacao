import webbrowser
import pyautogui
from time import sleep

webbrowser.open_new("https://mail.google.com/mail/u/0/#inbox")
pyautogui.click(80,170,duration=3)
pyautogui.click(1356,493,duration=3)
pyautogui.write("nikolas.moraes@outlook.com.br") #Remetente
pyautogui.click(1768,527,duration=3)
pyautogui.write("Notas referente ao mes 09") #Titulo do Email
pyautogui.click(1454,661,duration=3)
pyautogui.write("Oi, tudo bem? poderia por gentileza me mandar as notas referente ao mes 09 ")#Mensagem que vai no corpo do Email
pyautogui.click(1257,1013,duration=3)

pyautogui.click(80,170,duration=3)
pyautogui.click(1356,493,duration=3)
pyautogui.write("nk.amv.edicoes@gmail.com")#Remetente
pyautogui.click(1768,527,duration=3)
pyautogui.write("Notas referente ao mes 09")#Titulo do Email
pyautogui.click(1454,661,duration=3)
pyautogui.write("Oi, tudo bem? poderia por gentileza me mandar as notas referente ao mes 09 ")#Mensagem que vai no corpo do Email
pyautogui.click(1257,1013,duration=3)







