import mysql.connector as connector
from contextlib import AbstractContextManager
from abc import ABC, abstractmethod


class Mapper (AbstractContextManager, ABC):
    """Abstrakte Basisklasse aller Mapper-Klassen"""

    def __init__(self):
        self._cnx = None

    def __enter__(self):
        '''
        In der enter-Methode wird die Datenbankverbindung, sprich Datenbank, user, host und Passwort angegeben.
        :return: self._cnx (Verbindung)
        '''

        self._cnx = connector.connect(user='quanto_solutions', password='QUANTO-Solutions',
                                      host='localhost',
                                      database='SmartOffice')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Was soll geschehen, wenn wir (evtl. vorübergehend) aufhören, mit dem Mapper zu arbeiten?"""
        self._cnx.close()

    """Formuliere nachfolgend sämtliche Auflagen, die instanzierbare Mapper-Subklassen mind. erfüllen müssen."""

    @abstractmethod
    def find_all(self):
        """Lies alle Tupel aus und gib sie als Objekte zurück."""
        pass

    @abstractmethod
    def find_by_key(self, key):
        """Lies den einen Tupel mit der gegebenen ID (vgl. Primärschlüssel) aus."""
        pass

    @abstractmethod
    def insert(self, object):
        """Füge das folgende Objekt als Datensatz in die DB ein."""
        pass

    @abstractmethod
    def update(self, object):
        """Ein Objekt auf einen bereits in der DB enthaltenen Datensatz abbilden."""
        pass

    @abstractmethod
    def delete(self, object):
        """Den Datensatz, der das gegebene Objekt in der DB repräsentiert löschen."""
        pass
