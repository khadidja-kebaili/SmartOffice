from flask import render_template, jsonify
from flask_restx import Resource, Api, fields
import time
from datetime import datetime
from flaskr import app

api = Api(app, version='1.0', title='Device API',
          description='Eine rudimentäre Demo-API für eine einfache Gerätesteuerung.')

bo = api.model('Businessobject', {
    'id': fields.Integer(attribute='_id', description='Der Unique Identifier eines Business Object'),
})

jalousie = api.inherit('Jalousie', bo, {
    'device_id': fields.String(attribute='_device_id', description='Device_ID der Jalousie'),
    'local_key': fields.String(attribute='_local_key', description='Local_Key der Jalousie'),
    'ip_address': fields.String(attribute='_ip_address', description='IP-Addresse der Jalousie')
})


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/Test', methods=["GET"])
def Test():
    """
    Return a simple odata container with date time information
    :return:
    """
    odata = {
        'd': {
            'results': []
        }
    }
    i = 0
    names = 'abcdefghijklmnopqrxtu'
    while i < 20:
        odata['d']['results'].append({
            "id": i,
            "name": names[i]
        })
        i += 1

    return jsonify(odata)

    @app.route('/jalousie')
@app.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
class JalousieListOperations(Resource):
    @app.marshal_list_with(jalousie)
    def get(self):
        """Auslesen aller Jalousie-Objekte.
        Sollten keine Jalousie-Objekte verfügbar sein, so wird eine leere Sequenz zurückgegeben."""
        adm = DeviceAdministration()
        jalousies = adm.get_all_jalousies()
        return jalousies

    @app.marshal_with(jalousie, code=200)
    # Wir erwarten ein Jalousie-Objekt von Client-Seite.
    @app.expect(jalousie)
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


@app.route('/jalousie/<int:id>')
@app.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
@app.param('device_id', 'Die Geräte-ID des Jalousie-Objekts')
class JalousieOperations(Resource):
    @app.marshal_list_with(jalousie)
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

    @app.marshal_with(jalousie)
    @app.expect(jalousie, validate=True)
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


@app.route('/jalousienstatus')
@app.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
class JalousienStatusListOperations(Resource):
    @app.marshal_list_with(status)
    def get(self):
        """Auslesen aller Jalousie-Objekte.
        Sollten keine Jalousie-Objekte verfügbar sein, so wird eine leere Sequenz zurückgegeben."""
        adm = DeviceAdministration()
        stats = adm.get_all_status()
        return stats


@app.route('/setstatus')
@app.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
class JalousienSetStatusListOperations(Resource):
    @app.marshal_with(status, code=200)
    @app.expect(status)
    def post(self):
        """Anlegen eines neuen Jalousie-Objekts.
        **ACHTUNG:** Wir fassen die vom Client gesendeten Daten als Vorschlag auf.
        So ist zum Beispiel die Vergabe der ID nicht Aufgabe des Clients.
        Selbst wenn der Client eine ID in dem Proposal vergeben sollte, so
        liegt es an der DeviceAdministration (Businesslogik), eine korrekte ID
        zu vergeben. *Das korrigierte Objekt wird schließlich zurückgegeben.*
        """
        adm = DeviceAdministration()
        proposal = JalousienStatusBO.from_dict(api.payload)
        if proposal is not None:

            c = adm.set_status_to_percentage_by_id(
                proposal.get_device(), proposal.get_percentage())
            return c, 200
        else:
            # Wenn irgendetwas schiefgeht, dann geben wir nichts zurück und werfen einen Server-Fehler.
            return '', 500


@app.route('/openjalousie')
@app.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
class JalousienSetStatusListOperations(Resource):
    @app.marshal_with(status, code=200)
    @app.expect(status)
    def post(self):
        """Anlegen eines neuen Jalousie-Objekts.
        **ACHTUNG:** Wir fassen die vom Client gesendeten Daten als Vorschlag auf.
        So ist zum Beispiel die Vergabe der ID nicht Aufgabe des Clients.
        Selbst wenn der Client eine ID in dem Proposal vergeben sollte, so
        liegt es an der DeviceAdministration (Businesslogik), eine korrekte ID
        zu vergeben. *Das korrigierte Objekt wird schließlich zurückgegeben.*
        """
        adm = DeviceAdministration()
        proposal = JalousienStatusBO.from_dict(api.payload)
        if proposal is not None:

            c = adm.open_jalousie_by_id(
                proposal.get_device())
            return c, 200
        else:
            # Wenn irgendetwas schiefgeht, dann geben wir nichts zurück und werfen einen Server-Fehler.
            return '', 500


@app.route('/closejalousie')
@app.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
class JalousienSetStatusListOperations(Resource):
    @app.marshal_with(status, code=200)
    @app.expect(status)
    def post(self):
        """Anlegen eines neuen Jalousie-Objekts.
        **ACHTUNG:** Wir fassen die vom Client gesendeten Daten als Vorschlag auf.
        So ist zum Beispiel die Vergabe der ID nicht Aufgabe des Clients.
        Selbst wenn der Client eine ID in dem Proposal vergeben sollte, so
        liegt es an der DeviceAdministration (Businesslogik), eine korrekte ID
        zu vergeben. *Das korrigierte Objekt wird schließlich zurückgegeben.*
        """
        adm = DeviceAdministration()
        proposal = JalousienStatusBO.from_dict(api.payload)
        if proposal is not None:

            c = adm.close_jalousie_by_id(
                proposal.get_device())
            return c, 200
        else:
            # Wenn irgendetwas schiefgeht, dann geben wir nichts zurück und werfen einen Server-Fehler.
            return '', 500
