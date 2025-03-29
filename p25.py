import mysql.connector
from mysql.connector import Error

def fetch_all_records():
    try:
        # Connect to the MySQL database
        connection = mysql.connector.connect(
            host='127.0.0.1',       # Default XAMPP MySQL host
            database='mypython',     # Replace with your database name
            user='root',            # Default XAMPP username
            password=''  
        )
        
        if connection.is_connected():
            print("Successfully connected to MySQL database")
            
            # Define the query to fetch all records
            cursor = connection.cursor()
            query = "SELECT * FROM employees"  # Replace 'your_table' with your table name
            
            cursor.execute(query)
            records = cursor.fetchall()  # Fetch all records
            
            # Print all records
            print("Records in the database:")
            for row in records:
                print(row)
    
    except Error as e:
        print("Error while connecting to MySQL", e)
    
    finally:
        # Close the connection
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

if __name__ == "__main__":
    fetch_all_records()
