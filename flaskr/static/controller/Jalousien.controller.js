sap.ui.define([
    "../controller/SmartOffice.controller",
    "sap/ui/model/json/JSONModel",
    "sap/m/MessageToast",
    "sap/ui/core/routing/History"
], function (SmartOfficeController, JSONModel, MessageToast, History) {
    "use strict";

    var self;
    return SmartOfficeController.extend("com.quanto.solutions.ui.smartoffice.controller.Jalousien", {
        onInit: function () {
            this.oModelSettings = new JSONModel({
                maxIterations: 200,
                maxTime: 500,
                initialTemperature: 200,
                coolDownStep: 1
            });
            this.getView().setModel(this.oModelSettings, "settings");
            this.getView().setModel(sap.ui.getCore().getModel("TestModel"), "TestModel");
            sap.ui.core.BusyIndicator.hide(0);

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
            console.log("Neuer Wert wurde eingestellt.");
            sap.ui.core.BusyIndicator.hide(0);
            //var oThis = this;
            var oData = {
                'value': oEvent.getParameter("value")
            };
            console.log(oData),
                jQuery.ajax({
                    url: "/Jalousien",
                    type: "POST",
                    dataType: "json",
                    async: true,
                    data: oData,
                    success: function (response) {
                        MessageToast.show(response.data.message);
                        //oThis.makeGraph(response.graph);
                        sap.ui.core.BusyIndicator.hide();
                    },
                    error: function (response) {
                        console.log(response);
                    }
                });
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

