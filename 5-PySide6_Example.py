from PySide6.QtWidgets import QApplication, QWidget, QFrame, QGridLayout, QVBoxLayout, QLabel, QLineEdit, QCheckBox, QPushButton, QFileDialog, QTextEdit, QMessageBox
from PySide6.QtCore import Qt

# for more information and practice using PySide6, go to this 3rd-party GitHub repository: https://github.com/Erriez/pyside6-getting-started

class main(QWidget):
    def __init__(self, size_x:int, size_y:int):
        super().__init__()
        self.resize(size_x, size_y)

        self.main_layout = QVBoxLayout(self)

        self.main_label = QLabel("This is a PySide6 Window!")
        self.main_layout.addWidget(self.main_label)
        self.main_label.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.run_btn = QPushButton("Press Here!")
        self.run_btn.clicked.connect(self.change_label)
        self.main_layout.addWidget(self.run_btn)

    def change_label(self, text:str):
        self.main_label.setText(text)

if __name__ == "__main__":
    app = QApplication()
    window = main(500,500)
    window.show()
    app.exec()