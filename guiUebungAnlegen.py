from tkinter import *
from tkinter import ttk
from datenbankUebung import *
from guiBMI import *

class guiUebungAnlegen:
    # Name der Datenbank
    tNameDatenbank = "DatenbankUebungen"

    # Konstruktor
    def __init__(self, master, tNameDatenbank = None):

        self.master = master
        self.master.wm_title("Übung anlegen")

        # neues Datenbank Objekt
        dbUebungen = datenbankUebung()

        tTitel = "Neue Übung anlegen"
        tBtnOK = "Hinzufügen"
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
        self.labKategorie = Label(self.master, text = "Kategorie", font = appFontSmall) \
            .grid(row = 1, column = 0)
        self.labGruppe = Label(self.master, text="Gruppe", font=appFontSmall) \
            .grid(row = 2, column = 0)
        self.labBezeichnung = Label( self.master, text = "Bezeichnung", font = appFontSmall)\
            .grid(row = 3, column = 0)


        # Combobox Kategorie
        self.cbKategorie = ttk.Combobox(self.master, values = dbUebungen.tKategorien)
        self.cbKategorie.grid(row = 1, column = 1, padx = 10)

        # Combobox Gruppe
        self.cbGruppe = ttk.Combobox(self.master, values = dbUebungen.tGruppe)
        self.cbGruppe.grid(row = 2, column = 1, padx = 10)

        # Entryfelder
        #self.entKategorie = Entry(self.master)
        #self.entKategorie.grid(row = 1, column = 1)
        self.entBezeichnung= Entry(self.master)
        self.entBezeichnung.grid(row = 3, column = 1, padx = 10)
        #self.entGruppe = Entry(self.master)
        #self.entGruppe.grid(row = 3, column = 1)

        # Treeview Feld
        self.tvAusgabe = ttk.Treeview(self.master)
        self.tvAusgabe["columns"] = ("Id", "Kategorie", "Gruppe", "Bezeichnung")
        self.tvAusgabe.column("#0", width=0, stretch=NO)
        self.tvAusgabe.column("Id", anchor=CENTER, width=120)
        self.tvAusgabe.column("Kategorie", anchor=CENTER, width=120)
        self.tvAusgabe.column("Gruppe", anchor=CENTER, width=120)
        self.tvAusgabe.column("Bezeichnung", anchor=CENTER, width=120)

        self.tvAusgabe.heading("#0", text="", anchor=CENTER)
        self.tvAusgabe.heading("Id", text="Id", anchor=CENTER)
        self.tvAusgabe.heading("Kategorie", text="Kategorie", anchor=CENTER)
        self.tvAusgabe.heading("Gruppe", text="Gruppe", anchor=CENTER)
        self.tvAusgabe.heading("Bezeichnung", text="Bezeichnung", anchor=CENTER)
        self.tvAusgabe.grid(row = 4, columnspan=2, padx=10)

        # Scrollbar
        self.scrollbar = Scrollbar(self.master)
        self.scrollbar.grid(row = 4, column=3, sticky="nsew", padx=10)

        self.tvAusgabe.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.tvAusgabe.yview)

        # Label fuer Status informationen
        self.labStatus = Label( self.master, text = "Keine Statusmeldungen vorhanden")
        self.labStatus.grid(row = 5, columnspan =2)

        # Label fuer die Anzahl der Datensaetze
        self.labDatensaetze = Label( self.master, text="")
        self.labDatensaetze.grid(row = 6, columnspan=2, padx = 30, pady = 20)

        # Button
        self.btnOK = Button( self.master, text = tBtnOK, font = appFontSmall, command = self.uebSpeichern, width = 20)
        self.btnEnd = Button( self.master, text = tBtnEnd, font = appFontSmall, command = self.master.destroy, width = 20)
        self.btnOK.grid(row = 7, column = 0, padx = 20, pady = 20)
        self.btnEnd.grid(row = 7, column = 1, padx = 20, pady = 20)

        # Anpassen der Label auf die Fenstergroesse (weight = 1)
        self.master.columnconfigure(0, weight=1)
        self.master.columnconfigure(1, weight=1)
        for row in range(9):
            self.master.rowconfigure(row, weight=1)

        # neues Datenbank Objekt
        dbUebungen = datenbankUebung()

        # Datenbank initialisieren und Rueckgabewert in der Statuszeile ausgeben
        self.labStatus["text"] = dbUebungen.initDB()
        # Ergebnis des SQL Statemantes in der Variablen result speichern
        result = dbUebungen.leseDB()
        # Treeview Feld fuellen
        count = 0
        for row in result:
            self.tvAusgabe.insert(parent="", index=count, iid=count, text="", values=result[count])
            count = count + 1
        self.labDatensaetze["text"] = "Anzahl Datensätze: " + str(count)

    def uebSpeichern(self):
        dbUebungen = datenbankUebung()
        self.labStatus["text"] = ""
        # Einzelne Eingabefelder auslesen und Daten speichern
        dbUebungen.schreibDB(self.cbKategorie.get(), self.cbGruppe.get(), self.entBezeichnung.get())
        # Datenbank auslesen
        result = dbUebungen.leseDB()
        count = 0
        for i in self.tvAusgabe.get_children():
            self.tvAusgabe.delete(i)
        for row in result:
            self.tvAusgabe.insert(parent = "", index = count, iid = count, text = "", values = result[count])
            count = count + 1
        self.labDatensaetze["text"] = "Anzahl Datensätze: " + str(count)

