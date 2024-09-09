'''
Created on 2017. 5. 16.

@author: korea
'''
import csv
import sqlite3

history_file = open('periodic_table_history_cleaned.csv', 'r')
history_reader = csv.reader(history_file, delimiter=',', quotechar='"',
                            lineterminator='\n', doublequote=True)

connection = sqlite3.connect("periodic_table.db")
cursor = connection.cursor()

sql_command_create_table_history = """
CREATE TABLE history (
    atomic_number INTEGER,
    symbol CHAR(3),
    name VARCHAR(64),
    year_discovered INTEGER,
    discoverer VARCHAR(64),
    history VARCHAR(64)
);"""

cursor.execute(sql_command_create_table_history)

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

    sql_command = format_str.format(atomic_number=e[0],
                                    symbol=e[1],
                                    name=e[2],
                                    year_discovered=e[3],
                                    discoverer=e[4],
                                    history=e[5])  
    cursor.execute(sql_command)
"""
print('+---------------------------------------------------------------------+')
cursor.execute("""SELECT * FROM history""") 
print("Print content of data table:")
result = cursor.fetchall() 
for r in result:
    print(r)
"""
print('+---------------------------------------------------------------------+')
cursor.execute("""
                 SELECT atomic_number, symbol, name, FROM data
                 WHERE atomic_number;
                 
            """)     # TO BE COMPLETED
print("Print SQL statement #1:")
result = cursor.fetchall() 
for r in result:
    print(r)
print('+---------------------------------------------------------------------+')    
cursor.execute(""" """)     # TO BE COMPLETED
print("Print SQL statement #2:")
result = cursor.fetchall() 
for r in result:
    print(r)
print('+---------------------------------------------------------------------+')    
cursor.execute(""" """)     # TO BE COMPLETED
print("Print SQL statement #3:")
result = cursor.fetchall() 
for r in result:
    print(r)
print('+---------------------------------------------------------------------+')
cursor.execute(""" """)     # TO BE COMPLETED
print("Print SQL statement #4:")
result = cursor.fetchall() 
for r in result:
    print(r)
print('+---------------------------------------------------------------------+')
cursor.execute(""" """)     # TO BE COMPLETED
print("Print SQL statement #5:")
result = cursor.fetchall() 
for r in result:
    print(r)
print('+---------------------------------------------------------------------+')
cursor.execute(""" """)     # TO BE COMPLETED
print("Print SQL statement #6:")
result = cursor.fetchall() 
for r in result:
    print(r)
print('+---------------------------------------------------------------------+')
cursor.execute(""" """)     # TO BE COMPLETED
print("Print SQL statement #7:")
result = cursor.fetchall() 
for r in result:
    print(r)
print('+---------------------------------------------------------------------+')   
cursor.execute(""" """)     # TO BE COMPLETED
print("Print SQL statement #8:")
result = cursor.fetchall() 
for r in result:
    print(r)
print('+---------------------------------------------------------------------+')
    
# save changes
connection.commit()

# close the database
connection.close()