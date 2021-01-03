# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'recipe_list_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_recipeListDialog(object):
    def setupUi(self, recipeListDialog):
        recipeListDialog.setObjectName("recipeListDialog")
        recipeListDialog.setWindowModality(QtCore.Qt.WindowModal)
        recipeListDialog.resize(250, 350)
        recipeListDialog.setMinimumSize(QtCore.QSize(250, 350))
        recipeListDialog.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(recipeListDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(recipeListDialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.searchTextBox = QtWidgets.QLineEdit(recipeListDialog)
        self.searchTextBox.setObjectName("searchTextBox")
        self.verticalLayout.addWidget(self.searchTextBox)
        self.recipesList = QtWidgets.QTreeView(recipeListDialog)
        self.recipesList.setObjectName("recipesList")
        self.verticalLayout.addWidget(self.recipesList)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.editButton = QtWidgets.QPushButton(recipeListDialog)
        self.editButton.setEnabled(False)
        self.editButton.setObjectName("editButton")
        self.horizontalLayout.addWidget(self.editButton)
        self.deleteButton = QtWidgets.QPushButton(recipeListDialog)
        self.deleteButton.setEnabled(False)
        self.deleteButton.setObjectName("deleteButton")
        self.horizontalLayout.addWidget(self.deleteButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(recipeListDialog)
        QtCore.QMetaObject.connectSlotsByName(recipeListDialog)

    def retranslateUi(self, recipeListDialog):
        _translate = QtCore.QCoreApplication.translate
        recipeListDialog.setWindowTitle(_translate("recipeListDialog", "Recipe Editor"))
        self.label.setText(_translate("recipeListDialog", "Select a recipe..."))
        self.searchTextBox.setToolTip(_translate("recipeListDialog", "Search for Items"))
        self.searchTextBox.setPlaceholderText(_translate("recipeListDialog", "Search..."))
        self.editButton.setText(_translate("recipeListDialog", "Edit..."))
        self.deleteButton.setText(_translate("recipeListDialog", "Delete"))
