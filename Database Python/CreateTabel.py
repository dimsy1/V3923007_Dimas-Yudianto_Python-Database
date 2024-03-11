import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "D3_TI_2023"
)

cursorObject = dataBase.cursor()

tblMataKuliah = """CREATE TABLE MATA_KULIAH(
                    KODE_MATA_KULIAH VARCHAR(10) NOT NULL PRIMARY KEY,
                    NAMA_MATA_KULIAH VARCHAR(50) NOT NULL,
                    WAKTU DATE,
                    RUANGAN VARCHAR(10)
                    )"""

tblMahasiswa = """CREATE TABLE MAHASISWA(
                    NIM VARCHAR(10) NOT NULL PRIMARY KEY,
                    NAMA_MAHASISWA VARCHAR(30) NOT NULL,
                    ALAMAT VARCHAR(255),
                    MATA_KULIAH_DIIKUTI VARCHAR(10),
                    FOREIGN KEY (MATA_KULIAH_DIIKUTI) REFERENCES MATA_KULIAH(KODE_MATA_KULIAH)
                    )"""

tblDosen = """CREATE TABLE DOSEN(
                NIP VARCHAR(20) NOT NULL PRIMARY KEY,
                NAMA_DOSEN VARCHAR(50) NOT NULL,
                MATA_KULIAH_AJAR VARCHAR(50),
                FOREIGN KEY (MATA_KULIAH_AJAR) REFERENCES MATA_KULIAH(KODE_MATA_KULIAH)
                )"""

cursorObject.execute(tblMataKuliah)
cursorObject.execute(tblMahasiswa)
cursorObject.execute(tblDosen)

dataBase.close()