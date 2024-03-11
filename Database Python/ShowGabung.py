import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="D3_TI_2023"
)

cursorObject = database.cursor()

query = """
    SELECT MATA_KULIAH.NAMA_MATA_KULIAH, MAHASISWA.NAMA_MAHASISWA, DOSEN.NAMA_DOSEN
    FROM MAHASISWA
    JOIN MATA_KULIAH ON MAHASISWA.MATA_KULIAH_DIIKUTI = MATA_KULIAH.KODE_MATA_KULIAH
    JOIN DOSEN ON DOSEN.MATA_KULIAH_AJAR = MATA_KULIAH.KODE_MATA_KULIAH
"""
cursorObject.execute(query)

hasil = cursorObject.fetchall()

for row in hasil:
    print("Mata Kuliah:", row[0])
    print("Mahasiswa:", row[1])
    print("Dosen:", row[2])
    print()

database.close()
