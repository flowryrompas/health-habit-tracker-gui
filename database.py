import sqlite3
import pandas as pd
import os

DB_NAME = 'health_data.db'

def initialize_db(db_name=DB_NAME):
    """Creates the database file and table if they don't exist."""
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    # We define the 'schema' here
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS health_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            sleep_hours REAL,
            mood_score INTEGER,
            exercise_minutes INTEGER,
            water_intake_liters REAL,
            calories_consumed INTEGER,
            screen_time_hours REAL
        )
    ''')
    
    conn.commit()
    conn.close()
    print("✅ Database initialized successfully.")

def add_entry_to_db(data_dict, db_name=DB_NAME):
    """Inserts a dictionary of health data into the SQL table."""
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    query = '''
        INSERT INTO health_logs 
        (date, sleep_hours, mood_score, exercise_minutes, water_intake_liters, calories_consumed, screen_time_hours)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    '''
    
    values = (
        data_dict['date'], 
        data_dict['sleep_hours'], 
        data_dict['mood_score'],
        data_dict['exercise_minutes'], 
        data_dict['water_intake_liters'],
        data_dict['calories_consumed'], 
        data_dict['screen_time_hours']
    )
    
    cursor.execute(query, values)
    conn.commit()
    conn.close()

def fetch_all_data(db_name=DB_NAME):
    """Retrieves all records from the database as a Pandas DataFrame."""
    conn = sqlite3.connect(db_name)
    # a Pandas feature: it can run SQL queries directly
    df = pd.read_sql("SELECT * FROM health_logs", conn)
    conn.close()
    return df

def clear_data(db_name=DB_NAME):
    # clear all the data and restart
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM health_logs") # SQL command to delete all rows but keeps headers
    conn.commit()
    conn.close()

# Run the initialization immediately when this file is imported
initialize_db()