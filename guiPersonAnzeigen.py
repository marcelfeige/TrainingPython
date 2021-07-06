from tkinter import *
from datenbankPersonen import *

class guiPersonAnzeigen:
    def __init__(self, master, tNameDatenbank=None):
        self.master = master
        self.master.wm_title("Datenbank Personen")

        tTitel = "Datenbank Personen"
        tBtnEnd = "Ende"

        # Schriftart und -groessen festlegen
        appFontStyle = "Calibri"
        appFontSizeSmall = 12
        appFontSizeMedium = 14
        appFontSizeBig = 16
        appFontSmall = appFontStyle + ", " + str(appFontSizeSmall)
        appFontMedium = appFontStyle + ", " + str(appFontSizeMedium)
        appFontBig = appFontStyle + ", " + str(appFontSizeBig)

        # Label Titel
        self.labTitel = Label(self.master, text = tTitel, font = appFontBig)
        self.labTitel.grid(row = 0, columnspan = 2)

        # Mehrzeiliges Textfeld
        self.feldAusgabe = Text(self.master, height = 15, width = 60)
        self.feldAusgabe.grid(row = 2, columnspan = 2, padx = 10, pady = 10, sticky = "nsew")

        # Scrollbar
        self.scrollbar = Scrollbar(self.master, command=self.feldAusgabe.yview)
        self.scrollbar.grid(row = 2, column = 2, sticky = "nsew", padx = 10)

        self.feldAusgabe["yscrollcommand"] = self.scrollbar.set

        # Label fuer Status informationen
        self.labStatus = Label(self.master, text="Keine Statusmeldungen vorhanden", font=appFontSmall)
        self.labStatus.grid(row = 3, columnspan = 2)

        # Button beenden
        self.btnEnd = Button(master, text = "Beenden", font = appFontSmall, command = master.destroy)
        self.btnEnd.grid(row = 4, columnspan = 2, padx = 20, pady = 20)

        # Anpassen der Label auf die Fenstergroesse (weight = 1)
        self.master.columnconfigure(0, weight = 1)
        self.master.columnconfigure(1, weight = 1)
        for row in range(5):
            self.master.rowconfigure(row, weight = 1)



        # neues Datenbank Objekt
        dbPersonen = datenbankPersonen()

        # Datenbank initialisieren und Rueckgabewert in der Statuszeile ausgeben
        self.labStatus["text"] = dbPersonen.initDB()
        # Ergebnis des SQL Statemantes in der Variablen result speichern
        result = dbPersonen.leseDB()
        # Teile des Ergebnisses im mehrzeiligen Textfeld anzeigen
        self.feldAusgabe.insert(END, result[0])


