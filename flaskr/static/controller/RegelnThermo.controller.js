sap.ui.define([
    "../controller/SmartOffice.controller",
    "sap/m/MessageToast",
    "sap/ui/core/routing/History"
], function(SmartOfficeController, MessageToast, History) {
        "use strict";

        var self;

        return SmartOfficeController.extend("com.quanto.solutions.ui.smartoffice.controller.RegelnThermo", {
          onInit : function() {
              let oRouter = sap.ui.core.UIComponent.getRouterFor(this);
              oRouter.getRoute("regelnthermo").attachMatched(this._onRouteMatched, this);
              
            },

          _onRouteMatched : function (oEvent){
            this.getMinTemp().done(function(result) {
              var minTemp = result.d.results
              console.log(minTemp)
            })

          },
          // maxTemp fehlt noch - get und set
          getMinTemp: function() {
            console.log('Get min temp')
            return jQuery.ajax({
                url: "/GetMinTemp",
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
        