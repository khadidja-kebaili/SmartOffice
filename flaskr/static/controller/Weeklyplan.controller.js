sap.ui.define([
    "../controller/SmartOffice.controller",
    "sap/ui/model/json/JSONModel",
    "sap/m/MessageToast",
    'sap/ui/core/Element',
    'sap/ui/core/Core',
], function(SmartOfficeController, JSONModel, MessageToast, Element) {
        "use strict";

        var self;
        return SmartOfficeController.extend("com.quanto.solutions.ui.smartoffice.controller.Weeklyplan", {
            onInit : function() {
                var dummyData = [{"startzeit":"8:00","endzeit":"10:00","wert":"23"},{"startzeit":"10:00","endzeit":"12:00","wert":"20"},{"startzeit":"12:00","endzeit":"14:00","wert":"18"}]

                var oModel = new sap.ui.model.json.JSONModel({data : dummyData});

                this.getView().setModel(oModel);

                this.addEmptyObject();
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
                var obj = {
                  startzeit: null,
                  endzeit: null, 
                  wert: null,
                  createNew: false,
                  removeNew: false,
                  saveNew: true
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

                this.addEmptyObject();
              },
            onSelectionChange: function (oEvent) {
                var oSegmentedButton = this.byId('SB1'),
                    oSelectedItemId = oSegmentedButton.getSelectedItem(),
                    oSelectedItem = Element.registry.get(oSelectedItemId),
                    oTextControl = this.byId('selectedItemPreview');

                //the selected item could be found via the "item" parameter of "selectionChange" event
                MessageToast.show("Ausgewählter Wochentag:" + oEvent.getParameter("item").getText() );

                //the selected item could also be found via the "selectItem" association not only when "selectionChange" but when needed
                oTextControl.setText("Ausgewählter Wochentag:" + oSelectedItem.getText());
                console.log('Ausgewählter Wochentag:', oSelectedItem.getText())
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
        
