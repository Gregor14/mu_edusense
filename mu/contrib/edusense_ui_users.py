# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_users.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from mu.resources import load_icon, load_pixmap

class Ui_dialog(object):
    def setupUi(self, dialog):
        dialog.setObjectName("dialog")
        dialog.resize(768, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(dialog.sizePolicy().hasHeightForWidth())
        dialog.setSizePolicy(sizePolicy)
        dialog.setWindowTitle("Your workplace")
        self.verticalLayout = QtWidgets.QVBoxLayout(dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.user_icon = QtWidgets.QLabel(dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.user_icon.sizePolicy().hasHeightForWidth())
        self.user_icon.setSizePolicy(sizePolicy)
        self.user_icon.setMaximumSize(QtCore.QSize(80, 80))
        self.user_icon.setInputMethodHints(QtCore.Qt.ImhNone)
        self.user_icon.setText("")
        # self.user_icon.setPixmap(QtGui.QPixmap("mu/resources/images/user.png"))
        self.user_icon.setPixmap(load_pixmap("user"))
        self.user_icon.setScaledContents(True)
        self.user_icon.setObjectName("user_icon")
        self.horizontalLayout.addWidget(self.user_icon)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.user_label = QtWidgets.QLabel(dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.user_label.sizePolicy().hasHeightForWidth())
        self.user_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.user_label.setFont(font)
        self.user_label.setInputMethodHints(QtCore.Qt.ImhNone)
        self.user_label.setText("Input your name")
        self.user_label.setObjectName("user_label")
        self.verticalLayout_2.addWidget(self.user_label)
        self.user_edit = QtWidgets.QLineEdit(dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.user_edit.sizePolicy().hasHeightForWidth())
        self.user_edit.setSizePolicy(sizePolicy)
        self.user_edit.setMinimumSize(QtCore.QSize(0, 42))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.user_edit.setFont(font)
        self.user_edit.setToolTip("")
        self.user_edit.setAccessibleDescription("")
        self.user_edit.setInputMethodHints(QtCore.Qt.ImhNone)
        self.user_edit.setText("")
        self.user_edit.setObjectName("user_edit")
        self.verticalLayout_2.addWidget(self.user_edit)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.user_button = QtWidgets.QPushButton(dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.user_button.sizePolicy().hasHeightForWidth())
        self.user_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.user_button.setFont(font)
        self.user_button.setInputMethodHints(QtCore.Qt.ImhNone)
        self.user_button.setText("Confirm")
        # icon = QtGui.QIcon()
        # icon.addPixmap(QtGui.QPixmap("mu/resources/images/check.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon = load_icon("check")
        self.user_button.setIcon(icon)
        self.user_button.setIconSize(QtCore.QSize(48, 48))
        self.user_button.setObjectName("user_button")
        self.horizontalLayout.addWidget(self.user_button)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 5)
        self.horizontalLayout.setStretch(2, 2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line = QtWidgets.QFrame(dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setMinimumSize(QtCore.QSize(0, 15))
        self.line.setInputMethodHints(QtCore.Qt.ImhNone)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lessons_label = QtWidgets.QLabel(dialog)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lessons_label.setFont(font)
        self.lessons_label.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lessons_label.setText("These are your lessons")
        self.lessons_label.setObjectName("lessons_label")
        self.verticalLayout_4.addWidget(self.lessons_label)
        self.lessons_list = QtWidgets.QListWidget(dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lessons_list.setFont(font)
        self.lessons_list.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lessons_list.setIconSize(QtCore.QSize(30, 30))
        self.lessons_list.setTextElideMode(QtCore.Qt.ElideNone)
        self.lessons_list.setProperty("isWrapping", False)
        self.lessons_list.setWordWrap(False)
        self.lessons_list.setObjectName("lessons_list")
        self.verticalLayout_4.addWidget(self.lessons_list)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lesson_use_button = QtWidgets.QPushButton(dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lesson_use_button.sizePolicy().hasHeightForWidth())
        self.lesson_use_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lesson_use_button.setFont(font)
        self.lesson_use_button.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lesson_use_button.setText("Use")
        # icon1 = QtGui.QIcon()
        # icon1.addPixmap(QtGui.QPixmap("mu/resources/images/new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1 = load_icon("new")
        self.lesson_use_button.setIcon(icon1)
        self.lesson_use_button.setIconSize(QtCore.QSize(48, 48))
        self.lesson_use_button.setObjectName("lesson_use_button")
        self.horizontalLayout_4.addWidget(self.lesson_use_button)
        self.lesson_remove_button = QtWidgets.QPushButton(dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lesson_remove_button.sizePolicy().hasHeightForWidth())
        self.lesson_remove_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lesson_remove_button.setFont(font)
        self.lesson_remove_button.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lesson_remove_button.setText("Remove")
        # icon2 = QtGui.QIcon()
        # icon2.addPixmap(QtGui.QPixmap("mu/resources/images/trash.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2 = load_icon("trash")
        self.lesson_remove_button.setIcon(icon2)
        self.lesson_remove_button.setIconSize(QtCore.QSize(48, 48))
        self.lesson_remove_button.setObjectName("lesson_remove_button")
        self.horizontalLayout_4.addWidget(self.lesson_remove_button)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 20)
        self.verticalLayout_4.setStretch(2, 3)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.example_button = QtWidgets.QPushButton(dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.example_button.sizePolicy().hasHeightForWidth())
        self.example_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.example_button.setFont(font)
        self.example_button.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.example_button.setInputMethodHints(QtCore.Qt.ImhNone)
        self.example_button.setText("")
        # icon3 = QtGui.QIcon()
        # icon3.addPixmap(QtGui.QPixmap("mu/resources/images/arrow_left.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon3 = load_icon("arrow_left")
        self.example_button.setIcon(icon3)
        self.example_button.setIconSize(QtCore.QSize(48, 48))
        self.example_button.setObjectName("example_button")
        self.horizontalLayout_2.addWidget(self.example_button)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.examples_label = QtWidgets.QLabel(dialog)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.examples_label.setFont(font)
        self.examples_label.setInputMethodHints(QtCore.Qt.ImhNone)
        self.examples_label.setText("Here are new examples")
        self.examples_label.setObjectName("examples_label")
        self.verticalLayout_5.addWidget(self.examples_label)
        self.examples_tree = QtWidgets.QTreeWidget(dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.examples_tree.sizePolicy().hasHeightForWidth())
        self.examples_tree.setSizePolicy(sizePolicy)
        self.examples_tree.setMinimumSize(QtCore.QSize(0, 35))
        self.examples_tree.setSizeIncrement(QtCore.QSize(0, 0))
        self.examples_tree.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.examples_tree.setFont(font)
        self.examples_tree.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.examples_tree.setToolTip("")
        self.examples_tree.setStatusTip("")
        self.examples_tree.setWhatsThis("")
        self.examples_tree.setAccessibleName("")
        self.examples_tree.setAccessibleDescription("")
        self.examples_tree.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.examples_tree.setAutoFillBackground(False)
        self.examples_tree.setInputMethodHints(QtCore.Qt.ImhNone)
        self.examples_tree.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.examples_tree.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.examples_tree.setLineWidth(1)
        self.examples_tree.setMidLineWidth(0)
        self.examples_tree.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.examples_tree.setProperty("showDropIndicator", True)
        self.examples_tree.setAlternatingRowColors(False)
        self.examples_tree.setIconSize(QtCore.QSize(30, 30))
        self.examples_tree.setTextElideMode(QtCore.Qt.ElideNone)
        self.examples_tree.setIndentation(20)
        self.examples_tree.setRootIsDecorated(True)
        self.examples_tree.setUniformRowHeights(True)
        self.examples_tree.setAnimated(True)
        self.examples_tree.setWordWrap(False)
        self.examples_tree.setHeaderHidden(True)
        self.examples_tree.setObjectName("examples_tree")
        self.examples_tree.headerItem().setText(0, "1")
        self.examples_tree.header().setVisible(False)
        self.examples_tree.header().setCascadingSectionResizes(False)
        self.examples_tree.header().setDefaultSectionSize(98)
        self.examples_tree.header().setHighlightSections(False)
        self.examples_tree.header().setMinimumSectionSize(59)
        self.verticalLayout_5.addWidget(self.examples_tree)
        self.verticalLayout_5.setStretch(0, 1)
        self.verticalLayout_5.setStretch(1, 23)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        self.examples_tree.setSortingEnabled(False)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()
    ui = Ui_dialog()
    ui.setupUi(dialog)
    dialog.show()
    sys.exit(app.exec_())
