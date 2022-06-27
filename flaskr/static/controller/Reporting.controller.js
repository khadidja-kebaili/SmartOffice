sap.ui.define([
    "../controller/SmartOffice.controller",
    "sap/ui/model/json/JSONModel",
    "sap/m/MessageToast",
    "sap/ui/core/routing/History",
    "sap/ui/core/Core",
	"sap/ui/core/library",
	"sap/ui/unified/library",
	"sap/ui/unified/DateTypeRange"
    //"require",
    ],
    function (SmartOfficeController, JSONModel, MessageToast, History,  Core, CoreLibrary, UnifiedLibrary, DateTypeRange) {
        "use strict";
        var CalendarDayType = UnifiedLibrary.CalendarDayType,
		ValueState = CoreLibrary.ValueState;
        var self;

        return SmartOfficeController.extend("com.quanto.solutions.ui.smartoffice.controller.Reporting",{
            onInit: function () {
                self=this;
                // set mock data
			    //var sPath = require.toUrl("./SampleData.json");
			    //var oModel = new JSONModel(sPath);
			    //this.getView().setModel(oModel);
                //this.oModelSettings = new JSONModel({
                    //maxIterations: 200,
                    //maxTime: 500,
                    //initialTemperature: 200,
                    //coolDownStep: 1
                //});
                //this.getView().setModel(this.oModelSettings, "settings");
                //this.getView().setModel(sap.ui.getCore().getModel("TestModel"), "TestModel");
                var oModel = new sap.ui.model.json.JSONModel({"tageszeit": null, "value": null});
                this.getView().setModel(oModel)
                let oRouter = sap.ui.core.UIComponent.getRouterFor(this);
                oRouter.getRoute("reporting").attachMatched(this._onRouteMatched, this);

                // for the data binding example do not use the change event for check but the data binding parsing events
                Core.attachParseError(
                    function(oEvent) {
                        var oElement = oEvent.getParameter("element");

                        if (oElement.setValueState) {
                            oElement.setValueState(ValueState.Error);
                        }
                    });

                Core.attachValidationSuccess(
                        function(oEvent) {
                            var oElement = oEvent.getParameter("element");

                            if (oElement.setValueState) {
                                oElement.setValueState(ValueState.None);
                            }
                        });
                //Bar Chart
                var Bar = this.getView().byId("vizBar");
                var dataset = new sap.viz.ui5.data.FlattenedDataset({
                    dimensions:[{
                        axis: 1,
                        name:'Tageszeit',
                        value: "{tageszeitjalist}"
                    }],
                    measures: [{
                        name:"Status in %",
                        value: "{valuejalist}"
                    }],
                    data: {
                        path: "/data"
                    }
                });
                Bar.setDataset(dataset);
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
                //var datareporting = []
                //this.getValue().done(function(result) {

                    //var data = result.d.results
                    //data.map(function(eintrag, index) {
                        //datareporting.push(eintrag)
                    //})
                    //console.log(datareporting)
                    //var oModel = new sap.ui.model.json.JSONModel({data: datareporting});
                    //self.getView().setModel(oModel);
                    //self.addObject();
                    //console.log("Jetzt bin ich am Ende")
                //})
            //},
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

            //Jalousien GET
            handleJalChange: function (oEvent) {
                var datajalistreporting = []
			    var oText = this.byId("DP2"),
				    oDP = oEvent.getSource(),
				    sValue = oEvent.getParameter("value"),
                    bValid = oEvent.getParameter("valid");
                //oText.setText(sValue)
                if (bValid) {
                    oDP.setValueState(ValueState.None);
                } else {
                    oDP.setValueState(ValueState.Error);
                }
			    console.log(sValue)
			    var oData = {"day": sValue};
			    this.getValue(oData).done(function(result) {

                    var data = result.d.results
                    data.map(function(eintrag, index) {
                        datajalistreporting.push(eintrag)
                    })
                    datajalistreporting.map(function(eintrag){
                        if (eintrag.tageszeitjalist == 0){
                            eintrag.tageszeitjalist = "10 Uhr"
                        }
                        if (eintrag.tageszeitjalist == 1){
                            eintrag.tageszeitjalist = "13 Uhr"
                        }
                        if (eintrag.tageszeitjalist == 2){
                            eintrag.tageszeitjalist = "16 Uhr"
                        }
                        if (eintrag.tageszeitjalist == 3){
                            eintrag.tageszeitjalist = "19 Uhr"
                        }
                    })

                    var oModel = new sap.ui.model.json.JSONModel({data: datajalistreporting});
                    self.getView().setModel(oModel);
                })
		    },

            getValue: function (oData) {
                return jQuery.ajax({
                        url :"/JalIstStatusPerDay",
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

            //Temperatur GET
            handleTempChange: function (oEvent) {
                var datareporting = []
			    var oText = this.byId("DP1"),
				    oDP = oEvent.getSource(),
				    sValue = oEvent.getParameter("value"),
                    bValid = oEvent.getParameter("valid");
                //oText.setText(sValue)
                if (bValid) {
                    oDP.setValueState(ValueState.None);
                } else {
                    oDP.setValueState(ValueState.Error);
                }
			    console.log(sValue)
			    var url = {"day": sValue};
			    this.getValueTemp(url).done(function(result) {

                    var data = result.d.results
                    data.map(function(eintrag, index) {
                        datareporting.push(eintrag)
                    })
                    datareporting.map(function(eintrag){
                        if (eintrag.tageszeit == 0){
                            eintrag.tageszeit = "10 Uhr"
                        }
                        if (eintrag.tageszeit == 1){
                            eintrag.tageszeit = "13 Uhr"
                        }
                        if (eintrag.tageszeit == 2){
                            eintrag.tageszeit = "16 Uhr"
                        }
                        if (eintrag.tageszeit == 3){
                            eintrag.tageszeit = "19 Uhr"
                        }
                    })

                    var oModel = new sap.ui.model.json.JSONModel({data: datareporting});
                    self.getView().setModel(oModel);
                })
		    },

            getValueTemp: function (url) {
                return jQuery.ajax({
                        url : url,
                        type: "GET",
                        dataType: "json",
                        async : true,
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