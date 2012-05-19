# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'formnewfolder.ui'
#
# Created: Tue Jun 29 23:17:03 2010
#      by: The PyQt User Interface Compiler (pyuic) 3.18.1
#
# WARNING! All changes made in this file will be lost!


from qt import *


class FormNewFolder(QDialog):
    def __init__(self,parent = None,name = None,modal = 0,fl = 0):
        QDialog.__init__(self,parent,name,modal,fl)

        if not name:
            self.setName("FormNewFolder")

        self.setSizeGripEnabled(1)

        FormNewFolderLayout = QGridLayout(self,1,1,11,6,"FormNewFolderLayout")

        layout12 = QHBoxLayout(None,0,6,"layout12")
        spacer4 = QSpacerItem(40,20,QSizePolicy.Expanding,QSizePolicy.Minimum)
        layout12.addItem(spacer4)

        self.buttonOk = QPushButton(self,"buttonOk")
        self.buttonOk.setAutoDefault(1)
        self.buttonOk.setDefault(1)
        layout12.addWidget(self.buttonOk)

        self.buttonCancel = QPushButton(self,"buttonCancel")
        self.buttonCancel.setAutoDefault(1)
        layout12.addWidget(self.buttonCancel)

        FormNewFolderLayout.addLayout(layout12,2,0)

        self.lineEdit4 = QLineEdit(self,"lineEdit4")

        FormNewFolderLayout.addWidget(self.lineEdit4,1,0)

        self.textLabel3 = QLabel(self,"textLabel3")

        FormNewFolderLayout.addWidget(self.textLabel3,0,0)

        self.languageChange()

        self.resize(QSize(253,114).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.connect(self.buttonOk,SIGNAL("clicked()"),self.accept)
        self.connect(self.buttonCancel,SIGNAL("clicked()"),self.reject)


    def languageChange(self):
        self.setCaption(self.__tr("Add New Folder"))
        self.buttonOk.setText(self.__tr("&OK"))
        self.buttonOk.setAccel(QKeySequence(QString.null))
        self.buttonCancel.setText(self.__tr("&Cancel"))
        self.buttonCancel.setAccel(QKeySequence(QString.null))
        self.textLabel3.setText(self.__tr("Folder name:"))


    def __tr(self,s,c = None):
        return qApp.translate("FormNewFolder",s,c)
