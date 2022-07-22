from flaskr.server.database.Mapper import Mapper
from flaskr.server.bo.RulesBO import RulesBO


class RulesMapper(Mapper):
    '''
    Implemenierung der Mapper-Klasse für Regeln bzw. Einschränkungen der Gerätesteuerung.
    Hierzu wird eine Reihe von Methoden zur Verfügung gestellt, mit deren Hilfe z.B.
    Objekte gesucht, erzeugt, modifiziert und gelöscht werden können.
    Das Mapping ist bidirektional. D.h., Objekte können in DB-Strukturen und DB-Strukturen in Objekte umgewandelt werden.
    '''

    def __init__(self):
        super().__init__()

    def insert(self, rule):
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM rules ")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            if maxid[0] is None:
                rule.set_id(1)
            else:
                """Wenn wir KEINE maximale ID feststellen konnten, dann gehen wir
                davon aus, dass die Tabelle leer ist und wir mit der ID 1 beginnen können."""
                rule.set_id(maxid[0] + 1)

        command = "INSERT INTO rules (id, type, min, max, start, end) VALUES (%s, %s, %s, %s, %s, %s)"
        data = (
            rule.get_id(),
            rule.get_type(),
            rule.get_min(),
            rule.get_max(),
            rule.get_start_time(),
            rule.get_end_time()
        )

        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()
        return rule

    def find_all(self):
        """
        Auslesen aller Regelungen aus der Datenbank.
        :return: Array mit RuleBOs
        """
        result = []
        cursor = self._cnx.cursor()
        command = "SELECT id, type, min, max, start, end FROM rules"
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, type, min, max, start, end) in tuples:
            rule = RulesBO()
            rule.set_id(id)
            rule.set_type(type)
            rule.set_min(min)
            rule.set_max(max)
            rule.set_start_time(start)
            rule.set_end_time(end)
            result.append(rule)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_type(self, type):
        """
        Lädt alle Regeln eines bestimmten Typs mithilfe des angegebenen Typs.
        :param type: 'T' oder 'J'
        :return: Liste mit RuleBOs
        """
        result = []
        cursor = self._cnx.cursor()
        command = "SELECT id, type, min, max, start, end FROM rules WHERE type='{}'".format(type)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, type, min, max, start, end) in tuples:
            rule = RulesBO()
            rule.set_id(id)
            rule.set_type(type)
            rule.set_min(min)
            rule.set_max(max)
            rule.set_start_time(start)
            rule.set_end_time(end)
            result.append(rule)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_key(self, id):
        """
        Lädt eine Jalousie aus der Datenbank mithilfe der Regel-Id
        :param id: Id des RuleBOs
        :return: RuleBO
        """
        result = None
        cursor = self._cnx.cursor()
        command = "SELECT id, type, min, max, start, end  FROM rules WHERE id={}".format(
            id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, type, min, max, start, end) = tuples[0]
            rule = RulesBO()
            rule.set_id(id)
            rule.set_type(type)
            rule.set_min(min)
            rule.set_max(max)
            rule.set_start_time(start)
            rule.set_end_time(end)
            result = rule

        except IndexError:
            """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
            keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def update(self, rule):
        """
        Wiederholtes Schreiben eines Objekts in die Datenbank.
        :param rule: das Objekt, das in die DB geschrieben werden soll
        """
        cursor = self._cnx.cursor()

        command = "UPDATE rules " + \
                  "SET min=%s, max=%s, start=%s, end=%s WHERE id=%s"
        data = (rule.get_id(),
                rule.get_type(),
                rule.get_min(),
                rule.get_max(),
                rule.get_start_time(),
                rule.get_end_time())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return rule

    def delete(self, rule):
        """
        Löschen eines Regel-Objekts aus der Datenbank.
        :param rule: das aus der DB zu löschende "Objekt"
        """
        cursor = self._cnx.cursor()

        command = "DELETE FROM rules WHERE id={}".format(
            rule.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()

    def delete_jal_rules_byId(self, id_entry):
        cursor = self._cnx.cursor()
        command = "DELETE FROM rules WHERE id=%s and type=%s"
        data=(id_entry, "J")
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()