# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'listdialog.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_ListDialog(QDialog):
    # Caixa de diálogo utilizada na criação ou alteração de listas
    def __init__(self, parent=None):
        QDialog.__init__(self, parent=parent)
        self.setupUi(self)
        return

    def reset(self):
        self.nameLineEdit.setText("")
        return

    def setupUi(self, ListDialog):
        if not ListDialog.objectName():
            ListDialog.setObjectName(u"ListDialog")
        ListDialog.resize(400, 71)
        self.formLayout = QFormLayout(ListDialog)
        self.formLayout.setObjectName(u"formLayout")
        self.nameLabel = QLabel(ListDialog)
        self.nameLabel.setObjectName(u"nameLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.nameLabel)

        self.nameLineEdit = QLineEdit(ListDialog)
        self.nameLineEdit.setObjectName(u"nameLineEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.nameLineEdit)

        self.buttonBox = QDialogButtonBox(ListDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.formLayout.setWidget(1, QFormLayout.SpanningRole, self.buttonBox)


        self.retranslateUi(ListDialog)
        self.buttonBox.accepted.connect(ListDialog.accept)
        self.buttonBox.rejected.connect(ListDialog.reject)

        QMetaObject.connectSlotsByName(ListDialog)
    # setupUi

    def retranslateUi(self, ListDialog):
        ListDialog.setWindowTitle(QCoreApplication.translate("ListDialog", u"Dialog", None))
        self.nameLabel.setText(QCoreApplication.translate("ListDialog", u"Nome", None))
    # retranslateUi

