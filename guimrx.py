print(f"""Je suis là presentement, j'espere que je serai maintenant present
Je vais bien que nous clarifions juste les lignes du travail

je fais une demo avec ce fichier une petite interface graphique
""")


# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 19:41:08 2022

@author: Exaucé Maruba
"""

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_graphique_principal(object):
    def setupUi(self, graphique_principal):
        graphique_principal.setObjectName("graphique_principal")
        graphique_principal.resize(580, 448)
        graphique_principal.setWhatsThis("")
        self.centralwidget = QtWidgets.QWidget(graphique_principal)
        self.centralwidget.setObjectName("centralwidget")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(280, 370, 185, 41))
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(90, 130, 421, 231))
        self.groupBox.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";")
        self.groupBox.setObjectName("groupBox")
        self.precision = QtWidgets.QSlider(self.groupBox)
        self.precision.setGeometry(QtCore.QRect(80, 0, 331, 21))
        self.precision.setOrientation(QtCore.Qt.Horizontal)
        self.precision.setObjectName("precision")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 60, 61, 41))
        self.label.setText("")
        self.label.setObjectName("label")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(90, 30, 241, 91))
        self.lcdNumber.setMinimumSize(QtCore.QSize(241, 91))
        self.lcdNumber.setMaximumSize(QtCore.QSize(241, 161))
        self.lcdNumber.setLineWidth(0)
        self.lcdNumber.setMidLineWidth(0)
        self.lcdNumber.setObjectName("lcdNumber")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(180, 70, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(330, 70, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label.raise_()
        self.commandLinkButton.raise_()
        self.groupBox.raise_()
        self.lcdNumber.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        graphique_principal.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(graphique_principal)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 580, 21))
        self.menubar.setObjectName("menubar")
        graphique_principal.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(graphique_principal)
        self.statusbar.setObjectName("statusbar")
        graphique_principal.setStatusBar(self.statusbar)

        self.retranslateUi(graphique_principal)
        QtCore.QMetaObject.connectSlotsByName(graphique_principal)

    def retranslateUi(self, graphique_principal):
        _translate = QtCore.QCoreApplication.translate
        graphique_principal.setWindowTitle(_translate("graphique_principal", "Graphique"))
        self.commandLinkButton.setText(_translate("graphique_principal", "Ingenious Team"))
        self.groupBox.setTitle(_translate("graphique_principal", "Zoom"))
        self.label_2.setText(_translate("graphique_principal", "Lancement..."))
        self.label_3.setText(_translate("graphique_principal", "seconde"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    graphique_principal = QtWidgets.QMainWindow()
    ui = Ui_graphique_principal()
    ui.setupUi(graphique_principal)
    graphique_principal.show()
    sys.exit(app.exec_())

