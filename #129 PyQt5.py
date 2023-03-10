#129-#130 PyQt5

from PyQt5 import QtWidgets
import sys
import time

app=QtWidgets.QApplication(sys.argv)
w=QtWidgets.QMainWindow()

w.show()
sys.exit(app.exec_())