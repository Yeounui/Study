# import the necessary modules
import csv  # module to read from and write to csv files
import pprint as pp


def extract_relevant_cols(csv_file):
    with open(csv_file, "r") as infile:
        csv_reader = csv.reader(infile, delimiter=',')
        lines = [line if len(line) == 5 else line[:5] for line in csv_reader]
    return lines


def write_to_csv_file(csv_file, data):
    with open(csv_file, 'w', newline='') as outfile:
        csv_writer = csv.writer(outfile)
        csv_writer.writerows(data)


if __name__ == "__main__":

    # open csv file and extract relevant columns
    data1 = extract_relevant_cols("./gwas_ancestry_01.csv")
    data2 = extract_relevant_cols("./gwas_ancestry_02.csv")

    # ensure the column headings are the same
    assert data1[0] == data2[0], 'ensure that the columns match'

    # merge the two collections of data records
    data = data1 + data2[1:]
    print("length of cleaned data: {}".format(len(data)))

    # remove rows with any 'NA' values
    # cleaned_rows = []
    # for row in data:
    #     if 'NA' in row:
    #         continue
    #     else:
    #         cleaned_rows.append(row)
    cleaned_rows = [row for row in data if 'NA' not in row]

    # print out some information about the data
    print("length of uncleaned data: {}".format(len(cleaned_rows)))
    pp.pprint(cleaned_rows[:10])

    # write processed data back to a csv file
    write_to_csv_file("cleaned_gwas_ancestry.csv", cleaned_rows)