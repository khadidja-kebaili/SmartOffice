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
            let oRouter = sap.ui.core.UIComponent.getRouterFor(this);
            oRouter.getRoute("jalousien").attachMatched(this._onRouteMatched, this);
        },

        //Sobald Route Jalousien aufgerufen wird, hole den letzten Wert und setze ihn auf den Slider
        _onRouteMatched : function (oEvent){
            this.getStatus().done(function(result) {
                console.log(result.d.results[0])  
                var currentvalue = result.d.results[0]
                self.byId("sliderrealtime").setValue(currentvalue)       
            })
        },

        //Get Abfrage des letzten Status der Jalousie
        getStatus: function() {
            return jQuery.ajax({
                url: "/LastStatusJalousien",
                type: "GET"
              });
        },

        //Button WeeklyPlan führt zu Wochenplan-View
        pressnavWeeklyPlan: function (evt) {
            var oRouter = sap.ui.core.UIComponent.getRouterFor(this);
            oRouter.navTo("wochenplan")
        },

        //Button Regeln führt zu Regel-View
        pressnavRegeln: function (evt) {
            var oRouter = sap.ui.core.UIComponent.getRouterFor(this);
            oRouter.navTo("regelnjalousien")
        },

        //Post Methode nach Einstellen eines neuen Werts
        sendValue: function (oEvent) {
            sap.ui.core.BusyIndicator.hide(0);
            //var oThis = this;
            //Daten, hier nur Wert, der gesendet werden soll
            var oData = {
                'value': oEvent.getParameter("value")
            };
            console.log(oData),
                //Senden der Daten an folgende Route
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
                        if (errorcheck == "0") {
                            MessageBox.error("Der Eintrag verstößt gegen eine Regel. \n Aktuell darf sich der Wert nur zwischen " + mindestwert + "% und " + maximalwert + "% befinden.");
                        }
                    },
                    error: function (response) {
                        console.log(typeof(response.responseText));
                        
                    }
                }).done(function() { 
                    self.getStatus().done(function(result) { 
                        var currentvalue = result.d.results[0]
                        self.byId("sliderrealtime").setValue(currentvalue)       
                    })
            })
                
        },
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

