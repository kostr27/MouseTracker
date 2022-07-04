import gui
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5.QtCore import QTimer, QTime, Qt, pyqtSlot
from mousePos import getDirection
import pyautogui
import subprocess
import os
import platform
from settings import SettingsDialog


class MouseTracker(QMainWindow, gui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.codes_list = []
        self.code = []
        self.x_prev = 0
        self.y_prev = 0
        self.settings_dict = {
            'tick': 10,
            'delay': 100,
            'teleport': False
        }
        self.startButton.clicked.connect(self.start)
        self.stopButton.clicked.connect(self.stop)
        self.openButton.clicked.connect(self.openFile)
        self.settingsButton.clicked.connect(self.show_settings)
        self.browseButton.clicked.connect(self.browse)
        self.timerId = None
        self.actionTimer = QTimer(self)
        self.actionTimer.timeout.connect(self.actionTimeout)
        self.timeLeftTimer = QTimer(self)
        self.timeLeftTimer.timeout.connect(self.decTime)
        self.recordStart = False
        self.zero_count = 0
        self.startTime = QTime()

    def start(self):
        self.codes_list.clear()
        self.startButton.setEnabled(False)
        self.stopButton.setEnabled(True)
        self.groupBox.setEnabled(False)
        self.x_prev, self.y_prev = pyautogui.position()
        self.zero_count = 0
        if self.timeModeButton.isChecked():
            self.startTime = self.timeEdit.time()
            self.timerId = self.startTimer(self.settings_dict['tick'])
            self.timeLeftTimer.start(1000)
        else:
            self.recordStart = False
            self.actionTimer.start(self.settings_dict['tick'])

    def stop(self):
        self.startButton.setEnabled(True)
        self.stopButton.setEnabled(False)
        self.groupBox.setEnabled(True)
        if self.timeModeButton.isChecked():
            self.killTimer(self.timerId)
            self.timeLeftTimer.stop()
        else:
            self.actionTimer.stop()
        with open(self.fileEdit.text(), 'w') as file:
            if self.actionModeButton.isChecked():
                for code in self.codes_list:
                    file.write("".join([str(num) for num in code]))
                    file.write('\n')
            else:
                file.write("".join([str(code) for code in self.codes_list]))

    def openFile(self):
        filepath = self.fileEdit.text()
        if platform.system() == 'Darwin':  # macOS
            subprocess.call(('open', filepath))
        elif platform.system() == 'Windows':  # Windows
            os.startfile(filepath)
        else:  # linux variants
            subprocess.call(('xdg-open', filepath))

    def timerEvent(self, event):
        x, y = pyautogui.position()
        self.codes_list.append(getDirection(self.x_prev, self.y_prev, x, y))
        self.x_prev = x
        self.y_prev = y
        event.accept()

    def actionTimeout(self):
        x, y = pyautogui.position()
        if self.recordStart:
            if (x, y) != (self.x_prev, self.y_prev):
                self.code.append(getDirection(self.x_prev, self.y_prev, x, y))
                self.zero_count = 0
            elif self.zero_count == self.settings_dict['delay']:
                if self.manyActionsBox.isChecked():
                    self.codes_list.append(self.code.copy())
                    self.recordStart = False
                    self.statusLabel.setText('Ожидание')
                    self.zero_count = self.zero_count + 1
                else:
                    self.statusLabel.setText('Ожидание')
                    self.stop()
            else:
                self.zero_count = self.zero_count + 1
        else:
            if (x, y) != (self.x_prev, self.y_prev):
                self.code.clear()
                self.recordStart = True
                self.statusLabel.setText('Запись')

        if self.settings_dict['teleport']:
            if x == pyautogui.size()[0] - 1:
                x = 0
                pyautogui.moveTo(x, y)
            elif x == 0:
                x = pyautogui.size()[0] - 1
                pyautogui.moveTo(x, y)
            elif y == pyautogui.size()[1] - 1:
                y = 0
                pyautogui.moveTo(x, y)
            elif y == 0:
                y = pyautogui.size()[1]-1
                pyautogui.moveTo(x, y)

        self.x_prev = x
        self.y_prev = y

    def decTime(self):
        self.timeEdit.setTime(self.timeEdit.time().addSecs(-1))
        if self.timeEdit.time() == QTime(0, 0):
            self.stop()
            self.timeEdit.setTime(self.startTime)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape and self.stopButton.isEnabled():
            self.stop()
            event.accept()

    @pyqtSlot(dict)
    def updateSettings(self, settings_dict):
        self.settings_dict = settings_dict

    def show_settings(self):
        settingsDialog = SettingsDialog(self.settings_dict, self)
        settingsDialog.settings_accepted.connect(self.updateSettings)
        settingsDialog.show()

    def browse(self):
        file_path = QFileDialog.getOpenFileName(self, 'Выбор файла', '.', 'Text files (*.txt)')
        if file_path[0]:
            self.fileEdit.setText(file_path[0])
