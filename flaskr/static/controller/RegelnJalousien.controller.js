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

        return SmartOfficeController.extend("com.quanto.solutions.ui.smartoffice.controller.RegelnJalousien", {
            onInit : function() {
                self = this;
                var oModel = new sap.ui.model.json.JSONModel({"id": null, "startzeit":null,"endzeit":null,"wert":null});
                this.getView().setModel(oModel)
                let oRouter = sap.ui.core.UIComponent.getRouterFor(this);
                oRouter.getRoute("regelnjalousien").attachMatched(this._onRouteMatched, this);
                
              },

            addEmptyObject : function() {
                var oModel = this.getView().getModel();
                var aData  = oModel.getProperty("/data");

                var emptyObject = { createNew: true};

                aData.push(emptyObject);
                oModel.setProperty("/data", aData);
                this.addEntry();
              },

            test: function() {
                ///var selectedDay = oEvent.getParameter("item").getText()
                MessageToast.show("Hallo Juhu")
               
            },
            _onRouteMatched : function (oEvent){
                var datatest2 = []
                this.getData().done(function(result) {
                    
                    var dummyDatat = result.d.results
                    dummyDatat.map(function(eintrag, index) {
                        datatest2.push(eintrag)
                    })
                    console.log(datatest2)                
                    var oModel = new sap.ui.model.json.JSONModel({data: datatest2});
                    self.getView().setModel(oModel);
                    self.addEmptyObject();
                    //console.log("Jetzt bin ich am Ende")
                })

                //var oModel = new sap.ui.model.json.JSONModel({data: datatest2});
                //this.getView().setModel(oModel);
                //this.addEmptyObject()

            },
            getData: function () {
				console.log('Get data für Regeln Jalousien')
				return jQuery.ajax({
					url: "/RegelnJalousien",
					type: "GET"
				});
			},

              enableControl : function(value) {
                return !!value;
              },

              disableControl : function(value) {
                return !value;
              },

              addEntry : function(oEvent) {
                var path = oEvent.getSource().getBindingContext().getPath();
                var obj = {
                  id: null,
                  startzeit: null,
                  endzeit: null, 
                  wert: null,
                  createNew: false,
                  removeNew: false,
                  saveNew: true,
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

                console.log("Neuer Wert wurde eingestellt. Juhu");
                sap.ui.core.BusyIndicator.hide(0);
                //var oThis = this;
                var oData = {
                    'jalousien_id': 1,
                    'start': obj.startzeit,
                    'end': obj.endzeit, 
                    'value': obj.wert
                };
                console.log(oData),

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
                this.addEmptyObject();
                console.log('object',obj)
            },

            removeEntry: function (oEvent) {
                var path = oEvent.getSource().getBindingContext().getPath();
                var obj = oEvent.getSource().getBindingContext().getObject();
                
                obj.saveNew = false;
                obj.removeNew = true;

                var oModel = this.getView().getModel();

                oModel.setProperty(path, obj);
                MessageToast.show("Löschen Eintrag mit ID:" + obj.id) 
                var oData = {
                    'jalousien_id': 1,
                    'id': obj.id
                }; 
                console.log(oData)
                 //jQuery.ajax({
                    //url : "/remove/{obj.id}",
                    //type : "DELETE",
                    //dataType : "json",
                    //success : function(response){
                        //MessageToast.show(response.data.message);
                        //sap.ui.core.BusyIndicator.hide();
                    //},
                    //error: function(response){
                        //console.log(response);
                    //}
                //});
            },
            
            onPress: function () {
                var FlexBox=this.byId('TimeStepContainer')
                FlexBox.addItem(Button)
            },
            handleChange: function (oEvent) {
				var oText = this.byId("T1"),
					oTP = oEvent.getSource(),
					sValue = oEvent.getParameter("value"),
					bValid = oEvent.getParameter("valid");
				this._iEvent++;
				oText.setText("'change' Event #" + this._iEvent + " from TimePicker '" + oTP.getId() + "': " + sValue + (bValid ? ' (valid)' : ' (invalid)'));

				if (bValid) {
					oTP.setValueState(ValueState.None);
				} else {
					oTP.setValueState(ValueState.Error);
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
        