sap.ui.define([
    "../controller/SmartOffice.controller",
    "sap/ui/model/json/JSONModel",
    "sap/m/MessageBox",
    "sap/m/MessageToast",
    "sap/ui/core/routing/History"
], function (SmartOfficeController, JSONModel, MessageBox, MessageToast, History) {
    "use strict";

    var self;
    return SmartOfficeController.extend("com.quanto.solutions.ui.smartoffice.controller.Jalousien", {
        onInit: function () {
            self = this;
            this.oModelSettings = new JSONModel({
                maxIterations: 200,
                maxTime: 500,
                initialTemperature: 200,
                coolDownStep: 1
            });
            this.getView().setModel(this.oModelSettings, "settings");
            this.getView().setModel(sap.ui.getCore().getModel("TestModel"), "TestModel");
            sap.ui.core.BusyIndicator.hide(0);
            //Route an match-Funktion binden
            let oRouter = sap.ui.core.UIComponent.getRouterFor(this);
            oRouter.getRoute("jalousien").attachMatched(this._onRouteMatched, this);
        },
        //Wenn Route aufgerufen wird, rufe den letzten Status aus der Datenbank ab und setz ihn auf den Slider
        _onRouteMatched : function (oEvent){
            this.getStatus().done(function(result) {
                console.log(result.d.results[0])  
                var currentvalue = result.d.results[0]
                self.byId("sliderrealtime").setValue(currentvalue)       
            })
        },
        //GET-Methode zum Abrufen des letzten Status der Jalousien
        getStatus: function() {
            return jQuery.ajax({
                url: "/LastStatusJalousien",
                type: "GET"
              });
        },
        //Neuen Wert einstellen, sobald Slider bewegt wurde/neuer Wert eingestellt wurde
        sendValue: function (oEvent) {
            sap.ui.core.BusyIndicator.hide(0);
            //var oThis = this;
            //Wert speichern
            var oData = {
                'value': oEvent.getParameter("value")
            };
            console.log(oData),
                //POST-Methode um Wert an Backend zu senden
                jQuery.ajax({
                    url: "/Jalousien",
                    type: "POST",
                    dataType: "json",
                    async: true,
                    data: oData,
                    success: function (response) {
                        console.log(response)
                        sap.ui.core.BusyIndicator.hide();
                        var errorcheck = response.type
                        var mindestwert = response.min
                        var maximalwert = response.max
                        //Wenn Wert von errorcheck = 0 ist liegt ein Regelverstoß vor
                        if (errorcheck == "0") {
                            //MessageBox mit erlaubten Werten anzeigen
                            MessageBox.error("Der Eintrag verstößt gegen eine Regel. \n Aktuell darf sich der Wert nur zwischen " + mindestwert + "% und " + maximalwert + "% befinden.");
                        }
                    },
                    error: function (response) {
                        console.log(typeof(response.responseText));
                        
                    }
                }).done(function() { 
                    //Erneut letzten Wert abrufen und setzen
                    self.getStatus().done(function(result) { 
                        var currentvalue = result.d.results[0]
                        self.byId("sliderrealtime").setValue(currentvalue)       
                    })
            })
                
        },
        //Zurück-Navigation führt zu vorheriger Seite
        onNavBack: function () {

            var oHistory = History.getInstance();
            var sPreviousHash = oHistory.getPreviousHash();

            if (sPreviousHash !== undefined) {
                window.history.go(-1);
            } else {
                var oRouter = sap.ui.core.UIComponent.getRouterFor(this);
                oRouter.navTo("/", {}, true);
            }
        }
    });
});

