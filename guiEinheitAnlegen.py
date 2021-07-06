from tkinter import *
from tkinter import ttk
from datenbankTrainingseinheiten import *
from datenbankUebung import *
from tkcalendar import *

class guiEinheitAnlegen:

    def __init__(self, master, tNameDatenbank=None):

        self.master = master

        self.master.wm_title("Trainingseinheit anlegen")

        tTitel = "Neue Trainingseinheit anlegen"
        tBtnOK = "Hinzufügen"
        tBtnEnd = "Ende"


        # Schriftart und -groessen festlegen
        appFontStyle = "Calibri"
        appFontSizeSmall = 12
        appFontSizeMedium = 16
        appFontSizeBig = 14
        appFontSmall = appFontStyle + ", " + str(appFontSizeSmall)
        appFontMedium = appFontStyle + ", " + str(appFontSizeMedium)
        appFontBig = appFontStyle + ", " + str(appFontSizeBig)

        # Label
        self.labTitel = Label(master, text =tTitel, font = appFontBig)
        self.labTitel.grid(row=0, columnspan=2)

        # Label mit den Bezeichnungen erstellen
        self.labKategorie = Label(self.master, text="Kategorie", font=appFontSmall) \
            .grid(row=1, column=0)
        self.labBezeichnung = Label(self.master, text="Bezeichnung", font=appFontSmall) \
            .grid(row=2, column=0)
        self.labGruppe = Label(self.master, text="Gruppe", font=appFontSmall) \
            .grid(row=3, column= 0)

        dbUebungen = datenbankUebung()

        # Optionmenu
        # Zuordnung der Kategorien und Bezeichnungen
        self.bezeichnungenBeine = dbUebungen.getBezeichnung("Beine")
        self.bezeichnungenOberkoerper = dbUebungen.getBezeichnung("Oberkörper")
        self.bezeichnungenRuecken = dbUebungen.getBezeichnung("Rücken")
        self.bezeichnungenArme = dbUebungen.getBezeichnung("Arme")

        self.dict = {"Beine": self.bezeichnungenBeine,
                     "Oberkörper": self.bezeichnungenOberkoerper,
                     "Rücken": self.bezeichnungenRuecken,
                     "Arme" : self.bezeichnungenArme}

        self.varKategorie = StringVar()
        self.varBezeichnung = StringVar()

        self.varKategorie.trace("w", self.updateKategorie)

        self.omKategorie = OptionMenu(self.master, self.varKategorie, *self.dict.keys())
        self.omBezeichnung = OptionMenu(self.master, self.varBezeichnung, "")

        self.varKategorie.set("Beine")

        self.omKategorie.grid(row = 1, column = 1)
        self.omBezeichnung.grid(row = 2, column = 1)

        # Label
        self.labAnzahlSaetze = Label(self.master, text = "Anzahl Sätze", font = appFontSmall)
        self.labAnzahlSaetze.grid(row = 3, column = 0)
        self.labAnzahlWiederrholungen = Label(self.master, text="Anzahl Wiederholungen", font = appFontSmall)
        self.labAnzahlWiederrholungen.grid(row = 4, column = 0)
        self.labGewicht = Label(self.master, text = "Gewicht (in kg)", font = appFontSmall)
        self.labGewicht.grid(row = 5, column = 0)
        self.labKalender = Label(self.master, text = "Datum", font = appFontSmall)
        self.labKalender.grid(row = 6, column = 0)

        # Entry id
        self.entAnzahlSaetze = Entry(self.master)
        self.entAnzahlSaetze.grid(row = 3, column = 1)
        self.entAnzahlWiederholungen = Entry(self.master)
        self.entAnzahlWiederholungen.grid(row=4, column=1)
        self.entGewicht = Entry(self.master)
        self.entGewicht.grid(row = 5, column = 1)

        # Kalender
        self.entDatum = DateEntry(self.master, width = 12, background="grey",
                                  foreground="white", borderwidth=2, locale="de_DE", date_pattern="dd.mm.y")
        self.entDatum.grid(row=6, column=1)

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

        self.tvAusgabe.grid(row = 7, columnspan = 2, padx=10)

        # Scrollbar
        self.scrollbar = Scrollbar(self.master)
        self.scrollbar.grid(row=7, column=3, sticky="nsew", padx=10)

        self.tvAusgabe.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.tvAusgabe.yview)

        # Label fuer Status informationen
        self.labStatus = Label(self.master, text="Keine Statusmeldungen vorhanden", font = appFontSmall)
        self.labStatus.grid(row = 8, columnspan = 2)

        # Label fuer die Anzahl der Datensaetze
        self.labDatensaetze = Label(self.master, text="", font = appFontSmall)
        self.labDatensaetze.grid(row = 9, columnspan = 2, padx = 30, pady = 20)

        # Button
        self.btnOK = Button(self.master, text=tBtnOK, font=appFontSmall, command = self.einheitSpeichern, width=20)
        self.btnEnd = Button(self.master, text=tBtnEnd, font=appFontSmall, command = self.master.destroy, width=20)
        self.btnOK.grid(row = 10, column = 0, padx = 20, pady = 0)
        self.btnEnd.grid(row = 10, column = 1, padx = 20, pady = 20)

        # Anpassen der Label auf die Fenstergroesse (weight = 1)
        self.master.columnconfigure(0, weight = 1)
        self.master.columnconfigure(1, weight = 1)

        for row in range(10):
            self.master.rowconfigure(row, weight = 1)

        # neues Datenbank Objekt
        dbTrainingseinheiten = datenbankTrainingseinheiten()

        # Datenbank initialisieren und Rueckgabewert in der Statuszeile ausgeben
        self.labStatus["text"] = dbTrainingseinheiten.initDB()
        # Ergebnis des SQL Statemantes in der Variablen result speichern
        result = dbTrainingseinheiten.leseDB()
        # Treeview Feld fuellen
        count = 0
        for row in result:
            self.tvAusgabe.insert(parent="", index=count, iid=count, text="", values=result[count])
            count = count + 1
        self.labDatensaetze["text"] = "Anzahl Datensätze: " + str(count)

    def einheitSpeichern(self):

        dbTrainingseinheiten = datenbankTrainingseinheiten()
        self.labStatus["text"] = ""
        # Einzelne Eingabefelder auslesen und Daten speichern
        dbTrainingseinheiten.schreibDB(self.varKategorie.get(), self.varBezeichnung.get(), self.entAnzahlSaetze.get(), self.entAnzahlWiederholungen.get(),
            self.entGewicht.get(), self.entDatum.get())
        # Datenbank auslesen
        result = dbTrainingseinheiten.leseDB()
        count = 0
        for i in self.tvAusgabe.get_children():
            self.tvAusgabe.delete(i)
        for row in result:
            self.tvAusgabe.insert(parent = "", index = count, iid = count, text = "", values = result[count])
            count = count + 1
        self.labDatensaetze["text"] = "Anzahl Datensätze: " + str(count)


    def updateKategorie(self, *args):
        kategorien = self.dict[self.varKategorie.get()]
        self.varBezeichnung.set(kategorien[0])

        menu = self.omBezeichnung["menu"]
        menu.delete(0, "end")

        for kategorie in kategorien:
            menu.add_command(label=kategorie,
                             command=lambda bezeichnung=kategorie: self.varBezeichnung.set(bezeichnung))

