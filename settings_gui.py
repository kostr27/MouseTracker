# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Lenovo\PycharmProjects\MouseTracker\settings.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_settingsDialog(object):
    def setupUi(self, settingsDialog):
        settingsDialog.setObjectName("settingsDialog")
        settingsDialog.resize(231, 173)
        settingsDialog.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(settingsDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.teleportBox = QtWidgets.QCheckBox(settingsDialog)
        self.teleportBox.setObjectName("teleportBox")
        self.verticalLayout.addWidget(self.teleportBox)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(settingsDialog)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.delayEdit = QtWidgets.QLineEdit(settingsDialog)
        self.delayEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.delayEdit.setObjectName("delayEdit")
        self.horizontalLayout_3.addWidget(self.delayEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(settingsDialog)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.tickEdit = QtWidgets.QLineEdit(settingsDialog)
        self.tickEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tickEdit.setObjectName("tickEdit")
        self.horizontalLayout_2.addWidget(self.tickEdit)
        self.label_2 = QtWidgets.QLabel(settingsDialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.okButton = QtWidgets.QPushButton(settingsDialog)
        self.okButton.setObjectName("okButton")
        self.horizontalLayout.addWidget(self.okButton)
        self.cancelButton = QtWidgets.QPushButton(settingsDialog)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout.addWidget(self.cancelButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(settingsDialog)
        self.cancelButton.clicked.connect(settingsDialog.close)
        QtCore.QMetaObject.connectSlotsByName(settingsDialog)

    def retranslateUi(self, settingsDialog):
        _translate = QtCore.QCoreApplication.translate
        settingsDialog.setWindowTitle(_translate("settingsDialog", "Настройки"))
        self.teleportBox.setText(_translate("settingsDialog", "Перенос курсора"))
        self.label_3.setText(_translate("settingsDialog", "Задержка"))
        self.delayEdit.setText(_translate("settingsDialog", "100"))
        self.label.setText(_translate("settingsDialog", "Частота снятия"))
        self.tickEdit.setText(_translate("settingsDialog", "10"))
        self.label_2.setText(_translate("settingsDialog", "мс"))
        self.okButton.setText(_translate("settingsDialog", "Ok"))
        self.cancelButton.setText(_translate("settingsDialog", "Отмена"))

