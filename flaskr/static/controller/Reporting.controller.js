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
                this.oModelSettings = new JSONModel;
                this.getView().setModel(this.oModelSettings, "settings");
                this.getView().setModel(sap.ui.getCore().getModel("TestModel"), "TestModel");
                sap.ui.core.BusyIndicator.hide(0);
            }
    });
});