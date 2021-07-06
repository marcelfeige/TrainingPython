
# Datenbank mit Benutzereingabe und -ausgabe

import sqlite3
import os.path

class datenbankPersonen:
    def initDB(self):
        # Pruefen, ob eine SQL Datenbank existiert
        # Wenn nicht wird diese erzeugt
        #nameDatenbankPath = str(nameDatenbank) + ".db"
        if not os.path.exists("personenDatenbank.db"):
            connection = sqlite3.connect("personenDatenbank.db")
            cursor = connection.cursor()
            cursor.execute('''CREATE TABLE personen(id INTEGER PRIMARY KEY, name TEXT, vorname TEXT, age INTEGER, groesse REAL, gewicht REAL)''')
            return "Datenbank erstellt"
        else:
            return "Datenbank vorhanden"

    # lesen in der Datenbank
    def leseDB(self):
        dbString = ""
        counter = 0
        #nameDatenbankPath = str(nameDatenbank) + ".db"
        if os.path.exists("personenDatenbank.db"):
            connection = sqlite3.connect("personenDatenbank.db")
            cursor = connection.cursor()
            cursor.execute(''' SELECT * FROM personen''')
            rows = cursor.fetchall()
            for row in rows:
                counter += 1
                dbString +=\
                    str(row[0]) + ", " + row[1] + ", " + str(row[2]) + ", " + str(row[3]) +\
                    ", " + str(row[4]) + ", " + str(row[5]) + "\n"
            connection.close()
            return [dbString, str(counter)]
        else:
            return "Datenbank nicht vorhanden"

    # schreiben in der Datenbank
    def schreibDB(self, nname, vname, alter, groesse, gewicht):
        #nameDatenbankPath = str(nameDatenbank) + ".db"
        if os.path.exists("personenDatenbank.db"):
            connection = sqlite3.connect("personenDatenbank.db")
            cursor = connection.cursor()

            cursor.execute('''INSERT INTO personen (name, vorname, age, groesse, gewicht) VALUES(?,?,?,?,?)''', (nname, vname, alter, groesse, gewicht))
            connection.commit()
            connection.close()
            return "Daten geschrieben: " + nname + ", " + vname + ", " + alter + ", " + str(groesse) + ", " + str(gewicht)
        else:
            return "Datenbank nicht vorhanden"

    def deleteDB(self, id):
        if os.path.exists("personenDatenbank.db"):
            connection = sqlite3.connect("personenDatenbank.db")
            cursor = connection.cursor()
            cursor.execute('''DELETE FROM personen WHERE id = ?''', (id, ))
            connection.commit()
            connection.close()
        else:
            return "Datenbank nicht vorhanden"

    # Bearbeitung ohne if Abfrage moeglich ????
    def updateDB(self, id, strCol, strUpdate):
        if os.path.exists("personenDatenbank.db"):
            connection = sqlite3.connect("personenDatenbank.db")
            cursor = connection.cursor()

            if (strCol == "name"):
                cursor.execute('''UPDATE personen SET name = ? WHERE id = ?''', (strUpdate, id))
                connection.commit()
                connection.close()
            elif (strCol == "vorname"):
                cursor.execute('''UPDATE personen SET vorname = ? WHERE id = ?''', (strUpdate, id))
                connection.commit()
                connection.close()
            elif (strCol == "age"):
                cursor.execute('''UPDATE personen SET age = ? WHERE id = ?''', (strUpdate, id))
                connection.commit()
                connection.close()
            elif (strCol == "groesse"):
                cursor.execute('''UPDATE personen SET groesse = ? WHERE id = ?''', (strUpdate, id))
                connection.commit()
                connection.close()
            elif (strCol == "gewicht"):
                cursor.execute('''UPDATE personen SET gewicht = ? WHERE id = ?''', (strUpdate, id))
                connection.commit()
                connection.close()

        else:
            return "Datenbank nicht vorhanden"

    def getGroesse(self, nname, vname):
        fGroesse = 0.0
        #nameDatenbankPath = str(nameDatenbank) + ".db"
        if os.path.exists("personenDatenbank.db"):
            connection = sqlite3.connect("personenDatenbank.db")
            cursor = connection.cursor()
            cursor.execute(''' SELECT groesse REAL FROM personen WHERE name = ? AND vorname = ?''', (nname, vname))
            rows = cursor.fetchone()

            fGroesse = float(rows[0])

            return fGroesse
        else:
                return "Keine Größe eingetragen"


    def getGewicht(self, nname, vname):
        fGewicht = 0.0
        # nameDatenbankPath = str(nameDatenbank) + ".db"
        if os.path.exists("personenDatenbank.db"):
            connection = sqlite3.connect("personenDatenbank.db")
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()
            cursor.execute(''' SELECT gewicht REAL FROM personen WHERE name = ? AND vorname = ?''', (nname, vname))
            rows = cursor.fetchone()

            fGewicht = float(rows[0])

            return fGewicht
        else:
            return "Kein Gewicht eingetragen"