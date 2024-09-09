# import the sqlite3 module from the Python Standard Library
import sqlite3

# connect to the database file and create a cursor object
connection = sqlite3.connect('maxdb')
cursor = connection.cursor()

# remove tables from the database, making it possible to start from scratch
# again whenever this Python script is executed
cursor.execute("""DROP TABLE IF EXISTS people;""")
cursor.execute("""DROP TABLE IF EXISTS stores;""")

# define the SQL command to create the table people
sql_command_create_table_people = """
CREATE TABLE people (
    name CHAR(10),
    hired DATE,
    store INTEGER,
    hourly BOOL
);"""

# execute the SQL command to create the table people
cursor.execute(sql_command_create_table_people)

# populate the table people with four records
cursor.execute("""INSERT INTO people
                          VALUES    ( 'topsy', '2012/11/01', 4, 0 ),
                                    ( 'max'  , '2012/02/14', 4, 0 ),
                                    ( 'zach' , '2009/03/24', 6, 0 ),
                                    ( 'sam'  , '2008/01/28', 6, 1 );""")

cursor.execute("""INSERT INTO   people(name, store)
                            VALUES  ('percy', 2),
                                    ('bailey', 2);""")

print('+--------------------------------------------------------------------+')
cursor.execute("""SELECT    name
                    FROM    people
                    WHERE   store = 4;""")

print("Print content of table people:")
result = cursor.fetchall()
for r in result:
    print(r)

print('+--------------------------------------------------------------------+')
cursor.execute("""
                SELECT * FROM people;
               """)

print("Print content of table people:")
result = cursor.fetchall()
for r in result:
    print(r)

print('+--------------------------------------------------------------------+')
cursor.execute("""SELECT *
                    FROM people
                    ORDER BY name;""")

print("Print content of table people:")
result = cursor.fetchall()
for r in result:
    print(r)

print('+--------------------------------------------------------------------+')
cursor.execute("""SELECT    name
                    FROM    people
                    WHERE   store > 2;""")

print("Print content of table people:")
result = cursor.fetchall()
for r in result:
    print(r)

print('+--------------------------------------------------------------------+')
cursor.execute("""SELECT    name
                    FROM    people
                    WHERE   name LIKE '%m%';""")

print("Print content of table people:")
result = cursor.fetchall()
for r in result:
    print(r)

print('+====================================================================+')
cursor.execute("""DELETE FROM    people
                    WHERE    name='bailey'
                        OR  name='percy';""")

cursor.execute("""UPDATE    people
                    SET hourly = TRUE
                    WHERE name = 'sam'
                        OR name = 'topsy';""")

cursor.execute("""UPDATE    people
                    SET hired = strftime('%Y/%m/%d', 'now')
                    WHERE   name='max';""")
print('!!!') ### different command for current time
print('+--------------------------------------------------------------------+')
cursor.execute("""
                SELECT * FROM people;
               """)

print("Print content of table people:")
result = cursor.fetchall()
for r in result:
    print(r)

print('+====================================================================+')
# define the SQL command to create the table people
sql_command_create_table_people = """
CREATE TABLE stores (
    name VARCHAR(20),
    number INTEGER,
    city VARCHAR(20));"""

# execute the SQL command to create the table people
cursor.execute(sql_command_create_table_people)

# populate the table people with four records
cursor.execute("""INSERT INTO stores
                          VALUES    ( 'headquarters', 4, 'new york'),
                                    ( 'max', 5, 'chicago'),
                                    ( 'zach', 5, 'san francisco');""")

print('+--------------------------------------------------------------------+')
cursor.execute("""
                SELECT * FROM stores;
               """)

print("Print content of table people:")
result = cursor.fetchall()
for r in result:
    print(r)

print('+--------------------------------------------------------------------+')

cursor.execute("""
                SELECT * 
                    FROM people, stores
                    WHERE store = number;
               """)

print("Print content of table people:")
result = cursor.fetchall()
for r in result:
    print(r)

print('+--------------------------------------------------------------------+')
cursor.execute("""
                SELECT  p.name,
                        city
                    FROM people p JOIN stores s
                    ON p.store = s.number;
               """)

print("Print content of table people:")
result = cursor.fetchall()
for r in result:
    print(r)

print('+--------------------------------------------------------------------+')
cursor.execute("""
                SELECT  *
                    FROM stores s JOIN people p
                    ON p.store = s.number;
               """)

print("Print content of table people:")
result = cursor.fetchall()
for r in result:
    print(r)

print('+--------------------------------------------------------------------+')
cursor.execute("""
                SELECT  name
                    FROM people
                    WHERE store = 
                        (SELECT number
                            FROM    stores
                            WHERE city = 'new york'
                        );
               """)
print("Print content of table people:")
result = cursor.fetchall()
for r in result:
    print(r)

print('+--------------------------------------------------------------------+')

# commit changes and close the connection to the database file
connection.commit()
connection.close()