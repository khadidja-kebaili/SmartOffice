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

                //Bar Chart JalousienStatus
                var JalBar = this.getView().byId("vizBarJal");
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
                        path: "/datajalist"
                    }
                });
                JalBar.setDataset(dataset);

                   //Bar Chart ThermostatStatus
                var TempBar = this.getView().byId("vizBarTemp");
                var dataset = new sap.viz.ui5.data.FlattenedDataset({
                    dimensions:[{
                        axis: 1,
                        name:'Tageszeit',
                        value: "{tageszeittempist}"
                    }],
                    measures: [{
                        name:"Status in °C",
                        value: "{valuetempist}"
                    }],
                    data: {
                        path: "/datatempist"
                    }
                });
                TempBar.setDataset(dataset);
            },

            //Jalousien IST Status
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

                    var datajalist = result.d.results
                    datajalist.map(function(eintrag, index) {
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

                    var oModel = new sap.ui.model.json.JSONModel({datajalist: datajalistreporting});
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

            //Temperatur IST Status
            handleTempChange: function (oEvent) {
                var datatempistreporting = []
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
			    this.getValueTemp(oData, "/TempIstStatusPerDay").done(function(result) {

                    var data = result.d.results
                    data.map(function(eintrag, index) {
                        datatempistreporting.push(eintrag)
                    })
                    datatempistreporting.map(function(eintrag){
                        if (eintrag.tageszeittempist == 0){
                            eintrag.tageszeittempist = "10 Uhr"
                        }
                        if (eintrag.tageszeittempist == 1){
                            eintrag.tageszeittempist = "13 Uhr"
                        }
                        if (eintrag.tageszeittempist == 2){
                            eintrag.tageszeittempist = "16 Uhr"
                        }
                        if (eintrag.tageszeittempist == 3){
                            eintrag.tageszeittempist = "19 Uhr"
                        }
                    })

                    var oModel = new sap.ui.model.json.JSONModel({datatempist: datatempistreporting});
                    self.getView().setModel(oModel);
                })
		    },

            getValueTemp: function (oData, url) {
                return jQuery.ajax({
                        url : url,
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