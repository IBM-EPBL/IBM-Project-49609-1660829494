import ibm_db

connection = ibm_db.connect("DATABASE=bludb;HOSTNAME=125f9f61-9715-46f9-9399-c8177b21803b.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=30426;SECURITY=SSL;SSLServerCertificate=Certificate.crt;UID=vcr98026;PWD=TJRDiXCGyZVp0dwl",'','')

print(connection)
print("Connection Successfull !\n\n")

sql = "SELECT EMAIL,PASSWORD FROM logins"
stmt = ibm_db.exec_immediate(connection, sql)
dictionary = ibm_db.fetch_assoc(stmt)
while dictionary != False:
    # printing
    print("Full Row : ", dictionary)
    dictionary = ibm_db.fetch_assoc(stmt)