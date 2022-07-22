from flaskr.server.database.Mapper import Mapper
from flaskr.server.bo.WochenplanThermoBO import WeeklyPlanTempBO


class WeeklyPlanTempMapper(Mapper):
    '''
    Implemenierung der Mapper-Klasse für Thermostat-Wochenplaneinträge.
    Hierzu wird eine Reihe von Methoden zur Verfügung gestellt, mit deren Hilfe z.B.
    Objekte gesucht, erzeugt, modifiziert und gelöscht werden können.
    Das Mapping ist bidirektional. D.h., Objekte können in DB-Strukturen und DB-Strukturen in Objekte umgewandelt werden.
    '''

    def __init__(self):
        super().__init__()

    def insert(self, entry):
        """Einfügen eines Thermostat-Wochenplaneintrag-Objekts in die Datenbank.

        Dabei wird auch der Primärschlüssel des übergebenen Objekts geprüft und ggf.
        berichtigt.

        :param entry das zu speichernde Objekt
        :return das bereits übergebene Objekt, jedoch mit ggf. korrigierter ID.
        """
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM standard_temp ")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            if maxid[0] is None:
                entry.set_id(1)
            else:
                """Wenn wir KEINE maximale ID feststellen konnten, dann gehen wir
                davon aus, dass die Tabelle leer ist und wir mit der ID 1 beginnen können."""
                entry.set_id(maxid[0] + 1)

        command = "INSERT INTO standard_temp (id, weekday, monday_id, tuesday_id, wednesday_id, thursday_id, friday_id) \
                  VALUES (%s, %s, %s, %s, %s, %s, %s)"
        data = (
            entry.get_id(),
            entry.get_weekday(),
            entry.get_monday_id(),
            entry.get_tuesday_id(),
            entry.get_wednesday_id(),
            entry.get_thursday_id(),
            entry.get_friday_id()
        )

        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()
        return entry

    def find_all(self):
        """
        Auslesen aller Thermostat-Wochenplaneinträge aus der Datenbank.
        :return: Array mit WeeklyPlanTempBOs
        """
        result = []
        cursor = self._cnx.cursor()
        command = "SELECT * FROM standard_temp"
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, weekday, monday_id, tuesday_id, wednesday_id, thursday_id, friday_id) in tuples:
            weeklyplanjal = WeeklyPlanTempBO()
            weeklyplanjal.set_id(id)
            weeklyplanjal.set_weekday(weekday),
            weeklyplanjal.set_monday_id(monday_id),
            weeklyplanjal.set_tuesday_id(tuesday_id),
            weeklyplanjal.set_wednesday_id(wednesday_id),
            weeklyplanjal.set_thursday_id(thursday_id),
            weeklyplanjal.set_friday_id(friday_id)
            result.append(weeklyplanjal)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_key(self, key):
        cursor = self._cnx.cursor()
        command = "SELECT * FROM standard_temp WHERE id={}".format(key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, weekday, monday_id, tuesday_id, wednesday_id, thursday_id, friday_id) = tuples[0]
            weeklyplanjal = WeeklyPlanTempBO()
            weeklyplanjal.set_id(id)
            weeklyplanjal.set_weekday(weekday),
            weeklyplanjal.set_monday_id(monday_id),
            weeklyplanjal.set_tuesday_id(tuesday_id),
            weeklyplanjal.set_wednesday_id(wednesday_id),
            weeklyplanjal.set_thursday_id(thursday_id),
            weeklyplanjal.set_friday_id(friday_id)
            result = weeklyplanjal

        except IndexError:
            """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
            keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_weekday(self, weekday):
        result = []
        cursor = self._cnx.cursor()
        command = "SELECT * FROM standard_temp WHERE weekday={}".format(weekday)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, weekday, monday_id, tuesday_id, wednesday_id, thursday_id, friday_id) in tuples:
            entry = WeeklyPlanTempBO()
            entry.set_id(id)
            entry.set_weekday(weekday),
            entry.set_monday_id(monday_id),
            entry.set_tuesday_id(tuesday_id),
            entry.set_wednesday_id(wednesday_id),
            entry.set_thursday_id(thursday_id),
            entry.set_friday_id(friday_id)
            result.append(entry)

        self._cnx.commit()
        cursor.close()

        return result


    def update(self, entry):
        """
        Wiederholtes Schreiben eines Objekts in die Datenbank.
        :param entry: das Objekt, das in die DB geschrieben werden soll
        """
        cursor = self._cnx.cursor()

        command = "UPDATE standard_temp" + \
                  "SET weekday=%s, monday_id=%s, tuesday_id=%s, wednesday_id=%s, thursday_id=%s, friday_id=%s WHERE " \
                  "id=%s "
        data = (entry.get_id(),
                entry.get_weekday(),
                entry.get_monday_id(),
                entry.get_tuesday_id(),
                entry.get_wednesday_id(),
                entry.get_thursday_id(),
                entry.get_friday_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return entry

    def delete(self, entry):
        """
        Löschen eines Thermostat-Wochenplan-Objekts aus der Datenbank.
        :param entry: das aus der DB zu löschende "Objekt"
        """
        cursor = self._cnx.cursor()

        command = "DELETE FROM standard_temp WHERE id={}".format(
            entry.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()
