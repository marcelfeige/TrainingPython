from tkinter import *
from tkinter import ttk
from datenbankPersonen import *
from datenbankTrainingseinheiten import *
from tkcalendar import *
from datenbankUebung import *

class guiEinheitAendern():
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
        appFontSizeMedium = 14
        appFontSizeBig = 16
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
                     "Arme": self.bezeichnungenArme}

        self.varKategorie = StringVar()
        self.varBezeichnung = StringVar()

        self.varKategorie.trace("w", self.updateKategorie)

        self.omKategorie = OptionMenu(self.master, self.varKategorie, *self.dict.keys())
        self.omBezeichnung = OptionMenu(self.master, self.varBezeichnung, "")

        self.varKategorie.set("Beine")

        self.omKategorie.grid(row = 3, column=1)
        self.omBezeichnung.grid(row = 4, column=1)

        # Label fuer die Aenderungen
        self.labKategorie = Label(self.master, text= "Kategorie", font = appFontSmall) \
            .grid(row = 3, column = 0)
        self.labBezeichnung = Label(self.master, text = "Bezeichnung", font = appFontSmall) \
            .grid(row = 4, column = 0)
        self.labAnzahlSatze = Label(self.master, text = "Anzahl Sätze", font = appFontSmall) \
            .grid(row = 5, column = 0)
        self.labAnzahlWiederholungen = Label(self.master, text = "Anzahl Wiederholungen", font = appFontSmall) \
            .grid(row = 6, column = 0)
        self.labAnzahlGewicht = Label(self.master, text = "Gewicht (in kg)", font = appFontSmall) \
            .grid(row = 7, column = 0)
        self.labDatum = Label(self.master, text = "Datum", font = appFontSmall) \
            .grid(row = 8, column = 0)

        # Entry id
        self.entAnzahlSaetze = Entry(self.master)
        self.entAnzahlSaetze.grid(row = 5, column = 1)
        self.entAnzahlWiederholungen = Entry(self.master)
        self.entAnzahlWiederholungen.grid(row = 6, column = 1)
        self.entGewicht = Entry(self.master)
        self.entGewicht.grid(row = 7, column=1)

        # Kalender
        self.entDatum = DateEntry(self.master, width = 12, background = "grey",
                                  foreground = "white", borderwidth = 2, locale = "de_DE", date_pattern = "dd.mm.y")
        self.entDatum.grid(row = 8, column = 1)

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

        self.tvAusgabe.grid(row = 9, columnspan = 2, padx=10)

        # Scrollbar
        self.scrollbar = Scrollbar(self.master)
        self.scrollbar.grid(row=9, column=3, sticky="nsew", padx=10)

        self.tvAusgabe.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.tvAusgabe.yview)

        # Label fuer Status informationen
        self.labStatus = Label(self.master, text="Keine Statusmeldungen vorhanden", font = appFontSmall)
        self.labStatus.grid(row = 11, columnspan = 2)

        # Label Bestaetigung
        self.labDatensaetze = Label(self.master, text = "")
        self.labDatensaetze.grid(row = 12, columnspan = 2, padx = 30, pady = 20)

        # Button
        self.btnOK = Button(self.master, text=tBtnOK, font=appFontSmall, command = self.einheitAendern, width = 20)
        self.btnEnd = Button(self.master, text=tBtnEnd, font=appFontSmall, command = self.master.destroy, width = 20)
        self.btnOK.grid(row = 13, column = 0, padx = 20, pady = 20)
        self.btnEnd.grid(row = 13, column = 1, padx = 20, pady = 20)


        # Anpassen der Label auf die Fenstergroesse (weight = 1)
        self.master.columnconfigure(0, weight=1)
        self.master.columnconfigure(1, weight=1)
        for row in range(13):
            self.master.rowconfigure(row, weight=1)

        # neues Datenbank Objekt
        dbTreiningseinheit = datenbankTrainingseinheiten()

        result = dbTreiningseinheit.leseDB()

        # Treeview Feld fuellen
        count = 0
        for row in result:
            self.tvAusgabe.insert(parent="", index=count, iid=count, text="", values=result[count])
            count = count + 1
        self.labDatensaetze["text"] = "Anzahl Datensätze: " + str(count)

    def einheitAendern(self):

        dbTreiningseinheit = datenbankTrainingseinheiten()

        id = 0
        id = int(self.entId.get())

        if (id == 0):
            self.labDatensaetze["text"] = "Keine Id eingegeben"
            return
        # Datenbank auslesen
        result = dbTreiningseinheit.leseDB()

        kategorie = self.varKategorie.get()
        bezeichnung = self.varBezeichnung.get()
        saetze = self.entAnzahlSaetze.get()
        wiederholung = self.entAnzahlWiederholungen.get()
        gewicht = self.entGewicht.get()
        datum = self.entDatum.get()

        listUpdate = ["kategorie", "bezeichnung", "saetze", "wiederholung", "gewicht", "datum"]
        eingabe = [kategorie, bezeichnung, saetze, wiederholung, gewicht, datum]


        # Laenge der Eintraege ermittel
        lenList = len(result)
        # Fuer alle Eintraege in der Liste
        for i in range(lenList):
            # Abfragen, ob die id im aktuellen Eintrag ist
            if (id in result[i]):
                # Werte aus den Eingabefeldern nehmen, wenn diese nicht leer sind
                for value in eingabe:
                    if (value != ""):
                        index = eingabe.index(value)
                        strCol = listUpdate[index]
                        strUpdate = value
                        dbTreiningseinheit.updateDB(id, strCol, strUpdate)

                # aktualisierte Datenbank auslesen
                new_result = dbTreiningseinheit.leseDB()
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



    def updateKategorie(self, *args):
        kategorien = self.dict[self.varKategorie.get()]
        self.varBezeichnung.set(kategorien[0])

        menu = self.omBezeichnung["menu"]
        menu.delete(0, "end")

        for kategorie in kategorien:
            menu.add_command(label=kategorie,
                             command=lambda bezeichnung=kategorie: self.varBezeichnung.set(bezeichnung))