import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "D3_TI_2023"
)

cursorObject = dataBase.cursor()

insertMatkul = "INSERT INTO MATA_KULIAH (KODE_MATA_KULIAH, NAMA_MATA_KULIAH, WAKTU, RUANGAN) VALUES (%s, %s, %s, %s)"
valueMatkul = [
    ("MK001", "Praktik Pemrograman Python", "2024-03-11", "L2R2"),
    ("MK002", "Statistika dan Probabilitas", "2024-03-11", "L2R2"),
    ("MK003", "Pemrograman Berorientasi Objek", "2024-03-12", "L2R3"),
    ("MK004", "Praktik Basis Data", "2024-03-13", "L2R2"),
    ("MK005", "Praktik Sistem Operasi", "2024-03-13", "L2R2")    
]

insertDosen = "INSERT INTO DOSEN (NIP, NAMA_DOSEN, MATA_KULIAH_AJAR) VALUES (%s, %s, %s)"
valueDosen = [
    ("123456781", "Yusuf Fadilla Rachman", "MK001"),
    ("123456782", "Nur Azizul Haqimi", "MK005"),
    ("123456783", "Darmawan Lahru Riatma", "MK003"),
    ("123456784", "Trisna Ari Roshinta", "MK002"),
    ("123456785", "Masbahah", "MK004")
]

insertMahasiswa = "INSERT INTO MAHASISWA (NIM, NAMA_MAHASISWA, ALAMAT, MATA_KULIAH_DIIKUTI) VALUES (%s, %s, %s, %s)"
valueMahasiswa = [
    ("V1234561", "Dimas", "Madiun", "MK001"),
    ("V1234562", "Yudi", "Surabaya", "MK005"),
    ("V1234563", "Anto", "Surakarta", "MK004"),
    ("V1234564", "Aldo", "Jakarta", "MK003"),
    ("V1234565", "Soni", "Yogyakarta", "MK002")
]

cursorObject.executemany(insertMatkul, valueMatkul)
cursorObject.executemany(insertDosen, valueDosen)
cursorObject.executemany(insertMahasiswa, valueMahasiswa)

dataBase.commit()

dataBase.close()