sap.ui.define([
    "../controller/SmartOffice.controller",
    "sap/ui/model/json/JSONModel",
    "sap/m/MessageToast",
    'sap/ui/core/Element',
    'sap/ui/core/Core',
], function(SmartOfficeController, JSONModel, MessageToast, Element) {
        "use strict";

        var self;
        var dummyData = [{"id": 1, "day":"Mo", "startzeit":"8:00","endzeit":"10:00","wert":23},
                {"id": 2, "day":"Mo", "startzeit":"10:00","endzeit":"12:00","wert":23.2},
                {"id": 3, "day":"Di","startzeit":"12:00","endzeit":"14:00","wert":19},
                {"id": 4, "day":"Mi","startzeit":"13:00","endzeit":"14:00","wert":23},
                {"id": 5, "day":"Do","startzeit":"14:00","endzeit":"15:00","wert":44},
                {"id": 6, "day":"Fr","startzeit":"15:00","endzeit":"19:00","wert":23}, ]
                var mondayData = []
                var tuesdayData = []
                var wednesdayData = []
                var thursdayData = []
                var fridayData = []

                dummyData.map(function(eintrag, index) {
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
        return SmartOfficeController.extend("com.quanto.solutions.ui.smartoffice.controller.Weeklyplan", {
            onInit : function() {
              },

              addEmptyObject : function() {
                var oModel = this.getView().getModel();
                var aData  = oModel.getProperty("/data");

                var emptyObject = { createNew: true};

                aData.push(emptyObject);
                oModel.setProperty("/data", aData);
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
                var oData = {
                    'jalousien_id': 1,
                    'day': obj.day,
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
            onSelectionChange: function (oEvent) {
                MessageToast.show("Ausgewählter Wochentag:" + oEvent.getParameter("item").getText() );
                
                
                var selectedDay = oEvent.getParameter("item").getText()
                if(selectedDay == "Mo"){
                    var oModel = new sap.ui.model.json.JSONModel({data : mondayData});
                    this.getView().setModel(oModel);
                    this.addEmptyObject();
                }
                if(selectedDay == "Di"){
                    var oModel = new sap.ui.model.json.JSONModel({data : tuesdayData});
                    this.getView().setModel(oModel);
                }
                if(selectedDay == "Mi"){
                    var oModel = new sap.ui.model.json.JSONModel({data : wednesdayData});
                    this.getView().setModel(oModel);
                    this.addEmptyObject();
                }
                if(selectedDay == "Do"){
                    var oModel = new sap.ui.model.json.JSONModel({data : thursdayData});
                    this.getView().setModel(oModel);
                    this.addEmptyObject();
                }
                if(selectedDay == "Fr"){
                    var oModel = new sap.ui.model.json.JSONModel({data : fridayData});
                    this.getView().setModel(oModel);
                    this.addEmptyObject();
                }
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
        
