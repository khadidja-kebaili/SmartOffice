from flaskr.server.bo.JalosuienStatusBO import JalousienStatusBO
from flaskr.server.database.Mapper import Mapper
from datetime import datetime


class JalousienStatusMapper(Mapper):
    """Mapper-Klasse, die Account-Objekte auf eine relationale
    Datenbank abbildet. Hierzu wird eine Reihe von Methoden zur Verfügung
    gestellt, mit deren Hilfe z.B. Objekte gesucht, erzeugt, modifiziert und
    gelöscht werden können. Das Mapping ist bidirektional. D.h., Objekte können
    in DB-Strukturen und DB-Strukturen in Objekte umgewandelt werden.
    """

    def __init__(self):
        super().__init__()

    def insert(self, status):
        """Einfügen eines Account-Objekts in die Datenbank.

        Dabei wird auch der Primärschlüssel des übergebenen Objekts geprüft und ggf.
        berichtigt.

        :param status das zu speichernde Objekt
        :return das bereits übergebene Objekt, jedoch mit ggf. korrigierter ID.
        """
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM jalousienstatus")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            if maxid[0] is not None:
                status.set_id(maxid[0]+1)
            else:
                status.set_id(1)

        command = "INSERT INTO jalousienstatus (id, percentage, status, jalousieid, date) VALUES (%s,%s,%s,%s,%s)"
        data = (status.get_id(), status.get_percentage(),
                status.get_status(), status.get_device(), status.get_date())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()
        return status

    def find_all(self):
        """Auslesen aller Konten.

        :return Eine Sammlung mit Account-Objekten, die sämtliche Konten
                repräsentieren.
        """
        result = []
        cursor = self._cnx.cursor()
        cursor.execute(
            "SELECT id, percentage, status, jalousieid, date from jalousienstatus")
        tuples = cursor.fetchall()

        for (id, percentage, status, jalousieid, date) in tuples:
            jalousie = JalousienStatusBO()
            jalousie.set_id(id)
            jalousie.set_percentage(percentage)
            jalousie.set_status(status)
            jalousie.set_device(jalousieid)
            jalousie.set_date(date)
            result.append(jalousie)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_key(self, id):
        """Auslesen aller Konten eines durch Fremdschlüssel (Kundennr.) gegebenen Kunden.

        :param device_id Schlüssel des zugehörigen Kunden.
        :return Eine Sammlung mit Account-Objekten, die sämtliche Konten des
                betreffenden Kunden repräsentieren.
        """
        result = None
        cursor = self._cnx.cursor()
        command = "SELECT id, percentage, status, jalousieid, date FROM jalousienstatus WHERE id={} ORDER BY id".format(
            id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, percentage, status, jalousieid, date) in tuples:
            jalousie = JalousienStatusBO()
            jalousie.set_id(id)
            jalousie.set_percentage(percentage)
            jalousie.set_status(status)
            jalousie.set_device(jalousieid)
            jalousie.set_date(date)
            result = jalousie

        self._cnx.commit()
        cursor.close()

        return result

    def update(self, status):
        """Wiederholtes Schreiben eines Objekts in die Datenbank.

        :param status das Objekt, das in die DB geschrieben werden soll
        """
        cursor = self._cnx.cursor()

        command = "UPDATE jalousienstatus " + "SET status=%s WHERE id=%s"
        data = (status.get_id(), status.get_status())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

    def delete(self, status):
        """Löschen der Daten eines Account-Objekts aus der Datenbank.

        :param status das aus der DB zu löschende "Objekt"
        """
        cursor = self._cnx.cursor()

        command = "DELETE FROM jalousienstatus WHERE id={}".format(
            status.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()