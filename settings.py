import settings_gui
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal


class SettingsDialog(QtWidgets.QDialog, settings_gui.Ui_settingsDialog):

    settings_accepted = pyqtSignal(dict, name='settings_accepted')

    def __init__(self, settings_dict, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.settings_dict = settings_dict
        self.init_gui()
        self.okButton.clicked.connect(self.accept_settings)

    def init_gui(self):
        if 'teleport' in self.settings_dict:
            self.teleportBox.setChecked(self.settings_dict['teleport'])
        if 'tick' in self.settings_dict:
            self.tickEdit.setText(str(self.settings_dict['tick']))
        if 'delay' in self.settings_dict:
            self.delayEdit.setText(str(self.settings_dict['delay']))

    def accept_settings(self):
        self.settings_dict['teleport'] = self.teleportBox.isChecked()
        self.settings_dict['tick'] = int(self.tickEdit.text())
        self.settings_dict['delay'] = int(self.delayEdit.text())
        self.settings_accepted.emit(self.settings_dict)
        self.accept()
        self.close()
