# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication
try:
    from .ui import Ui_Verteste
    from .verteste import Verteste
except ImportError:
    from ui import Ui_Verteste
    from verteste import Verteste


if __name__ == "__main__":
    app = QApplication([])

    gui = Ui_Verteste()
    main = Verteste(gui)

    gui.show()

    sys.exit(app.exec())
