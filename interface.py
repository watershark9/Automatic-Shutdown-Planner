# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'v1 interface.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWidgets, uic
import sys
import main as function


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(295, 91)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 265, 83))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label1 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label1.setObjectName("label1")
        self.horizontalLayout.addWidget(self.label1)
        self.time_input = QtWidgets.QDateTimeEdit(self.verticalLayoutWidget)
        self.time_input.setObjectName("time_input")
        self.horizontalLayout.addWidget(self.time_input)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.abort_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.abort_button.setObjectName("abort_button")
        self.horizontalLayout_2.addWidget(self.abort_button)
        self.shutdown_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.shutdown_button.setObjectName("shutdown_button")
        self.horizontalLayout_2.addWidget(self.shutdown_button)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.line = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.StatusLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.StatusLabel.setText("")
        self.StatusLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.StatusLabel.setObjectName("StatusLabel")
        self.verticalLayout.addWidget(self.StatusLabel)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        #Custom Code:
        #self.names = ['time_input', 'shutdown_button', 'abort_button', 'StatusLabel']
        
        #Date Time Input:
        self.input1 = self.time_input
        self.present = QtCore.QDateTime.currentDateTime()
        self.input1.setMinimumDateTime( self.present )
        #Shutdown Button:
        self.button = self.shutdown_button
        self.button.clicked.connect( self.sendDateandTime )
        #Abort Shutdown
        self.button2 = self.abort_button
        self.button2.clicked.connect( self.abort )

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label1.setText(_translate("Form", "Time to shutdown system:"))
        self.abort_button.setText(_translate("Form", "Abort Shutdown"))
        self.shutdown_button.setText(_translate("Form", "Queue Shutdown"))

    #Custom Code:
        
    def sendDateandTime(self):
        # Date and Time Input
        input = self.time_input
        input = input.dateTime()
        input = input.toPyDateTime()
        self.changeStatusLabel( function.shutdown_procedure( input ) ) #changes label and executes function

    def abort(self):
        #Aborting
        function.abort_shutdown_procedure
        #Label
        self.changeStatusLabel( str('Shutdown Aborted') )
    
    def changeStatusLabel(self, new_text):
        label = self.StatusLabel
        label.setText( new_text )
    #Custom Code End

print('Interface Started')
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
