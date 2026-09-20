from PySide6.QtWidgets import QApplication, QWidget, QFrame, QGridLayout, QVBoxLayout, QLabel, QLineEdit, QCheckBox, QPushButton, QFileDialog, QTextEdit, QMessageBox
from PySide6.QtCore import Qt

class label_button(QWidget):
    def __init__(self, label_text:str):
        super().__init__()

        self.main_layout = QVBoxLayout(self)

        self.label1 = QLabel(label_text)
        self.main_layout.addWidget(self.label1)

        self.btn1 = QPushButton("Remove")
        self.btn1.clicked.connect(lambda: self.label1.setText(""))
        self.main_layout.addWidget(self.btn1)

class main(QWidget):
    def __init__(self):
        super().__init__()

        self.widget1 = label_button("label1")
        self.widget2 = label_button("label2")
        self.widget3 = label_button("label3")

        self.main_layout = QVBoxLayout(self)
        self.main_layout.addWidget(self.widget1)
        self.main_layout.addWidget(self.widget2)
        self.main_layout.addWidget(self.widget3)

class alt(QWidget):
    max_rows = 10

    def __init__(self, num_widgets:int):
        super().__init__()

        self.main_layout = QGridLayout(self)

        row = 0
        column = 0
        for i in range(1,num_widgets+1):
            if row >= self.max_rows:
                column += 1
                row = 0

            widget_name = f"widget{i}"
            label_text = f"label{i}"

            setattr(self, widget_name, label_button(label_text))

            self.main_layout.addWidget(getattr(self, widget_name), row, column)
            row += 1

if __name__ == "__main__":
    app = QApplication()
    window = main()
    window.show()
    app.exec()