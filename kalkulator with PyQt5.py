import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit

def on_click(text):
    if text == "=":
        try:
            result = eval(display.text())
            display.setText(str(result))
        except Exception as e:
            display.setText("Error")
    elif text == "C":
        display.clear()
    else:
        display.insert(text)

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Kalkulator")

layout = QVBoxLayout()

display = QLineEdit()
display.setReadOnly(True)
layout.addWidget(display)

button_grid = [
    ['7', '8', '9', '+'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '*'],
    ['C', '0', '=', '/']
]

for row in button_grid:
    button_row = []
    for text in row:
        button = QPushButton(text)
        button.clicked.connect(lambda _, t=text: on_click(t))
        button_row.append(button)
    layout.addWidget(button_row[0])
    layout.addWidget(button_row[1])
    layout.addWidget(button_row[2])
    layout.addWidget(button_row[3])

window.setLayout(layout)
window.show()

sys.exit(app.exec_())
