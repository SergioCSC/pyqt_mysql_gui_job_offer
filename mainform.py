from PyQt4 import QtCore, QtGui, uic  # подключает основные модули PyQt
 
# прототип главной формы
class MainForm(QtGui.QDialog):
 
    # конструктор
    def __init__(self):
        super(MainForm, self).__init__()
 
        # динамически загружает визуальное представление формы
        uic.loadUi("mainform.ui", self)
 
        # связывает событие нажатия на кнопку с методом
        # old style (before pyqt 4.5):
        # self.connect(self.pushButton, QtCore.SIGNAL("clicked()"),
        #     self.setTextEdit)
        # new style (qt 4.5):
        self.pushButton.clicked.connect(self.setLabelText)

    # def setTextEdit(self):
    #     self.textEdit.setText(self.plainTextEdit.text()) # не пашет

    def setLabelText(self):
        self.label.setText("New label text")