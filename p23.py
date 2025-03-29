import mysql.connector
from mysql.connector import Error

def connect_to_db():
    """Establishes and returns a connection to the MySQL database."""
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',       # Default XAMPP MySQL host
            database='mypython',     # Replace with your database name
            user='root',            # Default XAMPP username
            password=''             # Blank if no password is set
        )
        return connection
    except Error as e:
        print("Error while connecting to MySQL:", e)
        return None

def search_record(search_term):
    """Search records by name or department."""
    try:
        connection = connect_to_db()
        if connection:
            cursor = connection.cursor()
            query = "SELECT * FROM employees WHERE name LIKE %s OR department LIKE %s"
            like_pattern = f"%{search_term}%"
            cursor.execute(query, (like_pattern, like_pattern))
            records = cursor.fetchall()

            if records:
                print("\nSearch Results:")
                for row in records:
                    print(f"ID: {row[0]}, Name: {row[1]}, Department: {row[2]}")
            else:
                print("\nNo matching records found.")
            cursor.close()
            connection.close()
    except Error as e:
        print("Error:", e)

if __name__ == "__main__":
    print("Search Records from the Database")
    search_term = input("Enter the search term (name or department): ")
    search_record(search_term)
