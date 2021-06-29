# This Python file uses the following encoding: utf-8
from PySide6.QtCore import QDateTime
from .basemodels import BasicModel, BasicItem, dateTimeFormatString
from .listsmodel import ListsModel


class ProjectItem(BasicItem):
    def __init__(self, id: int, name: str, descr: str,
                 created_at: str = None):
        BasicItem.__init__(self, 4)
        # Um item de projeto possui quatro itens em
        # sua lista e registra seu horário de criação
        if created_at is None:
            created_at = (QDateTime.currentDateTime()
                          .toString(dateTimeFormatString))
        self.setItemData(id, name, descr, created_at)
        # Cada item de projeto possui um modelo de lista, do qual é pai
        self.lists = ListsModel(self)
        return

    def toDict(self):
        return {'id': self.id,
                'name': self.name,
                'descr': self.description,
                'created_at': self.created_at,
                'lists': self.lists.toDictList()}

    def setItemData(self, id: int, name: str,
                    descr: str, created_at: str = None):
        self.modeldata[0].setText(str(id))
        self.modeldata[1].setText(str(name))
        self.modeldata[2].setText(str(descr))
        self.modeldata[3].setText(str(created_at))
        return

    @property
    def id(self):
        return int(self.modeldata[0].text())

    @property
    def name(self):
        return self.modeldata[1].text()

    @property
    def description(self):
        return self.modeldata[2].text()

    @property
    def created_at(self):
        return self.modeldata[3].text()


class ProjectsModel(BasicModel):
    def __init__(self):
        BasicModel.__init__(self, 0, 4)
        self.setHorizontalHeaderLabels(['ID', 'Nome', 'Descrição',
                                        'Criado em'])
        return

    def add(self, id: int, name: str, descr: str, created_at: str = None):
        self.items.append(ProjectItem(id, name, descr, created_at))
        self.appendRow(self.items[-1].modeldata)
        return

    def new(self, name: str, descr: str):
        return self.add(self.rowCount(), name, descr)
