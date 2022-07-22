from flaskr.server.bo.Jalousien import JalousienBO
from flaskr.server.database.Mapper import Mapper


class JalousienMapper(Mapper):
    '''
    Implemenierung der Mapper-Klasse für Jalousien bzw. Jalousiensteuerungsgeräte.
    Hierzu wird eine Reihe von Methoden zur Verfügung gestellt, mit deren Hilfe z.B.
    Objekte gesucht, erzeugt, modifiziert und gelöscht werden können.
    Das Mapping ist bidirektional. D.h., Objekte können in DB-Strukturen und DB-Strukturen in Objekte umgewandelt werden.
    '''

    def __init__(self):
        super().__init__()

    def insert(self, jalousie):
        """Einfügen eines Jalousie-Objekts in die Datenbank.

        Dabei wird auch der Primärschlüssel des übergebenen Objekts geprüft und ggf.
        berichtigt.

        :param jalousie das zu speichernde Objekt
        :return das bereits übergebene Objekt, jedoch mit ggf. korrigierter ID.
        """
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM jalousien")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            if len(maxid) == 1:
                jalousie.set_id(1)
            else:
                jalousie.set_id(int(maxid[0]) + 1)

        command = "INSERT INTO jalousien (id, device_id, ip_address, local_key) VALUES (%s,%s,%s,%s)"
        data = (jalousie.get_id(), jalousie.get_device_id(),
                jalousie.get_ip_address(), jalousie.get_local_key())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()
        return jalousie

    def find_all(self):
        """
        Auslesen aller Jalousie-Steuerungsgeräte.
        :return: Array mit Jalousie-Steuerungsgeräten
        """
        result = []
        cursor = self._cnx.cursor()
        cursor.execute(
            "SELECT * from Smartoffice.jalousien")
        tuples = cursor.fetchall()

        for (id, ip_address, local_key, device_id) in tuples:
            jalousie = JalousienBO()
            jalousie.set_id(id)
            jalousie.set_device_id(device_id)
            jalousie.set_ip_address(ip_address)
            jalousie.set_local_key(local_key)
            result.append(jalousie)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_device_id(self, device_id):
        """
        Lädt eine Jalousie aus der Datenbank mithilfe einer Device-Id.
        :param device_id Id des Geräts
        :return: JalousieBO
        """
        result = None
        cursor = self._cnx.cursor()
        command = "SELECT id, device_id, ip_address, local_key FROM jalousien WHERE device_id={} ORDER BY id".format(
            device_id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, device_id, ip_address, local_key) in tuples:
            jalousie = JalousienBO()
            jalousie.set_id(id)
            jalousie.set_device_id(device_id)
            jalousie.set_ip_address(ip_address)
            result = jalousie

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_id(self, id):
        """
        Lädt eine Jalousie aus der Datenbank mithilfe der Jalousie-Id
        :param id: Id des JalousieBOs
        :return: JalousieBO
        """
        result = None
        cursor = self._cnx.cursor()
        command = "SELECT id, device_id, ip_address, local_key FROM jalousien WHERE id={} ORDER BY id".format(
            id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, device_id, ip_address, local_key) in tuples:
            jalousie = JalousienBO()
            jalousie.set_id(id)
            jalousie.set_device_id(device_id)
            jalousie.set_ip_address(ip_address)
            result = jalousie

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_key(self, local_key):
        """
        Lädt eine Jalousie aus der Datenbank mithilfe einer local-key.
        :param local_key: Local-Key des Geräts
        :return: JalousieBO
        """
        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, device_id, ip_address, local_key FROM jalousien WHERE local_key={}".format(
            local_key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        if tuples[0] is not None:
            (id, device_id, ip_address, local_key) = tuples[0]
            jalousie = JalousienBO()
            jalousie.set_id(id)
            jalousie.set_device_id(device_id)
            jalousie.set_ip_address(ip_address)
            jalousie.set_local_key(local_key)
            result = jalousie

        self._cnx.commit()
        cursor.close()
        return result

    def update(self, jalousie):
        """
        Wiederholtes Schreiben eines Objekts in die Datenbank.
        :param jalousie das Objekt, das in die DB geschrieben werden soll
        """
        cursor = self._cnx.cursor()

        command = "UPDATE jalousien " + \
            "SET device_id=%s, ip_address=%s, local_key=%s WHERE id=%s"
        data = (jalousie.get_device_id(), jalousie.get_ip_address(),
                jalousie.get_local_key(), jalousie.get_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

    def delete(self, jalousie):
        """
        Löschen eines Jalousie-Objekts aus der Datenbank.
        :param jalousie: das aus der DB zu löschende "Objekt"
        """
        cursor = self._cnx.cursor()

        command = "DELETE FROM jalousien WHERE id={}".format(jalousie.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()
