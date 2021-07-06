from tkinter import *

from datenbankPersonen import datenbankPersonen
from guiBMI import *

class guiPersonAnlegen():
    # Name der Datenbank
    tNameDatenbank = "personenDatenbank"


    # Konstruktor
    def __init__(self, master, tNameDatenbank = None):

        self.master = master
        self.master.wm_title("Person anlegen")

        tTitel = "Angaben zur Person"
        tBtnOK = "OK"
        tBtnEnd = "Ende"
        tBtnBMI = "BMI berechnen"

        # Schriftart und -groessen festlegen
        appFontStyle = "Calibri"
        appFontSizeSmall = 12
        appFontSizeMedium = 16
        appFontSizeBig = 14
        appFontSmall = appFontStyle + ", " + str(appFontSizeSmall)
        appFontMedium = appFontStyle + ", " + str(appFontSizeMedium)
        appFontBig = appFontStyle + ", " + str(appFontSizeBig)

        # Label
        self.labTitel = Label(master, text = tTitel, font = appFontBig)
        self.labTitel.grid(row = 0, columnspan = 2)

        # Label mit den Bezeichnungen erstellen
        self.labNname = Label( self.master, text = "Nachname", font = appFontSmall)\
            .grid(row = 1, column = 0)
        self.labVname = Label( self.master, text = "Vorname", font = appFontSmall)\
            .grid(row = 2, column = 0)
        self.labAlter = Label( self.master, text = "Alter (Jahre)", font = appFontSmall)\
            .grid(row = 3, column = 0)
        self.labGroesse = Label( self.master, text="Größe (x,xx in m)", font=appFontSmall) \
            .grid(row = 4, column=0)
        self.labGewicht = Label( self.master, text = "Gewicht (xx,x in kg)", font = appFontSmall)\
            .grid(row = 5, column = 0)

        # Geschlecht auswaehlen durch drop down

        # Entry fuer die Bezeichnungen erstellen
        self.entNname = Entry(self.master)
        self.entNname.grid(row = 1, column = 1)
        self.entVname = Entry( self.master)
        self.entVname.grid(row = 2, column = 1)
        self.entAlter = Entry( self.master)
        self.entAlter.grid(row = 3, column = 1)
        self.entGroesse = Entry( self.master)
        self.entGroesse.grid(row = 4, column=1)
        self.entGewicht = Entry( self.master)
        self.entGewicht.grid(row = 5, column = 1)


        # Mehrzeiliges Textfeld
        self.feldAusgabe = Text(self.master, height = 4, width = 40)
        self.feldAusgabe.grid(row = 6, columnspan = 2, padx = 10, pady = 10, sticky = "nswe")

        # Scrollbar
        self.scrollbar = Scrollbar(self.master, command = self.feldAusgabe.yview)
        self.scrollbar.grid(row = 6, column = 2, sticky = "nsew", padx = 10)

        self.feldAusgabe["yscrollcommand"] = self.scrollbar.set

        # Label fuer Status informationen
        self.labStatus = Label( self.master, text = "Keine Statusmeldungen vorhanden", font = appFontSmall)
        self.labStatus.grid(row = 7, columnspan =2)

        # Label fuer die Anzahl der Datensaetze
        self.labDatensaetze = Label( self.master, text="")
        self.labDatensaetze.grid(row =8, columnspan=2, padx = 30, pady = 20)

        # Button
        self.btnOK = Button( self.master, text = tBtnOK, font = appFontSmall, command = self.perSpeichern, width = 20)
        self.btnEnd = Button( self.master, text = tBtnEnd, font = appFontSmall, command = self.master.destroy, width = 20)
        self.btnOK.grid(row = 9, column = 0, padx = 20, pady = 20)
        self.btnEnd.grid(row = 9, column = 1, padx = 20, pady = 20)

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

        # Attribut state auf disable setzen, dadurch sind nur programmiertechnische Eingaben in diesem Feld moeglich
        # keine Benutzereingaben
        self.feldAusgabe.configure(state="disabled")
        self.labDatensaetze["text"] = "Anzahl Datensätze: " + result[1]

    def perSpeichern(self):
        dbPersonen = datenbankPersonen()
        self.labStatus["text"] = ""
        # Einzelne Eingabefelder auslesen und Daten speichern

        # Fehler abfangen bei der Eingabe der Groesse und des Gewichts
        # Umwandlung von , in . fuer die Verarbeitung als float

        # Eingbae bekommen und speichern
        groesse = self.entGroesse.get()
        # nach , im String suchen
        char = groesse.find(",")
        # Wenn char != 0 ist, wurde ein , gedfunden
        if (char != 0):
            # das , wird durch einen . ersetzt
            groesse = groesse.replace(",", ".")
        # Die Variable wird in flaot umgewandelt
        self.groesse = float(groesse)

        # Eingbae bekommen und speichern
        gewicht = self.entGewicht.get()
        # nach , im String suchen
        char = gewicht.find(",")
        # Wenn char != 0 ist, wurde ein , gedfunden
        if (char != 0):
            # das , wird durch einen . ersetzt
            gewicht = gewicht.replace(",", ".")
        # Die Variable wird in flaot umgewandelt
        self.gewicht = float(gewicht)

        dbPersonen.schreibDB(self.entNname.get(), self.entVname.get(), self.entAlter.get(), self.groesse, self.gewicht)
        self.feldAusgabe.config(state="normal")
        # Datenbank auslesen
        result = dbPersonen.leseDB()
        # Anzeige des mehrzeiligen Textfelds wird von Anfang bis Ende geloescht
        self.feldAusgabe.delete(1.0, END)
        # Hinzufuegen des Resultats der Datenbank abfrage
        self.feldAusgabe.insert(END, result[0])
        self.feldAusgabe.config(state = "disable")
        self.labDatensaetze["text"] = "Anzahl Datensätze: " + result[1]
