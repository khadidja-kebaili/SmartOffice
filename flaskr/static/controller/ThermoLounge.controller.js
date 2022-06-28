sap.ui.define([
    "sap/ui/core/mvc/Controller",
    "sap/m/MessageToast",
    "sap/ui/core/routing/History"
], function(
    Controller,
    MessageToast,
    History
) {
    "use strict";

    return Controller.extend("com.quanto.solutions.ui.smartoffice.controller.ThermoLounge", {
        onInit: function() {
            self = this;
            this.getView();
            sap.ui.core.BusyIndicator.hide(0);

            let oRouter = sap.ui.core.UIComponent.getRouterFor(this);
            oRouter.getRoute("thermoLounge").attachMatched(this._onRouteMatched, this);
        },
        
        _onRouteMatched : function (oEvent){
            this.getTemp().done(function(result) {
                console.log(result.d.results[0].temperature)  
                var currentTemp = result.d.results[0].temperature
                self.byId("currentTemp").setValue(currentTemp)
            })
        },
        getTemp: function () {
            console.log('Get data für Thermo')
            return jQuery.ajax({
            url: "/GetTemp",
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
                    MessageToast.show(response.data.message);
                    sap.ui.core.BusyIndicator.hide();
                },
                error: function (response) {
                    console.log(response);
                }
            });
        }
    });
});