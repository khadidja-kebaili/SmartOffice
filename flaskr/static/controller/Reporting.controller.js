sap.ui.define([
    "../controller/SmartOffice.controller",
    "sap/ui/model/json/JSONModel",
    "sap/m/MessageToast"
    ],
    function (SmartOfficeController, JSONModel, MessageToast) {
        "use strict";

        var self;

        return SmartOfficeController.extend("com.quanto.solutions.ui.smartoffice.controller.Reporting",{
            onInit: function () {
                this.oModelSettings = new JSONModel({
                    maxIterations: 200,
                    maxTime: 500,
                    initialTemperature: 200,
                    coolDownStep: 1
                });
                this.getView().setModel(this.oModelSettings, "settings");
                this.getView().setModel(sap.ui.getCore().getModel("TestModel"), "TestModel");
                this.getView().setModel(this.oModelSettings, "percentage");
                sap.ui.core.BusyIndicator.hide(0);
            },
            getValue: function(oEvent) {
                console.log("Werte werden geladen.");
                sap.ui.core.BusyIndicator.hide(0);
                //var oThis = this;
                var oData = {
                    'percentage': oEvent.getParameter("percentage")
                };
                console.log(oData),
                jQuery.ajax({
                    url : "/LastStatusJalousien",
                    type : "GET",
                    dataType : "json",
                    async : true,
                    data : oData,
                    success : function(response){
                        MessageToast.show(response.data.message);
                        //oThis.makeGraph(response.graph);
                        sap.ui.core.BusyIndicator.hide();
                    },
                    error: function(response){
                        console.log(response);
                    }
                });
            },
        });
    });