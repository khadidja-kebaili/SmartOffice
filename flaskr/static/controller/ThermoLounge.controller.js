sap.ui.define([
	"sap/ui/core/mvc/Controller",
	"sap/ui/core/routing/History"
], function(
	Controller,
	History
) {
	"use strict";

	return Controller.extend("com.quanto.solutions.ui.smartoffice.controller.ThermoLounge", {
		onInit: function() {
			let oRouter = sap.ui.core.UIComponent.getRouterFor(this);
            oRouter.getRoute("thermoLounge").attachMatched(this._onRouteMatched, this);
		},
		
            _onRouteMatched : function (oEvent){
              //this.addEmptyObject()
                //var datatest2 = []
                this.getData().done(function(result) {
                    
                    var data = result.d.results
                    console.log(data)
                    //console.log("Jetzt bin ich am Ende")
                })

            },
            getData: function () {
              console.log('Get data für Thermo')
              return jQuery.ajax({
                url: "/GetTemp",
                type: "GET"
              });
            },
		
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