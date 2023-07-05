import app_data
from ui_mainwindow import Ui_MainWindow
from ui_aboutwindow import Ui_Dialog
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QStatusBar
from PySide6.QtCore import Qt, Signal, Slot
import os
import sys
import datetime
import logging
import ctypes



## Globals
debug_level = logging.INFO # Debug level for console output (logfile always DEBUG)
do_not_exit = False # e.g. unsaved state
log = logging.getLogger()

## Windows
main_win = None
about_win = None

## Icon
# A fix to get the app icon to show in taskbar (by default all python apps are grouped into one taskbar icon (default icon for pythonw.exe))
myappid = 'mycompany.myproduct.subproduct.version' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)


## Logging

def setup_logger():
    log.setLevel(logging.DEBUG)
    # Stream handler for console output
    stream_handler = logging.StreamHandler()
    stream_fmt = '%(name)s %(levelname)s\t%(message)s'
    stream_formatter = logging.Formatter(stream_fmt, datefmt='%H:%M:%S')
    stream_handler.setFormatter(stream_formatter)
    stream_handler.setLevel(debug_level)
    log.addHandler(stream_handler)
    # File handler for logfile output
    file_handler = logging.FileHandler(f"{app_data.app_name.replace(' ', '_')}.log", mode='w')
    file_fmt = '%(asctime)s.%(msecs)03d %(name)20s %(levelname)8s %(message)s'
    file_formatter = logging.Formatter(file_fmt, datefmt='%H:%M:%S')
    file_handler.setFormatter(file_formatter)
    file_handler.setLevel(logging.DEBUG)
    log.addHandler(file_handler)



## Main window
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle(app_data.app_name)
        #self.createStatusBar()
        self.ui.lineEdit.setToolTip("Send with Enter")
        self.ui.plainTextEdit.setReadOnly(True)

        # Input
        self.ui.lineEdit.returnPressed.connect(self.send_to_output)

        # Clear
        self.ui.pushButton.clicked.connect(self.clear_output)

        # Menu: About > About
        self.ui.actionAbout.triggered.connect(self.about_win)

        # Menu: Menu > Exit
        self.ui.actionExit.setShortcut("Ctrl+Q")
        self.ui.actionExit.triggered.connect(self.exit_app)
    
    @Slot()
    def send_to_output(self):
        self.ui.plainTextEdit.appendPlainText(self.ui.lineEdit.text())
        self.ui.lineEdit.clear()
    
    @Slot()
    def clear_output(self):
        self.ui.plainTextEdit.clear()
        self.set_status("Output cleared")

    # About window
    @Slot()
    def about_win(self):
        global about_win
        about_win = AboutWindow()
        about_win.show()

    # Write to status bar
    def set_status(self, str, timeout=5000):
        self.ui.statusbar.showMessage(str, timeout)

    # Exit application
    @Slot()
    def closeEvent(self, event):
        log.info(f'Application exited')
        if do_not_exit:
            event.ignore()
        else:
            event.accept()
            

    @Slot()
    def exit_app(self):
        QApplication.quit()
        log.debug(f'User quit application')




## About window
class AboutWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("About")
        self.setFixedSize(300,200)

        self.ui.label_appname.setText(app_data.app_name)
        self.ui.label_author.setText(app_data.author)
        self.ui.label_company.setText(app_data.company)
        self.ui.label_date.setText(app_data.date_created)








if __name__ == "__main__":
    date = datetime.datetime.now().strftime("[%Y-%m-%d]")
    setup_logger()
    #log.info(f"App started\n\n--= {app_name} =--\n{date}\n")
    log.info(f"App started {date}")
    app = QApplication(sys.argv)

    main_win = MainWindow()
    main_win.show()

    sys.exit(app.exec())


# Recompile ui-files:
# pyside6-uic mainwindow.ui > ui_mainwindow.py
# pyside6-uic aboutwindow.ui > ui_aboutwindow.py

# Dev container locations:
# /home/vscode/.local/lib/python3.11/site-packages/PySide6/designer
# /home/vscode/.local/lib/python3.11/site-packages/PySide6/