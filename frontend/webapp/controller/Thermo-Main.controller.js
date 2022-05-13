sap.ui.define([
	"sap/ui/core/mvc/Controller",
	"sap/ui/core/Fragment"
], function(
	Controller, Fragment
) {
	"use strict";

	return Controller.extend("com.quanto.solutions.ui.smartoffice.controller.Thermo-Main", {
        onInit: function () {

        },

		handleOpenDialog: function() {
			var oView = this.getView();
            if (!this._pDialog) {													// Abfrage ob Dialog im Fragment schon existiert
				this._pDialog = Fragment.load({										// Dialog laden
					id: oView.getId(),
					name: "com.quanto.solutions.ui.smartoffice.view.Dialog",
					controller: this
				}).then(function(oDialog) {											 
					oView.addDependent(oDialog);									// Abhängigkeit herstellen
					return oDialog;
				});
			}
			this._pDialog.then(function(oDialog){									
				oDialog.setModel(oView.getModel());
				oDialog.open();
			});
		},

		closeDialog: function(oEvent) {
			this.byId('mySettingsDialog').close();
		}
	});
});