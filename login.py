from PyQt6.QtWidgets import QMainWindow, QApplication
import sys
from PyQt6 import uic #đọc file .ui 

# Login class kế thừa từ QMainWindow
# có các thuộc tính và phương thức của QMainWindow
class Login(QMainWindow):
    def __init__ (self) -> None:
        super().__init__() # gọi hàm khởi tạo của lớp cha
        uic.loadUi("login.ui", self) # load file .ui vào chương trình

app = QApplication(sys.argv) # tạo 1 ứng dụng giao diện
login = Login()
login.show() # hiển thị cửa sổ