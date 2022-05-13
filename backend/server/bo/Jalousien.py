from server.bo.BusinessObject import Businessobject as bo
from TinyTuya import tinytuya


class JalousienBO(bo):
    """
    Klasse für Jalousien
    """

    def __init__(self):
        super().__init__()
        self._d = None
        self._device_id = ''
        self._ip_address = ''
        self._local_key = ''


    def set_device_id(self, device_id):
        self._device_id = device_id

    def get_device_id(self):
        return self._device_id

    def set_ip_address(self, ip_address):
        self._ip_address = ip_address

    def get_ip_address(self):
        return self._ip_address

    def set_local_key(self, local_key):
        self._local_key = local_key

    def get_local_key(self):
        return self._local_key

    def set_device(self):
        self._d = tinytuya.OutletDevice(self.get_device_id(), self.get_ip_address(), self.get_local_key())
        self._d.set_version(3.3)

    def get_device(self):
        return self._d

    def get_status_of_device(self):
        return self._d.status()

    def __str__(self):
        """Erzeugen einer einfachen textuellen Repräsentation der jeweiligen Kontoinstanz."""
        return "Jalousie: id {}, device_id {}, ip_address {}, local_key {}".format(
            self.get_id(), self.get_device_id(), self.get_ip_address(), self.get_local_key())

    @staticmethod
    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in ein Account()."""
        obj = JalousienBO()
        obj.set_id(dictionary["id"])
        obj.set_device_id(dictionary["device_id"])
        obj.set_ip_address(dictionary["ip_address"])
        obj.set_local_key(dictionary['local_key'])
        return obj