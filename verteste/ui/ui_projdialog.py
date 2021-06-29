# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'projdialog.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_ProjectDialog(QDialog):
    # Caixa de diálogo utilizada na criação ou edição de projetos
    def __init__(self, parent=None):
        QDialog.__init__(self, parent=parent)
        self.setupUi(self)
        return

    def reset(self):
        self.nameLineEdit.setText("")
        self.descrTextEdit.setText("")
        return

    def setupUi(self, ProjectDialog):
        if not ProjectDialog.objectName():
            ProjectDialog.setObjectName(u"ProjectDialog")
        ProjectDialog.resize(286, 300)
        self.formLayout = QFormLayout(ProjectDialog)
        self.formLayout.setObjectName(u"formLayout")
        self.nameLabel = QLabel(ProjectDialog)
        self.nameLabel.setObjectName(u"nameLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.nameLabel)

        self.nameLineEdit = QLineEdit(ProjectDialog)
        self.nameLineEdit.setObjectName(u"nameLineEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.nameLineEdit)

        self.descrLabel = QLabel(ProjectDialog)
        self.descrLabel.setObjectName(u"descrLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.descrLabel)

        self.descrTextEdit = QTextEdit(ProjectDialog)
        self.descrTextEdit.setObjectName(u"descrTextEdit")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.descrTextEdit)

        self.buttonBox = QDialogButtonBox(ProjectDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.formLayout.setWidget(2, QFormLayout.SpanningRole, self.buttonBox)

#if QT_CONFIG(shortcut)
        self.nameLabel.setBuddy(self.nameLineEdit)
        self.descrLabel.setBuddy(self.descrTextEdit)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(ProjectDialog)
        self.buttonBox.accepted.connect(ProjectDialog.accept)
        self.buttonBox.rejected.connect(ProjectDialog.reject)

        QMetaObject.connectSlotsByName(ProjectDialog)
    # setupUi

    def retranslateUi(self, ProjectDialog):
        ProjectDialog.setWindowTitle(QCoreApplication.translate("ProjectDialog", u"Dialog", None))
        self.nameLabel.setText(QCoreApplication.translate("ProjectDialog", u"Nome", None))
        self.descrLabel.setText(QCoreApplication.translate("ProjectDialog", u"Descri\u00e7\u00e3o", None))
    # retranslateUi

