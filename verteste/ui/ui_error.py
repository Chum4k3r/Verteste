# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'errordialog.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_ErrorDialog(QDialog):
    # Caixa de diálogo utilizada para criação ou edição de linhas
    def __init__(self, parent=None):
        QDialog.__init__(self, parent=parent)
        self.setupUi(self)
        return

    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(418, 168)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.quitLabel = QLabel(Dialog)
        self.quitLabel.setObjectName(u"quitLabel")
        self.quitLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.quitLabel, 1, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Aten\u00e7\u00e3o!", None))
        self.label.setText("")
        self.quitLabel.setText(QCoreApplication.translate("Dialog", u"Pressione ESC para sair", None))
    # retranslateUi

