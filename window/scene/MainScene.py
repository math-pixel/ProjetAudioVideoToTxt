from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QDesktopWidget
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QDragEnterEvent, QDropEvent
from Utils import Utils
from window.scene.Scene import *
from window.scene.mainScene.UserInputForTranscriptionWidget import UserInputForTranscriptionWidget
import threading


# The MainScene (the first one !)
class MainScene(Scene):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Interface")
        self.resize(1280, 556)
        self.center()

        self.dragDiv = UserInputForTranscriptionWidget()
        
        hLayout = QHBoxLayout()
        hLayout.addWidget(self.dragDiv) 

        self.setLayout(hLayout)

    def start(self):
        pass

    def end(self):
        pass

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())



