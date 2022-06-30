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
        _onRouteMatched : function (oEvent){
            this.getStatus().done(function(result) {
                console.log(result.d.results[0])  
                var currentvalue = result.d.results[0]
                self.byId("sliderrealtime").setValue(currentvalue)       
            })
        },
        getStatus: function() {
            return jQuery.ajax({
                url: "/sap/LastStatusJalousien",
                type: "GET"
              });
        },

        onLiveChange: function (oEvent) {
            var sNewValue = oEvent.getParameter("value");
            this.byId("getValue").setText(sNewValue);
        },
        pressnavWeeklyPlan: function (evt) {
            var oRouter = sap.ui.core.UIComponent.getRouterFor(this);
            oRouter.navTo("wochenplan")
        },
        pressnavRegeln: function (evt) {
            var oRouter = sap.ui.core.UIComponent.getRouterFor(this);
            oRouter.navTo("regelnjalousien")
        },
        sendValue: function (oEvent) {
            sap.ui.core.BusyIndicator.hide(0);
            //var oThis = this;
            var oData = {
                'value': oEvent.getParameter("value")
            };
            console.log(oData),
                jQuery.ajax({
                    url: "/sap/Jalousien",
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

