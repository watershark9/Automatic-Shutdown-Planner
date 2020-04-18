from PyQt5 import QtWidgets, uic, QtCore
import sys
import main as function

ui_file = r'v1 interface.ui'

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi(ui_file, self)
        
        self.names = ['time_input', 'shutdown_button', 'abort_button']
        
        #Date Time Input:
        self.input1 = self.findChild(QtWidgets.QDateTimeEdit, self.names[0])
        self.present = QtCore.QDateTime.currentDateTime()
        self.input1.setMinimumDateTime( self.present )
        #Shutdown Button:
        self.button = self.findChild(QtWidgets.QPushButton, self.names[1])
        self.button.clicked.connect( self.sendDateandTime )
        #Abort Shutdown
        self.button2 = self.findChild(QtWidgets.QPushButton, self.names[2])
        self.button2.clicked.connect( function.abort_shutdown_procedure )

        self.show()
        
    def sendDateandTime(self):
        input = self.findChild(QtWidgets.QDateTimeEdit, self.names[0]) # Date and Time Input
        input = input.dateTime()
        input = input.toPyDateTime()
        function.shutdown_procedure( input )

def run_window():
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()

run_window()