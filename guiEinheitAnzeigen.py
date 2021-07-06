from tkinter import *
from tkinter import ttk
from datenbankTrainingseinheiten import *

class guiEinheitAnzeigen:
    def __init__(self, master, tNameDatenbank=None):
        self.master = master
        self.master.wm_title("Datenbank Personen")

        tTitel = "Datenbank Trainingseinheiten"
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
        self.tvAusgabe.heading("Datum", text="Gewicht", anchor=CENTER)

        self.tvAusgabe.heading("#0", text = "", anchor = CENTER)
        self.tvAusgabe.heading("Id", text = "Id", anchor = CENTER)
        self.tvAusgabe.heading("Kategorie", text = "Kategorie", anchor = CENTER)
        self.tvAusgabe.heading("Bezeichnung", text="Bezeichnung", anchor = CENTER)
        self.tvAusgabe.heading("Sätze", text = "Sätze", anchor = CENTER)
        self.tvAusgabe.heading("Wiederholungen", text="Wiederholungen", anchor = CENTER)
        self.tvAusgabe.heading("Gewicht", text = "Gewicht", anchor = CENTER)
        self.tvAusgabe.heading("Datum", text="Datum", anchor=CENTER)

        self.tvAusgabe.grid(row = 2, columnspan = 2, padx=10)

        self.tvAusgabe.heading("Id", text="Id",
                               command=lambda: self.treeview_sort_column(self.tvAusgabe, "Id", FALSE))
        self.tvAusgabe.heading("Kategorie", text="Kategorie",
                               command=lambda: self.treeview_sort_column(self.tvAusgabe, "Kategorie", FALSE))
        self.tvAusgabe.heading("Bezeichnung", text="Bezeichnung",
                               command=lambda: self.treeview_sort_column(self.tvAusgabe, "Bezeichnung", FALSE))
        self.tvAusgabe.heading("Datum", text="Datum",
                               command=lambda: self.treeview_sort_column(self.tvAusgabe, "Gewicht", FALSE))

        # Scrollbar
        self.scrollbar = Scrollbar(self.master)
        self.scrollbar.grid(row=2, column=3, sticky="nsew", padx=10)

        self.tvAusgabe.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.tvAusgabe.yview)

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

    def treeview_sort_column(self, tv, col, reverse):
        l = [(tv.set(k, col), k) for k in tv.get_children("")]
        try:
            l.sort(key=lambda t: int(t[0]), reverse=reverse)
            #      ^^^^^^^^^^^^^^^^^^^^^^^
        except ValueError:
            l.sort(reverse=reverse)

        # rearrange items in sorted positions
        for index, (val, k) in enumerate(l):
            tv.move(k, '', index)

        tv.heading(col,
                   command=lambda: self.treeview_sort_column(tv, col, not reverse))

