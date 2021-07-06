
# Datenbank mit Benutzereingabe und -ausgabe
# Speicherung von Uebungen

import sqlite3
import os.path

class datenbankUebung:

    tKategorien = ["Beine", "Rücken", "Oberkörper", "Arme"]
    tGruppe = ["Langhantel", "Kurz Hantel", "Gerät", "Frei"]

    def initDB(self):
        # Pruefen, ob eine SQL Datenbank existiert
        # Wenn nicht wird diese erzeugt
        #nameDatenbankPath = str(nameDatenbank) + ".db"
        if not os.path.exists("DatenbankUebungen.db"):
            connection = sqlite3.connect("DatenbankUebungen.db")
            cursor = connection.cursor()
            cursor.execute(
                '''CREATE TABLE uebungen(id INTEGER PRIMARY KEY, kategorie TEXT, gruppe TEXT, bezeichnung TEXT)''')
            return "Datenbank erstellt"
        else:
            return "Datenbank vorhanden"

    # lesen in der Datenbank
    def leseDB(self):
        dbString = ""
        counter = 0
        #nameDatenbankPath = str(nameDatenbank) + ".db"
        if os.path.exists("DatenbankUebungen.db"):
            connection = sqlite3.connect("DatenbankUebungen.db")
            cursor = connection.cursor()
            cursor.execute(''' SELECT * FROM uebungen''')
            rows = cursor.fetchall()
            for row in rows:
                counter += 1
                dbString +=\
                    str(row[0]) + ", " + row[1] + ", " + str(row[2]) + ", " + str(row[3]) + "\n"
            connection.close()
            #return [dbString, str(counter)]
            return rows
        else:
            return "Datenbank nicht vorhanden"

    # schreiben in der Datenbank
    def schreibDB(self, kategorie, gruppe, bezeichnung):
        #nameDatenbankPath = str(nameDatenbank) + ".db"
        if os.path.exists("DatenbankUebungen.db"):
            connection = sqlite3.connect("DatenbankUebungen.db")
            cursor = connection.cursor()

            cursor.execute('''INSERT INTO uebungen (kategorie, gruppe, bezeichnung) VALUES(?,?,?)''', (kategorie, gruppe, bezeichnung))
            connection.commit()
            connection.close()
            return "Daten geschrieben: " + kategorie + ", " + gruppe + ", " + bezeichnung
        else:
            return "Datenbank nicht vorhanden"

    def deleteDB(self, id):
        if os.path.exists("DatenbankUebungen.db"):
            connection = sqlite3.connect("DatenbankUebungen.db")
            cursor = connection.cursor()
            cursor.execute('''DELETE FROM uebungen WHERE id = ?''', (id, ))
            connection.commit()
            connection.close()
        else:
            return "Datenbank nicht vorhanden"

    def updateDB(self, id, strCol, strUpdate):
        if os.path.exists("DatenbankUebungen.db"):
            connection = sqlite3.connect("DatenbankUebungen.db")
            cursor = connection.cursor()
            if (strCol == "kategorie"):
                cursor.execute('''UPDATE uebungen SET kategorie = ? WHERE id = ?''', (strUpdate, id))
                connection.commit()
                connection.close()
            elif (strCol == "gruppe"):
                cursor.execute('''UPDATE uebungen SET gruppe = ? WHERE id = ?''', (strUpdate, id))
                connection.commit()
                connection.close()
            elif (strCol == "bezeichnung"):
                cursor.execute('''UPDATE uebungen SET bezeichnung = ? WHERE id = ?''', (strUpdate, id))
                connection.commit()
                connection.close()
        else:
            return "Datenbank nicht vorhanden"

    def getKategorie(self):
        dbtString = []
        #nameDatenbankPath = str(nameDatenbank) + ".db"
        if os.path.exists("DatenbankUebungen.db"):
            connection = sqlite3.connect("DatenbankUebungen.db")
            cursor = connection.cursor()
            # DISTINCT - keine doppelten Werte
            cursor.execute(''' SELECT DISTINCT kategorie FROM uebungen''')
            rows = cursor.fetchall()
            for row in rows:
                dbtString.append(row[0])
            connection.close()
            return dbtString

        else:
            return "Datenbank nicht vorhanden"

    def getBezeichnung(self, tkategorie):
        dbtString = []
        counter = 0
        #nameDatenbankPath = str(nameDatenbank) + ".db"
        if os.path.exists("DatenbankUebungen.db"):
            connection = sqlite3.connect("DatenbankUebungen.db")
            cursor = connection.cursor()
            cursor.execute(''' SELECT bezeichnung FROM uebungen WHERE kategorie LIKE ?''', (tkategorie, ))
            rows = cursor.fetchall()
            for row in rows:
                dbtString.append(row[0])
            connection.close()
            return dbtString

        else:
            return "Datenbank nicht vorhanden"



