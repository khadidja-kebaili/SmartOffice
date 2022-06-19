sap.ui.define([
    "../controller/SmartOffice.controller",
    "sap/ui/model/json/JSONModel",
    "sap/m/MessageToast",
    'sap/ui/core/Element',
    'sap/ui/core/Core',
    "sap/ui/core/routing/History"
], function(SmartOfficeController, JSONModel, MessageToast, Element, Core, History) {
        "use strict";

        var self;
        var mondayData = []
        var tuesdayData = []
        var wednesdayData = []
        var thursdayData = []
        var fridayData = []

        return SmartOfficeController.extend("com.quanto.solutions.ui.smartoffice.controller.Weeklyplan", {
            onInit : function() {
                    self = this;
                    var oModel = new sap.ui.model.json.JSONModel({"id": null, "day": null, "startzeit":null,"endzeit":null,"wert":null});
                    this.getView().setModel(oModel);
                    let oRouter = sap.ui.core.UIComponent.getRouterFor(this);
                    oRouter.getRoute("wochenplan").attachMatched(this._onRouteMatched, this);
              },
              
            _onRouteMatched : function (oEvent){
                mondayData.length = 0
                tuesdayData.length = 0
                wednesdayData.length = 0
                thursdayData.length = 0
                fridayData.length = 0
                this.getData().done(function(result) {
                    
                    var data = result.d.results
                    
                    data.map(function(eintrag, index) {
                      if(eintrag.day == "Mo"){
                          mondayData.push(eintrag)
                      }
                      if(eintrag.day == "Di"){
                          tuesdayData.push(eintrag)
                      }
                      if(eintrag.day == "Mi"){
                          wednesdayData.push(eintrag)
                      }
                      if(eintrag.day == "Do"){
                          thursdayData.push(eintrag)
                      }
                      if(eintrag.day == "Fr"){
                          fridayData.push(eintrag)
                      }
                      })       
                    var oModel = new sap.ui.model.json.JSONModel({data: mondayData});
                    self.getView().setModel(oModel);
                })
            },
            
            getData: function () {
              console.log('Get data für Wochenplan Jalousien')
              return jQuery.ajax({
                url: "/WochenplanJalousien",
                type: "GET"
              });
            },

              addEmptyObject : function() {
                var oModel = this.getView().getModel();
                var aData  = oModel.getProperty("/data");

                var emptyObject = { createNew: true, removeNew: false};

                aData.push(emptyObject);
                oModel.setProperty("/data", aData);
                this.addEntry();
              },

              enableControl : function(value) {
                return !!value;
              },

              disableControl : function(value) {
                return !value;
              },

              addEntry : function(oEvent) {
                var path = oEvent.getSource().getBindingContext().getPath();
                var oSegmentedButton = this.byId('SB1');
                var oSelectedItemId = oSegmentedButton.getSelectedItem();
                var oSelectedItem = Element.registry.get(oSelectedItemId);
                var obj = {
                  startzeit: null,
                  endzeit: null, 
                  wert: null,
                  createNew: false,
                  removeNew: false,
                  saveNew: true,
                  day: oSelectedItem.getText()
                };

                var oModel = this.getView().getModel();

                oModel.setProperty(path, obj);
              },

              saveEntry : function(oEvent) {
                var path = oEvent.getSource().getBindingContext().getPath();
                var obj = oEvent.getSource().getBindingContext().getObject();
                obj.saveNew = false;
                obj.removeNew = true;

                var oModel = this.getView().getModel();

                oModel.setProperty(path, obj);
                console.log("Neuer Wert wurde eingestellt.");
                sap.ui.core.BusyIndicator.hide(0);
                //var oThis = this;
                console.log('objSave', obj, "path", path, "obj.", )
                var oData = {
                    'jalousien_id': 1,
                    'day': obj.day,
                    'start': obj.startzeit,
                    'end': obj.endzeit, 
                    'wert': obj.wert
                };
                console.log(oData)
                //jQuery.ajax({
                    //url : "/",
                    //type : "POST",
                    //dataType : "json",
                    //async : true,
                    //data : oData,
                    //success : function(response){
                        //MessageToast.show(response.data.message);
                        //oThis.makeGraph(response.graph);
                        //sap.ui.core.BusyIndicator.hide();
                    //},
                    //error: function(response){
                        //console.log(response);
                    //}
                //});

              },
              removeEntry: function (oEvent) {
                var path = oEvent.getSource().getBindingContext().getPath();
                var obj = oEvent.getSource().getBindingContext().getObject();
                console.log('objDelte', obj)
                MessageToast.show("Löschen Eintrag mit ID:" + obj.id)  
            },
            onSelectionChange: function (oEvent) {
                //MessageToast.show("Ausgewählter Wochentag:" + oEvent.getParameter("item").getText() );
              
                var selectedDay = oEvent.getParameter("item").getText()
                if(selectedDay == "Mo"){
                    var oModel = new sap.ui.model.json.JSONModel({data : mondayData});
                    this.getView().setModel(oModel);
                }
                if(selectedDay == "Di"){
                    var oModel = new sap.ui.model.json.JSONModel({data : tuesdayData});
                    this.getView().setModel(oModel);
                }
                if(selectedDay == "Mi"){
                    var oModel = new sap.ui.model.json.JSONModel({data : wednesdayData});
                    this.getView().setModel(oModel);
                }
                if(selectedDay == "Do"){
                    var oModel = new sap.ui.model.json.JSONModel({data : thursdayData});
                    this.getView().setModel(oModel);
                }
                if(selectedDay == "Fr"){
                    var oModel = new sap.ui.model.json.JSONModel({data : fridayData});
                    this.getView().setModel(oModel);
                }
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
        
