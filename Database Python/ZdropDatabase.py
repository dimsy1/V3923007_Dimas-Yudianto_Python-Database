import mysql.connector
  
dataBase = mysql.connector.connect(
  host ="localhost",
  user ="root",
  passwd ="",
  database = "D3_TI_2023"
)

cursorObject = dataBase.cursor()

query = "DROP DATABASE D3_TI_2023"

cursorObject.execute(query)
dataBase.commit()

dataBase.close()