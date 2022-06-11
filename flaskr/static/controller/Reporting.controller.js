sap.ui.define([
    "../controller/SmartOffice.controller",
    "sap/ui/model/json/JSONModel",
    "sap/m/MessageToast"
],
    /**
     * @param {typeof sap.ui.core.mvc.SmartOfficeController} SmartOfficeController
     */
    function (SmartOfficeController, JSONModel, MessageToast) {
    "use strict";

        return SmartOfficeController.extend("com.quanto.solutions.ui.smartoffice.controller.Jalousien",{
            onInit: function () {
                this.oModelSettings = new JSONModel;
                this.getView().setModel(this.oModelSettings, "settings");
                this.getView().setModel(sap.ui.getCore().getModel("TestModel"), "TestModel");
                sap.ui.core.BusyIndicator.hide(0);
            }
    });
});