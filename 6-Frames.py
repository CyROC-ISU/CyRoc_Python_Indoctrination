from PySide6.QtWidgets import QApplication, QWidget, QFrame, QGridLayout, QVBoxLayout, QLabel, QLineEdit, QCheckBox, QPushButton, QFileDialog, QTextEdit, QMessageBox
from PySide6.QtCore import Qt

class main(QWidget):
    def __init__(self):
        super().__init__()

if __name__ == "__main__":
    app = QApplication()
    window = main()
    window.show()
    app.exec()