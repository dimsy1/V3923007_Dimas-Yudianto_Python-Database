import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "D3_TI_2023"
)

cursorObject = dataBase.cursor()

showMataKuliah = "SELECT * FROM MATA_KULIAH"

cursorObject.execute(showMataKuliah)

hasil = cursorObject.fetchall()

print("==> Data Tabel Mata Kuliah")
for x in hasil:
    print(x)

dataBase.close()
