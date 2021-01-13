import csv
import re
from datetime import datetime

startTime = datetime.now()

with open('t8.shakespeare.txt', 'r') as file :
    filedata = file.read()
  

with open('french_dictionary.csv', 'r') as file,open('result.csv', 'w', newline='') as file1:
    reader = csv.reader(file)
    writer = csv.writer(file1)
    writer.writerow(["English", "French", "Occurence"])
    l=[]
    for row in reader:
        writer.writerow([row[0],row[1],filedata.count(row[0])])
        src_str  = re.compile(row[0], re.IGNORECASE)
        filedata = src_str.sub(row[1],filedata)

with open('file.txt', 'w') as file:
    file.write(filedata)
print("Number of occurrences was saved in the result.csv file")
print("Time taken to execute this program : ",datetime.now()-startTime)
