import sys 
from PyQt6.QtWidgets import QMainWindow, QApplication 
from PyQt6 import uic
class Login(QMainWindow):
    def __init__(self) -> None:
        super().__init__() 
        uic.loadUi("login.ui", self)

if __name__ == "__main__": 
    # print(sys.argv)
    app = QApplication(sys.argv)
    window = Login()
    window.show()


    sys.exit(app.exec())