# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\dango_repo\cutting_frames\ui.ui'
#
# Created: Wed Aug 12 14:56:46 2020
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

try:
    from PySide2 import QtWidgets, QtCore
except ImportError:
    import PySide.QtGui as QtWidgets
    from PySide import QtCore


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(458, 330)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.root_ctrl_pb = QtWidgets.QPushButton(Dialog)
        self.root_ctrl_pb.setObjectName("root_ctrl_pb")
        self.horizontalLayout.addWidget(self.root_ctrl_pb)
        self.root_ctrl_le = QtWidgets.QLineEdit(Dialog)
        self.root_ctrl_le.setReadOnly(True)
        self.root_ctrl_le.setObjectName("root_ctrl_le")
        self.horizontalLayout.addWidget(self.root_ctrl_le)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.track_ctrl_pb = QtWidgets.QPushButton(Dialog)
        self.track_ctrl_pb.setObjectName("track_ctrl_pb")
        self.horizontalLayout_4.addWidget(self.track_ctrl_pb)
        self.track_ctrl_le = QtWidgets.QLineEdit(Dialog)
        self.track_ctrl_le.setReadOnly(True)
        self.track_ctrl_le.setObjectName("track_ctrl_le")
        self.horizontalLayout_4.addWidget(self.track_ctrl_le)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.all_controls_pb = QtWidgets.QPushButton(Dialog)
        self.all_controls_pb.setEnabled(False)
        self.all_controls_pb.setObjectName("all_controls_pb")
        self.horizontalLayout_2.addWidget(self.all_controls_pb)
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout_2.addWidget(self.textEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.spinBox = QtWidgets.QSpinBox(Dialog)
        self.spinBox.setValue(2)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout_3.addWidget(self.spinBox)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.bake_pb = QtWidgets.QPushButton(Dialog)
        self.bake_pb.setObjectName("bake_pb")
        self.horizontalLayout_5.addWidget(self.bake_pb)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle("CuttingFramesTool")
        self.root_ctrl_pb.setText("Root Control  >>")
        self.track_ctrl_pb.setText("Tracking(Hip)>>")
        self.all_controls_pb.setText("ControlsToBake  >>")
        self.label.setText("Set Key on Every")
        self.label_2.setText("frames.")
        self.bake_pb.setText("bake")

