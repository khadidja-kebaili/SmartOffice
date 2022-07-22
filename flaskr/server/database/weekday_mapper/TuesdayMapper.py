from flaskr.server.database.Mapper import Mapper
from flaskr.server.bo.weekdays_jal.TuesdayBO import Tuesday

class TuesdayMapper(Mapper):
    '''
    Implemenierung der Mapper-Klasse für Wochenplaneinträge am Dienstag.
    Hierzu wird eine Reihe von Methoden zur Verfügung gestellt, mit deren Hilfe z.B.
    Objekte gesucht, erzeugt, modifiziert und gelöscht werden können.
    Das Mapping ist bidirektional. D.h., Objekte können in DB-Strukturen und DB-Strukturen in Objekte umgewandelt werden.
    '''

    def __init__(self):
        super().__init__()

    def insert(self, tuesday):
        """Einfügen eines Tuesday-Objekts in die Datenbank.

        Dabei wird auch der Primärschlüssel des übergebenen Objekts geprüft und ggf.
        berichtigt.

        :param tuesday das zu speichernde Objekt
        :return das bereits übergebene Objekt, jedoch mit ggf. korrigierter ID.
        """
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM tuesday")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            if maxid[0] is None:
                tuesday.set_id(1)
            else:
                """Wenn wir KEINE maximale ID feststellen konnten, dann gehen wir
                davon aus, dass die Tabelle leer ist und wir mit der ID 1 beginnen können."""
                tuesday.set_id(maxid[0]+1)

        command = "INSERT INTO tuesday (id, type, start_time, end_time, value) VALUES (%s, %s, %s, %s, %s)"
        data = (
            tuesday.get_id(),
            tuesday.get_type(),
            tuesday.get_start_time(),
            tuesday.get_end_time(),
            tuesday.get_value()
            )

        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()
        return tuesday

    def find_all(self):
        """
        Auslesen aller Einträge zu Dienstag.
        :return: Array mit TuesdayBOs
        """
        result = []
        cursor = self._cnx.cursor()
        command = "SELECT * FROM tuesday"
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, type, start_time, end_time, value) in tuples:
            tuesday = Tuesday()
            tuesday.set_id(id)
            tuesday.set_type(type)
            tuesday.set_start_time(start_time)
            tuesday.set_end_time(end_time)
            tuesday.set_value(value)
            result.append(tuesday)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_key(self, key):
        """
        Lädt einen Dienstagseintrag aus der Datenbank mithilfe der Id
        :param id: TuesdayBO-Id
        :return: TuesdayBO
        """
        result = None
        cursor = self._cnx.cursor()
        command = "SELECT * FROM tuesday WHERE id={}".format(key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, type, start_time, end_time, value) = tuples[0]
            tuesday = Tuesday()
            tuesday.set_id(id)
            tuesday.set_type(type)
            tuesday.set_start_time(start_time)
            tuesday.set_end_time(end_time)
            tuesday.set_value(value)
            result = tuesday

        except IndexError:
            """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
            keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def find_all_jal_entries(self):
        '''
        Lädt alle  Jalousien-Eintrage am Dienstag aus der Datenbank
        :return: Liste mit TuesdayBOs
        '''
        result = []
        cursor = self._cnx.cursor()
        command = "SELECT * FROM tuesday WHERE type='J'"
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, type, start_time, end_time, value) in tuples:
            tuesday = Tuesday()
            tuesday.set_id(id)
            tuesday.set_type(type)
            tuesday.set_start_time(start_time)
            tuesday.set_end_time(end_time)
            tuesday.set_value(value)
            result.append(tuesday)

        self._cnx.commit()
        cursor.close()

        return result

    def find_all_temp_entries(self):
        '''
        Lädt alle  Thermostat-Eintrage am Dienstag aus der Datenbank
        :return: Liste mit TuesdayBOs
        '''
        result = []
        cursor = self._cnx.cursor()
        command = "SELECT * FROM tuesday WHERE type='T'"
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, type, start_time, end_time, value) in tuples:
            tuesday = Tuesday()
            tuesday.set_id(id)
            tuesday.set_type(type)
            tuesday.set_start_time(start_time)
            tuesday.set_end_time(end_time)
            tuesday.set_value(value)
            result.append(tuesday)

        self._cnx.commit()
        cursor.close()

        return result

    def find_latest_jal_entry(self):
        '''
        Lädt den letzten Jalousien-Eintrag am Dienstag aus der Datenbank
        :return: TuesdayBO
        '''
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM tuesday")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            command = "SELECT * FROM tuesday WHERE id={} and type='J'".format(maxid[0])
            cursor.execute(command)
            tuples = cursor.fetchall()

            try:
                (id, type, start_time, end_time, value) = tuples[0]
                tuesday = Tuesday()
                tuesday.set_id(id)
                tuesday.set_type(type)
                tuesday.set_start_time(start_time)
                tuesday.set_end_time(end_time)
                tuesday.set_value(value)
                result = tuesday

            except IndexError:
                """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
                keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
                result = None

            self._cnx.commit()
            cursor.close()

            return result

    def find_latest_temp_entry(self):
        '''
        Lädt den letzten Thermostat-Eintrag am Dienstag aus der Datenbank
        :return: TuesdayBO
        '''
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM tuesday")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            command = "SELECT * FROM tuesday WHERE id={} and type='T'".format(maxid[0])
            cursor.execute(command)
            tuples = cursor.fetchall()

            try:
                (id, type, start_time, end_time, value) = tuples[0]
                tuesday = Tuesday()
                tuesday.set_id(id)
                tuesday.set_type(type)
                tuesday.set_start_time(start_time)
                tuesday.set_end_time(end_time)
                tuesday.set_value(value)
                result = tuesday

            except IndexError:
                """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
                keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
                result = None

            self._cnx.commit()
            cursor.close()

            return result

    def update(self, tuesday):
        """Wiederholtes Schreiben eines Objekts in die Datenbank.

        :param jalousie das Objekt, das in die DB geschrieben werden soll
        """
        cursor = self._cnx.cursor()

        command = "UPDATE tuesday " + \
            "SET value=%s, start_time=%s, end_time=%s WHERE id=%s and type=%s"
        data = (tuesday.get_value(), tuesday.get_start_time(), tuesday.get_end_time(), tuesday.get_id(), tuesday.get_type())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return tuesday

    def delete(self, tuesday):
        """
        Löschen eines Dienstag-Objekts aus der Datenbank.

        :param tuesday: das aus der DB zu löschende "Objekt"
        """
        cursor = self._cnx.cursor()

        command = "DELETE FROM tuesday WHERE id=%s and type=%s"
        data = (tuesday.get_id(), tuesday.get_type())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

