import csv         # for reading CSV files
import sqlite3     # for working with SQLite (https://www.sqlite.org/about.html)

data_file = open('radioactivity.csv', 'r')
data_reader = csv.reader(data_file, delimiter=',', quotechar='"',
                         lineterminator='\n', doublequote=True)

connection = sqlite3.connect("radioactivity.db")

cursor = connection.cursor()

cursor.execute("""DROP TABLE IF EXISTS radioactivity;""")

sql_command_create_table_radioactivity = """
CREATE TABLE radioactivity (
    radioactive_element VARCHAR(100),
    symbol VARCHAR(4),
    atomic_number INTEGER,
    atomic_mass INTEGER,
    synthetic CHAR(3),
    decay_type VARCHAR(100),
    half_life VARCHAR(100)
);"""

cursor.execute(sql_command_create_table_radioactivity)

#cursor.execute('PRAGMA encoding="UTF-8";')

switch = 0
for line in data_reader:
    print(line)
    if switch == 0:
        switch = 1
    else:
        format_str = """INSERT INTO radioactivity (radioactive_element,
                                               symbol,
                                               atomic_number,
                                               atomic_mass,
                                               synthetic,
                                               decay_type,
                                               half_life)
    VALUES ({radioactive_element},
            {symbol},
            {atomic_number},
            {atomic_mass},
            {synthetic},
            {decay_type},
            {half_life});"""
            
        sql_command = format_str.format(radioactive_element = line[0],
                                    symbol = line[1],
                                    atomic_number = line[2],
                                    atomic_mass = line[3],
                                    synthetic = line[4],
                                    decay_type = line[5],
                                    half_life = line[6])
    
        cursor.execute(sql_command)
    
print('+---------------------------------------------------------------------+')
cursor.execute("""
                SELECT * FROM radioactivity
            """) 
print("Print content of data table:")
result = cursor.fetchall() 
for r in result:
    print(r)

print('+---------------------------------------------------------------------+')
cursor.execute("""
                SELECT radioactive_element, 
                       atomic_mass
                       FROM radioactivity
                       WHERE    synthetic = 'No';
            """) 
print("Print content of data table:")
result = cursor.fetchall() 
for r in result:
    print(r)
    
print('+---------------------------------------------------------------------+')
cursor.execute("""
                SELECT COUNT(radioactive_element) 
                       FROM radioactivity
                       WHERE    Decay_Type LIKE '%Beta%';
            """) 
print("Print content of data table:")
result = cursor.fetchall() 
for r in result:
    print(r)

print('+---------------------------------------------------------------------+')
cursor.execute("""
                SELECT radioactive_element,
                       symbol,
                       atomic_mass
                       FROM radioactivity
                       WHERE    atomic_mass >= 50
                               and atomic_mass <= 80;
            """) 
print("Print content of data table:")
result = cursor.fetchall() 
for r in result:
    print(r)
    
print('+---------------------------------------------------------------------+')
cursor.execute("""
                SELECT radioactive_element,
                       half_life
                       FROM radioactivity
                       WHERE NOT    radioactive_element = '%ium';
            """) 
print("Print content of data table:")
result = cursor.fetchall() 
for r in result:
    print(r)

#save TestRaiseChanges
connection.commit()

#close the database
connection.close()

#close all text files that have been opened for reading
data_file.close()