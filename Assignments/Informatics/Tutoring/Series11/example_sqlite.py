# import the necessary modules
import csv, sqlite3

if __name__ == '__main__':
    # open and read csv file
    infile = open('gwas_associations.csv', 'r', encoding='utf-8')
    data_reader = csv.reader(infile, delimiter=',')
    # we move the reader to the line after the header (column names) since
    # we are going to create the column names using the sql command below
    _ = next(data_reader, None)

    # connect to the sqlite database
    conn = sqlite3.connect('gwas_associations.db')
    # get the current cursor
    cursor = conn.cursor()

    # run an sql command to remove an already existing association table
    cursor.execute("""DROP TABLE IF EXISTS association;""")

    # create an sql command to create the association table
    create_table_sql_cmd = """
    CREATE TABLE association (
                            'DATE ADDED TO CATALOG' DATE,
                            PUBMEDID INTEGER,
                            AUTHOR CHAR,
                            DISEASE VARCHAR,
                            PVALUE VARCHAR,
                            PVALUE_MLOG VARCHAR,
                            CI VARCHAR);
    """

    # execute the above sql command to create an association table
    cursor.execute(create_table_sql_cmd)

    # insert records into the association table
    insert_records = """INSERT INTO association(
                                            'DATE ADDED TO CATALOG',
                                            'PUBMEDID', 
                                            'AUTHOR', 
                                            'DISEASE', 
                                            'PVALUE', 
                                            'PVALUE_MLOG', 
                                            'CI')
                          VALUES (?, ?, ?, ?, ?, ?, ?)"""

    cursor.executemany(insert_records, data_reader)

    # select all the records (rows) from the association table (no fields are left out)
    cursor.execute("SELECT * FROM association;")

    # print some information about the results obtained for the previous query
    col_names = [col[0] for col in cursor.description]
    print(col_names)
    records = cursor.fetchall()

    # print the first 10 records (rows)
    for record in records[:10]:
        print(record)

    print("number of rows: {}".format(len(records)))

    # save all changes made to the database
    conn.commit()

    # close the database and disconnect
    conn.close()

    # close the csv file
    infile.close()