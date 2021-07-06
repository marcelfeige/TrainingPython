from tkinter import *

from datenbankPersonen import *


class guiPersonAendern():
    # Name der Datenbank
    tNameDatenbank = "personenDatenbank"


    # Konstruktor
    def __init__(self, master, tNameDatenbank = None):

        self.master = master
        self.master.wm_title("Eintrag loeschen")

        tTitel = "Eintrag in der Datenbank ändern"
        tBtnOK = "Speichern"
        tBtnEnd = "Ende"

        # Schriftart und -groessen festlegen
        appFontStyle = "Calibri"
        appFontSizeSmall = 12
        appFontSizeMedium = 16
        appFontSizeBig = 14
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

        # Label Beschreibung
        self.labBeschr = Label(self.master, text = "Daten für die Änderung eingeben", font = appFontSmall)
        self.labBeschr.grid(row = 2, columnspan = 2)

        # Label fuer die Aenderungen
        self.labNname = Label(self.master, text= "Nachname", font = appFontSmall) \
            .grid(row = 3, column = 0)
        self.labVname = Label(self.master, text = "Vorname", font = appFontSmall) \
            .grid(row = 4, column = 0)
        self.labAlter = Label(self.master, text = "Alter (Jahre)", font = appFontSmall) \
            .grid(row = 5, column = 0)
        self.labGroesse = Label(self.master, text = "Größe (x,xx in m)", font = appFontSmall) \
            .grid(row = 6, column = 0)
        self.labGewicht = Label(self.master, text = "Gewicht (xx,x in kg)", font = appFontSmall) \
            .grid(row = 7, column = 0)

        # Geschlecht auswaehlen durch drop down

        # Entry fuer die Bezeichnungen erstellen
        self.entNname = Entry(self.master)
        self.entNname.grid(row = 3, column=1)
        self.entVname = Entry(self.master)
        self.entVname.grid(row = 4, column=1)
        self.entAlter = Entry(self.master)
        self.entAlter.grid(row = 5, column=1)
        self.entGroesse = Entry(self.master)
        self.entGroesse.grid(row = 6, column=1)
        self.entGewicht = Entry(self.master)
        self.entGewicht.grid(row = 7, column = 1)

        # Mehrzeiliges Textfeld
        self.feldAusgabe = Text(self.master, height=4, width=40)
        self.feldAusgabe.grid(row = 8, columnspan=2, padx=10, pady=10, sticky="nsew")

        # Scrollbar
        self.scrollbar = Scrollbar(self.master, command=self.feldAusgabe.yview)
        self.scrollbar.grid(row = 8, column = 2, sticky = "nsew", padx = 10)

        self.feldAusgabe["yscrollcommand"] = self.scrollbar.set

        # Label fuer Status informationen
        self.labStatus = Label(self.master, text="Keine Statusmeldungen vorhanden", font=appFontSmall)
        self.labStatus.grid(row = 9, columnspan = 2)

        # Label Bestaetigung
        self.labDatensaetze = Label(self.master, text="")
        self.labDatensaetze.grid(row = 10, columnspan = 2, padx = 30, pady = 20)

        # Button
        self.btnOK = Button(self.master, text=tBtnOK, font=appFontSmall, command = self.perAendern, width = 20)
        self.btnEnd = Button(self.master, text=tBtnEnd, font=appFontSmall, command = self.master.destroy, width = 20)
        self.btnOK.grid(row = 11, column = 0, padx = 20, pady = 20)
        self.btnEnd.grid(row = 11, column = 1, padx = 20, pady = 20)


        # Anpassen der Label auf die Fenstergroesse (weight = 1)
        self.master.columnconfigure(0, weight=1)
        self.master.columnconfigure(1, weight=1)
        for row in range(9):
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

    def perAendern(self):
        dbPersonen = datenbankPersonen()


        id = self.entId.get()

        if (id == ""):
            self.labDatensaetze["text"] = "Keine Id eingegeben"
            return
        # Datenbank auslesen
        result = dbPersonen.leseDB()

        nname = self.entNname.get()
        vname = self.entVname.get()
        alter = self.entAlter.get()
        groesse = self.entGroesse.get()
        gewicht = self.entGewicht.get()


        listUpdate = ["name", "vorname", "age", "groesse", "gewicht"]
        eingabe = [nname, vname, alter, groesse, gewicht]

        if (id in result[0]):
            # Schreiben in Textfeld erlauben
            self.feldAusgabe.config(state="normal")

            for value in eingabe:
                if (value != ""):
                    index = eingabe.index(value)
                    strCol = listUpdate[index]
                    strUpdate = value
                    dbPersonen.updateDB(id, strCol, strUpdate)

            # Anzeige des mehrzeiligen Textfelds wird von Anfang bis Ende geloescht
            self.feldAusgabe.delete(1.0, END)
            # aktualisierte Datenbank auslesen
            new_result = dbPersonen.leseDB()
            # Hinzufuegen des Resultats der Datenbank abfrage
            self.feldAusgabe.insert(END, new_result[0])
            # Schreiben in Textfeld nicht mehr erlauben
            self.feldAusgabe.config(state="disable")
            self.labDatensaetze["text"] = "Datensatz mit der Id " + str(id) + " geändert"
        elif (id not in result):
            self.labDatensaetze["text"] = "Id nicht gefunden"










