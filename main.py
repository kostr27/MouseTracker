from MouseTracker import MouseTracker
from PyQt5 import QtWidgets
import sys

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MouseTracker()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()