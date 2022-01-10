import csv
filename =  "C:\\Users\\Root\\To\\File\\"+"TESTFILE2"+".csv"
def readFile ():
    Datalist =[]
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            Datalist.append(row[3])
    return Datalist
















