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
