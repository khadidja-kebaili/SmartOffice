/*global QUnit*/

sap.ui.define([
	"comquantosolutionsui/smartoffice/controller/SmartOffice.controller"
], function (Controller) {
	"use strict";

	QUnit.module("SmartOffice Controller");

	QUnit.test("I should test the SmartOffice controller", function (assert) {
		var oAppController = new Controller();
		oAppController.onInit();
		assert.ok(oAppController);
	});

});
