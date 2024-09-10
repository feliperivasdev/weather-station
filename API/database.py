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

#Close connection
conn.close()