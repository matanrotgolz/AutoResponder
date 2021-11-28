from csv import writer
excelName = "ComapnyDataexample1"
filename =  "C:\\Users\\matan\\OneDrive\\Desktop\\"+excelName+".csv"
# List 



def update(data):
    data.sort()
    # Open our existing CSV file in append mode
    # Create a file object for this file
    i = len(data)-1
    with open(filename, 'a',newline="") as f_object:
        writer_object = writer(f_object)
        while i >=0 :
                if(i % 2 == 0):
                        tempdata = [data[i],data[i+1],0]
                        writer_object.writerow(tempdata)
                i = i -1 
        # Pass this file object to csv.writer()
        # and get a writer object
        
  
        # Pass the list as an argument into
        # the writerow()
        
  
        #Close the file object
    f_object.close()

