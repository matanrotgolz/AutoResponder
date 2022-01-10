import csv
import write
import Company_Email_Controll_Pannel
def test(filename,data):
    r = csv.reader(open(filename))
    lines = list(r)
    for i in range(1,len(lines)):
            for j in range(len(data)):
                if lines[i][1]in data [j][0]:
                    if(int(lines[i][2]) == 10):
                        number = 0
                        lines[i][2] = number 
                        write.openAndWrite(filename,lines)
                    else:
                        Company_Email_Controll_Pannel.readAndSend(lines[i][1],lines[i][0],int(lines[i][2]))
                        number = int (lines[i][2]) +1
                        lines[i][2] = number
                        print("OK")
                        write.openAndWrite(filename,lines)

