import mysql.connector
 
dataBase = mysql.connector.connect(
  host ="localhost",
  user ="root",
  passwd ="nurikshurik1"
)
 
# preparing a cursor object
cursorObject = dataBase.cursor()
 
# creating database
cursorObject.execute("CREATE DATABASE todo_db")