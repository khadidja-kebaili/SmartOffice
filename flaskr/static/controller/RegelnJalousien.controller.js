sap.ui.define([
    "../controller/SmartOffice.controller",
    "sap/ui/model/json/JSONModel",
    "sap/m/MessageToast",
    'sap/ui/core/Element',
    'sap/ui/core/Core',
], function(SmartOfficeController, JSONModel, MessageToast, Element) {
        "use strict";

        var self;
        var dummyData = [{"id": 1, "startzeit":"8:00","endzeit":"10:00","wert":50},
                {"id": 2, "startzeit":"11:00","endzeit":"12:00","wert":70}]
        var datatest = []

        dummyData.map(function(eintrag, index) {
                
                    datatest.push(eintrag)
            })

        return SmartOfficeController.extend("com.quanto.solutions.ui.smartoffice.controller.RegelnJalousien", {
            onInit : function() {
              },

              addEmptyObject : function() {
                var oModel = this.getView().getModel();
                var aData  = oModel.getProperty("/data");

                var emptyObject = { createNew: true};

                aData.push(emptyObject);
                oModel.setProperty("/data", aData);
              },

            test: function() {
                ///var selectedDay = oEvent.getParameter("item").getText()

                var oModel = new sap.ui.model.json.JSONModel({data : datatest});
                this.getView().setModel(oModel);
                this.addEmptyObject()
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

                console.log("Neuer Wert wurde eingestellt.");
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

            removeEntry: function () {
                MessageToast.show("Löschen Eintrag mit ID:")  
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
			}

		});

     });
        