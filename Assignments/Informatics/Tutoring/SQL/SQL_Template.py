'''
Created on 2017. 8. 12.

@author: korea
'''

import csv
import sqlite3

data_open = open('Data_organized_file-example.csv', 'r')
data_reader = csv.reader(data_open, delimiter=',', quotechar='"',
                         lineterminator='\n', doublequote=True)

connection = sqlite3.connect("Example.db")
cursor = connection.cursor()

cursor.execute("""DROP TABLE IF EXISTS data;""")
# needed to execute a command
# move commands from Python to SQL 

sql_command_create_table_data = """
CREATE TABLE TableName (
    character CHAR(255),
    variable_character VARCHAR(65535),
    integer INTEGER,
    date DATE,
    boolean_value BOOL
);"""

cursor.execute(sql_command_create_table_data) # needed for creating table

for e in data_reader:
    format_str = """INSERT INTO TableName (   character,
                                            variable_character,
                                            integer,
                                            date,
                                            boolean_value)
    VALUES ("{character}",
            "{variable_character}",
            "{integer}",
            "{date}",
            "{boolean_value}");"""
            
    sql_command = format_str.format(character=e[0],
                                    variable_character=e[1],
                                    integer=e[2],
                                    date=e[3],
                                    boolean_value=e[4])
    
    
#history=e[5].replace('"', '""')
#In SQL, double quotechars(") are removed during insert,
#so we must change into typing twice.
    
    cursor.execute(sql_command)

##RETRIEVING DATA
cursor.execute("""
                SELECT * FROM TableName
                        ORDER BY character
                        Where integer > 2
                        Where character LIKE '%m%';
            """)
#'%': zero or more characters / '_': any single character
result = cursor.fetchall() 
for r in result:
    print(r)
    
##MODIFYING DATA
cursor.execute("""
                DELETE FROM TableName
                        WHERE character='bailey'
                                OR character='percy';
            """)

cursor.execute("""
                UPDATE FROM TableName
                        SET boolean_value=TRUE
                            AND date=CURDATE()
                        WHERE character='bailey'
                                OR character='percy';
            """)

##JOINS
# inner joins: queries do not return rows if TableName1.integer1 != TableName2.integer2.
cursor.execute("""
                SELECT * FROM TableName1, TableName2
                        WHERE integer1 = integer2;
            """)
# outer joins: quires can return rows saving both all values in tables.
cursor.execute("""
                SELECT * FROM TableName1 t1 RIGHT JOIN TableName2 t2
                        ON t1.integer1 = t2.integer2;
            """) # left outer joins: 'JOIN' instead of 'RIGHT JOIN'
#Why we need to set nickname of TableName?

##Subqueries: command in command
cursor.execute("""
                SELECT character1,
                    FROM TableName1
                    WHERE integer1 =
                    (SELECT integer2
                            FROM TableName2
                            WHERE character2 = 'Example');        
            """)