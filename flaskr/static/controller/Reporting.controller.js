sap.ui.define([
    "../controller/SmartOffice.controller",
    "sap/ui/model/json/JSONModel",
    "sap/m/MessageToast",
    "sap/ui/core/routing/History",
    //"require",
    ],
    function (SmartOfficeController, JSONModel, MessageToast, History, require) {
        "use strict";

        var self;

        return SmartOfficeController.extend("com.quanto.solutions.ui.smartoffice.controller.Reporting",{
            onInit: function () {
                self=this;
                // set mock data
			    //var sPath = require.toUrl("./SampleData.json");
			    //var oModel = new JSONModel(sPath);
			    //this.getView().setModel(oModel);
                this.oModelSettings = new JSONModel({
                    maxIterations: 200,
                    maxTime: 500,
                    initialTemperature: 200,
                    coolDownStep: 1
                });
                this.getView().setModel(this.oModelSettings, "settings");
                this.getView().setModel(sap.ui.getCore().getModel("TestModel"), "TestModel");
                sap.ui.core.BusyIndicator.hide(0);
                let oRouter = sap.ui.core.UIComponent.getRouterFor(this);
                oRouter.getRoute("reporting").attachMatched(this._onRouteMatched, this);

                //Bar Chart
                //var Bar = this.getView().byId("vizBar");
                //var dataset = new sap.viz.ui5.data.FlattenedDataset({
                    //dimensions:[{
                        //axis: 1,
                        //name:"id",
                        //value: "{Model>id}"
                    //}],
                    //measures: [{
                        //name:"percentage",
                        //value: "{Model>percentage}"
                    //}],
                    //data: {
                        //path: "{Model>/value}"
                    //}
                //});
                //Bar.setDataset(dataset);
            },

            //Line Chart
            //onAfterRendering: function() {
                //var oBusinessData =
                    //[{
                        //Name: "Arav",
                        //2015 : 93.4,
                      // 2015: 96
                    //},
                    //{
                        //Name: "Brij",
                        //2015 : 75.7,
                      // 2015: 93
                    //},
                    //{
                        //Name: "Sia",
                        //2015 : 92.5,
                      // 2015: 98
                    //},
                    //{
                        //Name: "Preya",
                        //2015 : 98.1,
                      //2015: 98
                    //},
                    //{
                        //Name: "Avi",
                        //2015 : 85.3,
                      // 2015: 101
                    //}];
            //},

            //_onRouteMatched : function (oEvent){
                //this.getValues().done(function(result) {
                    //console.log(result.d.results[0])
                    //var dayvalue = result.d.results[0]
                    //self.byId("InputData").setValue(dayvalue)
                //})
                //Jal
                //this.getActualValueJal().done(function(result) {

                    //console.log(result.d.results[0])
                    //var actualValueJal = result.d.results[0]
                    //self.byId("actualvaluejalid").setText(actualValueJal)
                //})
                /*this.getSupposedValueJal().done(function(result)

                    console.log(result.d.results[0])
                    var supposedValueJal = result.d.results[0]
                    self.byId("supposedvaluejalid").setText(supposedValueJal)
                })*/

                //Temp
                /*this.getActualValueTemp().done(function(result) {

                    console.log(result.d.results[0])
                    var actualValueTemp = result.d.results[0]
                    self.byId("actualvaluetempid").setText(actualValueTemp)
                })*/
                /*this.getSupposedValueTemp().done(function(result)

                    console.log(result.d.results[0])
                    var supposedValueTemp = result.d.results[0]
                    self.byId("supposedvaluetempid").setText(supposedValueTemp)
                })*/

            //Jal
            //getActualValueJal: function() {
            //return jQuery.ajax({
                //url: "/LastStatusJalousien",
                //type: "GET"
              //});

            //},

            /*getSupposedValueJal: function() {
            return jQuery.ajax({
                url: "",
                type: "GET"
              });
            },*/

            handleChange: function (oEvent) {
			    var oText = this.byId("DP2"),
				    oDP = oEvent.getSource(),
				    sValue = oEvent.getParameter("value"),
				    bValid = oEvent.getParameter("valid");

			    console.log(sValue)
			    var oData = {"day": sValue};
			    this.getValue(oData)
		    },

            getValue: function (oData) {
                return jQuery.ajax({
                        url :"/StatusPerDay",
                        type: "GET",
                        dataType: "json",
                        async : true,
                        data : oData,
                        success : function(response){
                            //MessageToast.show(response.data.message);
                            console.log(response)
                            sap.ui.core.BusyIndicator.hide();
                        },
                        error: function(response){
                            console.log(response);
                        }
                });
            },

            //LineChart

            press: function (oEvent) {
			    MessageToast.show("The interactive line chart is pressed.");
		    },

		    selectionChanged: function (oEvent) {
			    var oPoint = oEvent.getParameter("point");
			    MessageToast.show("The selection changed: " + oPoint.getLabel() + " " + ((oPoint.getSelected()) ? "selected" : "deselected"));
		    },

            onNavBack: function () {

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