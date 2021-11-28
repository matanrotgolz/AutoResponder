import csv
import csv
import regex as re
import readFile
import compare
import updateFile
import roeiham
import time
def writer(filename,header, newData,oldData, option):
        roeiham.test(filename,oldData)
        
        if option == "write":           
            emailListToWrite = newData[0][1]
            userNameListToWrite = newData[0][2]
            with open (filename, "w", newline = "") as csvfile:
                comapnyfile = csv.writer(csvfile)
                comapnyfile.writerow(header)
                for i in range(len(emailListToWrite)):
                    dataToWrite =[(userNameListToWrite[i],emailListToWrite[i])]
                    for data in dataToWrite:
                        comapnyfile.writerow(data)
        elif option == "update":
                updateFile.update(newData)
                


def checkValues(filename,data):
    #This funtion cheacking wheter the cliet data is already there by opening the file that contain the names and data
    #After that he is reading the names and email from the Company client data file and compare between the new emails and the on that already here
    #if he finds a diffrent he will add them to a new list and write them down
    newClientusernameList =[]
    newClientEmailList =[]
    emaildatafromexcel = []
    usenamedatafromexcel = []
    userCheckList = data[0][1]
    emailChecklist =data[0][0]
    with open(filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                 emaildatafromexcel.append(row[1])
                 usenamedatafromexcel.append(row[0])
    del usenamedatafromexcel[0]            
    del emaildatafromexcel[0]
        #After he is getting the relevent data from the comapny DB file , he will send them to a file that will find the diffrence
        #using method calles findeDiffrence
    newClientEmailList = compare.findDeffrence(emailChecklist,emaildatafromexcel)
    newClientusernameList  = compare.findDeffrence(userCheckList,usenamedatafromexcel)
    return newClientusernameList , newClientEmailList 
    






def main(filename,header,datatosend):
    nenewClientusernameList , newClientEmailList =checkValues(filename,datatosend)
    newdatatosend =  nenewClientusernameList +newClientEmailList
    writer(filename,header,newdatatosend,datatosend,  "update")



lineCount =0
excelName = "ComapnyDataexample1"
filename =  "C:\\Users\\matan\\OneDrive\\Desktop\\"+excelName+".csv"
header = ("clients name","clients Email","video")

def dataFromFile():
#First in this function ive read from a file (DB file), and sorted them between emails and name.
#After I return them
    UsernameList =[]
    emaiLList =[]
    dataList =readFile.readFile()
    string_check= re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    for data in dataList:
        if(string_check.search(data)==None):
            UsernameList.append(data)
        else:
            emaiLList.append(data)
    return emaiLList,UsernameList



def startThejob():
    emailList , userNameList  =dataFromFile()


    datatosend = [(emailList, userNameList)]
    main(filename,header,datatosend)

counter = 1

while True:
    print(" Startign the programe for the " + str(counter)+ " time!")
    startThejob()
    print("starting the timer...")
    time.sleep(5)
    counter = counter + 1

