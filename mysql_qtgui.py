__author__ = 'pif'

import sys
from PyQt4 import QtSql
from PyQt4 import QtCore
from PyQt4 import QtGui
import view

app = QtGui.QApplication(sys.argv)
app.exec()

# while query.next():
#     for field_number in range(0, query.record().count()):
#         value = query.value(field_number)
#         if isinstance(value, QtCore.QPyNullVariant):
#             value = 'null'
#         print(value, end='\t')
#     print()
#     # name = query.value(0) if not isinstance(query.value(0), QtCore.QPyNullVariant) else 'null'
#     # sex = query.value(1) if not isinstance(query.value(1), QtCore.QPyNullVariant) else 'null'
#     # sex_lover = query.value(2) if not isinstance(query.value(2), QtCore.QPyNullVariant) else 'null'
#     # print(name, sex, sex_lover)
#
# print(db.tables())



