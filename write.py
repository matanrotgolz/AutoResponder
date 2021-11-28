import csv
def openAndWrite(filename,data):
     writer = csv.writer(open(filename,'w',newline=""))
     writer.writerows(data)