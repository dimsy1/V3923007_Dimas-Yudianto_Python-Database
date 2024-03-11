import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "D3_TI_2023"
)

cursorObject = dataBase.cursor()

showDosen = "SELECT * FROM DOSEN"

cursorObject.execute(showDosen)

hasil = cursorObject.fetchall()

print("==> Data Tabel Dosen")
for x in hasil:
    print(x)

dataBase.close()
