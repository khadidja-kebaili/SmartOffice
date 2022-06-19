sap.ui.define([
	"sap/ui/core/mvc/Controller",
	"sap/ui/core/routing/History"
], function(
	Controller,
	History
) {
	"use strict";

	return Controller.extend("com.quanto.solutions.ui.smartoffice.controller.ThermoLounge", {
		
        pressnavWeeklyPlanThermo: function (evt) {
			var oRouter = sap.ui.core.UIComponent.getRouterFor(this);
			oRouter.navTo("wochenplanthermo")
		},
		onNavBack: function(){

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