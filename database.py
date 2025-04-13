# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, declarative_base

# DATABASE_URL = "mssql+pyodbc://sa:12345@localhost/Chat_Bot?driver=ODBC+Driver+17+for+SQL+Server"

# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = declarative_base()

# from sqlalchemy import create_engine

# DATABASE_URL = "mssql+pyodbc://sa:12345@localhost/Chat_Bot?driver=ODBC+Driver+17+for+SQL+Server"
# engine = create_engine(DATABASE_URL)

# try:
#     with engine.connect() as connection:
#         result = connection.execute("SELECT 1")
#         print(result.fetchone())
# except Exception as e:
#     print("Connection failed:", e)
# finally:
#     engine.dispose()

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
