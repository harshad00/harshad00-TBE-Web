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

def display_records():
    """Fetch and display all records."""
    try:
        connection = connect_to_db()
        if connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM employees")
            records = cursor.fetchall()
            print("\nRecords in the 'employees' table:")
            for row in records:
                print(f"ID: {row[0]}, Name: {row[1]}, Department: {row[2]}")
            cursor.close()
            connection.close()
    except Error as e:
        print("Error:", e)

def modify_record(record_id, new_name, new_department):
    """Modify an existing record by ID."""
    try:
        connection = connect_to_db()
        if connection:
            cursor = connection.cursor()
            query = "UPDATE employees SET name=%s, department=%s WHERE id=%s"
            cursor.execute(query, (new_name, new_department, record_id))
            connection.commit()
            print(f"Record with ID {record_id} modified successfully.")
            cursor.close()
            connection.close()
    except Error as e:
        print("Error:", e)

def delete_record(record_id):
    """Delete a record by ID."""
    try:
        connection = connect_to_db()
        if connection:
            cursor = connection.cursor()
            query = "DELETE FROM employees WHERE id=%s"
            cursor.execute(query, (record_id,))
            connection.commit()
            print(f"Record with ID {record_id} deleted successfully.")
            cursor.close()
            connection.close()
    except Error as e:
        print("Error:", e)

if __name__ == "__main__":
    while True:
        print("\nOptions:")
        print("1. Display all records")
        print("2. Modify a record")
        print("3. Delete a record")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            display_records()
        elif choice == '2':
            record_id = int(input("Enter the ID of the record to modify: "))
            new_name = input("Enter the new name: ")
            new_department = input("Enter the new department: ")
            modify_record(record_id, new_name, new_department)
        elif choice == '3':
            record_id = int(input("Enter the ID of the record to delete: "))
            delete_record(record_id)
        elif choice == '4':
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please try again.")
