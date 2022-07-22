from abc import ABC, abstractmethod


class Businessobject(ABC):
    '''
    Superklasse alle Businessobjekte
    Vererbung einer globalen Id, die für alle Objekte in der Applikation gilt.
    '''

    def __init__(self):
        # Die eindeutige Identifikationsnummer einer Instanz dieser Klasse.
        self._id = 0

    def get_id(self):
        """Auslesen der ID."""
        return self._id

    def set_id(self, value):
        """Setzen der ID."""
        self._id = value
