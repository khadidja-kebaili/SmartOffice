import mysql.connector as connector
import os
from contextlib import AbstractContextManager
from abc import ABC, abstractmethod


class Mapper (AbstractContextManager, ABC):
    """Abstrakte Basisklasse aller Mapper-Klassen"""

    def __init__(self):
        self._cnx = None

    def __enter__(self):
        """Check ob der Code im Kontext der lokalen Entwicklungsumgebung oder in der Cloud ausgeführt wird.
        Dies ist erforderlich, da die Modalitäten für den Verbindungsaufbau mit der Datenbank kontextabhängig sind."""

        self._cnx = connector.connect(user='root', password='hdmsw2022!',
                                          host='localhost',
                                          database='smartoffice')
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