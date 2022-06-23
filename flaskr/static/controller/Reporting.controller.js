sap.ui.define([
    "../controller/SmartOffice.controller",
    "sap/ui/model/json/JSONModel",
    "sap/m/MessageToast",
    "sap/ui/core/routing/History"
    ],
    function (SmartOfficeController, JSONModel, MessageToast, History) {
        "use strict";

        var self;
        var dayData =[]

        return SmartOfficeController.extend("com.quanto.solutions.ui.smartoffice.controller.Reporting",{
            onInit: function () {
                self=this;
                var oModel = new sap.ui.model.json.JSONModel({"day": null});
                this.getView().setModel(oModel);
                let oRouter = sap.ui.core.UIComponent.getRouterFor(this);
                oRouter.getRoute("reporting").attachMatched(this._onRouteMatched, this);
                //this.oModelSettings = new JSONModel({
                    //maxIterations: 200,
                    //maxTime: 500,
                    //initialTemperature: 200,
                    //coolDownStep: 1
                //});
                //this.getView().setModel(this.oModelSettings, "settings");
                //this.getView().setModel(sap.ui.getCore().getModel("TestModel"), "TestModel");
                //sap.ui.core.BusyIndicator.hide(0);

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

            _onRouteMatched : function (oEvent){
                dayData.length = 0
                this.getData("/StatusPerDay").done(function(result) {
                    var data = result.d.results
                    var oModel = new sap.ui.model.json.JSONModel({data: dayData});
                    self.getView().setModel(oModel);

                })
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
            },

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

            getData: function (url) {
              console.log('Get data für Day')
              return jQuery.ajax({
                url: url,
                type: "GET"
              });
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