# -*- coding: utf-8 -*-
import os
import subprocess
import sys
import time

from pathlib import Path

from qtpy.QtCore import QCoreApplication, Qt, QSettings
from qtpy.QtWidgets import QApplication, QMessageBox, QMainWindow, QFileDialog

from form import Ui_MainWindow as Ui_form


class mainWindow(QMainWindow):
    def __init__(self, *args):
        super(mainWindow, self).__init__(*args)
        self.ui = Ui_form()
        self.ui.setupUi(self)
        self.hex_fname = ""

    def setup_ui(self):
        # buttons
        self.ui.programmButton.clicked.connect(self.programm)
        self.ui.selectAvrdude.clicked.connect(self.select_avr_dude)
        self.ui.selectAVRdude.clicked.connect(self.select_hex)
        self.ui.saveSettings.clicked.connect(self.save_settings)
        self.ui.loadDefSetWin.clicked.connect(self.load_def_settings_win)
        self.ui.loadDefSetLin.clicked.connect(self.load_def_settings_lin)

        self.load_settings()

    def show_error(self, e):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Error")
        msg.setInformativeText(str(e))
        msg.setWindowTitle("Error")
        msg.exec_()

    def programm(self):
        exe = self.ui.avrdudeEXE.toPlainText()
        param = self.ui.avrdudeParams.toPlainText()
        hex_name = self.ui.hexFile.text()
        conf = self.ui.avrdudeConf.toPlainText()
        task = str(exe) + ' -C"' + str(conf) + '" ' + str(param) + ' -U flash:w:"' + str(hex_name) + ':i"'  # #, " -C" + str(conf)
        print(task)
        process = subprocess.Popen(task, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=None, text=True)
        while process.poll() is None:
            output_line = str(process.stderr.readline())  # .stdout.readline())
            self.ui.textLog.appendPlainText(str(output_line).rstrip())

    def select_avr_dude(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file')[0]
        if os.path.exists(fname):
            self.ui.avrdudeEXE.setText(fname)

    def select_hex(self):
        self.hex_fname = QFileDialog.getOpenFileName(self, 'Open file')[0]
        if os.path.exists(self.hex_fname):
            self.ui.hexFile.setText(self.hex_fname)

    def load_def_settings_win(self):
        fname = r"C:\Program Files (x86)\Arduino\hardware\tools\avr\bin\avrdude.exe"
        self.ui.avrdudeEXE.setText(fname)
        conf = r"C:\Program Files (x86)\Arduino\hardware\tools\avr\etc\avrdude.conf"
        self.ui.avrdudeConf.setText(conf)
        param = "-v -patmega328p -carduino -PCOM9 -b57600 -D"
        self.ui.avrdudeParams.setText(param)

    def load_def_settings_lin(self):
        fname = "text3"
        self.ui.avrdudeEXE.setText(fname)
        param = "text4"
        self.ui.avrdudeParams.setText(param)

    def save_settings(self):
        exe = self.ui.avrdudeEXE.toPlainText()
        param = self.ui.avrdudeParams.toPlainText()
        conf = self.ui.avrdudeConf.toPlainText()

        settings = QSettings()
        settings.setValue(SETTINGS_AVRDUDE_EXE, exe)
        settings.setValue(SETTINGS_AVRDUDE_CONF, conf)
        settings.setValue(SETTINGS_AVRDUDE_PARAM, param)
        settings.sync()

    def load_settings(self):
        settings = QSettings()
        state_avrdude = settings.value(SETTINGS_AVRDUDE_EXE, "-")
        state_avrdude_conf = settings.value(SETTINGS_AVRDUDE_CONF, "-")
        state_avrdude_param = settings.value(SETTINGS_AVRDUDE_PARAM, "-")

        self.ui.avrdudeEXE.setText(state_avrdude)
        self.ui.avrdudeConf.setText(state_avrdude_conf)
        self.ui.avrdudeParams.setText(state_avrdude_param)


SETTINGS_AVRDUDE_EXE = "avrdude"
SETTINGS_AVRDUDE_CONF = "avrdudeconf"
SETTINGS_AVRDUDE_PARAM = "avrdudeparam"

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
