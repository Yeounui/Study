'''
Informatics - Academic Year 2016-2017
Series 15: Databases and SQL

Student name: Seungchan Oh
Student ID: 01603277
'''

import csv         # for reading CSV files
import sqlite3     # for working with SQLite (https://www.sqlite.org/about.html)

# open text file in ASCII mode and read records
#
#    quotechar:  a one-character string used to quote fields containing special
#                characters, such as the delimiter or quotechar, or which
#                contain new-line characters.
#    doublequote: controls how instances of quotechar appearing inside a field
#                 should themselves be quoted. When True, the character is
#                 doubled.

data_file = open('periodic_table_data_cleaned.csv', 'r')
data_reader = csv.reader(data_file, delimiter=',', quotechar='"',
                         lineterminator='\n', doublequote=True)

history_file = open('periodic_table_history_cleaned.csv', 'r')
history_reader = csv.reader(history_file, delimiter=',', quotechar='"',
                            lineterminator='\n', doublequote=True)

# to use a database, it is required to create a Connection object, and where
# this object will represent the database; the argument of connection is the
# name of the database (this database does not have to exist yet)
connection = sqlite3.connect("periodic_table.db")

# to be able to send an SQL command to the database, we need a cursor object
cursor = connection.cursor()

# remove tables from the database, making it possible to start from scratch
# again whenever this Python script is executed 
cursor.execute("""DROP TABLE IF EXISTS data;""")
cursor.execute("""DROP TABLE IF EXISTS history;""")

# it is recommended to define an SQL command with a triple-quoted string; that
# way, the SQL command can contain single and double quotes, if necessary

# define the SQL command to create the data table
sql_command_create_table_data = """
CREATE TABLE data (
    atomic_number INTEGER,
    symbol CHAR(3),
    name VARCHAR(64),
    atomic_mass VARCHAR(1024),
    color CHAR(10),
    electronic_configuration VARCHAR(1024),
    electronegativity VARCHAR(128),
    atomic_radius VARCHAR(128),
    ion_radius VARCHAR(128),
    van_der_waals_radius VARCHAR(128),
    ie VARCHAR(128),
    ea VARCHAR(128),
    standard_state VARCHAR(128),
    bonding_type VARCHAR(128),
    melting_point VARCHAR(128),
    boiling_point VARCHAR(128),
    density VARCHAR(128),
    metal VARCHAR(128),
    year_discovered INTEGER
);"""

# define the SQL command to create the history table
sql_command_create_table_history = """
CREATE TABLE history (
    atomic_number INTEGER,
    symbol CHAR(3),
    name VARCHAR(64),
    year_discovered INTEGER,
    discoverer VARCHAR(64),
    history VARCHAR(64)
);"""   # TO BE COMPLETED

# store strings in the database my means of UTF-8 encoding
# cursor.execute('PRAGMA encoding="UTF-8";')

# execute the SQL commands
cursor.execute(sql_command_create_table_data)
cursor.execute(sql_command_create_table_history)
    
# read records from the data file; insert each record into the data table
for e in data_reader:
    format_str = """INSERT INTO data (  atomic_number,
                                        symbol,
                                        name,
                                        atomic_mass,
                                        color,
                                        electronic_configuration,
                                        electronegativity,
                                        atomic_radius,
                                        ion_radius,
                                        van_der_waals_radius,
                                        ie,
                                        ea,
                                        standard_state,
                                        bonding_type,
                                        melting_point,
                                        boiling_point,
                                        density,
                                        metal,
                                        year_discovered)
    VALUES ("{atomic_number}",
            "{symbol}",
            "{name}",
            "{atomic_mass}",
            "{color}",
            "{electronic_configuration}",
            "{electronegativity}",
            "{atomic_radius}",
            "{ion_radius}",
            "{van_der_waals_radius}",
            "{ie}",
            "{ea}",
            "{standard_state}",
            "{bonding_type}",
            "{melting_point}",
            "{boiling_point}",
            "{density}",
            "{metal}",
            "{year_discovered}");"""
      
    sql_command = format_str.format(atomic_number=e[0],
                                    symbol=e[1],
                                    name=e[2],
                                    atomic_mass=e[3],
                                    color=e[4],
                                    electronic_configuration=e[5],
                                    electronegativity=e[6],
                                    atomic_radius=e[7],
                                    ion_radius=e[8],
                                    van_der_waals_radius=e[9],
                                    ie=e[10],
                                    ea=e[11],
                                    standard_state=e[12],
                                    bonding_type=e[13],
                                    melting_point=e[14],
                                    boiling_point=e[15],
                                    density=e[16],
                                    metal=e[17],
                                    year_discovered=e[18])   
    cursor.execute(sql_command)

# read records from the history file; insert each record into the history table
for e in history_reader:
    format_str = """INSERT INTO history (   atomic_number,
                                            symbol,
                                            name,
                                            year_discovered,
                                            discoverer,
                                            history)
    VALUES ("{atomic_number}",
            "{symbol}",
            "{name}",
            "{year_discovered}",
            "{discoverer}",
            "{history}");"""
    # TO BE COMPLETED

    # the CSV reader removes each double quotechar; in order to make the SQL
    # command work, we need to manually double each quotechar again

    sql_command = format_str.format(atomic_number=e[0],
                                    symbol=e[1],
                                    name=e[2],
                                    year_discovered=e[3],
                                    discoverer=e[4],
                                    history=e[5].replace('"', '""'))
    
    cursor.execute(sql_command)

# the database and the tables have been set up; we are now ready to execute
# SQL statements against the populated database

print('+---------------------------------------------------------------------+')
cursor.execute("""
                SELECT * FROM data
            """) 
print("Print content of data table:")
result = cursor.fetchall() 
for r in result:
    print(r)
print('+---------------------------------------------------------------------+')
cursor.execute("""
                SELECT atomic_number, symbol, name
                    FROM data
                    WHERE metal = 'halogen'; """)     # TO BE COMPLETED
print("Print SQL statement #1:")
result = cursor.fetchall() 
for r in result:
    print(r)
print('+---------------------------------------------------------------------+')    
cursor.execute("""
                SELECT atomic_number, symbol, name
                    FROM history
                    WHERE year_discovered <= 1805
                          AND year_discovered >= 1800; """)     # TO BE COMPLETED
print("Print SQL statement #2:")
result = cursor.fetchall() 
for r in result:
    print(r)
print('+---------------------------------------------------------------------+')    
cursor.execute("""
                SELECT atomic_number, symbol, name
                    FROM history
                    WHERE discoverer LIKE '%Marie Curie%'
                          OR discoverer LIKE '%Pierre Curie%'; """)     # TO BE COMPLETED
print("Print SQL statement #3:")
result = cursor.fetchall() 
for r in result:
    print(r)
print('+---------------------------------------------------------------------+')
cursor.execute("""
                SELECT atomic_number, symbol, name
                    FROM history
                    WHERE name LIKE '__e%_%'; """)     # TO BE COMPLETED
print("Print SQL statement #4:")
result = cursor.fetchall() 
for r in result:
    print(r)
print('+---------------------------------------------------------------------+')
cursor.execute("""
                SELECT atomic_number, symbol, name
                    FROM history
                    WHERE name LIKE 'T%_%'
                          AND name NOT LIKE '%i%'; """)     # TO BE COMPLETED
print("Print SQL statement #5:")
result = cursor.fetchall() 
for r in result:
    print(r)
print('+---------------------------------------------------------------------+')
cursor.execute("""SELECT COUNT(name)
                    FROM data
                    WHERE standard_state = 'gas'; """)     # TO BE COMPLETED
print("Print SQL statement #6:")
result = cursor.fetchall() 
for r in result:
    print(r)
print('+---------------------------------------------------------------------+')
cursor.execute("""SELECT name, discoverer, year_discovered
                    FROM history
                    WHERE year_discovered >= 1960; """)     # TO BE COMPLETED
print("Print SQL statement #7:")
result = cursor.fetchall() 
for r in result:
    print(r)
print('+---------------------------------------------------------------------+')   
cursor.execute("""SELECT name, discoverer, year_discovered
                    FROM history
                    WHERE year_discovered >= 1880
                          AND year_discovered <= 1980
                    ORDER BY year_discovered""")     # TO BE COMPLETED
print("Print SQL statement #8:")
result = cursor.fetchall() 
for r in result:
    print(r)
print('+---------------------------------------------------------------------+')
    
# save changes
connection.commit()

# close the database
connection.close()
