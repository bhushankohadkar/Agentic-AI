class MySQLDatabase:
    def connect(self):
        print("Connecting to MySQL database...")
class SQLServerDatabase:
    def connect(self):
        print("Connecting to SQL Server database...")
class OracleDatabase:
    def connect(self):
        print("Connecting to Oracle database...")

connection = [
    MySQLDatabase(),
    SQLServerDatabase(),
    OracleDatabase()
]

for db in connection:
    db.connect()