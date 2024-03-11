import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "D3_TI_2023"
)

cursorObject = dataBase.cursor()

showMahasiswa = "SELECT * FROM MAHASISWA"

cursorObject.execute(showMahasiswa)

hasil = cursorObject.fetchall()

print("==> Data Tabel Mahasiswa")
for x in hasil:
    print(x)

dataBase.close()
