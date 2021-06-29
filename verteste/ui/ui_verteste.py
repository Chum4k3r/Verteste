# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'verteste.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore
from .ui_projdialog import Ui_ProjectDialog
from .ui_listdialog import Ui_ListDialog
from .ui_linedialog import Ui_LineDialog
from .ui_removedialog import Ui_RemoveDialog
from .ui_help import Ui_HelpDialog
from .ui_error import Ui_ErrorDialog
from .ui_about import Ui_AboutDialog


class Ui_Verteste(QMainWindow):
    # Janela principal do programa,
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.projDialog = Ui_ProjectDialog(self)
        self.listDialog = Ui_ListDialog(self)
        self.lineDialog = Ui_LineDialog(self)
        self.removeDialog = Ui_RemoveDialog(self)
        self.errorDialog = Ui_ErrorDialog(self)
        self.helpDialog = Ui_HelpDialog(self)
        self.aboutDialog = Ui_AboutDialog(self)
        return

    def setupUi(self, Verteste):
        if not Verteste.objectName():
            Verteste.setObjectName(u"Verteste")
        Verteste.resize(1063, 626)
        font = QFont()
        font.setFamilies([u"Sans Serif"])
        Verteste.setFont(font)
        self.actionNovoProjeto = QAction(Verteste)
        self.actionNovoProjeto.setObjectName(u"actionNovoProjeto")
        self.actionAbrirProjeto = QAction(Verteste)
        self.actionAbrirProjeto.setObjectName(u"actionAbrirProjeto")
        self.actionSalvarProjeto = QAction(Verteste)
        self.actionSalvarProjeto.setObjectName(u"actionSalvarProjeto")
        self.actionNovaLista = QAction(Verteste)
        self.actionNovaLista.setObjectName(u"actionNovaLista")
        self.actionInserirLinha = QAction(Verteste)
        self.actionInserirLinha.setObjectName(u"actionInserirLinha")
        self.actionRemoverLinha = QAction(Verteste)
        self.actionRemoverLinha.setObjectName(u"actionRemoverLinha")
        self.actionRemoverLista = QAction(Verteste)
        self.actionRemoverLista.setObjectName(u"actionRemoverLista")
        self.actionSair = QAction(Verteste)
        self.actionSair.setObjectName(u"actionSair")
        self.actionAlterarLinha = QAction(Verteste)
        self.actionAlterarLinha.setObjectName(u"actionAlterarLinha")
        self.actionSobre = QAction(Verteste)
        self.actionSobre.setObjectName(u"actionSobre")
        self.actionManual = QAction(Verteste)
        self.actionManual.setObjectName(u"actionManual")
        self.actionAlterarProjeto = QAction(Verteste)
        self.actionAlterarProjeto.setObjectName(u"actionAlterarProjeto")
        self.actionAlterarLista = QAction(Verteste)
        self.actionAlterarLista.setObjectName(u"actionAlterarLista")
        self.actionHistorico = QAction(Verteste)
        self.actionHistorico.setObjectName(u"actionHistorico")
        self.actionFecharProjeto = QAction(Verteste)
        self.actionFecharProjeto.setObjectName(u"actionFecharProjeto")
        self.centralwidget = QWidget(Verteste)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.projFrame = QFrame(self.centralwidget)
        self.projFrame.setObjectName(u"projFrame")
        self.projFrame.setFrameShape(QFrame.StyledPanel)
        self.projFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.projFrame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.projComboBox = QComboBox(self.projFrame)
        self.projComboBox.setObjectName(u"projComboBox")

        self.gridLayout.addWidget(self.projComboBox, 0, 1, 1, 1)

        self.projLabel = QLabel(self.projFrame)
        self.projLabel.setObjectName(u"projLabel")

        self.gridLayout.addWidget(self.projLabel, 0, 0, 1, 1)

        self.projTimeLabel = QLabel(self.projFrame)
        self.projTimeLabel.setObjectName(u"projTimeLabel")

        self.gridLayout.addWidget(self.projTimeLabel, 2, 0, 1, 1)

        self.projIdLabel = QLabel(self.projFrame)
        self.projIdLabel.setObjectName(u"projIdLabel")

        self.gridLayout.addWidget(self.projIdLabel, 1, 0, 1, 1)

        self.projTreeView = QTreeView(self.projFrame)
        self.projTreeView.setObjectName(u"projTreeView")
        self.projTreeView.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.gridLayout.addWidget(self.projTreeView, 7, 0, 1, 2)

        self.projDescrLabel = QLabel(self.projFrame)
        self.projDescrLabel.setObjectName(u"projDescrLabel")

        self.gridLayout.addWidget(self.projDescrLabel, 3, 0, 1, 1)

        self.projIdLineEdit = QLineEdit(self.projFrame)
        self.projIdLineEdit.setObjectName(u"projIdLineEdit")
        self.projIdLineEdit.setReadOnly(True)

        self.gridLayout.addWidget(self.projIdLineEdit, 1, 1, 1, 1)

        self.projTimeLineEdit = QLineEdit(self.projFrame)
        self.projTimeLineEdit.setObjectName(u"projTimeLineEdit")
        self.projTimeLineEdit.setReadOnly(True)

        self.gridLayout.addWidget(self.projTimeLineEdit, 2, 1, 1, 1)

        self.projListsLabel = QLabel(self.projFrame)
        self.projListsLabel.setObjectName(u"projListsLabel")

        self.gridLayout.addWidget(self.projListsLabel, 5, 0, 1, 2)

        self.projDescrTextEdit = QTextEdit(self.projFrame)
        self.projDescrTextEdit.setObjectName(u"projDescrTextEdit")
        self.projDescrTextEdit.setReadOnly(True)

        self.gridLayout.addWidget(self.projDescrTextEdit, 4, 0, 1, 2)


        self.gridLayout_3.addWidget(self.projFrame, 0, 0, 1, 1, Qt.AlignLeft)

        self.listFrame = QFrame(self.centralwidget)
        self.listFrame.setObjectName(u"listFrame")
        self.listFrame.setFrameShape(QFrame.StyledPanel)
        self.listFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.listFrame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.listLabel = QLabel(self.listFrame)
        self.listLabel.setObjectName(u"listLabel")

        self.gridLayout_2.addWidget(self.listLabel, 0, 0, 1, 1)

        self.listIdLineEdit = QLineEdit(self.listFrame)
        self.listIdLineEdit.setObjectName(u"listIdLineEdit")
        self.listIdLineEdit.setReadOnly(True)

        self.gridLayout_2.addWidget(self.listIdLineEdit, 1, 1, 1, 1)

        self.listIdLabel = QLabel(self.listFrame)
        self.listIdLabel.setObjectName(u"listIdLabel")

        self.gridLayout_2.addWidget(self.listIdLabel, 1, 0, 1, 1)

        self.listTimeLineEdit = QLineEdit(self.listFrame)
        self.listTimeLineEdit.setObjectName(u"listTimeLineEdit")
        self.listTimeLineEdit.setReadOnly(True)

        self.gridLayout_2.addWidget(self.listTimeLineEdit, 2, 1, 1, 1)

        self.listComboBox = QComboBox(self.listFrame)
        self.listComboBox.setObjectName(u"listComboBox")

        self.gridLayout_2.addWidget(self.listComboBox, 0, 1, 1, 1)

        self.listTimeLabel = QLabel(self.listFrame)
        self.listTimeLabel.setObjectName(u"listTimeLabel")

        self.gridLayout_2.addWidget(self.listTimeLabel, 2, 0, 1, 1)

        self.listTableView = QTableView(self.listFrame)
        self.listTableView.setObjectName(u"listTableView")
        self.listTableView.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.gridLayout_2.addWidget(self.listTableView, 4, 0, 1, 2)

        self.listLinesLabel = QLabel(self.listFrame)
        self.listLinesLabel.setObjectName(u"listLinesLabel")

        self.gridLayout_2.addWidget(self.listLinesLabel, 3, 0, 1, 2)


        self.gridLayout_3.addWidget(self.listFrame, 0, 1, 1, 1)

        Verteste.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Verteste)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1063, 20))
        self.menuArquivo = QMenu(self.menubar)
        self.menuArquivo.setObjectName(u"menuArquivo")
        self.menuEditar = QMenu(self.menubar)
        self.menuEditar.setObjectName(u"menuEditar")
        self.menuAjuda = QMenu(self.menubar)
        self.menuAjuda.setObjectName(u"menuAjuda")
        Verteste.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Verteste)
        self.statusbar.setObjectName(u"statusbar")
        Verteste.setStatusBar(self.statusbar)
#if QT_CONFIG(shortcut)
        self.projLabel.setBuddy(self.projComboBox)
        self.projTimeLabel.setBuddy(self.projTimeLineEdit)
        self.projIdLabel.setBuddy(self.projIdLineEdit)
        self.projDescrLabel.setBuddy(self.projDescrTextEdit)
        self.projListsLabel.setBuddy(self.projTreeView)
        self.listLabel.setBuddy(self.listComboBox)
        self.listIdLabel.setBuddy(self.listIdLineEdit)
        self.listTimeLabel.setBuddy(self.listTimeLineEdit)
        self.listLinesLabel.setBuddy(self.listTableView)
#endif // QT_CONFIG(shortcut)

        self.menubar.addAction(self.menuArquivo.menuAction())
        self.menubar.addAction(self.menuEditar.menuAction())
        self.menubar.addAction(self.menuAjuda.menuAction())
        self.menuArquivo.addAction(self.actionNovoProjeto)
        self.menuArquivo.addAction(self.actionAbrirProjeto)
        self.menuArquivo.addAction(self.actionAlterarProjeto)
        self.menuArquivo.addAction(self.actionSalvarProjeto)
        self.menuArquivo.addAction(self.actionFecharProjeto)
        self.menuArquivo.addSeparator()
        self.menuArquivo.addAction(self.actionSair)
        self.menuEditar.addAction(self.actionNovaLista)
        self.menuEditar.addAction(self.actionAlterarLista)
        self.menuEditar.addAction(self.actionRemoverLista)
        self.menuEditar.addSeparator()
        self.menuEditar.addAction(self.actionInserirLinha)
        self.menuEditar.addAction(self.actionAlterarLinha)
        self.menuEditar.addAction(self.actionRemoverLinha)
        self.menuAjuda.addAction(self.actionSobre)
        self.menuAjuda.addAction(self.actionManual)
        self.menuAjuda.addAction(self.actionHistorico)

        self.retranslateUi(Verteste)

        QMetaObject.connectSlotsByName(Verteste)
    # setupUi

    def retranslateUi(self, Verteste):
        Verteste.setWindowTitle(QCoreApplication.translate("Verteste", u"Verteste", None))
        self.actionNovoProjeto.setText(QCoreApplication.translate("Verteste", u"Novo projeto", None))
#if QT_CONFIG(shortcut)
        self.actionNovoProjeto.setShortcut(QCoreApplication.translate("Verteste", u"Ctrl+Shift+N", None))
#endif // QT_CONFIG(shortcut)
        self.actionAbrirProjeto.setText(QCoreApplication.translate("Verteste", u"Abrir projeto", None))
#if QT_CONFIG(shortcut)
        self.actionAbrirProjeto.setShortcut(QCoreApplication.translate("Verteste", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionSalvarProjeto.setText(QCoreApplication.translate("Verteste", u"Salvar projeto", None))
#if QT_CONFIG(shortcut)
        self.actionSalvarProjeto.setShortcut(QCoreApplication.translate("Verteste", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionNovaLista.setText(QCoreApplication.translate("Verteste", u"Nova lista", None))
#if QT_CONFIG(shortcut)
        self.actionNovaLista.setShortcut(QCoreApplication.translate("Verteste", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.actionInserirLinha.setText(QCoreApplication.translate("Verteste", u"Inserir linha", None))
#if QT_CONFIG(shortcut)
        self.actionInserirLinha.setShortcut(QCoreApplication.translate("Verteste", u"Ctrl+I", None))
#endif // QT_CONFIG(shortcut)
        self.actionRemoverLinha.setText(QCoreApplication.translate("Verteste", u"Remover linha", None))
#if QT_CONFIG(shortcut)
        self.actionRemoverLinha.setShortcut(QCoreApplication.translate("Verteste", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
        self.actionRemoverLista.setText(QCoreApplication.translate("Verteste", u"Remover lista", None))
#if QT_CONFIG(shortcut)
        self.actionRemoverLista.setShortcut(QCoreApplication.translate("Verteste", u"Ctrl+D", None))
#endif // QT_CONFIG(shortcut)
        self.actionSair.setText(QCoreApplication.translate("Verteste", u"Sair", None))
#if QT_CONFIG(shortcut)
        self.actionSair.setShortcut(QCoreApplication.translate("Verteste", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.actionAlterarLinha.setText(QCoreApplication.translate("Verteste", u"Alterar linha", None))
#if QT_CONFIG(shortcut)
        self.actionAlterarLinha.setShortcut(QCoreApplication.translate("Verteste", u"Ctrl+E", None))
#endif // QT_CONFIG(shortcut)
        self.actionSobre.setText(QCoreApplication.translate("Verteste", u"Sobre", None))
#if QT_CONFIG(shortcut)
        self.actionSobre.setShortcut(QCoreApplication.translate("Verteste", u"Ctrl+Shift+B", None))
#endif // QT_CONFIG(shortcut)
        self.actionManual.setText(QCoreApplication.translate("Verteste", u"Manual", None))
#if QT_CONFIG(shortcut)
        self.actionManual.setShortcut(QCoreApplication.translate("Verteste", u"Ctrl+H", None))
#endif // QT_CONFIG(shortcut)
        self.actionAlterarProjeto.setText(QCoreApplication.translate("Verteste", u"Alterar projeto", None))
#if QT_CONFIG(shortcut)
        self.actionAlterarProjeto.setShortcut(QCoreApplication.translate("Verteste", u"Ctrl+Shift+E", None))
#endif // QT_CONFIG(shortcut)
        self.actionAlterarLista.setText(QCoreApplication.translate("Verteste", u"Alterar lista", None))
#if QT_CONFIG(shortcut)
        self.actionAlterarLista.setShortcut(QCoreApplication.translate("Verteste", u"Ctrl+A", None))
#endif // QT_CONFIG(shortcut)
        self.actionHistorico.setText(QCoreApplication.translate("Verteste", u"Hist\u00f3rico", None))
#if QT_CONFIG(shortcut)
        self.actionHistorico.setShortcut(QCoreApplication.translate("Verteste", u"Ctrl+Shift+H", None))
#endif // QT_CONFIG(shortcut)
        self.actionFecharProjeto.setText(QCoreApplication.translate("Verteste", u"Fechar projeto", None))
#if QT_CONFIG(shortcut)
        self.actionFecharProjeto.setShortcut(QCoreApplication.translate("Verteste", u"Ctrl+Shift+C", None))
#endif // QT_CONFIG(shortcut)
        self.projLabel.setText(QCoreApplication.translate("Verteste", u"Projeto ativo", None))
        self.projTimeLabel.setText(QCoreApplication.translate("Verteste", u"Criado em", None))
        self.projIdLabel.setText(QCoreApplication.translate("Verteste", u"ID", None))
        self.projDescrLabel.setText(QCoreApplication.translate("Verteste", u"Descri\u00e7\u00e3o", None))
        self.projListsLabel.setText(QCoreApplication.translate("Verteste", u"Listas", None))
        self.listLabel.setText(QCoreApplication.translate("Verteste", u"Lista ativa", None))
        self.listIdLabel.setText(QCoreApplication.translate("Verteste", u"ID", None))
        self.listTimeLabel.setText(QCoreApplication.translate("Verteste", u"Criado em", None))
        self.listLinesLabel.setText(QCoreApplication.translate("Verteste", u"Linhas", None))
        self.menuArquivo.setTitle(QCoreApplication.translate("Verteste", u"Arquivo", None))
        self.menuEditar.setTitle(QCoreApplication.translate("Verteste", u"Editar", None))
        self.menuAjuda.setTitle(QCoreApplication.translate("Verteste", u"Ajuda", None))
    # retranslateUi

