# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'aboutwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.setWindowModality(Qt.NonModal)
        Dialog.resize(300, 200)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(True)
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 281, 181))
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(68, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_appname = QLabel(self.widget)
        self.label_appname.setObjectName(u"label_appname")
        font = QFont()
        font.setPointSize(12)
        self.label_appname.setFont(font)
        self.label_appname.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_appname, 0, Qt.AlignHCenter)

        self.horizontalSpacer_2 = QSpacerItem(68, 19, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.label_author = QLabel(self.widget)
        self.label_author.setObjectName(u"label_author")
        self.label_author.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_author, 0, Qt.AlignHCenter)

        self.label_company = QLabel(self.widget)
        self.label_company.setObjectName(u"label_company")
        self.label_company.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_company, 0, Qt.AlignHCenter)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.line = QFrame(self.widget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.label_date = QLabel(self.widget)
        self.label_date.setObjectName(u"label_date")
        self.label_date.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_date, 0, Qt.AlignHCenter)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_appname.setText(QCoreApplication.translate("Dialog", u"About_appname", None))
        self.label_author.setText(QCoreApplication.translate("Dialog", u"About_author", None))
        self.label_company.setText(QCoreApplication.translate("Dialog", u"About_company", None))
        self.label_date.setText(QCoreApplication.translate("Dialog", u"About_date", None))
    # retranslateUi

