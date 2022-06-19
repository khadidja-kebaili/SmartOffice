sap.ui.define([
    "../controller/SmartOffice.controller",
    "sap/ui/model/json/JSONModel",
    "sap/m/MessageToast",
    "sap/ui/core/routing/History"
    ],
    function (SmartOfficeController, JSONModel, MessageToast) {
        "use strict";

        var self;

        return SmartOfficeController.extend("com.quanto.solutions.ui.smartoffice.controller.Reporting",{
            onInit: function () {
                self=this;
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
                oRouter.getRoute("reporting").attachMatched(this._onRouteMatched, this);
            },

            _onRouteMatched : function (oEvent){
                this.getStatus().done(function(result) {

                    console.log(result.d.results[0])
                    var wert = result.d.results[0]
                    self.byId("testtext").setText(wert)
                })
            },
            getStatus: function() {
            return jQuery.ajax({
                url: "/LastStatusJalousien",
                type: "GET"
              });
            },
        });
    });