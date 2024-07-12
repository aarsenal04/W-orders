import sys
from PySide6 import QtCore, QtWidgets, QtGui
import os

current_dir = os.getcwd()

class W_orders(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("W-orders")
        self.set_application_icon()
        self.color_palette()
        self.text_labels()
        self.image_label()
        self.layout_window()
        self.set_styles()

    def set_application_icon(self):
        logo_path = os.path.join(current_dir, "Images/logo.png")

        logo = QtGui.QPixmap(logo_path)
        icon_size = QtCore.QSize(32, 32)
        logo = logo.scaled(icon_size, QtCore.Qt.KeepAspectRatio)

        app = QtWidgets.QApplication.instance()
        app.setWindowIcon(QtGui.QIcon(logo))

    def color_palette(self):
        palette = self.palette()

        palette.setColor(QtGui.QPalette.Window, QtGui.QColor(53, 53, 53))
        palette.setColor(QtGui.QPalette.WindowText, QtCore.Qt.white)
        palette.setColor(QtGui.QPalette.Base, QtGui.QColor(15, 15, 15))
        palette.setColor(QtGui.QPalette.AlternateBase, QtGui.QColor(53, 53, 53))
        palette.setColor(QtGui.QPalette.ToolTipBase, QtCore.Qt.white)
        palette.setColor(QtGui.QPalette.ToolTipText, QtCore.Qt.white)
        palette.setColor(QtGui.QPalette.Text, QtCore.Qt.white)
        palette.setColor(QtGui.QPalette.Button, QtGui.QColor(53, 53, 53))
        palette.setColor(QtGui.QPalette.ButtonText, QtCore.Qt.white)
        palette.setColor(QtGui.QPalette.BrightText, QtCore.Qt.red)
        palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(142, 45, 197).lighter())
        palette.setColor(QtGui.QPalette.HighlightedText, QtCore.Qt.black)

        self.setPalette(palette)

    def text_labels(self):
        search_icon_path = os.path.join(current_dir, "Images/search-icon.png")

        self.welcome_label = QtWidgets.QLabel("Welcome to W-orders!")
        self.subtitle_label = QtWidgets.QLabel("OBDII Codes Definitions, Diagnostic, Description & Repair Information")
        
        # need to fix the font size later
        self.auto_code_label = QtWidgets.QLabel("Autocode:") 
        self.car_brand_label = QtWidgets.QLabel("Car's make:")

        self.welcome_label.setAlignment(QtCore.Qt.AlignCenter)
        self.subtitle_label.setAlignment(QtCore.Qt.AlignCenter)

        self.welcome_label.setStyleSheet("font-size: 18px; font-weight: bold; color: white;")
        self.subtitle_label.setStyleSheet("font-size: 16px; font-weight: bold; color: white;")
        
        self.auto_code_entry = QtWidgets.QLineEdit()
        self.car_brand_entry = QtWidgets.QLineEdit()

        self.send_button = QtWidgets.QPushButton("Search")
        self.send_button.setIcon(QtGui.QIcon(search_icon_path))
        self.send_button.clicked.connect(self.send_data)
    
    def image_label(self):
        image_path = os.path.join(current_dir, 'Images', 'autocodes.png')
        self.image_label = QtWidgets.QLabel()
        self.image = QtGui.QPixmap(image_path)
        self.image_label.setPixmap(self.image.scaled(150, 150, QtCore.Qt.KeepAspectRatio))
        self.image_label.setAlignment(QtCore.Qt.AlignCenter)

    def layout_window(self):
        self.layout = QtWidgets.QVBoxLayout(self)

        welcome_layout = QtWidgets.QHBoxLayout()
        welcome_layout.addWidget(self.welcome_label)

        subtitle_layout = QtWidgets.QHBoxLayout()
        subtitle_layout.addWidget(self.subtitle_label)

        auto_code_layout = QtWidgets.QHBoxLayout()
        auto_code_layout.addWidget(self.auto_code_label)
        auto_code_layout.addWidget(self.auto_code_entry)

        car_brand_layout = QtWidgets.QHBoxLayout()
        car_brand_layout.addWidget(self.car_brand_label)
        car_brand_layout.addWidget(self.car_brand_entry)

        self.layout.addLayout(welcome_layout)
        self.layout.addSpacing(10)
        self.layout.addWidget(self.image_label)
        self.layout.addSpacing(10)
        self.layout.addLayout(subtitle_layout)
        self.layout.addSpacing(20)
        self.layout.addLayout(auto_code_layout)
        self.layout.addSpacing(10)
        self.layout.addLayout(car_brand_layout)
        self.layout.addSpacing(20)
        self.layout.addWidget(self.send_button)

    def set_styles(self):
        self.setStyleSheet("""
            QPushButton {
                background-color: #8E2DC5;
                color: white;
                font-size: 14px;
                border-radius: 5px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #7B24B1;
            }
            QLineEdit {
                background-color: #353535;
                color: white;
                padding: 5px;
                border: 1px solid #5A5A5A;
                border-radius: 3px;
            }
            QLabel {
                color: white;
                font-size: 14px;
            }
        """)

    @QtCore.Slot()
    def send_data(self):
        auto_code = self.auto_code_entry.text()
        car_brand = self.car_brand_entry.text()
        print(f"Auto Code: {auto_code}, Car Brand: {car_brand}")

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = W_orders()
    widget.resize(500, 600)
    widget.show()

    sys.exit(app.exec())