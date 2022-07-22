from flaskr.server.database.Mapper import Mapper
from flaskr.server.bo.weekdays_jal.MondayBO import Monday


class MondayMapper(Mapper):
    '''
    Implemenierung der Mapper-Klasse für Wochenplaneinträge am Montag.
    Hierzu wird eine Reihe von Methoden zur Verfügung gestellt, mit deren Hilfe z.B.
    Objekte gesucht, erzeugt, modifiziert und gelöscht werden können.
    Das Mapping ist bidirektional. D.h., Objekte können in DB-Strukturen und DB-Strukturen in Objekte umgewandelt werden.
    '''

    def __init__(self):
        super().__init__()

    def insert(self, monday):
        """Einfügen eines Monday-Objekts in die Datenbank.

        Dabei wird auch der Primärschlüssel des übergebenen Objekts geprüft und ggf.
        berichtigt.

        :param monday das zu speichernde Objekt
        :return das bereits übergebene Objekt, jedoch mit ggf. korrigierter ID.
        """
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM monday")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            if maxid[0] is None:
                monday.set_id(1)
            else:
                """Wenn wir KEINE maximale ID feststellen konnten, dann gehen wir
                davon aus, dass die Tabelle leer ist und wir mit der ID 1 beginnen können."""
                monday.set_id(maxid[0] + 1)

        command = "INSERT INTO monday (id, type, start_time, end_time, value) VALUES (%s, %s, %s, %s, %s)"
        data = (
            monday.get_id(),
            monday.get_type(),
            monday.get_start_time(),
            monday.get_end_time(),
            monday.get_value()
        )

        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()
        return monday

    def find_all(self):
        """
        Auslesen aller Einträge zu Montag.
        :return: Array mit MondayBOs
        """
        result = []
        cursor = self._cnx.cursor()
        command = "SELECT * FROM monday"
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, type, start_time, end_time, value) in tuples:
            monday = Monday()
            monday.set_id(id)
            monday.set_type(type)
            monday.set_start_time(start_time)
            monday.set_end_time(end_time)
            monday.set_value(value)
            result.append(monday)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_key(self, key):
        """
        Lädt einen Montagseintrag aus der Datenbank mithilfe der Id
        :param id: MondayBO-Id
        :return: MondayBO
        """
        result = None
        cursor = self._cnx.cursor()
        command = "SELECT * FROM monday WHERE id={}".format(key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, type, start_time, end_time, value) = tuples[0]
            monday = Monday()
            monday.set_id(id)
            monday.set_type(type)
            monday.set_start_time(start_time)
            monday.set_end_time(end_time)
            monday.set_value(value)
            result = monday

        except IndexError:
            """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
            keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
            result = None

        self._cnx.commit()
        cursor.close()

        return result


    def find_all_jal_entries(self):
        '''
        Lädt alle  Jalousien-Eintrage am Montag aus der Datenbank
        :return: Liste mit MondayBOs
        '''
        result = []
        cursor = self._cnx.cursor()
        command = "SELECT * FROM monday WHERE type='J'"
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, type, start_time, end_time, value) in tuples:
            monday = Monday()
            monday.set_id(id)
            monday.set_type(type)
            monday.set_start_time(start_time)
            monday.set_end_time(end_time)
            monday.set_value(value)
            result.append(monday)

        self._cnx.commit()
        cursor.close()

        return result

    def find_all_temp_entries(self):
        '''
        Lädt alle  Thermostat-Eintrage am Donnertstag aus der Datenbank
        :return: Liste mit ThursdayBOs
        '''
        result = []
        cursor = self._cnx.cursor()
        command = "SELECT * FROM monday WHERE type='T'"
        cursor.execute(command)
        tuples = cursor.fetchall()


        for (id, type, start_time, end_time, value) in tuples:
            monday = Monday()
            monday.set_id(id)
            monday.set_type(type)
            monday.set_start_time(start_time)
            monday.set_end_time(end_time)
            monday.set_value(value)
            result.append(monday)

        self._cnx.commit()
        cursor.close()

        return result

    def find_latest_jal_entry(self):
        '''
        Lädt den letzten Jalousien-Eintrag am Montag aus der Datenbank
        :return: MondayBO
        '''
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM monday WHERE type='J'")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            command = "SELECT * FROM monday WHERE id={}".format(maxid[0])
            cursor.execute(command)
            tuples = cursor.fetchall()

            try:
                (id, type, start_time, end_time, value) = tuples[0]
                monday = Monday()
                monday.set_id(id)
                monday.set_type(type)
                monday.set_start_time(start_time)
                monday.set_end_time(end_time)
                monday.set_value(value)
                result = monday

            except IndexError:
                """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
                keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
                result = None

            self._cnx.commit()
            cursor.close()

            return result

    def find_latest_temp_entry(self):
        '''
        Lädt den letzten Thermostat-Eintrag am Montag aus der Datenbank
        :return: MondayBO
        '''
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM monday WHERE type='T'")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            command = "SELECT * FROM monday WHERE id={}".format(maxid[0])
            cursor.execute(command)
            tuples = cursor.fetchall()

            try:
                (id, type, start_time, end_time, value) = tuples[0]
                monday = Monday()
                monday.set_id(id)
                monday.set_type(type)
                monday.set_start_time(start_time)
                monday.set_end_time(end_time)
                monday.set_value(value)
                result = monday

            except IndexError:
                """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
                keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
                result = None

            self._cnx.commit()
            cursor.close()

            return result

    def update(self, monday):
        """Wiederholtes Schreiben eines Objekts in die Datenbank.

        :param jalousie das Objekt, das in die DB geschrieben werden soll
        """
        cursor = self._cnx.cursor()

        command = "UPDATE monday " + \
                  "SET value=%s, start_time=%s, end_time=%s WHERE id=%s and type=%s"
        data = (monday.get_value(), monday.get_start_time(), monday.get_end_time(), monday.get_id(), monday.get_type())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return monday

    def delete(self, monday):
        """
        Löschen eines Montag-Objekts aus der Datenbank.
        :param monday: das aus der DB zu löschende "Objekt"
        """
        cursor = self._cnx.cursor()

        command = "DELETE FROM monday WHERE id=%s and type=%s"
        data = (monday.get_id(), monday.get_type())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()
    
    def delete_by_id(self, id):
        """
        Löschen eines Montag-Objekts aus der Datenbank mithilfe deren Id.
        :param id: Id des aus der DB zu löschende "Objekts"
        """
        cursor = self._cnx.cursor()

        command = "DELETE FROM monday WHERE monday_id={}".format(id)
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()

    