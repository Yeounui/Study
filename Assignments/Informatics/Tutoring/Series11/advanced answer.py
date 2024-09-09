import csv, sqlite3

with open('gwas_associations.csv', 'r', encoding='utf-8') as opencsv:
    readcsv = csv.reader(opencsv, delimiter=',')
    _ = next(readcsv, None)

    conn = sqlite3.connect('gwas_associations.db')
    cursor = conn.cursor()

    cursor.execute("""DROP TABLE IF EXISTS association;""")

    cursor.execute("""CREATE TABLE association (
                                    'DATE ADDED TO CATALOG' DATE,
                                    PUBMEDID INTEGER,
                                    AUTHOR CHAR,
                                    DISEASE VARCHAR,
                                    PVALUE VARCHAR,
                                    PVALUE_MLOG VARCHAR,
                                    CI VARCHAR);
                            """)

    iterate_record = """INSERT INTO association(
                                    'DATE ADDED TO CATALOG',
                                    'PUBMEDID', 
                                    'AUTHOR', 
                                    'DISEASE', 
                                    'PVALUE', 
                                    'PVALUE_MLOG', 
                                    'CI')
                                    VALUES (?, ?, ?, ?, ?, ?, ?)"""
    cursor.executemany(iterate_record, readcsv)

    cursor.execute("""SELECT *
                                FROM association;""")

    records = cursor.fetchall()
    for record in records[:10]:
        print(record)

    print("number of rows: {}".format(len(records)))

    conn.commit()
    conn.close()



with open('cleaned_gwas_ancestry.csv', 'r') as opencsv:
    readcsv = csv.reader(opencsv, delimiter=',')
    _ = next(readcsv, None)

    conn = sqlite3.connect('gwas_associations.db')
    cursor = conn.cursor()

    cursor.execute("""DROP TABLE IF EXISTS ancestry;""")

    cursor.execute("""create table ancestry (PUBMEDID integer, 'FIRST AUTHOR' CHAR,
                                    CATEGORY VARCHAR,
                                    'COUNTRY OF ORIGIN' VARCHAR,
                                    'COUNTRY OF RECRUITMENT' VARCHAR);
                    """)

    iterate_record = """INSERT INTO ancestry(
                                    'PUBMEDID', 
                                    "FIRST AUTHOR", 
                                    CATEGORY, 
                                    "COUNTRY OF ORIGIN",
                                    "COUNTRY OF RECRUITMENT")
                                VALUES (?, ?, ?, ?, ?);
        """
    cursor.executemany(iterate_record, readcsv)

    cursor.execute("""SELECT *
                            FROM association
                        WHERE PUBMEDID IN
                        (SELECT PUBMEDID FROM ancestry
                        WHERE "COUNTRY OF ORIGIN" LIKE "Mexico%")
                        """)

    records = cursor.fetchall()
    for record in records:
        print(record)

    print("number of rows: {}".format(len(records)))

    conn.commit()
    conn.close()
