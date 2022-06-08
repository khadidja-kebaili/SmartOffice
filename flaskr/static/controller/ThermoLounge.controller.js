sap.ui.define([
	"sap/ui/core/mvc/Controller"
], function(
	Controller
) {
	"use strict";

	return Controller.extend("com.quanto.solutions.ui.smartoffice.controller.ThermoLounge", {
		
        pressnavWeeklyPlanThermo: function (evt) {
			var oRouter = sap.ui.core.UIComponent.getRouterFor(this);
			oRouter.navTo("wochenplanthermo")
		}
	});
});