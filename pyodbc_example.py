import pyodbc


print([x for x in pyodbc.drivers() if x.startswith('Microsoft Access Driver')])

conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=./SBMSectionIIv2.odb;'
)
cnxn = pyodbc.connect(conn_str)
crsr = cnxn.cursor()
for table_info in crsr.tables(tableType='TABLE'):
    print(table_info.table_name)




































