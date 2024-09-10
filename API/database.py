'''
Dev : Felipe Rivas
Script description: weather station Database
Engine: SQLite3
Version: 1.0
Date: 9/8/2024
'''
# Importing libraries database engine
import sqlite3

#Creating weather station database connection
conn = sqlite3.connect('weather_station.db')

#Create cursor
cur = conn.cursor()

#Create model users
users_model = '''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL,
    role TEXT NOT NULL,
    status BOOLEAN DEFAULT true,
    created_at TIMESTAMP DEFAULT (datetime('now','localtime')),
    updated_at TIMESTAMP DEFAULT (datetime('now','localtime')),
    deleted_at TIMESTAMP DEFAULT NULL
)
'''
#Execute query
cur.execute(users_model)

#Close connection
conn.close()