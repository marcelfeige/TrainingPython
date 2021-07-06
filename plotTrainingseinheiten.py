
import tkinter.ttk as ttk
import tkinter as tk

import matplotlib
import tkcalendar as tkc


from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import style
from matplotlib import figure
from matplotlib.figure import Figure

from datenbankTrainingseinheiten import *
from datenbankUebung import datenbankUebung

import datetime

style.use("ggplot")
matplotlib.use("TkAgg")

class plotTrainingseinheiten():

    # Konstruktor
    def __init__(self, master, tNameDatenbank = None):

        self.master = master
        self.master.wm_title("Plot Trainingseinheiten")

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
        tBtnBMIRechner = "BMI berechnen"
        tBtnOK = "OK"

        self.labTitel = tk.Label(self.master, text = "Trainingseinheiten", font = appFontMedium)
        self.labTitel.grid(row = 0, columnspan = 4)
        # Trennlinie
        self.sep = ttk.Separator(self.master, orient = tk.HORIZONTAL).grid(row = 1, columnspan = 4, sticky = "nsew", padx = 15)

        # Label
        self.labStartDatum = tk.Label(self.master, text = "Start:", font = appFontSmall)
        self.labStartDatum.grid(row = 2, column = 0)
        self.labEndDatum = tk.Label(self.master, text = "Ende:", font = appFontSmall)
        self.labEndDatum.grid(row = 2, column = 2)
        self.labBezeichnung = tk.Label(self.master, text = "Übung", font = appFontSmall)
        self.labBezeichnung.grid(row = 3, column = 0)

        # Kalender
        self.entStartDatum = tkc.DateEntry(self.master, width = 12, background = "grey",
                                  foreground = "white", borderwidth = 2, locale="de_DE", date_pattern = "dd.mm.y")
        self.entStartDatum.grid(row = 2, column = 1, padx = 10)

        self.entEndDatum = tkc.DateEntry(self.master, width = 12, background = "grey",
                                  foreground = "white", borderwidth = 2, locale="de_DE", date_pattern = "dd.mm.y")
        self.entEndDatum.grid(row = 2, column = 3, padx = 10)

        # Optionmenu

        dbUebungen = datenbankUebung()

        # Zuordnung der Kategorien und Bezeichnungen
        self.bezeichnungenBeine = dbUebungen.getBezeichnung("Beine")
        self.bezeichnungenOberkoerper = dbUebungen.getBezeichnung("Oberkörper")
        self.bezeichnungenRuecken = dbUebungen.getBezeichnung("Rücken")
        self.bezeichnungenArme = dbUebungen.getBezeichnung("Arme")

        self.dict = {"Beine": self.bezeichnungenBeine,
                     "Oberkörper": self.bezeichnungenOberkoerper,
                     "Rücken": self.bezeichnungenRuecken,
                     "Arme": self.bezeichnungenArme}

        self.varKategorie = tk.StringVar()
        self.varBezeichnung = tk.StringVar()

        self.varKategorie.trace("w", self.updateKategorie)

        self.omKategorie = tk.OptionMenu(self.master, self.varKategorie, *self.dict.keys())
        self.omBezeichnung = tk.OptionMenu(self.master, self.varBezeichnung, "")

        self.varKategorie.set("Beine")

        self.omKategorie.grid(row = 3 , column = 1)
        self.omBezeichnung.grid(row = 3, column = 2)

        # Button
        #self.btnOK = Button(self.master)
        self.btnPlot = tk.Button(self.master, text = "plotten", font = appFontSmall, command = self.plotxy)
        self.btnPlot.grid(row = 5, column = 1, pady = 10, sticky = "nswe")
        self.btnClear = tk.Button(self.master, text = "clear", font = appFontSmall, command = self.clearplot)
        self.btnClear.grid(row = 5, column = 2, pady = 10, sticky = "nswe")

        (w, h) = 120, 120
        inchsize = (w/25.4, h/25.4)
        # Figure Objekt
        self.figure = Figure(inchsize)
        # Kodierung für den Parameter ist dabei <nrows><ncols><figindex> mit ncol=Anzahl der Spalten, nrows = Anzahl
        # der Zeilen, figindex= Nummer des Diagramms (beginnend mit 1)
        self.axes = self.figure.add_subplot(111)
        self.axes.set_xlabel("Datum")
        self.axes.set_ylabel("Gewicht (in kg)")


        # Canvas als Bereich fue matplotlib
        self.canvas = FigureCanvasTkAgg(self.figure, self.master)
        self.canvas.get_tk_widget().grid(row = 4, columnspan = 4, padx = 30, sticky = "nswe")

        # Anpassen der Label auf die Fenstergroesse (weight = 1)
        self.master.columnconfigure(0, weight=1)
        self.master.columnconfigure(1, weight=1)
        self.master.columnconfigure(2, weight=1)
        self.master.columnconfigure(3, weight=1)
        for row in range(5):
            self.master.rowconfigure(row, weight=1)

    def plotxy(self):
        dbEinheiten = datenbankTrainingseinheiten()
        result = dbEinheiten.getGewicht(self.entStartDatum.get(), self.entEndDatum.get(), self.varBezeichnung.get())

        self.xDatum = result.get("Datum")
        self.yGewicht = result.get("Gewicht")

        self.xDatumNeu = []

        for datum in self.xDatum:

            xDNeu  = datum[8:10] + "." + datum[5:7] + "." + datum[:4]

            self.xDatumNeu.append(xDNeu)

        self.axes.plot(self.xDatumNeu, self.yGewicht)
        self.canvas.draw()


    def clearplot(self):
        self.axes.cla()
        self.canvas.draw()


    def getDaten(self):
        dbEinheiten = datenbankTrainingseinheiten()
        result = dbEinheiten.getGewicht(self.entStartDatum.get(), self.entEndDatum.get(), self.varBezeichnung.get())

        self.xDatum = result.get("Datum")
        self.yGewicht = result.get("Gewicht")




    def plotClear(self):
        pass

    def updateKategorie(self, *args):
        kategorien = self.dict[self.varKategorie.get()]
        self.varBezeichnung.set(kategorien[0])

        menu = self.omBezeichnung["menu"]
        menu.delete(0, "end")

        for kategorie in kategorien:
            menu.add_command(label=kategorie,
                             command=lambda bezeichnung=kategorie: self.varBezeichnung.set(bezeichnung))