__author__ = 'pif'

from PyQt4 import QtGui
from PyQt4 import uic


class View(QtGui.QMainWindow):

    def __init__(self):
        super(View, self).__init__()

        # загружаем интерфейс
        uic.loadUi("view.ui", self)

        # подправляем то, что не получилось сделать в Qt Designer
        self.gender.addItem("")
        self.gender.addItem("м")
        self.gender.addItem("ж")

    def get_fields_text(self):
        return (
                self.common_filter.text(),
                self.lastName.text(),
                self.firstName.text(),
                self.patrName.text(),
                self.gender.currentText(),
                self.age_from.value(),
                self.age_to.value(),
                self.birthDate_from.date().toString('yyyy-MM-dd'),
                self.birthDate_to.date().toString('yyyy-MM-dd'),
                self.document_serial.text(),
                self.document_number.text(),
                )

    def set_model(self, model):
        self.tableView.setModel(model)
        # v = QtGui.QTableView(self.tableWidget)
        # v.setModel(model)
        # v.show()