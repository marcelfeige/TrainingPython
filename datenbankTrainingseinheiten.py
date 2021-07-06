import sqlite3
import os.path
import datetime
class datenbankTrainingseinheiten:


    def initDB(self):
        # Pruefen, ob eine SQL Datenbank existiert
        # Wenn nicht wird diese erzeugt
        # nameDatenbankPath = str(nameDatenbank) + ".db"
        if not os.path.exists("DatenbankTrainingseinheiten.db"):
            connection = sqlite3.connect("DatenbankTrainingseinheiten.db")
            cursor = connection.cursor()
            cursor.execute(
                '''CREATE TABLE trainingseinheiten (id INTEGER PRIMARY KEY, kategorie TEXT, bezeichnung TEXT, saetze INTEGER,
                 wiederholung INTEGER, gewicht REAL, datum TEXT)''')
            return "Datenbank erstellt"
        else:
            return "Datenbank vorhanden"

    # lesen in der Datenbank
    def leseDB(self):
        dbString = ""
        counter = 0
        # nameDatenbankPath = str(nameDatenbank) + ".db"
        if os.path.exists("DatenbankTrainingseinheiten.db"):
            connection = sqlite3.connect("DatenbankTrainingseinheiten.db")
            cursor = connection.cursor()
            cursor.execute(''' SELECT * FROM trainingseinheiten''')
            rows = cursor.fetchall()
            for row in rows:
                counter += 1
                # Datum in local Format anzeigen lassen
                datum = row[6][8:10] + "." + row[6][5:7] + "." + row[6][:4]

                dbString += \
                    str(row[0]) + ", " + row[1] + ", " + str(row[2]) + ", " + str(row[3]) + ", " +\
                    str(row[4]) + ", " + str(row[5]) + ", " + datum + "\n"
            connection.close()
            #return [dbString, str(counter)]
            return rows
        else:
            return "Datenbank nicht vorhanden"

    # schreiben in der Datenbank
    def schreibDB(self, kategorie, bezeichnung, saetze, wiederholung, gewicht, datum):
        # nameDatenbankPath = str(nameDatenbank) + ".db"

        # String Datum umwandeln
        dDatum = datetime.datetime.strptime(datum, '%d.%m.%Y')

        if os.path.exists("DatenbankTrainingseinheiten.db"):
            connection = sqlite3.connect("DatenbankTrainingseinheiten.db")
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO trainingseinheiten (kategorie, bezeichnung, saetze, wiederholung,  gewicht, datum) VALUES(?,?,?,?,?,?)''',
                           (kategorie, bezeichnung, saetze, wiederholung,  gewicht, dDatum))
            connection.commit()
            connection.close()
            return "Daten geschrieben: " + kategorie + ", " + bezeichnung + ", " + saetze + ", " + wiederholung + ", " + gewicht + ", " + datum
        else:
            return "Datenbank nicht vorhanden"

    def deleteDB(self, id):
        if os.path.exists("DatenbankTrainingseinheiten.db"):
            connection = sqlite3.connect("DatenbankTrainingseinheiten.db")
            cursor = connection.cursor()
            cursor.execute('''DELETE FROM trainingseinheiten WHERE id = ?''', (id,))
            connection.commit()
            connection.close()
        else:
            return "Datenbank nicht vorhanden"

    def updateDB(self, id, strCol, strUpdate):
        if os.path.exists("DatenbankTrainingseinheiten.db"):
            connection = sqlite3.connect("DatenbankTrainingseinheiten.db")
            cursor = connection.cursor()
            if (strCol == "kategorie"):
                cursor.execute('''UPDATE trainingseinheiten SET kategorie = ? WHERE id = ?''', (strUpdate, id))
                connection.commit()
                connection.close()
            elif (strCol == "bezeichnung"):
                cursor.execute('''UPDATE trainingseinheiten SET bezeichnung = ? WHERE id = ?''', (strUpdate, id))
                connection.commit()
                connection.close()
            elif (strCol == "saetze"):
                cursor.execute('''UPDATE trainingseinheiten SET saetze = ? WHERE id = ?''', (strUpdate, id))
                connection.commit()
                connection.close()
            elif (strCol == "wiederholung"):
                cursor.execute('''UPDATE trainingseinheiten SET wiederholung = ? WHERE id = ?''', (strUpdate, id))
                connection.commit()
                connection.close()
            elif (strCol == "gewicht"):
                cursor.execute('''UPDATE trainingseinheiten SET gewicht = ? WHERE id = ?''', (strUpdate, id))
                connection.commit()
                connection.close()
            elif (strCol == "datum"):
                cursor.execute('''UPDATE trainingseinheiten SET datum = ? WHERE id = ?''', (strUpdate, id))
                connection.commit()
                connection.close()
        else:
            return "Datenbank nicht vorhanden"

    def getEinheit(self, id):
        dbtString = []
        # nameDatenbankPath = str(nameDatenbank) + ".db"
        if os.path.exists("DatenbankTrainingseinheiten.db"):
            connection = sqlite3.connect("DatenbankTrainingseinheiten.db")
            cursor = connection.cursor()
            # DISTINCT - keine doppelten Werte
            cursor.execute(''' SELECT DISTINCT * FROM trainingseinheiten WHERE id = ?''', (id, ))
            rows = cursor.fetchall()
            for row in rows:
                dbtString.append(row[0])
            connection.close()
            return dbtString

        else:
            return "Datenbank nicht vorhanden"

    def getGewicht(self, startDatum, endDatum, bezeichnung):
        listGewicht = []
        listDatum = []
        rows = []
        # String Datum in Datum umwandeln
        dStartDatum = datetime.datetime.strptime(startDatum, '%d.%m.%Y')
        dEndDatum = datetime.datetime.strptime(endDatum, '%d.%m.%Y')

        datumCount = dStartDatum

        # nameDatenbankPath = str(nameDatenbank) + ".db"
        if os.path.exists("DatenbankTrainingseinheiten.db"):
            connection = sqlite3.connect("DatenbankTrainingseinheiten.db")
            cursor = connection.cursor()
            for tag in range((dEndDatum - dStartDatum).days + 1):
            # DISTINCT - keine doppelten Werte
                cursor.execute(''' SELECT id, gewicht, datum FROM trainingseinheiten WHERE datum = ? AND bezeichnung = ?''', (datumCount, bezeichnung))

                # id, gewicht und datum speichern
                row = cursor.fetchall()
                rows = rows + row

                # Von Start bis Enddatum einen Tag dazuaddieren
                datumCount = datumCount + datetime.timedelta(days = 1)
                test = "test"

            id = [id[0] for id in rows]
            gewicht = [gewicht[1] for gewicht in rows]
            datum = [datum[2] for datum in rows]

            connection.close()

            dict = {"Id": id,
                         "Gewicht": gewicht,
                         "Datum": datum}

            return dict

        else:
            return "Datenbank nicht vorhanden"





