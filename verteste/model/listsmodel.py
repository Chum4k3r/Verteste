# This Python file uses the following encoding: utf-8
from PySide6.QtCore import QDateTime
from .basemodels import BasicModel, BasicItem, dateTimeFormatString
from .linesmodel import LinesModel


class ListItem(BasicItem):
    def __init__(self, id: int, name: str, projid: int,
                 created_at: str = None):
        BasicItem.__init__(self, 4)
        # Um novo item de lista registra seu horário de criação
        if created_at is None:
            created_at = (QDateTime.currentDateTime()
                          .toString(dateTimeFormatString))
        self.setItemData(id, name, projid, created_at)
        # Um item de lista possui um modelo de linhas
        self.lines = LinesModel(self)
        return

    def toDict(self):
        return {'id': self.id,
                'name': self.name,
                'created_at': self.created_at,
                'lines': self.lines.toDictList()}

    def setItemData(self, id: int, name: str,
                    projid: int, created_at: str = None):
        self.modeldata[0].setText(str(id))
        self.modeldata[1].setText(str(name))
        self.modeldata[2].setText(str(projid))
        self.modeldata[3].setText(str(created_at))
        return

    @property
    def id(self):
        return int(self.modeldata[0].text())

    @property
    def name(self):
        return self.modeldata[1].text()

    @property
    def projid(self):
        return int(self.modeldata[2].text())

    @property
    def created_at(self):
        return self.modeldata[3].text()


class ListsModel(BasicModel):
    def __init__(self, parent: BasicItem = None):
        BasicModel.__init__(self, 0, 4, parent)
        # Uma lista possui quatro colunas, definidas pelo cabeçalho abaixo
        self.setHorizontalHeaderLabels(['ID', 'Nome', 'Projeto (ID)',
                                        'Criado em'])
        return

    def add(self, id: int, name: str, created_at: str = None):
        self.items.append(ListItem(id, name, self.parent().id, created_at))
        self.appendRow(self.items[-1].modeldata)
        return

    def new(self, name: str):
        return self.add(self.rowCount(), name)
