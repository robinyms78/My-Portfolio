import mysql.connector
import tkinter as tk
from mysql.connector import Error
from dashboard import Dashboard

def connect():
    """ Connect to MySQL database """
    conn = None
    try:
        conn = mysql.connector.connect(host="localhost",
                                       database="customer_order",
                                       user="root",
                                       password="5tanda4katta#")

        if conn.is_connected():
            db_Info = conn.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = conn.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("Connected to MySQL database: ", record)

    except Error as e:
        print("Error while connecting to MySQL", e)

    finally:
        if conn is not None and conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQL connection is closed")

def show_dashboard():
     root = tk.Tk()
     root.title("Marketing Omotenashi Engine")
     root.geometry("1550x1000")
     app = Dashboard(root)
     app.pack(side="top", fill="both", expand=True)
     root.mainloop()

if __name__ == "__main__":
    #connect()
    show_dashboard()
    
    


