from tkinter import ttk
from guiPersonenAnlegen import *
from guiPersonLoeschen import *
from guiPersonAendern import *
from guiPersonAnzeigen import *
from guiUebungAnlegen import *
from guiUebungAendern import *
from guiUebungLoeschen import *
from guiUebungAnzeigen import *
from guiEinheitAnlegen import *
from guiEinheitLoeschen import *
from guiEinheitAendern import *
from guiEinheitAnzeigen import *
from plotTrainingseinheiten import plotTrainingseinheiten

# Fenster zur Auswahl der gewunschten Aktion

class guiMenu(Frame):


    # Konstruktor
    def __init__(self, master = None, tNameDatenbank = None):
        Frame.__init__(self, master)
        self.master = master
        self.master.wm_title("Menu")

        # Schriftart und -groessen festlegen
        appFontStyle = "Calibri"
        appFontSizeSmall = 12
        appFontSizeMedium = 14
        appFontSizeBig = 16
        appFontSmall = appFontStyle + ", " + str(appFontSizeSmall)
        appFontMedium = appFontStyle + ", " + str(appFontSizeMedium)
        appFontBig = appFontStyle + ", " + str(appFontSizeBig)

        tBtnPersonAnlegen = "Neue Person anlegen"
        tBtnUebungAnlegen = "Neue Übung anlegen"
        tBtnLoeschen = "Eintrag löschen"
        tBtnAendern = "Eintrag ändern"
        tBtnAnzeigen = "Datenbank anzeigen"
        tBtnEinheitAnlegen = "Trainingseinheit anlegen"
        tBtnBMIRechner= "BMI berechnen"


        self.labTitel = Label(master, text = "Menu", font = appFontMedium)
        self.labTitel.grid(row = 0, columnspan = 2)
        # Trennlinie
        ttk.Separator(master, orient = HORIZONTAL).grid(row = 1, columnspan = 2, sticky = "nsew", padx = 15)

        # Label Datenbank Personen
        self.labDatenbank = Label(master, text ="Optionen Datenbank Personen", font = appFontSmall)
        self.labDatenbank.grid(row = 2, columnspan = 2)

        # Button
        # Person anlegen
        self.btnPersonAnlegen = Button(master, text = tBtnPersonAnlegen, font = appFontSmall,command = self.openPersonAnlegen)
        self.btnPersonAnlegen.grid(row = 3, column = 0, padx = 20, pady = 20)
        # Person aus Datenbank loeschen
        self.btnPersonLoeschen = Button(master, text = tBtnLoeschen, font=appFontSmall, command = self.openPersonLoeschen)
        self.btnPersonLoeschen.grid(row = 3, column = 1, padx = 20, pady = 20)
        # Person aus Datenbank aendern
        self.btnPersonAendern = Button(master, text = tBtnAendern, font = appFontSmall, command = self.openPersonAendern)
        self.btnPersonAendern.grid(row = 4, column = 0, padx = 20, pady = 20)
        # Person aus Datenbank anzeigen
        self.btnPersonAnzeigen = Button(master, text = tBtnAnzeigen, font = appFontSmall, command = self.openPersonAnzeigen)
        self.btnPersonAnzeigen.grid(row = 4, column = 1, padx = 20, pady = 20)
        # Trennlinie
        ttk.Separator(master, orient = HORIZONTAL).grid(row = 5, columnspan = 2, sticky = "nsew", padx = 15)


        # Label Datenbank Uebungen
        self.labUebungen = Label(master, text = "Optionen Datenbank Übungen", font = appFontSmall)
        self.labUebungen.grid(row = 6, columnspan = 2)
        # Uebung in Datenbank anlegen, loeschen, aendern, anzeigen
        self.btnUebungAnlegen = Button(master, text = tBtnUebungAnlegen, font = appFontSmall, command = self.openUebungAnlegen)
        self.btnUebungAnlegen.grid(row = 7, column = 0, padx = 20, pady = 20)
        self.btnUebungLoeschen = Button(master, text = tBtnLoeschen, font = appFontSmall, command = self.openUebungLoeschen)
        self.btnUebungLoeschen.grid(row = 7, column = 1, padx = 20, pady = 20)
        self.btnUebungAendern = Button(master, text = tBtnAendern, font = appFontSmall, command = self.openUebungAendern)
        self.btnUebungAendern.grid(row = 8, column = 0, padx = 20, pady = 20)
        self.btnUebungenAnzeigen = Button(master, text = tBtnAnzeigen, font = appFontSmall, command = self.openUebungAnzeigen)
        self.btnUebungenAnzeigen.grid(row = 8, column = 1, padx = 20, pady = 20)
        # Trennlinie
        ttk.Separator(master, orient = HORIZONTAL).grid(row = 9, columnspan = 2, sticky = "nsew", padx = 15)


        # Label Trainingseinheiten
        self.labEinheiten = Label(master, text = "Optionen Datenbank Trainingseinheiten", font = appFontSmall)
        self.labEinheiten.grid(row = 10, columnspan = 2)
        # Trainingseinheiten in Datenbank anlegen, loeschen, aendern, anzeigen
        self.btnEinheitAnlegen = Button(master, text = tBtnEinheitAnlegen, font = appFontSmall, command = self.openEinheitAnlegen)
        self.btnEinheitAnlegen.grid(row = 11, column = 0, padx = 20, pady = 20)
        self.btnEinheitLoeschen = Button(master, text = tBtnLoeschen, font = appFontSmall, command = self.openEinheitLoeschen)
        self.btnEinheitLoeschen.grid(row = 11, column = 1, padx = 20, pady = 20)
        self.btnEinheitAendern = Button(master, text = tBtnAendern, font = appFontSmall, command = self.openEinheitAendern)
        self.btnEinheitAendern.grid(row = 12, column = 0, padx = 20, pady = 20)
        self.btnUebungenAnzeigen = Button(master, text = tBtnAnzeigen, font = appFontSmall, command = self.openEinheitAnzeigen)
        self.btnUebungenAnzeigen.grid(row = 12, column = 1, padx = 20, pady = 20)
        self.btnPlotEinheiten = Button(master, text = "Plot Trainingseinheiten", font = appFontSmall, command = self.openPlotEinheiten)
        self.btnPlotEinheiten.grid(row = 13, columnspan = 2, padx = 20, pady = 20)
        # Trennlinie
        ttk.Separator(master, orient = HORIZONTAL).grid(row = 14, columnspan = 2, sticky = "nsew", padx = 15)

        # Label BMI Rechner
        self.labBMIRechner = Label(master, text="BMI Rechner", font = appFontSmall)
        self.labBMIRechner.grid(row = 15, columnspan = 2)

        self.btnBMIRechner = Button(master, text = tBtnBMIRechner, font = appFontSmall, command = self.openBMIRechner)
        self.btnBMIRechner.grid(row = 16, column = 0, padx = 20, pady = 20)

        self.btnEnd = Button(master, text = "Beenden", font = appFontSmall, command = master.destroy)
        self.btnEnd.grid(row = 17, columnspan = 2, padx = 20, pady = 20)
        # Trennlinie
        ttk.Separator(master, orient = HORIZONTAL).grid(row = 21, columnspan = 2, sticky = "nsew", padx = 15)

        # Anpassen der Label auf die Fenstergroesse (weight = 1)
        self.master.columnconfigure(0, weight = 1)
        self.master.columnconfigure(1, weight=1)

        for row in range(17):
            self.master.rowconfigure(row, weight = 1)


    def openPersonAnlegen(self):

        # neues Fenster erstellen
        self.newWindow = Toplevel(self.master)

        guiPersonenAnlegen = guiPersonAnlegen(self.newWindow)

    def openPersonLoeschen(self):

        # neues Fenster erstellen
        self.newWindow = Toplevel(self.master)

        guiPersonenLoeschen = guiPersonLoeschen(self.newWindow)

    def openPersonAendern(self):

        # neues Fenster erstellen
        self.newWindow = Toplevel(self.master)

        guiPersonenAendern = guiPersonAendern(self.newWindow)

    def openPersonAnzeigen(self):
        # neues Fenster erstellen
        self.newWindow = Toplevel(self.master)

        guiPersonenAnzeigen = guiPersonAnzeigen(self.newWindow)

    def openUebungAnlegen(self):
        # neues Fenster erstellen
        self.newWindow = Toplevel(self.master)

        guiUebungenAnlegen = guiUebungAnlegen(self.newWindow)

    def openUebungLoeschen(self):
        # neues Fenster erstellen
        self.newWindow = Toplevel(self.master)

        guiUebungenLoeschen = guiUebungLoeschen(self.newWindow)

    def openUebungAendern(self):
        # neues Fenster erstellen
        self.newWindow = Toplevel(self.master)

        guiUebungdenAendern = guiUebungAendern(self.newWindow)

    def openUebungAnzeigen(self):
        # neues Fenster erstellen
        self.newWindow = Toplevel(self.master)

        guiUebungdenAnzeigen = guiUebungAnzeigen(self.newWindow)

    def openEinheitAnlegen(self):
        # neues Fenster erstellen
        self.newWindow = Toplevel(self.master)

        guiEinheitenAnlegen = guiEinheitAnlegen(self.newWindow)

    def openEinheitLoeschen(self):
        # neues Fenster erstellen
        self.newWindow = Toplevel(self.master)

        guiEinheitenLoeschen = guiEinheitLoeschen(self.newWindow)

    def openEinheitAendern(self):
        # neues Fenster erstellen
        self.newWindow = Toplevel(self.master)

        guiEinheitenAendern = guiEinheitAendern(self.newWindow)

    def openEinheitAnzeigen(self):
        # neues Fenster erstellen
        self.newWindow = Toplevel(self.master)

        guiEinheitenAnzeigen = guiEinheitAnzeigen(self.newWindow)

    def openPlotEinheiten(self):
        # neues Fenster erstellen
        self.newWindow = Toplevel(self.master)

        plotEinheiten = plotTrainingseinheiten(self.newWindow)

    def openBMIRechner(self):

        # neues Fenster erstellen
        self.newWindow = Toplevel(self.master)

        guiBMIRechner = guiBMI(self.newWindow)