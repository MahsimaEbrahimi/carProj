import pypyodbc as odbc
DRIVER_NAME='SQL SERVER'
SERVER_NAME='MSI'
DATABASE_NAME='CarProj'
connection_string=f'''
DRIVER={{{DRIVER_NAME}}};
SERVER={SERVER_NAME};
DATABASE={DATABASE_NAME};
Trust_Conection=yes;
'''
conn=odbc.connect(connection_string)
print(conn)
