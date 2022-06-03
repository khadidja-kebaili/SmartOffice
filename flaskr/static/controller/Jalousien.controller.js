sap.ui.define([
    'sap/m/MessageToast',
    "sap/ui/core/mvc/Controller",
    "sap/ui/model/json/JSONModel",
],
    /**
     * @param {typeof sap.ui.core.mvc.Controller} Controller
     */
    function (MessageToast, Controller, JSONModel) {
        "use strict";


        return Controller.extend("com.quanto.solutions.ui.smartoffice.controller.Jalousien", {
            onInit: function () {
                this.oModelSettings = new JSONModel({
                    maxIterations: 200,
                    maxTime: 500,
                    initialTemperature: 200,
                    coolDownStep: 1
                });
                this.getView().setModel(this.oModelSettings, "settings");
                this.getView().setModel(sap.ui.getCore().getModel("TestModel"), "TestModel");
                sap.ui.core.BusyIndicator.hide(0);

            },


            getData: function (url) {
                console.log('Something')
                console.log(url)
                return jQuery.ajax({
                    url: url,
                    type: "GET"
                });
            },

            pressit: function (tile) {
                console.log('Hier')
                var selectedData = {};
                this.getData(tile).done(function (result) {
                    var oModel = new sap.ui.model.json.JSONModel(result.d.results);
                    sap.ui.getCore().setModel(oModel, "TestModel");
                    console.log('Dann result.d.results: ', result.d.results)
                    var results = result.d.results
                    results.map(elem => console.log(elem))




                }).fail(function (result) {
                    console.log('Failed to load: ', result);
                });

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
