sap.ui.define([
    "../controller/SmartOffice.controller",
    "sap/ui/model/json/JSONModel",
    "sap/m/MessageToast"
], function(SmartOfficeController, JSONModel, MessageToast) {
        "use strict";

        var self;
        return SmartOfficeController.extend("com.quanto.solutions.ui.smartoffice.controller.RegelnJalousien", {
            onInit: function () {

            },
            onLiveChange: function (oEvent) {
                var sNewValue = oEvent.getParameter("value");
                this.byId("getValue").setText(sNewValue);
            },
            
            sendValue: function(oEvent) {
                console.log("Neuer Wert wurde eingestellt.");
                sap.ui.core.BusyIndicator.hide(0);
                //var oThis = this;
                var oData = {
                    'value': oEvent.getParameter("value")
                };
                console.log(oData),
                jQuery.ajax({
                    url : "/Jalousien",
                    type : "POST",
                    dataType : "json",
                    async : true,
                    data : oData,
                    success : function(response){
                        MessageToast.show(response.data.message);
                        //oThis.makeGraph(response.graph);
                        sap.ui.core.BusyIndicator.hide();
                    },
                    error: function(response){
                        console.log(response);
                    }
                });
            },
        });
    });