# import pyodbc

# def get_sql_connection():
#     return pyodbc.connect(
#         "DRIVER={ODBC Driver 17 for SQL Server};"
#         "SERVER=localhost;"
#         "DATABASE=chatbot_db;"
#         "UID=sa;"
#         "PWD=YourStrongPassword"
#     )

import pyodbc

def get_sql_connection():
    conn = pyodbc.connect(
        'DRIVER={SQL Server};'
        'SERVER=DESKTOP-UA7AC2D\\SQLSERVER;'  # Replace with your actual server name
        'DATABASE=Chat_Bot;'           # Replace with your actual database
        'Trusted_Connection=yes;'             
        # Use SQL login if needed
        'UID=sa;'
        'PWD=12345;'
    )
        
    return conn

try:
    conn = get_sql_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT 1")
    row = cursor.fetchone()
    print("Connection successful. Result:", row)
except Exception as e:
    print("Connection failed:", e)
finally:
    if 'conn' in locals():
        conn.close()