sap.ui.define(['sap/ui/core/mvc/Controller', 'sap/m/MessageToast'],
	function (Controller, MessageToast) {
		"use strict";

		var PageController = Controller.extend("com.quanto.solutions.ui.smartoffice.controller.Home", {
			press: function (evt) {
				var oRouter = sap.ui.core.UIComponent.getRouterFor(this);
				oRouter.navTo("jalousien")
			}


		});
		return PageController;
	});