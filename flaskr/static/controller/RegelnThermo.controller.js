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
            console.log(minTemp)
            self.byId("minTemp1").setValue(minTemp)
            
          })

          this.getMaxTemp().done(function(result) {
            var maxTemp = result.d.results[0].max_temperature
            console.log(maxTemp)
            self.byId("maxTemp").setValue(maxTemp)
          })

        },

        getMinTemp: function() {
          console.log('Get min temp')
          return jQuery.ajax({
              url: "/GetMinTemp",
              type: "GET"
          });
        },

        getMaxTemp: function() {
          console.log('Get max temp')
          return jQuery.ajax({
            url: "/GetMaxTemp",
            type: "GET"
        });
        },

        changeMinTemp: function(oEvent) {
          sap.ui.core.BusyIndicator.hide(0);
          var oData = {
              'value': oEvent.getParameter("value")
          };
          console.log(oData);
          console.log(typeof(oData.value));
          jQuery.ajax({
              url: "/SetMinTemp",
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
        },
        changeMaxTemp: function(oEvent) {
          sap.ui.core.BusyIndicator.hide(0);
          var oData = {
              'value': oEvent.getParameter("value")
          };
          console.log(oData);
          console.log(typeof(oData.value));
          jQuery.ajax({
              url: "/SetMaxTemp",
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
