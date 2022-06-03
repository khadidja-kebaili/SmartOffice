sap.ui.define([
	"sap/ui/core/mvc/Controller",
	"../model/formatter",
],
	/**
	 * @param {typeof sap.ui.core.mvc.Controller} Controller
	 */
	function (Controller, formatter) {
		"use strict";

		return Controller.extend("com.quanto.solutions.ui.smartoffice.controller.SmartOffice", {
			formatter: formatter,
			onInit: function () {

			},

			getData: function (url) {
				console.log('Something')
				console.log(url)
				return jQuery.ajax({
					url: url,
					type: "GET"
				});
			},

			getRouter: function () {
				return sap.ui.core.UIComponent.getRouterFor(this);
			},

			routeToApp: function (tile) {
				self.getRouter().navTo(tile, {});

			},
		});
	});
