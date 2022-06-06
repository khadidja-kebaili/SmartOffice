sap.ui.define([
    "../controller/SmartOffice.controller",
    "sap/ui/model/json/JSONModel",
    "sap/m/MessageToast",
    'sap/ui/core/Element',
    'sap/ui/core/Core',
], function(SmartOfficeController, JSONModel, Element, MessageToast) {
        "use strict";

        var self;
        return SmartOfficeController.extend("com.quanto.solutions.ui.smartoffice.controller.Weeklyplan", {
            onInit: function () {
                var timepicker = document.querySelector('#TimeFlexbox');
                let time = [
                    {
                      "id": 1,
                      "value":"08:00",
                      "valueFormat":"HH:mm",
                      "displayFormat":"HH:mm",
                      "change":"handleChange"
                    },
                    {
                        "id": 2,
                        "value":"09:00",
                        "valueFormat":"HH:mm",
                        "displayFormat":"HH:mm",
                        "change":"handleChange"
                    },
                ]
                
                time.map(function (time) {
                    console.log('timevalue', time.value)
                    return '<li>' + time.value + '</li>';
                }).join('') + '</ul>';
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

        });
        
    });
