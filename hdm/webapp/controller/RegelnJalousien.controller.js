sap.ui.define([
    "../controller/SmartOffice.controller",
    "sap/ui/model/json/JSONModel",
    "sap/m/MessageToast",
    "sap/m/MessageBox",
    'sap/ui/core/Element',
    'sap/ui/core/Core',
    "sap/ui/core/routing/History"
], function(SmartOfficeController, JSONModel, MessageToast, MessageBox, Element, Core, History) {
        "use strict";

        var self;

        return SmartOfficeController.extend("com.quanto.solutions.ui.smartoffice.controller.RegelnJalousien", {
            onInit : function() {
                self = this;
                var oModel = new sap.ui.model.json.JSONModel({"id": null, "startzeit":null,"endzeit":null,"min":null,"max": null});
                this.getView().setModel(oModel)
                //Route an match-Funktion binden
                let oRouter = sap.ui.core.UIComponent.getRouterFor(this);
                oRouter.getRoute("regelnjalousien").attachMatched(this._onRouteMatched, this);
                
              },
            //Funktion um leeres Objekt, leere Zeile hinzuzufügen
            addEmptyObject : function() {
                var oModel = this.getView().getModel();
                console.log(oModel)
                var aData  = oModel.getProperty("/data");
                console.log(aData)
                var emptyObject = { createNew: true };
                console.log(emptyObject)
                aData.push(emptyObject);
                oModel.setProperty("/data", aData);
                this.addEntry();
              },

            //Wenn Route "regelnjalousien" aufgerufen wird alle bestehenden Regeln abrufen und anzeigen
            _onRouteMatched : function (oEvent){
                var datatest2 = []
                this.getData().done(function(result) {
                    
                    var data = result.d.results
                    data.map(function(eintrag, index) {
                        datatest2.push(eintrag)
                    })
                    console.log(datatest2)                
                    var oModel = new sap.ui.model.json.JSONModel({data: datatest2});
                    self.getView().setModel(oModel);
                    self.addEmptyObject();
                })

            },
            //Get-Funktion, um bestehende Regeln aus Datenbank zu holen
            getData: function () {
              console.log('Get data für Regeln Jalousien')
              return jQuery.ajax({
                url: "/GetJalRule",
                type: "GET"
              });
            },

              enableControl : function(value) {
                return !!value;
              },

              disableControl : function(value) {
                return !value;
              },
              //Eintrag hinzufügen, wird nach Klicken auf das Plus aufgerufen. Erstellt neues Objekt
              addEntry : function(oEvent) {
                var path = oEvent.getSource().getBindingContext().getPath();
                var obj = {
                  id: null,
                  startzeit: null,
                  endzeit: null, 
                  min: null,
                  max: null,
                  createNew: false,
                  removeNew: false,
                  saveNew: true,
                };

                var oModel = this.getView().getModel();

                oModel.setProperty(path, obj);
              },
              //Eintrag speichern, wird nach Klicken auf Speichern aufgerufen
              //Speichert eingetragene Werte, schickt diese ins Backend und fügt Eintrag in Tabelle hinzu
              saveEntry : function(oEvent) {
                var path = oEvent.getSource().getBindingContext().getPath();
                var obj = oEvent.getSource().getBindingContext().getObject();
                
                obj.saveNew = false;
                obj.removeNew = true;

                var oModel = this.getView().getModel();

                oModel.setProperty(path, obj);

                console.log("Neuer Wert wurde eingestellt.");
                sap.ui.core.BusyIndicator.hide(0);
                //Hier werden Werte in oData gepspeichert
                var oData = {
                    'start': obj.startzeit,
                    'end': obj.endzeit, 
                    'min': obj.min,
                    'max': obj.max
                };
                console.log(oData),
                //POST-Methode zum senden der Werte
                jQuery.ajax({
                    url : "/SetJalRule",
                    type : "POST",
                    dataType : "json",
                    async : true,
                    data : oData,
                    success : function(response){
                        sap.ui.core.BusyIndicator.hide();
                        var errorcheck = response.type
                        console.log(errorcheck)
                        var start = response.start
                        var end = response.end
                        if (errorcheck == "0") {
                            MessageBox.information("Auf Grund von Überschneidungen wurde der Eintrag von " + start + " Uhr bis " + end + " Uhr gelöscht. \n Der so eben eingestelle Eintrag wurde gespeichert.");
                        }
                    },
                    error: function(response){
                        console.log(response);
                    }
                }).done(function() {
                  //Nachdem Werte gesendet wurden, hole erneut alle aktuellen Werte aus der Datenbank und zeige diese an
                  var datatest2 = []
                  self.getData().done(function(result) {
                    
                    var data = result.d.results
                    data.map(function(eintrag, index) {
                        datatest2.push(eintrag)
                    })
                    console.log(datatest2)                
                    var oModel = new sap.ui.model.json.JSONModel({data: datatest2});
                    self.getView().setModel(oModel);
                    //Hinzufügen einer neuen leeren Spalte
                    self.addEmptyObject();
                  })
                })
            },
            //Eintrag löschen, wird aufgerufen nach Klicken auf das Löschen-Icon
            removeEntry: function (oEvent) {
                var path = oEvent.getSource().getBindingContext().getPath();
                var obj = oEvent.getSource().getBindingContext().getObject();
                
                obj.saveNew = false;
                obj.removeNew = true;

                var oModel = this.getView().getModel();

                oModel.setProperty(path, obj);
                //ID des zu löschenden EIntrags speichern
                var oData = {
                    'id_entry': obj.id
                }; 
                console.log(oData)
                //DElETE-Methode sendet ID ans backend und löscht das zugehörige Objekt
                 jQuery.ajax({
                    url : "/DeleteJalRule",
                    type : "DELETE",
                    dataType : "json",
                    data: oData,
                    success : function(response){
                        MessageToast.show(response.data.message);
                        sap.ui.core.BusyIndicator.hide();
                    },
                    error: function(response){
                        console.log(response);
                    }
                });
                //Außerdem wird das Objekt so direkt aus der angezeigten Tabelle gelöscht
                var idx = parseInt(path.substring(path.lastIndexOf('/') +1));
                var m = this.getView().getModel();
                var aData  = m.getProperty("/data");
                aData.splice(idx, 1);
                m.setProperty("/data", aData);
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
            //Zurück Navigation führt zur vorherigen Seite
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
        