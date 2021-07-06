'''
Programmm zu erstellen und verwalten von Training, Trainingseinheiten, Trainingsplaenen
@ author Marcel Feige

'''

import tkinter as tk
from guiPersonenAnlegen import *
from datenbankPersonen import *
from guiBMI import *
from guiMenu import *
from datenbankUebung import *

root = Tk()
root.wm_title("Menu")
guiMenu = guiMenu(master = root)
guiMenu.mainloop()


