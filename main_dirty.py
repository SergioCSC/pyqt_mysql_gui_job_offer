__author__ = 'pif'

import sys
from PyQt4 import QtGui
from PyQt4 import QtSql

import view


class Main():

    def __init__(self):
        app = QtGui.QApplication(sys.argv)

        self.db = self.open_db()

        self.view = view.View()
        self.view.showTableButton.clicked.connect(self.query)  # TODO сделать проброс сигнала из view, а не вторгаться беспардонно
        self.view.show()

        app.exec()

    def open_db(self):
        db = QtSql.QSqlDatabase.addDatabase('QMYSQL')
        db.setHostName('localhost')
        db.setDatabaseName('spring_sql')
        db.setUserName('root')
        db.setPassword('')
        ok = db.open()  # TODO что там, если не ок? Кинуть исключение?
        return db

    def query(self):
        # query = QtSql.QSqlQuery()
        # query.setForwardOnly(True)  # speed optimization
        # query.exec('select * from cats')

        common_filter, \
            lastname_filter, \
            firstname_filter, \
            patrname_filter,\
            gender_filter,\
            age_from, \
            age_to, \
            birthdate_from,\
            birthdate_to, \
            document_serial_filter, \
            document_number_filter \
            = self.view.get_fields_text()

        model = QtSql.QSqlQueryModel()
        model.setQuery(
            "select "
            "CONCAT "
            "("
            "client.lastName, ' ', "
            "client.firstName, ' ', "
            "client.patrName"
            ") "
            "as 'ФИО', "  #TODO зависим от кодировки исходника, вынести в конфиг
            "client.birthDate as 'дата рождения', "
            "TIMESTAMPDIFF(YEAR,client.birthDate,CURDATE()) as 'возраст', "
            "case client.sex when 1 then 'м' when 2 then 'ж' end as 'пол', "
            "CONCAT"
            "("
            "clientdocument.serial, '  ', "
            "clientdocument.number"
            ") "
            "as 'документ (серия, номер)' "
            "from client INNER JOIN clientdocument "
            "ON client.id = clientdocument.client_id "
            "where "
            "("
            "client.lastName like '%" + lastname_filter + "%' and "
            "client.firstName like '%" + firstname_filter + "%' and "
            "client.patrName like '%" + patrname_filter + "%' and "
            "clientdocument.serial like '%" + document_serial_filter + "%' and "
            "clientdocument.number like '%" + document_number_filter + "%' and "
            "case client.sex when 1 then 'м' when 2 then 'ж' end like '%" + gender_filter + "%' and "
            "client.birthDate >= STR_TO_DATE('" + birthdate_from + "', '%Y-%m-%d') and "
            "client.birthDate <= STR_TO_DATE('" + birthdate_to + "', '%Y-%m-%d') and "
            "TIMESTAMPDIFF(YEAR,client.birthDate,CURDATE()) >= " + str(age_from) + " and "
            "TIMESTAMPDIFF(YEAR,client.birthDate,CURDATE()) <= " + str(age_to) +
            ") "
            "and "
            "("
            "client.lastName like '%" + common_filter + "%' or "
            "client.firstName like '%" + common_filter + "%' or "
            "client.patrName like '%" + common_filter + "%' or "
            "clientdocument.serial like '%" + common_filter + "%' or "
            "clientdocument.number like '%" + common_filter + "%'"
            ") "
            "; ")
            #TODO maybe model.setQuery(query)?
            #TODO обработать случаи NULL переменных в sql-запросе

        self.view.set_model(model)

    def __del__(self):  #TODO это может не вызваться, надо чистить ресурсы явно
        self.db.close()
        QtSql.QSqlDatabase.removeDatabase('QMYSQL')

if __name__ == '__main__':
    Main()