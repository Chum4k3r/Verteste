# This Python file uses the following encoding: utf-8
from PySide6.QtCore import QObject
from PySide6.QtGui import QStandardItemModel, QStandardItem


# Formato de data e hora utilizado para
# guardar momento de criação dos itens num modelo
dateTimeFormatString = "dd/MM/yyyy @ hh:mm:ss, 'GMT' t"


class BasicRow(QObject):
    # Um item básico dos modelos é, na verdade, uma capsula de uma lista de
    # itens de modelo padrão.
    def __init__(self, ncols):
        QObject.__init__(self)
        # Cada BasicItem representa uma linha no modelo,
        # os itens da linha estão na lista
        self.modeldata = []
        for cols in range(ncols):
            self.modeldata.append(QStandardItem(str()))
        return

    def __getitem__(self, idx: int):  # facilitador de acesso
        return self.modeldata[idx]

    def setRowData(self):
        # Um BasicItem é capaz de redefinir os
        # valores dos itens contidos em sua lista
        pass

    def toDict(self):
        # Cada item define seu próprio dicionário
        # a partir de suas propriedades
        # As propriedades, por sua vez, são também
        # argumentos para criação do objeto de item
        pass


class BasicModel(QStandardItemModel):
    # Modelo base para os modelos do programa. Uma extensão do modelo padrão
    def __init__(self, rows: int, cols: int,
                 parent: BasicRow = None):
        # Modelo pode ter um item pai, do qual obterá índice e estará contido
        # no dicionário para registro ou recriação
        QStandardItemModel.__init__(self, rows, cols, parent)
        self.rows = []  # Lista para prover itens na linha do modelo
        return

    def __getitem__(self, idx: int):
        return self.rows[idx]

    def add(self):
        # Um modelo é capaz de adicionar itens a si mesmo
        pass

    def new(self):
        # Modelo é capaz de criar um novo item e adicionálo a si mesmo
        pass

    def remove(self, row: int):
        # Modelo é capaz de remover um item a partir de seu índice de linha
        self.takeRow(row)
        return self.rows.pop(row)

    def toDictList(self):
        # Modelo é capaz de criar uma lista de dicionários de seus itens
        data = []
        for row in range(self.rowCount()):
            data.append(self.rows[row].toDict())
        return data
