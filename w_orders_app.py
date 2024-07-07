import sys
from PySide6 import QtCore, QtWidgets, QtGui

class W_orders(QtWidgets.QWidget):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("W-orders")  # App title
        self.color_palette() # call the color_palette function
        self.text_labels() # call the text_labels function
        self.layout_window() # call the layout_window function

    def color_palette(self): # colors for the window
        
        palette = self.palette() # call the palette function

        palette.setColor(QtGui.QPalette.Window, QtGui.QColor(53, 53, 53))  # background color of the window
        palette.setColor(QtGui.QPalette.WindowText, QtCore.Qt.white)  # text color for the window

        palette.setColor(QtGui.QPalette.Base, QtGui.QColor(15, 15, 15))  # background color of text entry 
        palette.setColor(QtGui.QPalette.AlternateBase, QtGui.QColor(53, 53, 53))  # background color of the alternate base

        palette.setColor(QtGui.QPalette.ToolTipBase, QtCore.Qt.white)  # tooltip background color
        palette.setColor(QtGui.QPalette.ToolTipText, QtCore.Qt.white)  # tooltip text color

        palette.setColor(QtGui.QPalette.Text, QtCore.Qt.white) # text color
        palette.setColor(QtGui.QPalette.Button, QtGui.QColor(53, 53, 53))  # button background color
        palette.setColor(QtGui.QPalette.ButtonText, QtCore.Qt.white)  # button text color

        palette.setColor(QtGui.QPalette.BrightText, QtCore.Qt.red)  # text color for bright text (e.g. red for errors)
        palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(142, 45, 197).lighter())  # color of the highlighted text
        palette.setColor(QtGui.QPalette.HighlightedText, QtCore.Qt.black)  # text color of the highlighted text

        self.setPalette(palette)

    def text_labels(self): # text labels for the window

        self.welcome_label = QtWidgets.QLabel("Welcome to W-orders") # welcome text label
        self.auto_code_label = QtWidgets.QLabel("Autocode:") # text label for the codes
        self.car_brand_label = QtWidgets.QLabel("Car's make:") # text label for the car brand

        self.welcome_label.setAlignment(QtCore.Qt.AlignCenter) # center the welcome text label
        self.auto_code_entry = QtWidgets.QLineEdit() # text entry for the codes
        self.car_brand_entry = QtWidgets.QLineEdit() # text entry for the car brand

        self.send_button = QtWidgets.QPushButton("Search") # button to send the data
        self.send_button.clicked.connect(self.send_data) # connect the button to the send_data

    def layout_window(self): # layout for the window

        self.layout = QtWidgets.QVBoxLayout(self) # layout for the window

        # Layout for the welcome text
        welcome_layout = QtWidgets.QHBoxLayout()
        welcome_layout.addWidget(self.welcome_label)

        # Layout for auto code
        auto_code_layout = QtWidgets.QHBoxLayout()
        auto_code_layout.addWidget(self.auto_code_label)
        auto_code_layout.addWidget(self.auto_code_entry)

        # Layout for car brand
        car_brand_layout = QtWidgets.QHBoxLayout()
        car_brand_layout.addWidget(self.car_brand_label)
        car_brand_layout.addWidget(self.car_brand_entry)

        # Add the layouts to the main layout
        self.layout.addLayout(welcome_layout)
        self.layout.addLayout(auto_code_layout)
        self.layout.addLayout(car_brand_layout)
        self.layout.addWidget(self.send_button) # add the send button to the layout

    @QtCore.Slot()
    def send_data(self): # function to send the data to the console when the button is clicked
        auto_code = self.auto_code_entry.text() # get the auto code
        car_brand = self.car_brand_entry.text() # get the car brand
        print(f"Auto Code: {auto_code}, Car Brand: {car_brand}")  # Aquí puedes procesar los datos como desees

if __name__ == "__main__": # run the app
    app = QtWidgets.QApplication([])

    widget = W_orders()
    widget.resize(400, 300) # window size (width, height)
    widget.show()

    sys.exit(app.exec())