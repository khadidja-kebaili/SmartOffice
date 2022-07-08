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

				self = this;

			},
			pressnav: function (evt) {
				var oRouter = sap.ui.core.UIComponent.getRouterFor(this);
				oRouter.navTo("jalousien")
			},

			load: function(tile) {
			console.log("Got there!")
			var selectedData = {};
			sap.ui.core.BusyIndicator.hide(0);
			this.getData(tile).done(function(result) {
				var oModel = new sap.ui.model.json.JSONModel(result.d);
				sap.ui.getCore().setModel(oModel, "TestModel");
				self.routeToApp(tile);
				console.log(result)

			}).fail(function(result) {
				console.log(result);
			});

			},

			press: function(tile) {
			console.log("Got there!")
			var selectedData = {};
			sap.ui.core.BusyIndicator.hide(0);
			this.getData(tile).done(function(result) {
				var oModel = new sap.ui.model.json.JSONModel(result.d);
				sap.ui.getCore().setModel(oModel, "TestModel");
				self.routeToApp(tile);
				console.log(result)

			}).fail(function(result) {
				console.log(result);
			});

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
			goToThermoMain: function(oEvent) {
				var oRouter = sap.ui.core.UIComponent.getRouterFor(this);
				oRouter.navTo("thermoMain")
			},
			pressnavtoReporting: function(oEvent) {
				var oRouter = sap.ui.core.UIComponent.getRouterFor(this);
				oRouter.navTo("reporting")
			},
		});
	});


