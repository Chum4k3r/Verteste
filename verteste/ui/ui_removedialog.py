# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'removedialog.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_RemoveDialog(QDialog):
    # Caixa de diálogo utilizada para remover listas e linhas
    def __init__(self, parent=None):
        QDialog.__init__(self, parent=parent)
        self.setupUi(self)
        return

    def reset(self):
        self.tableView.setModel(QStandardItemModel())
        return

    def setupUi(self, RemoveDialog):
        if not RemoveDialog.objectName():
            RemoveDialog.setObjectName(u"RemoveDialog")
        RemoveDialog.resize(400, 300)
        self.gridLayout = QGridLayout(RemoveDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.buttonBox = QDialogButtonBox(RemoveDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.tableView = QTableView(RemoveDialog)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableView.setSelectionMode(QAbstractItemView.MultiSelection)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.gridLayout.addWidget(self.tableView, 0, 0, 1, 1)


        self.retranslateUi(RemoveDialog)
        self.buttonBox.accepted.connect(RemoveDialog.accept)
        self.buttonBox.rejected.connect(RemoveDialog.reject)

        QMetaObject.connectSlotsByName(RemoveDialog)
    # setupUi

    def retranslateUi(self, RemoveDialog):
        RemoveDialog.setWindowTitle(QCoreApplication.translate("RemoveDialog", u"Dialog", None))
    # retranslateUi

