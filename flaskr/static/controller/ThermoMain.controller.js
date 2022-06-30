sap.ui.define([
    "sap/ui/core/mvc/Controller",
    "sap/m/MessageToast",
    "sap/ui/core/routing/History",
    "sap/m/MessageBox",
], function(
    Controller,
    MessageToast,
    History,
    MessageBox
) {
    "use strict";

    return Controller.extend("com.quanto.solutions.ui.smartoffice.controller.ThermoMain", {
        onInit: function() {
            self = this;
            this.getView();
            sap.ui.core.BusyIndicator.hide(0);

            let oRouter = sap.ui.core.UIComponent.getRouterFor(this);
            oRouter.getRoute("thermoMain").attachMatched(this._onRouteMatched, this);
        },
        
        _onRouteMatched : function (oEvent){
            this.getTemp().done(function(result) {
                console.log(result.d.results[0].temperature)  
                var currentTemp = result.d.results[0].temperature
                self.byId("currentTemp").setValue(currentTemp)
            })

            this.getSollTemp().done(function(result) {
                console.log(result.d.results[0].temperature)  
                var targetTemp = result.d.results[0].temperature
                self.byId("targetTemp").setValue(targetTemp)
            })
        },
        getTemp: function () {
            console.log('Get data für Thermo')
            return jQuery.ajax({
                url: "/GetTemp",
                type: "GET"
            });
        },

        getSollTemp: function() {
            console.log('Get soll temp')
            return jQuery.ajax({
                url: "/GetSollTemp",
                type: "GET"
            });
        },
        
        pressnavWeeklyPlanThermo: function (evt) {
            var oRouter = sap.ui.core.UIComponent.getRouterFor(this);
            oRouter.navTo("wochenplanthermo")
        },
        pressNavRegelnThermo: function(oEvent) {
            var oRouter = sap.ui.core.UIComponent.getRouterFor(this);
            oRouter.navTo("regelnthermo")
        },
        onNavBack: function(){

          var oHistory = History.getInstance();
          var sPreviousHash = oHistory.getPreviousHash();

          if (sPreviousHash !== undefined) {
            window.history.go(-1);
          } else {
            var oRouter = sap.ui.core.UIComponent.getRouterFor(this);
            oRouter.navTo("/", {}, true);
          }
        },
        
        changeTargetTemp: function(oEvent) {
            sap.ui.core.BusyIndicator.hide(0);
            var oData = {
                'value': oEvent.getParameter("value")
            };
            jQuery.ajax({
                url: "/SetTemp",
                type: "POST",
                dataType: "json",
                async: true,
                data: oData,
                success: function (response) {
                    sap.ui.core.BusyIndicator.hide();
                },
                error: function (response) {
                    console.log(response);
                }
            }).done(function(result) {
                var errorcheck = result.type
                var mindestwert = result.min / 10
                var maximalwert = result.max / 10
                console.log(errorcheck)
                if (errorcheck === "0") {
                    console.log('Temp zu hoch')
                    MessageBox.error("Der Eintrag verstößt gegen eine Regel. \n Die Temperatur darf maximal " + maximalwert + "°C betragen. \n Bitte versuche eine andere Einstellung!");
                    self.byId("targetTemp").setValue(null)
                }
                else if (errorcheck === "1") {
                    console.log('Temp zu niedrig')
                    MessageBox.error("Der Eintrag verstößt gegen eine Regel. \n Die Temperatur muss mindestens " + mindestwert + "°C betragen. \n Bitte versuche eine andere Einstellung!");
                    self.byId("targetTemp").setValue(null)
                }
                else if (errorcheck === "2") {
                    MessageToast.show('Die Temperatur wurde erfolgreich geändert.');
                }
            });
        }
    });
});