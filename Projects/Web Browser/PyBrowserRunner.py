import sys

from PyQt5.QtWidgets import QApplication
from D_L import mainLogic

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = mainLogic.Window()
    window.show()
    sys.exit(app.exec_())
