import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon


class Exercise2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui()

    def ui(self):
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('File')

        imp_edit = QMenu('Edit', self)
        imp_act = QAction('Copy', self)
        imp_act2 = QAction('Paste', self)

        imp_edit.addAction(imp_act)
        imp_edit.addAction(imp_act2)

        new_act = QAction('New', self)

        file_menu.addAction(new_act)
        file_menu.addMenu(imp_edit)
        save_act = QAction(QIcon(), "Save", self)
        save_act.setShortcut("Ctrl+S")
        quite_act = QAction(QIcon('app-icon.png'), "Quit", self)
        quite_act.setShortcut("Ctrl+Q")
        quite_act.setStatusTip('Exit application')
        quite_act.triggered.connect(QApplication.instance().quit)

        file_menu.addAction(save_act)
        file_menu.addAction(quite_act)

        self.statusBar().addPermanentWidget(QLabel(f'By {sys.argv[1]}'), 1), self.show()
        self.setGeometry(300, 300, 200, 150)
        self.setWindowTitle('Exercise 2')
        self.show()


def main_ex():
    app = QApplication(sys.argv)
    ex2 = Exercise2()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main_ex()
