from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

import resources

from ReverseIP import *


class MainWindow(QMainWindow):
    """ This is the main window class for the reverse ip lookup tool"""

    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Reverse IP Lookup Tool")
        self.icon = QIcon(":/icon.png")
        self.setWindowIcon(self.icon)

        self.results = []

        #call the initial layout method
        self.initial_layout()

        self.resize(300,400)

    def initial_layout(self):
        
        #widgets
        self.hostLineEdit = QLineEdit()
        self.resolveButton = QPushButton("Resolve")
        self.listWidget = QListWidget()
        self.searchLineEdit = QLineEdit()
        self.searchLabel = QLabel("Search")

        #layouts
        self.mainLayout = QVBoxLayout()
        self.hostLayout = QHBoxLayout()
        self.searchLayout = QHBoxLayout()

        #add the widgets to the host layout
        self.hostLayout.addWidget(self.hostLineEdit)
        self.hostLayout.addWidget(self.resolveButton)

        #add the widgets to the search layout
        self.searchLayout.addWidget(self.searchLabel)
        self.searchLayout.addWidget(self.searchLineEdit)
        
        #create the host layout widget
        self.hostLayoutWidget = QWidget()
        self.hostLayoutWidget.setLayout(self.hostLayout)

        #create the search layout widget
        self.searchLayoutWidget = QWidget()
        self.searchLayoutWidget.setLayout(self.searchLayout)
        
        #add widgets to the main layout
        self.mainLayout.addWidget(self.hostLayoutWidget)
        self.mainLayout.addWidget(self.listWidget)
        self.mainLayout.addWidget(self.searchLayoutWidget)
    

        #create the main widget
        self.mainWidget = QWidget()
        self.mainWidget.setLayout(self.mainLayout)

        #set the central widget
        self.setCentralWidget(self.mainWidget)


        #button connections
        self.resolveButton.clicked.connect(self.getIPs)
        self.hostLineEdit.returnPressed.connect(self.getIPs)
        self.searchLineEdit.textChanged.connect(self.searchResults)
        
    def getIPs(self):

        if self.hostLineEdit.text() != "":
            rIP = ReverseIP()
            res = rIP.getHosts(self.hostLineEdit.text())
            self.results = res
            if len(res) > 0:
                self.listWidget.clear()
                for each in res:
                    self.listWidget.addItem(each)
                self.hostLineEdit.clear()
            else:
                self.listWidget.clear()
                self.listWidget.addItem("No Results found!")
                self.hostLineEdit.clear()

    def searchResults(self):
        query = self.searchLineEdit.text()
        if query != "":
            self.listWidget.clear()
            for host in self.results:
                if query in host:
                    self.listWidget.addItem(host)
        
        
if __name__ == "__main__":

    app = QApplication(sys.argv)
    window  = MainWindow()
    window.show()
    window.raise_()
    app.exec_()
