__author__ = 'pif'

import sys
from PyQt4 import QtSql
from PyQt4 import QtCore
from PyQt4 import QtGui

instance = QtGui.QApplication(sys.argv)
db = QtSql.QSqlDatabase.addDatabase("QMYSQL")
db.setHostName("localhost")  # TODO localhost?
db.setDatabaseName("spring_sql")
db.setUserName('root')
db.setPassword('')
ok = db.open()

query = QtSql.QSqlQuery()
query.setForwardOnly(True) # speed optimization
query.exec('select * from client')
while query.next():
    for field_number in range(0, query.record().count()):
        value = query.value(field_number)
        if isinstance(value, QtCore.QPyNullVariant):
            value = 'null'
        print(value, end='\t')
    print()
    # name = query.value(0) if not isinstance(query.value(0), QtCore.QPyNullVariant) else 'null'
    # sex = query.value(1) if not isinstance(query.value(1), QtCore.QPyNullVariant) else 'null'
    # sex_lover = query.value(2) if not isinstance(query.value(2), QtCore.QPyNullVariant) else 'null'
    # print(name, sex, sex_lover)

print(db.tables())

db.close()
QtSql.QSqlDatabase.removeDatabase("QMYSQL") #TODO seriously? "QMYSQL"?


