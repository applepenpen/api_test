import pymssql

conn=pymssql.connect('192.168.100.210','fumengjiao','fumengjiao123','CarBasic')

cursor=conn.cursor()
sql_line="select * from Car where Vin = 'LVHRE183895010684'"
cursor.execute(sql_line)
print(cursor.fetchall())
