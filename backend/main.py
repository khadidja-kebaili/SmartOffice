# Unser Service basiert auf Flask
from flask import Flask
# Auf Flask aufbauend nutzen wir RestX
from flask_restx import Api, Resource, fields
# Wir benutzen noch eine Flask-Erweiterung für Cross-Origin Resource Sharing
from flask_cors import CORS

# Wir greifen natürlich auf unsere Applikationslogik inkl. BusinessObject-Klassen zurück
from server.bo.Jalousien import JalousienBO
from server.DeviceAdministration import DeviceAdministration

"""
Instanzieren von Flask. Am Ende dieser Datei erfolgt dann erst der 'Start' von Flask.
"""
app = Flask(__name__)

"""
Alle Ressourcen mit dem Präfix /device für **Cross-Origin Resource Sharing** (CORS) freigeben.
Diese eine Zeile setzt die Installation des Package flask-cors voraus. 

Sofern Frontend und Backend auf getrennte Domains/Rechnern deployed würden, wäre sogar eine Formulierung
wie etwa diese erforderlich:
CORS(app, resources={r"/device/*": {"origins": "*"}})
Allerdings würde dies dann eine Missbrauch Tür und Tor öffnen, so dass es ratsamer wäre, nicht alle
"origins" zuzulassen, sondern diese explizit zu nennen. Weitere Infos siehe Doku zum Package flask-cors.
"""
CORS(app, resources=r'/device/*')

"""
In dem folgenden Abschnitt bauen wir ein Modell auf, das die Datenstruktur beschreibt, 
auf deren Basis Clients und Server Daten austauschen. Grundlage hierfür ist das Package flask-restx.
"""
api = Api(app, version='1.0', title='Device API',
          description='Eine rudimentäre Demo-API für eine einfache Gerätesteuerung.')

"""Anlegen eines Namespace

Namespaces erlauben uns die Strukturierung von APIs. In diesem Fall fasst dieser Namespace alle
Device-relevanten Operationen unter dem Präfix /device zusammen. Eine alternative bzw. ergänzende Nutzung
von Namespace könnte etwa sein, unterschiedliche API-Version voneinander zu trennen, um etwa 
Abwärtskompatibilität (vgl. Lehrveranstaltungen zu Software Engineering) zu gewährleisten. Dies ließe
sich z.B. umsetzen durch /device/v1, /device/v2 usw."""
devicecontrolling = api.namespace(
    'device', description='Funktionen des DeviceBeispiels')

"""Nachfolgend werden analog zu unseren BusinessObject-Klassen transferierbare Strukturen angelegt.

BusinessObject dient als Basisklasse, auf der die weiteren Strukturen jalomer, Account und Transaction aufsetzen."""

"""Jalousie & Thermostat sind BusinessObjects..."""
jalousie = api.inherit('Jalousie', {
    'device_id': fields.String(attribute='_device_id', description='Device_ID der Jalousie'),
    'local_key': fields.String(attribute='_local_key', description='Local_Key der Jalousie'),
    'ip_address': fields.String(attribute='_ip_address', description='IP-Addresse der Jalousie')
})

thermostat = api.inherit('Thermostat', {
    'ain': fields.String(attribute='_ain', description='Geräte-ID für AVM Geräte'),
    'port': fields.String(attribute='_port', description='Netzwerk-Port')
})


@devicecontrolling.route('/jalousie')
@devicecontrolling.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
class JalousieListOperations(Resource):
    @devicecontrolling.marshal_list_with(jalousie)
    def get(self):
        """Auslesen aller Jalousie-Objekte.

        Sollten keine Jalousie-Objekte verfügbar sein, so wird eine leere Sequenz zurückgegeben."""
        adm = DeviceAdministration()
        jalousies = adm.get_all_jalousies()
        return jalousies

    @devicecontrolling.marshal_with(jalousie, code=200)
    # Wir erwarten ein Jalousie-Objekt von Client-Seite.
    @devicecontrolling.expect(jalousie)

    def post(self):
        """Anlegen eines neuen Jalousie-Objekts.

        **ACHTUNG:** Wir fassen die vom Client gesendeten Daten als Vorschlag auf.
        So ist zum Beispiel die Vergabe der ID nicht Aufgabe des Clients.
        Selbst wenn der Client eine ID in dem Proposal vergeben sollte, so
        liegt es an der DeviceAdministration (Businesslogik), eine korrekte ID
        zu vergeben. *Das korrigierte Objekt wird schließlich zurückgegeben.*
        """
        adm = DeviceAdministration()

        proposal = jalousie.from_dict(api.payload)

        """RATSCHLAG: Prüfen Sie stets die Referenzen auf valide Werte, bevor Sie diese verwenden!"""
        if proposal is not None:
            """ Wir verwenden lediglich Vor- und Nachnamen des Proposals für die Erzeugung
            eines Jalousie-Objekts. Das serverseitig erzeugte Objekt ist das maßgebliche und 
            wird auch dem Client zurückgegeben. 
            """
            c = adm.add_device(
                proposal.get_device_id(), proposal.get_ip_address(), proposal.get_local_key())
            return c, 200
        else:
            # Wenn irgendetwas schiefgeht, dann geben wir nichts zurück und werfen einen Server-Fehler.
            return '', 500


@devicecontrolling.route('/jalousie/<int:id>')
@devicecontrolling.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
@devicecontrolling.param('device_id', 'Die Geräte-ID des Jalousie-Objekts')
class JalousieOperations(Resource):
    @devicecontrolling.marshal_list_with(jalousie)
    def get(self, device_id):
        """Auslesen eines bestimmten Jalousie-Objekts.

        Das auszulesende Objekt wird durch die ```device_id``` in dem URI bestimmt.
        """
        adm = DeviceAdministration()
        jal = adm.get_jalousie_by_device_id(device_id)
        return jal

    def get(self, id):
        """Auslesen eines bestimmten Jalousie-Objekts.

        Das auszulesende Objekt wird durch die ```id``` in dem URI bestimmt.
        """
        adm = DeviceAdministration()
        jal = adm.get_jalousie_by_id(id)
        return jal

    def delete(self, device_id):
        """Löschen eines bestimmten Jalousie-Objekts.

        Das zu löschende Objekt wird durch die ```id``` in dem URI bestimmt.
        """
        adm = DeviceAdministration()
        jal = adm.get_jalousie_by_id(device_id)
        adm.delete_jalousie(jal)
        return '', 200

    @devicecontrolling.marshal_with(jalousie)
    @devicecontrolling.expect(jalousie, validate=True)
    def put(self, id):
        """Update eines bestimmten Jalousie-Objekts.

        **ACHTUNG:** Relevante id ist die id, die mittels URI bereitgestellt und somit als Methodenparameter
        verwendet wird. Dieser Parameter überschreibt das ID-Attribut des im Payload der Anfrage übermittelten
        Jalousie-Objekts.
        """
        adm = DeviceAdministration()
        c = jalousie.from_dict(api.payload)

        if c is not None:
            """Hierdurch wird die id des zu überschreibenden (vgl. Update) Jalousie-Objekts gesetzt.
            Siehe Hinweise oben.
            """
            c.set_id(id)
            adm.save_jalousie(c)
            return '', 200
        else:
            return '', 500


"""
Nachdem wir nun sämtliche Resourcen definiert haben, die wir via REST bereitstellen möchten,
müssen nun die App auch tatsächlich zu starten.

Diese Zeile ist leider nicht Teil der Flask-Doku! In jener Doku wird von einem Start via Kommandozeile ausgegangen.
Dies ist jedoch für uns in der Entwicklungsumgebung wenig komfortabel. Deshlab kommt es also schließlich zu den 
folgenden Zeilen. 

**ACHTUNG:** Diese Zeile wird nur in der lokalen Entwicklungsumgebung ausgeführt und hat in der Cloud keine Wirkung!
"""
if __name__ == '__main__':
    app.run(debug=True)
