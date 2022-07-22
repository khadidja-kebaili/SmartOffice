sap.ui.define([
  "../controller/SmartOffice.controller",
  "sap/m/MessageToast",
  "sap/ui/core/routing/History"
], function(SmartOfficeController, MessageToast, History) {
      "use strict";

      var self;

      return SmartOfficeController.extend("com.quanto.solutions.ui.smartoffice.controller.RegelnThermo", {
        onInit : function() {
            self = this;
            this.getView();
            sap.ui.core.BusyIndicator.hide(0);

            let oRouter = sap.ui.core.UIComponent.getRouterFor(this);
            oRouter.getRoute("regelnthermo").attachMatched(this._onRouteMatched, this);
          },

        _onRouteMatched : function (oEvent){
          this.getMinTemp().done(function(result) {
            var minTemp = result.d.results[0].min_temperature
            self.byId("minTemp").setValue(minTemp)
            
          })

          this.getMaxTemp().done(function(result) {
            var maxTemp = result.d.results[0].max_temperature
            self.byId("maxTemp").setValue(maxTemp)
          })

        },

        // get min temperature
        getMinTemp: function() {
          return jQuery.ajax({
              url: "/GetMinTemp",
              type: "GET"
          });
        },

        // get max temperature
        getMaxTemp: function() {
          return jQuery.ajax({
            url: "/GetMaxTemp",
            type: "GET"
        });
        },

        // change min temperature
        changeMinTemp: function(oEvent) {
          sap.ui.core.BusyIndicator.hide(0);
          var oData = {
              'value': oEvent.getParameter("value")
          };
          jQuery.ajax({
              url: "/SetMinTemp",
              type: "POST",
              dataType: "json",
              async: true,
              data: oData,
              statusCode: {
                200: function() {
                  MessageToast.show('Die min. Temperatur wurde erfolgreich geändert.');
                }
              },
          });
        },

        // change max temperature
        changeMaxTemp: function(oEvent) {
          sap.ui.core.BusyIndicator.hide(0);
          var oData = {
              'value': oEvent.getParameter("value")
          };
          jQuery.ajax({
              url: "/SetMaxTemp",
              type: "POST",
              dataType: "json",
              async: true,
              data: oData,
              statusCode: {
                200: function() {
                  MessageToast.show('Die max. Temperatur wurde erfolgreich geändert.');
                }
              },
          });
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
        }

  });

   });
