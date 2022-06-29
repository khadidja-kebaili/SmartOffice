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
                var oModelJalIst = new sap.ui.model.json.JSONModel({"tageszeit": null, "value": null});
                this.getView().setModel(oModelJalIst, "JalIstModel")

                var oModelJalSoll = new sap.ui.model.json.JSONModel({"tageszeit": null, "value": null});
                this.getView().setModel(oModelJalSoll, "JalSollModel")

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
                    measures: [
                        {
                            name:"Ist-Status in %",
                            value: "{valuejalist}"
                        },
                        {
                            name:"Soll-Status in %",
                            value: {path: "JalSollModel>/valuejalsoll"}
                        }
                    ],
                    data: {
                        path: "JalIstModel>/datajalist"
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
                    measures: [
                        {
                            name:"Status in °C",
                            value: "{valuetempist}"
                        },
                        {
                            name:"Soll-Status in °C",
                            value: {path: "TempSollModel>/valuetempsoll"}
                        }
                    ],
                    data: {
                        path: "TempIstModel>/datatempist"
                    }
                });
                TempBar.setDataset(dataset);
            },
            getValue: function (oData, url) {
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

            //Handle Datum Change
            handleJalChange: function (oEvent) {
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
                this.getJalIst(oData)
                this.getJalSoll(oData)
		    },
            //Get Jalousien IST
            getJalIst: function (oData) {
                var datajalistreporting = []
                this.getValue(oData, "/JalIstStatusPerDay").done(function(result) {

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
                        if (eintrag.valuejalist == 0){
                            eintrag.valuejalist = "Kein Eintrag vorhanden"
                        }
                    })

                    var oModelJalIst = new sap.ui.model.json.JSONModel({datajalist: datajalistreporting});
                    self.getView().setModel(oModelJalIst, "JalIstModel");
                })

            },
            //Get Jalousien Soll
            getJalSoll: function (oData) {
                
                var datajalsollreporting = []
                this.getValue(oData, "/JalSollStatusPerDay").done(function(result) {

                    var datajalsoll = result.d.results
                    datajalsoll.map(function(eintrag, index) {
                        datajalsollreporting.push(eintrag)
                    })
                    console.log(datajalsollreporting)
                    datajalsollreporting.map(function(eintrag){
                        if (eintrag.tageszeitjalsoll == 0){
                            eintrag.tageszeitjalsoll = "10 Uhr"
                        }
                        if (eintrag.tageszeitjalsoll == 1){
                            eintrag.tageszeitjalsoll = "13 Uhr"
                        }
                        if (eintrag.tageszeitjalsoll == 2){
                            eintrag.tageszeitjalsoll = "16 Uhr"
                        }
                        if (eintrag.tageszeitjalsoll == 3){
                            eintrag.tageszeitjalsoll = "19 Uhr"
                        }
                        if (eintrag.valuejalsoll == 0){
                            eintrag.valuejalsoll = "Kein Eintrag vorhanden"
                        }
                    })

                    var oModelJalSoll = new sap.ui.model.json.JSONModel({datajalsoll: datajalsollreporting});
                    self.getView().setModel(oModelJalSoll, "JalSollModel");
                })
            },

            //Handle Datum Change Temp
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
                this.getTempIst(oData)
                this.getTempSoll(oData)
            },
            //Get Temp Ist
            getTempIst: function(oData){
                var datatempistreporting = []
                this.getValue(oData, "/TempIstStatusPerDay").done(function(result) {

                    var data = result.d.results
                    data.map(function(eintrag, index) {
                        datatempistreporting.push(eintrag)
                    })
                    datatempistreporting.map(function(eintrag){
                        eintrag.valuetempist = (eintrag.valuetempist / 10)

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
                        if (eintrag.valuetempist == 0){
                            eintrag.valuetempist = "Kein Eintrag vorhanden"
                        }

                    })

                    var oModelTempIst = new sap.ui.model.json.JSONModel({datatempist: datatempistreporting});
                    self.getView().setModel(oModelTempIst, "TempIstModel");
                })
            },
            //Get Temp Soll
            getTempSoll: function(oData){
                var datatempsollreporting = []
                this.getValue(oData, "/TempSollStatusPerDay").done(function(result) {

                    var data = result.d.results
                    data.map(function(eintrag, index) {
                        datatempsollreporting.push(eintrag)
                    })
                    datatempsollreporting.map(function(eintrag){
                        eintrag.valuetempsoll = (eintrag.valuetempsoll / 10)

                        if (eintrag.tageszeittempsoll == 0){
                            eintrag.tageszeittempsoll = "10 Uhr"
                        }
                        if (eintrag.tageszeittempsoll == 1){
                            eintrag.tageszeittempsoll = "13 Uhr"
                        }
                        if (eintrag.tageszeittempsoll == 2){
                            eintrag.tageszeittempsoll = "16 Uhr"
                        }
                        if (eintrag.tageszeittempsoll == 3){
                            eintrag.tageszeittempsoll = "19 Uhr"
                        }
                        if (eintrag.valuetempsoll== 0){
                            eintrag.valuetempsoll = "Kein Eintrag vorhanden"
                        }
                    })

                    var oModelTempSoll= new sap.ui.model.json.JSONModel({datatempsoll: datatempsollreporting});
                    self.getView().setModel(oModelTempSoll, "TempSollModel");
                })
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