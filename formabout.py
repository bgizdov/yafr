# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'formabout.ui'
#
# Created: Tue Jun 29 23:17:03 2010
#      by: The PyQt User Interface Compiler (pyuic) 3.18.1
#
# WARNING! All changes made in this file will be lost!


from qt import *


class FormAbout(QDialog):
    def __init__(self,parent = None,name = None,modal = 0,fl = 0):
        QDialog.__init__(self,parent,name,modal,fl)

        if not name:
            self.setName("FormAbout")


        FormAboutLayout = QGridLayout(self,1,1,11,6,"FormAboutLayout")

        self.textLabel1 = QLabel(self,"textLabel1")

        FormAboutLayout.addWidget(self.textLabel1,0,0)

        self.textLabel3 = QLabel(self,"textLabel3")

        FormAboutLayout.addWidget(self.textLabel3,2,0)

        self.textLabel4 = QLabel(self,"textLabel4")

        FormAboutLayout.addWidget(self.textLabel4,3,0)

        self.pushButton1 = QPushButton(self,"pushButton1")

        FormAboutLayout.addWidget(self.pushButton1,4,0)

        self.textLabel2 = QLabel(self,"textLabel2")

        FormAboutLayout.addWidget(self.textLabel2,1,0)

        self.languageChange()

        self.resize(QSize(287,167).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.connect(self.pushButton1,SIGNAL("clicked()"),self.close)


    def languageChange(self):
        self.setCaption(self.__tr("About YAFR"))
        self.textLabel1.setText(self.__tr("<b>Yet Another Feed Reader</b>"))
        self.textLabel3.setText(self.__tr("<b>E-mail:</b> <u><font color=\"#0000ff\">borislav.gizdov@gmail.com</font></u>"))
        self.textLabel4.setText(self.__tr("<b>ICQ:</b> 340552027"))
        self.pushButton1.setText(self.__tr("OK"))
        self.textLabel2.setText(self.__tr("<b>Author: </b>Borislav \"PoisoneR\" Gizdov"))


    def __tr(self,s,c = None):
        return qApp.translate("FormAbout",s,c)
