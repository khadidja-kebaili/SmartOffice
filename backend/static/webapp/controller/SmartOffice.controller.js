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
            press: function(tile) {

			var selectedData = {};
			sap.ui.core.BusyIndicator.show(0);
			this.getData(tile).done(function(result) {
				var oModel = new sap.ui.model.json.JSONModel(result.d);
				sap.ui.getCore().setModel(oModel, "TestModel");
				self.routeToApp(tile);

			}).fail(function(result) {
				console.log(result);
			});

		},
		getData: function(url){
			return jQuery.ajax({
				url: url,
				type: "GET"
			});
		},

		getRouter : function () {
			return sap.ui.core.UIComponent.getRouterFor(this);
		},

		routeToApp: function(tile) {
			self.getRouter().navTo(tile, {});

		},
        });
    });
