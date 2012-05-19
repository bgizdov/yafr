# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'formrenamefolder.ui'
#
# Created: Tue Jun 29 23:17:03 2010
#      by: The PyQt User Interface Compiler (pyuic) 3.18.1
#
# WARNING! All changes made in this file will be lost!


from qt import *


class FormRenameFolder(QDialog):
    def __init__(self,parent = None,name = None,modal = 0,fl = 0):
        QDialog.__init__(self,parent,name,modal,fl)

        if not name:
            self.setName("FormRenameFolder")

        self.setSizeGripEnabled(1)

        FormRenameFolderLayout = QGridLayout(self,1,1,11,6,"FormRenameFolderLayout")

        Layout1 = QHBoxLayout(None,0,6,"Layout1")
        Horizontal_Spacing2 = QSpacerItem(20,20,QSizePolicy.Expanding,QSizePolicy.Minimum)
        Layout1.addItem(Horizontal_Spacing2)

        self.buttonOk = QPushButton(self,"buttonOk")
        self.buttonOk.setAutoDefault(1)
        self.buttonOk.setDefault(1)
        Layout1.addWidget(self.buttonOk)

        self.buttonCancel = QPushButton(self,"buttonCancel")
        self.buttonCancel.setAutoDefault(1)
        Layout1.addWidget(self.buttonCancel)

        FormRenameFolderLayout.addLayout(Layout1,2,0)

        self.lineEdit2 = QLineEdit(self,"lineEdit2")

        FormRenameFolderLayout.addWidget(self.lineEdit2,1,0)

        self.textLabel1 = QLabel(self,"textLabel1")

        FormRenameFolderLayout.addWidget(self.textLabel1,0,0)

        self.languageChange()

        self.resize(QSize(228,106).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.connect(self.buttonOk,SIGNAL("clicked()"),self.accept)
        self.connect(self.buttonCancel,SIGNAL("clicked()"),self.reject)


    def languageChange(self):
        self.setCaption(self.__tr("Rename Folder"))
        self.buttonOk.setText(self.__tr("&OK"))
        self.buttonOk.setAccel(QKeySequence(QString.null))
        self.buttonCancel.setText(self.__tr("&Cancel"))
        self.buttonCancel.setAccel(QKeySequence(QString.null))
        self.textLabel1.setText(self.__tr("Enter directory name:"))


    def __tr(self,s,c = None):
        return qApp.translate("FormRenameFolder",s,c)
