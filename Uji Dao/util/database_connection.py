import mysql.connector


class DatabaseConnection:
    HOST="localhost"
    PORT=3306
    USER="root"
    PASSWORD=""
    DATABASE="db_akademik"
    
    @staticmethod
    def get_connection():
        return mysql.connector.connect(
            host=DatabaseConnection.HOST,
            port=DatabaseConnection.PORT,
            user=DatabaseConnection.USER,
            password=DatabaseConnection.PASSWORD,
            database=DatabaseConnection.DATABASE,
        )