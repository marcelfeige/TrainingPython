from tkinter import *

from datenbankPersonen import *


class guiPersonLoeschen():
    # Name der Datenbank
    tNameDatenbank = "personenDatenbank"


    # Konstruktor
    def __init__(self, master, tNameDatenbank = None):

        self.master = master
        self.master.wm_title("Eintrag loeschen")

        tTitel = "Eintrag aus der Datenbank loeschen"
        tBtnOK = "Löschen"
        tBtnEnd = "Ende"

        # Schriftart und -groessen festlegen
        appFontStyle = "Calibri"
        appFontSizeSmall = 12
        appFontSizeMedium = 14
        appFontSizeBig = 15
        appFontSmall = appFontStyle + ", " + str(appFontSizeSmall)
        appFontMedium = appFontStyle + ", " + str(appFontSizeMedium)
        appFontBig = appFontStyle + ", " + str(appFontSizeBig)

        # Label Titel
        self.labTitel = Label(self.master, text=tTitel, font=appFontBig)
        self.labTitel.grid(row=0, columnspan=2)

        # Label id
        self.labId = Label(self.master, text = "Id: ", font = appFontSmall)
        self.labId.grid(row = 1, column = 0)

        # Entry id
        self.entId = Entry(self.master)
        self.entId.grid(row = 1, column = 1)

        # Mehrzeiliges Textfeld
        self.feldAusgabe = Text(self.master, height=4, width=40)
        self.feldAusgabe.grid(row=2, columnspan=2, padx=10, pady=10, sticky="nsew")

        # Scrollbar
        self.scrollbar = Scrollbar(self.master, command=self.feldAusgabe.yview)
        self.scrollbar.grid(row=2, column=2, sticky="nsew", padx=10)

        self.feldAusgabe["yscrollcommand"] = self.scrollbar.set

        # Label fuer Status informationen
        self.labStatus = Label(self.master, text="Keine Statusmeldungen vorhanden", font=appFontSmall)
        self.labStatus.grid(row = 3, columnspan = 2)

        # Label Bestaetigung
        self.labDatensaetze = Label(self.master, text="")
        self.labDatensaetze.grid(row = 4, columnspan = 2, padx = 30, pady = 20)

        # Button
        self.btnOK = Button(self.master, text=tBtnOK, font=appFontSmall, command = self.perLoeschen, width = 20)
        self.btnEnd = Button(self.master, text=tBtnEnd, font=appFontSmall, command = self.master.destroy, width = 20)
        self.btnOK.grid(row = 5, column = 0, padx = 20, pady = 20)
        self.btnEnd.grid(row = 5, column = 1, padx = 20, pady = 20)



        # Anpassen der Label auf die Fenstergroesse (weight = 1)
        self.master.columnconfigure(0, weight=1)
        self.master.columnconfigure(1, weight=1)
        for row in range(4):
            self.master.rowconfigure(row, weight=1)

        # neues Datenbank Objekt
        dbPersonen = datenbankPersonen()

        # Datenbank initialisieren und Rueckgabewert in der Statuszeile ausgeben
        self.labStatus["text"] = dbPersonen.initDB()
        # Ergebnis des SQL Statemantes in der Variablen result speichern
        result = dbPersonen.leseDB()
        # Teile des Ergebnisses im mehrzeiligen Textfeld anzeigen
        self.feldAusgabe.insert(END, result[0])
        self.labDatensaetze["text"] = ""

    def perLoeschen(self):
        dbPersonen = datenbankPersonen()

        id = self.entId.get()

        # Datenbank auslesen
        result = dbPersonen.leseDB()
        if (id in result[0]):
            # Schreiben in Textfeld erlauben
            self.feldAusgabe.config(state="normal")
            dbPersonen.deleteDB(id)
            # Anzeige des mehrzeiligen Textfelds wird von Anfang bis Ende geloescht
            self.feldAusgabe.delete(1.0, END)
            # aktualisierte Datenbank auslesen
            new_result = dbPersonen.leseDB()
            # Hinzufuegen des Resultats der Datenbank abfrage
            self.feldAusgabe.insert(END, new_result[0])
            # Schreiben in Textfeld nicht mehr erlauben
            self.feldAusgabe.config(state="disable")
            self.labDatensaetze["text"] = "Datensatz mit der Id " + str(id) + " gelöscht"
        elif (id not in result):
            self.labDatensaetze["text"] = "Id nicht gefunden"










