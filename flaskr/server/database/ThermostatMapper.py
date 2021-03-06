from flaskr.server.database.Mapper import Mapper
from flaskr.server.bo.Thermostat import ThermostatBO


class ThermostatMapper(Mapper):
    '''
    Implemenierung der Mapper-Klasse für Thermostate.
    Hierzu wird eine Reihe von Methoden zur Verfügung gestellt, mit deren Hilfe z.B.
    Objekte gesucht, erzeugt, modifiziert und gelöscht werden können.
    Das Mapping ist bidirektional. D.h., Objekte können in DB-Strukturen und DB-Strukturen in Objekte umgewandelt werden.
    '''

    def __init__(self):
        super().__init__()

    def insert(self, thermostat):
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM thermostate ")
        tuples = cursor.fetchall()
        for (maxid) in tuples:
            if len(maxid) == 1:
                thermostat.set_id(1)
            else:
                thermostat.set_id(int(maxid[0]) + 1)

        command = "INSERT INTO thermostate (id, ain) VALUES (%s, %s)"
        data = (
            thermostat.get_id(),
            thermostat.get_ain(),
            thermostat.get_sid()
        )

        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()
        return thermostat

    def find_all(self):
        """
        Auslesen aller Thermostate aus der Datenbank.
        :return: Array mit ThermostatBOs
        """
        result = []
        cursor = self._cnx.cursor()
        command = "SELECT id, ain FROM thermostate"
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id) in tuples:
            thermostat = ThermostatBO()
            thermostat.set_id(id)
            result.append(thermostat)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_ain(self, ain):
        result = None

        cursor = self._cnx.cursor()
        command = "SELECT ain FROM thermostate WHERE ain={}".format(
            ain)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (ain) = tuples[0]
            thermostat = ThermostatBO()
            thermostat.set_ain(ain)
            result = thermostat

        except IndexError:
            """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
            keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_key(self, id):
        result = None

        cursor = self._cnx.cursor()
        command = "SELECT ain  FROM thermostate WHERE id={}".format(
            id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id) = tuples[0]
            thermostat = ThermostatBO()
            thermostat.set_id(id)
            result = thermostat

        except IndexError:
            """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
            keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def update(self, thermostat):
        """
        Wiederholtes Schreiben eines Objekts in die Datenbank.
        :param thermostat: das Objekt, das in die DB geschrieben werden soll
        """
        cursor = self._cnx.cursor()

        command = "UPDATE thermostate " + \
            "SET ain=%s WHERE id=%s"
        data = (thermostat.get_ain())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return thermostat

    def delete(self, thermostat):
        """
        Löschen eines Thermostat-Objekts aus der Datenbank.
        :param thermostat: das aus der DB zu löschende "Objekt"
        """
        cursor = self._cnx.cursor()

        command = "DELETE FROM thermostate WHERE id={}".format(
            thermostat.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()
