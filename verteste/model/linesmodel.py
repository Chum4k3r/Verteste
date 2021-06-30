# This Python file uses the following encoding: utf-8
from PySide6.QtCore import QDateTime
from .basemodels import BasicModel, BasicRow, dateTimeFormatString


class LineRow(BasicRow):
    # Item básico de linha
    def __init__(self, id: int, name: str, tag: str,
                 type: str, signal: str, pid: str, version: int,
                 listid: int, created_at: str = None):
        BasicRow.__init__(self, 9)
        # Possui 9 itens em sua lista, registra o momento de criação
        if created_at is None:
            created_at = (QDateTime.currentDateTime()
                          .toString(dateTimeFormatString))
        # Define os valores de seus itens
        self.setRowData(id, name, tag, type, signal,
                        pid, version, listid, created_at)
        return

    def toDict(self):
        return {'id': self.id,
                'name': self.name,
                'tag': self.tag,
                'type': self.type,
                'signal': self.signal,
                'pid': self.pid,
                'version': self.version,
                'created_at': self.created_at}

    def setRowData(self, id: int, name: str, tag: str,
                   type: str, signal: str, pid: str, version: int,
                   listid: int, created_at: str = None):
        # Redefine os valores da lista.
        self.modeldata[0].setText(str(id))
        self.modeldata[1].setText(str(name))
        self.modeldata[2].setText(str(tag))
        self.modeldata[3].setText(str(type))
        self.modeldata[4].setText(str(signal))
        self.modeldata[5].setText(str(pid))
        self.modeldata[6].setText(str(version))
        self.modeldata[7].setText(str(listid))
        self.modeldata[8].setText(str(created_at))
        return

    # Propriedades para facilitar acesso aos dados
    @property
    def id(self):
        return int(self.modeldata[0].text())

    @property
    def name(self):
        return self.modeldata[1].text()

    @property
    def tag(self):
        return self.modeldata[2].text()

    @property
    def type(self):
        return self.modeldata[3].text()

    @property
    def signal(self):
        return self.modeldata[4].text()

    @property
    def pid(self):
        return self.modeldata[5].text()

    @property
    def version(self):
        return int(self.modeldata[6].text())

    @property
    def listid(self):
        return int(self.modeldata[7].text())

    @property
    def created_at(self):
        return self.modeldata[8].text()


class LinesModel(BasicModel):
    # Modelo de linha, extendendo o modelo básico
    def __init__(self, parent: BasicRow = None):
        BasicModel.__init__(self, 0, 9, parent)
        # inicialmente sem linhas e com 9 colunas
        # definidas pelo cabeçalho abaixo
        self.setHorizontalHeaderLabels(['ID', 'Nome', 'TAG',
                                        'Tipo', 'Sinal',
                                        'PID', 'Versão',
                                        'Lista (ID)', 'Criado em'])
        return

    def add(self, id: int, name: str, tag: str, type: str,
            signal: str, pid: str, version: int, created_at: str = None):
        if self.rowCount() == 50:
            raise RuntimeWarning("Essa lista já está no limite de TAGs (50)")
        # A adição de uma nova linha no modelo
        # consiste na criação de um item de linha
        self.rows.append(LineRow(id, name, tag, type, signal,
                         pid, version, self.parent().id, created_at))
        # E a inclusão da lista de itens padrão no modelo
        self.appendRow(self.rows[-1].modeldata)
        return

    def new(self, name: str, tag: str, type: str, signal: str, pid: str):
        # Uma nova linha no modelo é a adição de uma
        # linha com novos dados persistentes (ID, versão)
        return self.add(self.rowCount(), name, tag, type, signal, pid, 0)
