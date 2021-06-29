# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'linedialog.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore



class Ui_LineDialog(QDialog):
    # Caixa de diálogo utilizada para criação ou edição de linhas
    def __init__(self, parent=None):
        QDialog.__init__(self, parent=parent)
        self.setupUi(self)
        return

    def reset(self):
        self.nameLineEdit.setText("")
        self.tagLineEdit.setText("")
        self.typeComboBox.setCurrentIndex(0)
        self.signalComboBox.setCurrentIndex(0)
        self.pidLineEdit.setText("")
        return

    def setupUi(self, LineDialog):
        if not LineDialog.objectName():
            LineDialog.setObjectName(u"LineDialog")
        LineDialog.resize(311, 187)
        self.formLayout = QFormLayout(LineDialog)
        self.formLayout.setObjectName(u"formLayout")
        self.nameLabel = QLabel(LineDialog)
        self.nameLabel.setObjectName(u"nameLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.nameLabel)

        self.nameLineEdit = QLineEdit(LineDialog)
        self.nameLineEdit.setObjectName(u"nameLineEdit")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.nameLineEdit)

        self.tagLabel = QLabel(LineDialog)
        self.tagLabel.setObjectName(u"tagLabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.tagLabel)

        self.tagLineEdit = QLineEdit(LineDialog)
        self.tagLineEdit.setObjectName(u"tagLineEdit")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.tagLineEdit)

        self.typeLabel = QLabel(LineDialog)
        self.typeLabel.setObjectName(u"typeLabel")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.typeLabel)

        self.typeComboBox = QComboBox(LineDialog)
        self.typeComboBox.addItem("")
        self.typeComboBox.addItem("")
        self.typeComboBox.setObjectName(u"typeComboBox")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.typeComboBox)

        self.signalLabel = QLabel(LineDialog)
        self.signalLabel.setObjectName(u"signalLabel")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.signalLabel)

        self.signalComboBox = QComboBox(LineDialog)
        self.signalComboBox.addItem("")
        self.signalComboBox.addItem("")
        self.signalComboBox.setObjectName(u"signalComboBox")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.signalComboBox)

        self.pidLabel = QLabel(LineDialog)
        self.pidLabel.setObjectName(u"pidLabel")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.pidLabel)

        self.pidLineEdit = QLineEdit(LineDialog)
        self.pidLineEdit.setObjectName(u"pidLineEdit")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.pidLineEdit)

        self.buttonBox = QDialogButtonBox(LineDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.formLayout.setWidget(6, QFormLayout.SpanningRole, self.buttonBox)

        self.idComboBox = QComboBox(LineDialog)
        self.idComboBox.setObjectName(u"idComboBox")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.idComboBox)

        self.idLabel = QLabel(LineDialog)
        self.idLabel.setObjectName(u"idLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.idLabel)

#if QT_CONFIG(shortcut)
        self.nameLabel.setBuddy(self.nameLineEdit)
        self.tagLabel.setBuddy(self.tagLineEdit)
        self.typeLabel.setBuddy(self.typeComboBox)
        self.signalLabel.setBuddy(self.signalComboBox)
        self.pidLabel.setBuddy(self.pidLineEdit)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(LineDialog)
        self.buttonBox.accepted.connect(LineDialog.accept)
        self.buttonBox.rejected.connect(LineDialog.reject)

        QMetaObject.connectSlotsByName(LineDialog)
    # setupUi

    def retranslateUi(self, LineDialog):
        LineDialog.setWindowTitle(QCoreApplication.translate("LineDialog", u"Dialog", None))
        self.nameLabel.setText(QCoreApplication.translate("LineDialog", u"Nome", None))
        self.tagLabel.setText(QCoreApplication.translate("LineDialog", u"TAG", None))
        self.typeLabel.setText(QCoreApplication.translate("LineDialog", u"Tipo", None))
        self.typeComboBox.setItemText(0, QCoreApplication.translate("LineDialog", u"Causa", None))
        self.typeComboBox.setItemText(1, QCoreApplication.translate("LineDialog", u"Efeito", None))

        self.signalLabel.setText(QCoreApplication.translate("LineDialog", u"Sinal", None))
        self.signalComboBox.setItemText(0, QCoreApplication.translate("LineDialog", u"Digital", None))
        self.signalComboBox.setItemText(1, QCoreApplication.translate("LineDialog", u"Anal\u00f3gico", None))

        self.pidLabel.setText(QCoreApplication.translate("LineDialog", u"PID", None))
        self.idLabel.setText(QCoreApplication.translate("LineDialog", u"ID", None))
    # retranslateUi

