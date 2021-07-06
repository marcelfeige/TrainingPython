from tkinter import *


class guiBMI(Frame):

    def __init__(self, master, tNameDatenbank = None):
        Frame.__init__(self)

        self.master = master
        self.master.wm_title("BMI-Rechner")

        tTitel = "BMI-Rechner"
        tBtnOK = "OK"
        tBtnEnd = "Ende"
        tBtnBMI = "BMI berechnen"
        textRbtnPerson = "BMI für eine Person aus der Datenbank berechnen"
        textRbtnDaten = "BMI für eine Gewicht und Größe berechnen"

        # Schriftart und -groessen festlegen
        appFontStyle = "Calibri"
        appFontSizeSmall = 12
        appFontSizeMedium = 16
        appFontSizeBig = 14
        appFontSmall = appFontStyle + ", " + str(appFontSizeSmall)
        appFontMedium = appFontStyle + ", " + str(appFontSizeMedium)
        appFontBig = appFontStyle + ", " + str(appFontSizeBig)

        # Titel
        self.labTitel = Label(master, text=tTitel, font=appFontMedium) \
            .grid(row=0, columnspan = 2)

        # Radiobutton fuer die Abfrage der auszufuehrenden Aktion
        # BMI fuer Person aus der Datenbank berechnen
        self.varRadBtn = IntVar()
        self.rbtnPerson = Radiobutton(master, text = textRbtnPerson, font = appFontSmall,
                                      value = 1, variable = self.varRadBtn)
        self.rbtnPerson.grid(row = 1, column = 0, padx = 20)

        # Label mit den Bezeichnungen erstellen
        self.labNname = Label(master, text = "Nachname", font=appFontSmall)
        self.labNname.grid(row = 2, column = 0)
        self.labVname = Label(master, text = "Vorname", font=appFontSmall)
        self.labVname.grid(row = 3, column = 0)

        self.entNname = Entry(master)
        self.entNname.grid(row = 2, column = 1)
        self.entVname = Entry(master)
        self.entVname.grid(row = 3, column = 1)

        # BMI ueber Gewicht und Groesse
        self.rbtnDaten = Radiobutton(master, text=textRbtnDaten, font=appFontSmall, value=2,
                                     variable = self.varRadBtn)
        self.rbtnDaten.grid(row = 4, column = 0, padx = 5)

        self.labGewicht = Label(master, text="Gewicht", font=appFontSmall)
        self.labGewicht.grid(row=5, column = 0)
        self.labGroesse = Label(master, text="Größe", font=appFontSmall)
        self.labGroesse.grid(row=6, column = 0)

        self.entGewicht = Entry(master)
        self.entGewicht.grid(row = 5, column = 1)
        self.entGroesse = Entry(master)
        self.entGroesse.grid(row=6, column=1)


        self.labBMI = Label(master, text = "")
        self.labBMI.grid(row = 7, columnspan = 2, padx = 20)

        self.labBMIText = Label(master, text="")
        self.labBMIText.grid(row = 8, columnspan = 2, padx=20)

        self.btnOK = Button(master, text = tBtnOK, font = appFontSmall, width=20, command = self.bmiBerechnen)
        self.btnOK.grid(row = 9, column = 0, padx = 20, pady = 20)

        self.btnEnd = Button(master, text=tBtnEnd, font = appFontSmall, command = self.master.destroy, width = 20)
        self.btnEnd.grid(row = 9, column = 1, padx = 20, pady = 20)

        self.labBMI["text"] = "Berechneter BMI: "
        self.labBMIText["text"] = "Bewertung des BMI"


    def bmiBerechnen(self):
        db = DB()
        groesse = 0.0
        gewicht = 0.0
        bmi = 0.0

        varrad = self.varRadBtn.get()
        print(varrad)


        if (self.varRadBtn.get() == 2):

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

            bmi = round(self.gewicht / (self.groesse * self.groesse), 2)

        elif (self.varRadBtn.get() == 1):
            if (groesse == "Keine Größe eingetragen"):
                return "Keine Größe eingetragen"
            elif (gewicht == "Kein Gewicht eingetragen"):
                return "Kein Gewicht eingetragen"

            groesse = db.getGroesse(self.entNname.get(), self.entVname.get())

            gewicht = db.getGewicht(self.entNname.get(), self.entVname.get())


            bmi = round(gewicht / (groesse * groesse), 2)

        #self.labBMI.config(text="Berechneter BMI: " + str(bmi))
        self.labBMI["text"] = "Berechneter BMI: " + str(bmi)

        # Bmi Angaben bewerten
        if (bmi < 20):
            self.labBMIText["text"] = "Untergewicht (BMI unter 20)"
        elif (bmi >= 20 and bmi < 24.9):
            self.labBMIText["text"] = "Normalgewicht (BMI zwischen 20 und 24,9)"
        elif (bmi >= 25 and bmi < 29.9):
            self.labBMIText["text"] = "Übergewicht (BMI zwischen 25 und 29,9)"
        elif (bmi >= 30 and bmi < 34.9):
            self.labBMIText["text"] = "Adipositas Grad I (BMI zwischen 30 und 34,9)"
        elif (bmi >= 35 and bmi < 39.9):
            self.labBMIText["text"] = "Adipositas Grad II (BMI zwischen 35 und 39,9)"
        elif (bmi >= 40 ):
            self.labBMIText["text"] = "Adipositas Grad III (BMI über 40)"
        return bmi


