sap.ui.define([
    "../controller/SmartOffice.controller",
    "sap/ui/model/json/JSONModel",
    "sap/m/MessageToast",
    "sap/ui/core/routing/History"
    ],
    function (SmartOfficeController, JSONModel, MessageToast, History) {
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

                //Jal
                this.getActualValueJal().done(function(result) {

                    console.log(result.d.results[0])
                    var actualValueJal = result.d.results[0]
                    self.byId("actualvaluejalid").setText(actualValueJal)
                })
                /*this.getSupposedValueJal().done(function(result)

                    console.log(result.d.results[0])
                    var supposedValueJal = result.d.results[0]
                    self.byId("supposedvaluejalid").setText(supposedValueJal)
                })*/

                //Temp
                /*this.getActualValueTemp().done(function(result) {

                    console.log(result.d.results[0])
                    var actualValueTemp = result.d.results[0]
                    self.byId("actualvaluetempid").setText(actualValueTemp)
                })*/
                /*this.getSupposedValueTemp().done(function(result)

                    console.log(result.d.results[0])
                    var supposedValueTemp = result.d.results[0]
                    self.byId("supposedvaluetempid").setText(supposedValueTemp)
                })*/
            },

            //Jal
            getActualValueJal: function() {
            return jQuery.ajax({
                url: "/LastStatusJalousien",
                type: "GET"
              });

            },

            /*getSupposedValueJal: function() {
            return jQuery.ajax({
                url: "",
                type: "GET"
              });
            },*/

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