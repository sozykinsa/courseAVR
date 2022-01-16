# -*- coding: utf-8 -*-
import os
import sys

from qtpy.QtCore import QCoreApplication, Qt
from qtpy.QtWidgets import QApplication, QMessageBox, QMainWindow, QFileDialog

from form import Ui_MainWindow as Ui_form


class mainWindow(QMainWindow):
    def __init__(self, *args):
        super(mainWindow, self).__init__(*args)
        self.ui = Ui_form()
        self.ui.setupUi(self)

    def setup_ui(self):
        # buttons
        self.ui.programmButton.clicked.connect(self.programm)

    def show_error(self, e):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Error")
        msg.setInformativeText(str(e))
        msg.setWindowTitle("Error")
        msg.exec_()

    def programm(self):
        # create model
        df = 5


ORGANIZATION_NAME = 'SUSU'
ORGANIZATION_DOMAIN = 'susu.ru'
APPLICATION_NAME = 'AVRflasher'

QCoreApplication.setApplicationName(ORGANIZATION_NAME)
QCoreApplication.setOrganizationDomain(ORGANIZATION_DOMAIN)
QCoreApplication.setApplicationName(APPLICATION_NAME)

QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
app = QApplication(sys.argv)
window = mainWindow()
window.setup_ui()
window.show()

sys.exit(app.exec_())
