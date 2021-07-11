from PyQt5.QtWidgets import QMainWindow, QToolBar, QPushButton, QLineEdit
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QSize, QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Browser")
        self.setWindowIcon(QIcon("Logo/vector/black.svg"))
        self.setGeometry(200, 200, 1280, 720)

        toolbar = QToolBar()
        self.addToolBar(toolbar)


        self.backButton = QPushButton()
        self.backButton.setIcon(QIcon("Logo/back.png"))
        self.backButton.setIconSize(QSize(30, 30))
        self.backButton.clicked.connect(self.backBtn)
        toolbar.addWidget(self.backButton)

        self.reloadButton = QPushButton()
        self.reloadButton.setIcon(QIcon("Logo/reload.png"))
        self.reloadButton.setIconSize(QSize(30, 30))
        self.reloadButton.clicked.connect(self.reloadBtn)
        toolbar.addWidget(self.reloadButton)

        self.forwardButton = QPushButton()
        self.forwardButton.setIcon(QIcon("Logo/forward.png"))
        self.forwardButton.setIconSize(QSize(30, 30))
        self.forwardButton.clicked.connect(self.forwardBtn)
        toolbar.addWidget(self.forwardButton)

        self.homeButton = QPushButton()
        self.homeButton.setIcon(QIcon("Logo/home.png"))
        self.homeButton.setIconSize(QSize(30, 30))
        self.homeButton.clicked.connect(self.homeBtn)
        toolbar.addWidget(self.homeButton)

        self.addressLineEdit = QLineEdit()
        self.addressLineEdit.setFont(QFont("Sanserif", 10))
        self.addressLineEdit.returnPressed.connect(self.searchBtn)
        toolbar.addWidget(self.addressLineEdit)

        self.searchButton = QPushButton()
        self.searchButton.setIcon(QIcon("Logo/search.png"))
        self.searchButton.setIconSize(QSize(30, 30))
        self.searchButton.clicked.connect(self.searchBtn)
        toolbar.addWidget(self.searchButton)

        self.webEngineView = QWebEngineView()
        self.setCentralWidget(self.webEngineView)
        initialUrl = 'https://www.google.com'
        self.addressLineEdit.setText(initialUrl)
        self.webEngineView.load(QUrl(initialUrl))


    def searchBtn(self):
        myUrl = self.addressLineEdit.text()
        self.webEngineView.load(QUrl(myUrl))

    def backBtn(self):
        self.webEngineView.back()

    def forwardBtn(self):
        self.webEngineView.forward()

    def reloadBtn(self):
        self.webEngineView.reload()

    def homeBtn(self):
        self.webEngineView.load(QUrl('https://www.google.com'))


