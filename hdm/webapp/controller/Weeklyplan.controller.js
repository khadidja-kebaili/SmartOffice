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

        //Leere Listen für Wochenpläne pro Tag initiieren
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
                    //Route an match-Funktion binden
                    let oRouter = sap.ui.core.UIComponent.getRouterFor(this);
                    oRouter.getRoute("wochenplan").attachMatched(this._onRouteMatched, this);
              },
              //Sobald Route aufgerufen wird, hole alle Einträge für die Wochentage aus der Datenbank 
            _onRouteMatched : function (oEvent){
                //Listen wieder auf null setzen damit nichts doppelt angezeigt wird
                mondayData.length = 0
                tuesdayData.length = 0
                wednesdayData.length = 0
                thursdayData.length = 0
                fridayData.length = 0

                //Daten für Montag aus Datenbank abrufen, gleich für alle Wochentage
                this.getData("/GetStandardJalousienMonday").done(function(result) {
                    var data = result.d.results
                    //Daten in Liste pushen
                    data.map(function(eintrag, index) {
                      mondayData.push(eintrag)
                      })     
                    console.log(mondayData)
                    //Liste mit Daten an Model hängen  
                    var oModel = new sap.ui.model.json.JSONModel({data: mondayData});
                    //Daten in Tabelle anzeigen, hier nur für Montag da dass die erste Ansicht ist
                    //Andere Wochentage werden erst bei Wechsel des Tages angezeigt
                    self.getView().setModel(oModel);
                  
                })
                this.getData("/GetStandardJalousienTuesday").done(function(result) {
                  var data = result.d.results
                  data.map(function(eintrag, index) {
                    tuesdayData.push(eintrag)
                    })     
                  console.log(mondayData)  
              
                })
                this.getData("/GetStandardJalousienWednesday").done(function(result) {
                  var data = result.d.results
                  data.map(function(eintrag, index) {
                    wednesdayData.push(eintrag)
                    })     
                  console.log(mondayData)  
              
                })
                this.getData("/GetStandardJalousienThursday").done(function(result) {
                  var data = result.d.results
                  data.map(function(eintrag, index) {
                    thursdayData.push(eintrag)
                    })     
              
                })
                this.getData("/GetStandardJalousienFriday").done(function(result) {
                  var data = result.d.results
                  data.map(function(eintrag, index) {
                    fridayData.push(eintrag)
                    })     
              
                })
            },
            //GET-Methode um Daten aus Datenbank zu holen
            getData: function (url) {
              console.log('Get data für Wochenplan Jalousien')
              return jQuery.ajax({
                url: url,
                type: "GET"
              });
            },

            //Leeres Objekt erstellen und anzeigen lassen
              addEmptyObject : function() {
                var oModel = this.getView().getModel();
                var aData  = oModel.getProperty("/data");
                console.log(oModel)
                console.log(aData)
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
              //Eintrag hinzufügen, wird bei Klicken auf Plus aufgerufen
              //Jetzt kann der Eintrag konfiguriert werden
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

              //Eintrag speichern, wird bei Klicken auf Speichern aufgerufen
              //Eingestellte Werte werden gespeichert und an Backend gesendet
              saveEntry : function(oEvent) {
                
                var path = oEvent.getSource().getBindingContext().getPath();
                var obj = oEvent.getSource().getBindingContext().getObject();
                obj.saveNew = false;
                obj.removeNew = true;

                sap.ui.core.BusyIndicator.hide(0);

                //IF-Schleifen für jeden Tag: Hier wird nur Montag erklärt, gilt für alle gleich
                //Prüfen, ob Tag = Montag ist
                if(obj.day == "Mo"){
                    console.log("Send Monday")
                    //Speichern der Start- und Endzeit sowie des Werts
                    var oData = {
                    'start': obj.startzeit,
                    'end': obj.endzeit, 
                    'value': parseInt(obj.wert)
                    };
                    //Senden der Werte an Backend
                    this.sendValues(oData, "/SetJalousienStandardMonday").done(function(result) {
                      //Rückgabewerte in variablen speichern
                      var errorcheck = result.type
                      var mindestwert = result.min
                      var maximalwert = result.max
                      var start = result.start
                      var end = result.end
                        //Variable errorcheck prüfen: Wenn 0 liegt Regelverstoß vor
                        if (errorcheck == "0") {
                            //MessageBox mit erlaubter Zeit und Werten anzeigen
                            MessageBox.error("Der Eintrag verstößt gegen eine Regel. \n Für diesen Zeitraum muss der Wert zwischen " + mindestwert + "% und " + maximalwert + "% liegen. \n Bitte versuche eine andere Einstellung!");
                            //Eintrag kann nicht in Datenbank gespeichert werden, deswegen entfernen
                            var idx = parseInt(path.substring(path.lastIndexOf('/') +1));
                            var m = self.getView().getModel();
                            var aData  = m.getProperty("/data");
                            aData.splice(idx, 1);
                            m.setProperty("/data", aData);
                        }
                        else {
                          //Wenn errorcheck = 1 liegt Überschneidung vor
                          if (errorcheck == "1") {
                            //MessageBox mit Info, dass vorheriger Eintrag gelöscht wurde
                            MessageBox.information("Auf Grund von Überschneidungen wurde der Eintrag von " + start + " Uhr bis " + end + " Uhr gelöscht. \n Der so eben eingestelle Eintrag wurde gespeichert.");
                            var oModel = self.getView().getModel();
                            oModel.setProperty(path, obj);
                            mondayData.length = 0
                            //Erneut Daten für Montag aus Datenbank holen, damit gelöschter Eintrag nicht mehr angezeigt wird
                            self.getData("/GetStandardJalousienMonday").done(function(result) {
                              var data = result.d.results
                              data.map(function(eintrag, index) {
                                mondayData.push(eintrag)
                                })     
                              var oModel = new sap.ui.model.json.JSONModel({data: mondayData});
                              self.getView().setModel(oModel);
                              })
                          }  
                          else {
                            //Hier liegt weder Regelverstoß noch Überschneidung vor, kann also normal gespeichert werden
                            var oModel = self.getView().getModel();
                            oModel.setProperty(path, obj);
                            mondayData.length = 0
                            //Erneut Daten aus Datenbank holen damit Werte in richtiger Reihenfolge angezeigt werden
                            self.getData("/GetStandardJalousienMonday").done(function(result) {
                              var data = result.d.results
                              data.map(function(eintrag, index) {
                                mondayData.push(eintrag)
                                })     
                              var oModel = new sap.ui.model.json.JSONModel({data: mondayData});
                              self.getView().setModel(oModel);
                              })
                          }
                        }
                  
                    })
                    
                }

                if(obj.day == "Di"){
                  console.log("Send Tuesday")
                  var oData = {
                  'start': obj.startzeit,
                  'end': obj.endzeit, 
                  'value': parseInt(obj.wert)
                  };
                  this.sendValues(oData, "/SetJalousienStandardTuesday").done(function(result) {
                    var errorcheck = result.type
                    var mindestwert = result.min
                    var maximalwert = result.max
                    var start = result.start
                    var end = result.end
                      if (errorcheck == "0") {
                          MessageBox.error("Der Eintrag verstößt gegen eine Regel. \n Für diesen Zeitraum muss der Wert zwischen " + mindestwert + "% und " + maximalwert + "% liegen. \n Bitte versuche eine andere Einstellung!");

                          var idx = parseInt(path.substring(path.lastIndexOf('/') +1));
                          var m = self.getView().getModel();
                          var aData  = m.getProperty("/data");
                          aData.splice(idx, 1);
                          m.setProperty("/data", aData);
                      }
                      else {
                        if (errorcheck == "1") {
                          MessageBox.information("Auf Grund von Überschneidungen wurde der Eintrag von " + start + " Uhr bis " + end + " Uhr gelöscht. \n Der so eben eingestelle Eintrag wurde gespeichert.");
                          var oModel = self.getView().getModel();
                          oModel.setProperty(path, obj);
                          tuesdayData.length = 0
                          self.getData("/GetStandardJalousienTuesday").done(function(result) {
                            var data = result.d.results
                            data.map(function(eintrag, index) {
                              tuesdayData.push(eintrag)
                              })     
                            var oModel = new sap.ui.model.json.JSONModel({data: tuesdayData});
                            self.getView().setModel(oModel);
                          })
                          
                        }  
                        else {
                          var oModel = self.getView().getModel();
                          oModel.setProperty(path, obj);
                          tuesdayData.length = 0
                          self.getData("/GetStandardJalousienTuesday").done(function(result) {
                            var data = result.d.results
                            data.map(function(eintrag, index) {
                              tuesdayData.push(eintrag)
                              })     
                            var oModel = new sap.ui.model.json.JSONModel({data: tuesdayData});
                            self.getView().setModel(oModel);
                          })
                        }
                      }
                    
                  })
                }
                if(obj.day == "Mi"){
                  console.log("Send Wednesday")
                  var oData = {
                  'start': obj.startzeit,
                  'end': obj.endzeit, 
                  'value': parseInt(obj.wert)
                  };
                  this.sendValues(oData, "/SetJalousienStandardWednesday").done(function(result) {
                    var errorcheck = result.type
                    var mindestwert = result.min
                    var maximalwert = result.max
                    var start = result.start
                    var end = result.end
                      if (errorcheck == "0") {
                          MessageBox.error("Der Eintrag verstößt gegen eine Regel. \n Für diesen Zeitraum muss der Wert zwischen " + mindestwert + "% und " + maximalwert + "% liegen. \n Bitte versuche eine andere Einstellung!");

                          var idx = parseInt(path.substring(path.lastIndexOf('/') +1));
                          var m = self.getView().getModel();
                          var aData  = m.getProperty("/data");
                          aData.splice(idx, 1);
                          m.setProperty("/data", aData);
                      }
                      else {
                        if (errorcheck == "1") {
                          MessageBox.information("Auf Grund von Überschneidungen wurde der Eintrag von " + start + " Uhr bis " + end + " Uhr gelöscht. \n Der so eben eingestelle Eintrag wurde gespeichert.");
                          var oModel = self.getView().getModel();
                          oModel.setProperty(path, obj);
                          wednesdayData.length = 0
                          self.getData("/GetStandardJalousienWednesday").done(function(result) {
                            var data = result.d.results
                            data.map(function(eintrag, index) {
                              wednesdayData.push(eintrag)
                              })     
                            var oModel = new sap.ui.model.json.JSONModel({data: wednesdayData});
                            self.getView().setModel(oModel);
                          })
                        }  
                        else {
                          var oModel = self.getView().getModel();
                          oModel.setProperty(path, obj);
                          wednesdayData.length = 0
                          self.getData("/GetStandardJalousienWednesday").done(function(result) {
                            var data = result.d.results
                            data.map(function(eintrag, index) {
                              wednesdayData.push(eintrag)
                              })     
                            var oModel = new sap.ui.model.json.JSONModel({data: wednesdayData});
                            self.getView().setModel(oModel);
                          })
                        }
                      }
                
                  })
              }
                if(obj.day == "Do"){
                  console.log("Send Thursday")
                  var oData = {
                  'start': obj.startzeit,
                  'end': obj.endzeit, 
                  'value': parseInt(obj.wert)
                  };
                  this.sendValues(oData, "/SetJalousienStandardThursday").done(function(result) {
                    var errorcheck = result.type
                    var mindestwert = result.min
                    var maximalwert = result.max
                    var start = result.start
                    var end = result.end
                      if (errorcheck == "0") {
                          MessageBox.error("Der Eintrag verstößt gegen eine Regel. \n Für diesen Zeitraum muss der Wert zwischen " + mindestwert + "% und " + maximalwert + "% liegen. \n Bitte versuche eine andere Einstellung!");

                          var idx = parseInt(path.substring(path.lastIndexOf('/') +1));
                          var m = self.getView().getModel();
                          var aData  = m.getProperty("/data");
                          aData.splice(idx, 1);
                          m.setProperty("/data", aData);
                      }
                      else {
                        if (errorcheck == "1") {
                          MessageBox.information("Auf Grund von Überschneidungen wurde der Eintrag von " + start + " Uhr bis " + end + " Uhr gelöscht. \n Der so eben eingestelle Eintrag wurde gespeichert.");
                          var oModel = self.getView().getModel();
                          oModel.setProperty(path, obj);
                          thursdayData.length = 0
                          self.getData("/GetStandardJalousienThursday").done(function(result) {
                            var data = result.d.results
                            data.map(function(eintrag, index) {
                              thursdayData.push(eintrag)
                              })     
                            var oModel = new sap.ui.model.json.JSONModel({data: thursdayData});
                            self.getView().setModel(oModel);
                          })
                        }  
                        else {
                          var oModel = self.getView().getModel();
                          oModel.setProperty(path, obj);
                          thursdayData.length = 0
                          self.getData("/GetStandardJalousienThursday").done(function(result) {
                            var data = result.d.results
                            data.map(function(eintrag, index) {
                              thursdayData.push(eintrag)
                              })     
                            var oModel = new sap.ui.model.json.JSONModel({data: thursdayData});
                            self.getView().setModel(oModel);
                          })
                        }
                      }
                
                  })
              }
              if(obj.day == "Fr"){
                console.log("Send Friday")
                var oData = {
                'start': obj.startzeit,
                'end': obj.endzeit, 
                'value': parseInt(obj.wert)
                };
                this.sendValues(oData, "/SetJalousienStandardFriday").done(function(result) {
                  var errorcheck = result.type
                  var mindestwert = result.min
                  var maximalwert = result.max
                  var start = result.start
                  var end = result.end
                    if (errorcheck == "0") {
                        MessageBox.error("Der Eintrag verstößt gegen eine Regel. \n Für diesen Zeitraum muss der Wert zwischen " + mindestwert + "% und " + maximalwert + "% liegen. \n Bitte versuche eine andere Einstellung!");

                        var idx = parseInt(path.substring(path.lastIndexOf('/') +1));
                        var m = self.getView().getModel();
                        var aData  = m.getProperty("/data");
                        aData.splice(idx, 1);
                        m.setProperty("/data", aData);
                    }
                    else {
                      if (errorcheck == "1") {
                        MessageBox.information("Auf Grund von Überschneidungen wurde der Eintrag von " + start + " Uhr bis " + end + " Uhr gelöscht. \n Der so eben eingestelle Eintrag wurde gespeichert.");
                        var oModel = self.getView().getModel();
                        oModel.setProperty(path, obj);
                        fridayData.length = 0
                        self.getData("/GetStandardJalousienFriday").done(function(result) {
                            var data = result.d.results
                            data.map(function(eintrag, index) {
                              fridayData.push(eintrag)
                              })     
                            var oModel = new sap.ui.model.json.JSONModel({data: fridayData});
                            self.getView().setModel(oModel);
                          })
                      }  
                      else {
                        var oModel = self.getView().getModel();
                        oModel.setProperty(path, obj);
                        fridayData.length = 0
                        self.getData("/GetStandardJalousienFriday").done(function(result) {
                            var data = result.d.results
                            data.map(function(eintrag, index) {
                              fridayData.push(eintrag)
                              })     
                            var oModel = new sap.ui.model.json.JSONModel({data: fridayData});
                            self.getView().setModel(oModel);
                          })
                      }
                    }
              
                })
            }


              },
              //POST-Methode um Daten ins Backend zu senden
              sendValues: function(oData, url) {
                return jQuery.ajax({
                  url : url,
                  type : "POST",
                  dataType : "json",
                  async : true,
                  data : oData,
                  success : function(response){
                      //MessageToast.show(response.data.message);
                      console.log(response)
                      console.log(response.max)
                      console.log(response.min)
                      sap.ui.core.BusyIndicator.hide();
                      
                  },
                  error: function(response){
                      console.log(response);
                  }
                });
              },
              //Eintrag aus Datenbank löschen, wird bei Klicken auf Löschen aufgerufen
              removeEntry: function (oEvent) {
                var oTable = this.getView().byId("tbl");
                var path = oEvent.getSource().getBindingContext().getPath();
                var obj = oEvent.getSource().getBindingContext().getObject();
                var oModel = this.getView().getModel();

                oModel.setProperty(path, obj);
                //var selectedDay = oEvent.getParameter("item").getText()
                //MessageToast.show("Löschen Eintrag mit ID:" + obj.id)  
                console.log(obj)
                var oSegmentedButton = this.byId('SB1');
                var oSelectedItemId = oSegmentedButton.getSelectedItem();
                var oSelectedItem = Element.registry.get(oSelectedItemId);
                var selectedDay = oSelectedItem.getText()
                //Eigene Abfrage pro Tag damit richtige Route aufgerufen werden kann
                if(selectedDay == "Mo"){
                  console.log("Löschen Montag")
                  //Speichern der ID
                  var oData = {
                    'id_entry': obj.id,
                  };
                  console.log(oData)
                  //Löschen des Eintrags mit dieser ID
                  this.deleteValues(oData, "/DeleteStandardJalousienMonday")
                }
                if(selectedDay == "Di"){
                  console.log("Löschen Dienstag")
                  var oData = {
                    'id_entry': obj.id,
                  };
                  this.deleteValues(oData, "/DeleteStandardJalousienTuesday")
                }
                if(selectedDay == "Mi"){
                  var oData = {
                    'id_entry': obj.id,
                  };
                  this.deleteValues(oData, "/DeleteStandardJalousienWednesday")
              }
                if(selectedDay == "Do"){
                  var oData = {
                    'id_entry': obj.id,
                  };
                  this.deleteValues(oData, "/DeleteStandardJalousienThursday")
              }
              if(selectedDay == "Fr"){
                var oData = {
                  'id_entry': obj.id,
                };
                this.deleteValues(oData, "/DeleteStandardJalousienFriday")
              }

                var idx = parseInt(path.substring(path.lastIndexOf('/') +1));
                var m = this.getView().getModel();
                var aData  = m.getProperty("/data");
                aData.splice(idx, 1);
                m.setProperty("/data", aData);
                 
            },
            //DELETE-Methode
            deleteValues: function(oData, url) {
              jQuery.ajax({
                    url : url,
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
                })
            },
            //Auswahländerung des Wochentags
            //Wenn Wochentag geändert wird, werden die jeweiligen Daten angezeigt
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

            //Zurück-Navigation zur vorherigen Seite
            onNavBack: function(){

              var oHistory = History.getInstance();
              var sPreviousHash = oHistory.getPreviousHash();

              if (sPreviousHash !== undefined) {
                window.history.go(-1);
              } else {
                var oRouter = sap.ui.core.UIComponent.getRouterFor(this);
                oRouter.navTo("/", {}, true);
              }
            },
		});

});
        
