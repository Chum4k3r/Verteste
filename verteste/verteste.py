# This Python file uses the following encoding: utf-8
import os
import json
from PySide6.QtCore import QObject, Slot, QModelIndex
from PySide6.QtWidgets import QFileDialog
try:
    from .model import ProjectsModel, ListsModel, LinesModel
    from .ui import Ui_Verteste
except ImportError:
    from model import ProjectsModel, ListsModel, LinesModel
    from ui import Ui_Verteste


class Verteste(QObject):
    # Objeto principal do programa, responsável por atuar como
    # "controlador" do modelo e da visualização.
    # Possui a lógica de funcionamento entre GUI e modelos

    @staticmethod
    def connect_signals_and_slots(gui: Ui_Verteste, main: QObject):
        # Project logics
        gui.actionNovoProjeto.triggered.connect(
            main.on_actionNovoProjeto_triggered)
        gui.actionSalvarProjeto.triggered.connect(
            main.on_actionSalvarProjeto_triggered)
        gui.actionAbrirProjeto.triggered.connect(
            main.on_actionAbrirProjeto_triggered)
        gui.actionAlterarProjeto.triggered.connect(
            main.on_actionAlterarProjeto_triggered)
        gui.actionFecharProjeto.triggered.connect(
            main.on_actionFecharProjeto_triggered)
        gui.projDialog.accepted.connect(main.on_projDialog_accepted)
        gui.projDialog.rejected.connect(main.on_projDialog_rejected)
        gui.projComboBox.currentIndexChanged.connect(
            main.on_projComboBox_currentChanged)
        gui.projComboBox.textActivated.connect(
            main.on_projComboBox_currentChanged)
        gui.projTreeView.doubleClicked.connect(
            main.on_projTreeView_doubleClicked)

#        # List logics
        gui.actionNovaLista.triggered.connect(
            main.on_actionNovaLista_triggered)
        gui.actionAlterarLista.triggered.connect(
            main.on_actionAlterarLista_triggered)
        gui.actionRemoverLista.triggered.connect(
            main.on_actionRemoverLista_triggered)
        gui.listDialog.accepted.connect(
            main.on_listDialog_accepted)
        gui.listDialog.rejected.connect(
            main.on_listDialog_rejected)
        gui.listComboBox.currentIndexChanged.connect(
            main.on_listComboBox_currentChanged)
        gui.listComboBox.currentTextChanged.connect(
            main.on_listComboBox_currentChanged)
        gui.listTableView.doubleClicked.connect(
            main.on_listTableView_doubleClicked)

#        # Line logics
        gui.actionInserirLinha.triggered.connect(
            main.on_actionInserirLinha_triggered)
        gui.actionAlterarLinha.triggered.connect(
            main.on_actionAlterarLinha_triggered)
        gui.actionRemoverLinha.triggered.connect(
            main.on_actionRemoverLinha_triggered)
        gui.lineDialog.idComboBox.currentIndexChanged.connect(
            main.on_lineDialog_idComboBox_currentChanged)
        gui.lineDialog.accepted.connect(main.on_lineDialog_accepted)
        gui.lineDialog.rejected.connect(main.on_lineDialog_rejected)

        # Remove logic
        gui.removeDialog.accepted.connect(main.on_removeDialog_accepted)
        gui.removeDialog.rejected.connect(gui.removeDialog.reset)

        # Other actions logic
        gui.actionManual.triggered.connect(
            main.on_actionManual_triggered)
#        gui.actionHistorico.triggered.connect(
#            main.on_actionHistorico_triggered)
        gui.actionSobre.triggered.connect(gui.aboutDialog.open)
        return

    def __init__(self, ui: Ui_Verteste):
        QObject.__init__(self)
        self.ui = ui
        self.projects = ProjectsModel()
        self.ui.projComboBox.setModel(self.projects)
        self.ui.projComboBox.setModelColumn(1)
        Verteste.connect_signals_and_slots(self.ui, self)
        return

    @property
    def activeProject(self):  # Facilitador de acesso ao ProjectItem ativo
        if self.projects.rowCount() < 1:
            return
        return self.projects[self.ui.projComboBox.currentIndex()]

    @Slot()
    def on_actionNovoProjeto_triggered(self):
        # inclui novo projeto e
        # define novo projeto como ativo
        self.ui.projDialog.setWindowTitle("Novo projeto")
        self.projects.new('New', '')
        self.ui.projComboBox.setCurrentIndex(self.projects.rowCount()-1)
        self.ui.projDialog.open()
        return

    @Slot()
    def on_actionSalvarProjeto_triggered(self):
        if self.projects.rowCount() < 1:
            return
        # Salva projeto ativo
        defaultname = os.getcwd() + os.sep + self.activeProject.name + '.json'
        filename = QFileDialog.getSaveFileName(self.ui, "Salvar Projeto",
                                               defaultname,
                                               "Arquivos JSON (*.json)")
        if filename[0] == '' or filename[0][-4:].upper() != 'JSON':
            return
        with open(filename[0], 'w') as file:
            json.dump(self.activeProject.toDict(), file)
        return

    @Slot()
    def on_actionAbrirProjeto_triggered(self):
        # Seleciona arquivo para abrir
        filename = QFileDialog.getOpenFileName(self.ui, "Abrir Projeto",
                                               os.getcwd(),
                                               "Arquivos JSON (*.json)")
        if filename[0] == '' or filename[0][-4:].upper() != 'JSON':
            return
        with open(filename[0], 'r') as file:
            # Reconstrói árvore de projeto, listas
            # e linhas a partir dos dicionários
            projdata = json.load(file)
            lists = projdata.pop('lists')
            self.projects.add(**projdata)
            for listdata in lists:
                lines = listdata.pop('lines')
                self.projects[-1].lists.add(**listdata)
                for linedata in lines:
                    self.projects[-1].lists[-1].lines.add(**linedata)
        self.ui.projComboBox.setCurrentIndex(self.projects.rowCount() - 1)
        return

    @Slot()
    def on_actionAlterarProjeto_triggered(self):
        if self.projects.rowCount() < 1:
            return
        # Carrega informações do projeto ativo na caixa de diálogo
        # Para edição
        dialog = self.ui.projDialog
        dialog.setWindowTitle("Alterar projeto")
        dialog.nameLineEdit.setText(self.activeProject.name)
        dialog.descrTextEdit.setText(self.activeProject.description)
        dialog.open()
        return

    @Slot()
    def on_actionFecharProjeto_triggered(self):
        if self.projects.rowCount() < 1:
            return
        # Remove o projeto ativo do modelo de projetos abertos
        projidx = self.ui.projComboBox.currentIndex()
        self.projects.remove(projidx)
        self.ui.projComboBox.setCurrentIndex(projidx - 1)
        return

    @Slot()
    def on_projDialog_accepted(self):
        # Repassa valores da caixa de diálogo para projeto ativo
        # Dados persistentes (ID, hora de criação) são mantidos.
        dialog = self.ui.projDialog
        self.activeProject.setRowData(self.activeProject.id,
                                      dialog.nameLineEdit.text(),
                                      dialog.descrTextEdit.toPlainText(),
                                      self.activeProject.created_at)
        # Força atualização das informações sobre novo projeto
        self.on_projComboBox_currentChanged()
        dialog.reset()
        return

    @Slot()
    def on_projDialog_rejected(self):
        if self.projects[-1].name == 'New':
            # Se projeto novo for cancelado, deve ser removido do modelo
            self.ui.projComboBox.setCurrentIndex(
                self.ui.projComboBox.currentIndex() - 1)
            self.projects.remove(self.projects.rowCount()-1)
        self.ui.projDialog.reset()
        return

    @Slot()
    def on_projComboBox_currentChanged(self):
        if self.projects.rowCount() >= 1:
            # Caso existam projetos abertos, atualiza GUI com suas informações
            self.ui.projIdLineEdit.setText(str(self.activeProject.id))
            self.ui.projDescrTextEdit.setText(self.activeProject.description)
            self.ui.projTimeLineEdit.setText(self.activeProject.created_at)
            self.ui.projTreeView.setModel(self.activeProject.lists)
            self.ui.listComboBox.setModel(self.activeProject.lists)
            self.ui.listComboBox.setModelColumn(1)
        else:
            # Caso contrário, todos os valores são zerados
            self.ui.projIdLineEdit.setText("")
            self.ui.projDescrTextEdit.setText("")
            self.ui.projTimeLineEdit.setText("")
            self.ui.projTreeView.setModel(ListsModel(None))
            self.ui.listComboBox.setModel(ListsModel(None))
            self.ui.on_listComboBox_currentChanged()
        return

    @Slot()
    def on_projTreeView_doubleClicked(self, midx: QModelIndex):
        if (self.projects.rowCount() < 1
                or self.activeProject.lists.rowCount() < 1):
            return
        # Carrega as informações da lista ativa na caixa de diálogo
        self.ui.listDialog.setWindowTitle("Alterar lista")
        self.ui.listComboBox.setCurrentIndex(midx.row())
        self.ui.listDialog.nameLineEdit.setText(self.activeList.name)
        self.ui.listDialog.open()
        return

# IMPLEMENTAÇÃO PARA A LISTA
    @property
    def activeList(self):
        if self.activeProject.lists.rowCount() < 1:
            return
        # facilitador de acesso à lista selecionada para visualização
        return self.activeProject.lists[self.ui.listComboBox.currentIndex()]

    @Slot()
    def on_actionNovaLista_triggered(self):
        if self.projects.rowCount() >= 1:
            # caso exista um projeto ativo,
            # adiciona uma nova lista ao projeto ativo
            self.ui.listDialog.setWindowTitle("Nova lista")
            self.activeProject.lists.new('New')
            self.ui.listComboBox.setCurrentIndex(
                self.activeProject.lists.rowCount()-1)
            self.ui.listDialog.open()
        return

    @Slot()
    def on_actionAlterarLista_triggered(self):
        if (self.projects.rowCount() < 1
                or self.activeProjec.lists.rowCount() < 1):
            return
        # Carrega as informações da lista ativa na caixa de diálogo
        self.ui.listDialog.setWindowTitle("Alterar lista")
        self.ui.listDialog.nameLineEdit.setText(self.activeList.name)
        self.ui.listDialog.open()
        return

    @Slot()
    def on_actionRemoverLista_triggered(self):
        if (self.projects.rowCount() < 1
                or self.activeProjec.lists.rowCount() < 1):
            return

        # Carrega o modelo das listas para a caixa de remoção
        self.ui.removeDialog.setWindowTitle("Remover lista")
        self.ui.removeDialog.tableView.setModel(self.activeProject.lists)
        self.ui.removeDialog.open()
        return

    @Slot()
    def on_listDialog_accepted(self):
        # Atualiza informações da lista ativa, mas dados persistentes
        # (ID da lista e do projeto, momento de criação) são mantidos
        name = self.ui.listDialog.nameLineEdit.text()
        self.activeList.setRowData(self.activeList.id,
                                   name,
                                   self.activeList.projid,
                                   self.activeList.created_at)
        # Força atualização das informações da lista
        self.on_listComboBox_currentChanged()
        self.ui.listDialog.reset()
        return

    @Slot()
    def on_listDialog_rejected(self):
        if self.activeList.name == 'New':
            # em caso de nova lista não nomeada, deve-se remover do modelo.
            self.activeProject.lists.remove(
                self.activeProject.lists.rowCount() - 1)
            self.ui.listComboBox.setCurrentIndex(
                self.ui.listComboBox.currentIndex() - 1)
        self.ui.listDialog.reset()
        return

    @Slot()
    def on_listComboBox_currentChanged(self):
        if (self.projects.rowCount() >= 1
                and self.activeProject.lists.rowCount() >= 1):
            # Caso exista algum projeto e exista lista nesse projeto,
            # Insere as informações na GUI
            self.ui.listIdLineEdit.setText(str(self.activeList.id))
            self.ui.listTimeLineEdit.setText(self.activeList.created_at)
            self.ui.listTableView.setModel(self.activeList.lines)
        else:  # Se não há listas, remove qualquer informação de linha
            self.ui.listIdLineEdit.setText("")
            self.ui.listTimeLineEdit.setText("")
            self.ui.listTableView.setModel(LinesModel(None))
        return

    @Slot()
    def on_listTableView_doubleClicked(self, midx: QModelIndex):
        if (self.projects.rowCount() < 1
                or self.activeProject.lists.rowCount() < 1
                or self.activeList.lines.rowCount() < 1):
            return
        idcbox = self.ui.lineDialog.idComboBox
        self.ui.lineDialog.setWindowTitle("Alterar linha")
        idcbox.setModel(self.activeList.lines)  # define as linhas
        idcbox.setModelColumn(2)  # mostra as TAGs como identificação da linha
        idcbox.setEnabled(False)   # desativa a escolha de linhas
        idcbox.setCurrentIndex(midx.row())
        self.on_lineDialog_idComboBox_currentChanged(midx.row())
        self.ui.lineDialog.open()
        return

# IMPLEMENTAÇÃO DA LINHA
    @Slot()
    def on_actionInserirLinha_triggered(self):
        if (self.projects.rowCount() < 1
                or self.activeProjec.lists.rowCount() < 1):
            return
        # Inclui nova linha e desativa caixa de escolha de linhas
        try:
            self.activeList.lines.new('New', '', '', '', '')
            self.ui.lineDialog.setWindowTitle("Inserir linha")
            self.ui.lineDialog.idComboBox.setCurrentIndex(-1)
            self.ui.lineDialog.idComboBox.setEnabled(False)
            self.ui.lineDialog.open()
        except RuntimeWarning as e:
            self.ui.errorDialog.label.setText(str(e))
            self.ui.errorDialog.open()
        return

    @Slot()
    def on_actionAlterarLinha_triggered(self):
        if (self.projects.rowCount() < 1
                or self.activeProjec.lists.rowCount() < 1
                or self.activeList.lines.rowCount() < 1):
            return
        idcbox = self.ui.lineDialog.idComboBox
        self.ui.lineDialog.setWindowTitle("Alterar linha")
        idcbox.setEnabled(True)   # ativa a escolha de linhas
        idcbox.setModel(self.activeList.lines)  # define as linhas
        idcbox.setModelColumn(2)  # mostra as TAGs como identificação da linha

        # Força a atualização da caixa de diálogo com valores da linha
        self.on_lineDialog_idComboBox_currentChanged(
            self.ui.lineDialog.idComboBox.currentIndex())
        self.ui.lineDialog.open()
        return

    @Slot()
    def on_actionRemoverLinha_triggered(self):
        if (self.projects.rowCount() < 1
                or self.activeProjec.lists.rowCount() < 1
                or self.activeList.lines.rowCount() < 1):
            return
        # Carrega modelo de linhas na caixa de remoção.
        self.ui.removeDialog.setWindowTitle("Remover linha")
        self.ui.removeDialog.tableView.setModel(self.activeList.lines)
        self.ui.removeDialog.open()
        return

    @Slot()
    def on_lineDialog_idComboBox_currentChanged(self, idx: int):
        # Em caso de edição de linha, é possível escolher a linha que será
        # editada, definindo valores iniciais nos campos da caixa de diálogo.
        if idx != -1:
            dialog = self.ui.lineDialog
            dialog.nameLineEdit.setText(self.activeList.lines[idx].name)
            dialog.tagLineEdit.setText(self.activeList.lines[idx].tag)
            dialog.typeComboBox.setCurrentText(self.activeList.lines[idx].type)
            dialog.signalComboBox.setCurrentText(self.activeList
                                                 .lines[idx].signal)
            dialog.pidLineEdit.setText(self.activeList.lines[idx].pid)
        return

    @Slot()
    def on_lineDialog_accepted(self):
        # Se a escolha de linha dentro da janela de edição está desativada
        # Significa que uma nova linha foi adicionada, sendo a última linha.
        dialog = self.ui.lineDialog
        idx = (-1 if not dialog.idComboBox.isEnabled()
               and self.activeList.lines[-1].name == 'New'
               else dialog.idComboBox.currentIndex())
        linha = self.activeList.lines[idx]

        # Valores da caixa de diálogo são recolhidos
        name = dialog.nameLineEdit.text()
        tag = dialog.tagLineEdit.text()
        type = dialog.typeComboBox.currentText()
        signal = dialog.signalComboBox.currentText()
        pid = dialog.pidLineEdit.text()

        # Linha tem valores redefinidos, exceto persistentes
        # como ID, ID da lista a qual pertence, horário de criação;
        # Também aumenta o contador da versão em 1 a cada edição.
        linha.setRowData(linha.id, name, tag, type, signal, pid,
                         linha.version+1, linha.listid, linha.created_at)
        dialog.reset()
        return

    @Slot()
    def on_lineDialog_rejected(self):
        if (not self.ui.lineDialog.idComboBox.isEnabled()
                and self.activeList.lines[-1].name == 'New'):
            # Se a escolha de linhas estiver desativada a nova linha
            # foi cancelada, devendo ser, portanto, removida.
            self.activeList.lines.remove(self.activeList.lines.rowCount()-1)
        self.ui.lineDialog.reset()
        return

    @Slot()
    def on_removeDialog_accepted(self):
        model = self.ui.removeDialog.tableView.model()
        indexes = (self.ui.removeDialog.tableView
                   .selectionModel().selectedRows())
        # lista os índices que serão removidos
        indexes = [modelidx.row() for modelidx in indexes]
        indexes.sort()  # organiza do menor (início) para o maior (fim)
        for idx in indexes[::-1]:  # itera do fim para o começo
            model.remove(idx)  # remove o índice do fim para o começo,
            if self.ui.listComboBox.model() == model:
                # se o modelo da remoção for das listas de um projeto
                if idx == self.ui.listComboBox.currentIndex():
                    # se o índice a ser removido é o mesmo ativo
                    # altera o índice ativo
                    # evitando mudanças de índice dentro de uma mesma seleção
                    self.ui.listComboBox.setCurrentIndex(idx - 1)
        self.ui.removeDialog.reset()
        return

    @Slot()
    def on_actionManual_triggered(self):
        self.ui.helpDialog.setWindowTitle("Manual de ajuda")
        curr = os.getcwd()
        helppath = os.path.dirname(curr)
        with open(helppath + os.sep + 'README.md') as manual:
            self.ui.helpDialog.textBrowser.setMarkdown(manual.read())
        self.ui.helpDialog.open()
        return
