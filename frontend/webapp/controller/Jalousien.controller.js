sap.ui.define([
    'sap/m/MessageToast',
    "sap/ui/core/mvc/Controller"
],
    /**
     * @param {typeof sap.ui.core.mvc.Controller} Controller
     */
    function (MessageToast, Controller) {
        "use strict";

        return Controller.extend("com.quanto.solutions.ui.smartoffice.controller.Jalousien", {
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
            handleNavButtonPress: function (evt) {
                var oRouter = sap.ui.core.UIComponent.getRouterFor(this);
                oRouter.navTo("home");
            },
            onLiveChange: function (oEvent) {
                var sNewValue = oEvent.getParameter("value");
                this.byId("getValue").setText(sNewValue);
            }
        });
    });
