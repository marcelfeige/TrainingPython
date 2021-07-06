from tkinter import *
from tkinter import ttk
from datenbankPersonen import *
from datenbankTrainingseinheiten import *


class guiEinheitLoeschen():
    # Name der Datenbank
    tNameDatenbank = "personenDatenbank"


    # Konstruktor
    def __init__(self, master, tNameDatenbank = None):

        self.master = master
        self.master.wm_title("Eintrag loeschen")

        tTitel = "Eintrag aus der Datenbank löschen"
        tBtnOK = "Löschen"
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
        self.labTitel = Label(self.master, text=tTitel, font=appFontBig)
        self.labTitel.grid(row=0, columnspan=2)

        # Label id
        self.labId = Label(self.master, text = "Id: ")
        self.labId.grid(row = 1, column = 0)

        # Entry id
        self.entId = Entry(self.master)
        self.entId.grid(row = 1, column = 1)

        # Treeview Feld
        self.tvAusgabe = ttk.Treeview(self.master)
        self.tvAusgabe["columns"] = ("Id", "Kategorie", "Bezeichnung", "Sätze", "Wiederholungen", "Gewicht", "Datum")
        self.tvAusgabe.column("#0", width = 0, stretch=NO)
        self.tvAusgabe.column("Id", anchor = CENTER, width=120)
        self.tvAusgabe.column("Kategorie", anchor = CENTER, width=120)
        self.tvAusgabe.column("Bezeichnung", anchor = CENTER, width=120)
        self.tvAusgabe.column("Sätze", anchor = CENTER, width=120)
        self.tvAusgabe.column("Wiederholungen", anchor = CENTER, width=120)
        self.tvAusgabe.column("Gewicht", anchor = CENTER, width=120)
        self.tvAusgabe.column("Gewicht", anchor=CENTER, width=120)
        self.tvAusgabe.heading("Datum", text="Gewicht", anchor=CENTER)

        self.tvAusgabe.heading("#0", text = "", anchor = CENTER)
        self.tvAusgabe.heading("Id", text = "Id", anchor = CENTER)
        self.tvAusgabe.heading("Kategorie", text = "Kategorie", anchor = CENTER)
        self.tvAusgabe.heading("Bezeichnung", text="Bezeichnung", anchor = CENTER)
        self.tvAusgabe.heading("Sätze", text = "Sätze", anchor = CENTER)
        self.tvAusgabe.heading("Wiederholungen", text="Wiederholungen", anchor = CENTER)
        self.tvAusgabe.heading("Gewicht", text = "Gewicht", anchor = CENTER)
        self.tvAusgabe.heading("Datum", text="Gewicht", anchor=CENTER)

        self.tvAusgabe.grid(row=2, columnspan=2, padx=10)

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
        dbEinheit = datenbankTrainingseinheiten()

        # Datenbank initialisieren und Rueckgabewert in der Statuszeile ausgeben
        self.labStatus["text"] = dbEinheit.initDB()
        # Ergebnis des SQL Statemantes in der Variablen result speichern
        result = dbEinheit.leseDB()
        # Treeview Feld fuellen
        count = 0
        for row in result:
            self.tvAusgabe.insert(parent="", index=count, iid=count, text="", values=result[count])
            count = count + 1
        self.labDatensaetze["text"] = "Anzahl Datensätze: " + str(count)

    def perLoeschen(self):

        dbEinheit = datenbankTrainingseinheiten()

        id = 0
        id = int(self.entId.get())

        if (id == 0):
            self.labDatensaetze["text"] = "Keine Id eingegeben"
            return

        # Datenbank auslesen
        result = dbEinheit.leseDB()

        # Laenge der Eintraege ermittel
        lenList = len(result)
        # Fuer alle Eintraege in der Liste
        for i in range(lenList):
            # Abfragen, ob die id im aktuellen Eintrag ist
            if (id in result[i]):
                dbEinheit.deleteDB(id)
                # aktualisierte Datenbank auslesen
                new_result = dbEinheit.leseDB()
                count = 0
                for i in self.tvAusgabe.get_children():
                    self.tvAusgabe.delete(i)
                for row in new_result:
                    self.tvAusgabe.insert(parent="", index=count, iid=count, text="", values=new_result[count])
                    count = count + 1
                self.labDatensaetze["text"] = "Anzahl Datensätze: " + str(count)
                return
            elif (id not in result[i]):
                self.labDatensaetze["text"] = "Id nicht gefunden"








