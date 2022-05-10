sap.ui.define([
    "sap/ui/core/mvc/Controller"
],
    /**
     * @param {typeof sap.ui.core.mvc.Controller} Controller
     */
    function (Controller) {
        "use strict";

        return Controller.extend("com.quanto.solutions.ui.smartoffice.controller.SmartOffice", {
            onInit: function () {

            },
            goTo: function(oEvent) {
                var oRouter = sap.ui.core.UIComponent.getRouterFor(this);
                oRouter.navTo("Thermo-Main");
            }
            
        });
    });
