import csv
with open('SOCR-HeightWeight.csv', newline='') as f:
    reader = csv.reader(f)
    fileData=list(reader)
fileData.pop(0)
newData=[]
for i in range(len(fileData)):
    num=fileData[i][1]
    newData.append(float(num))
total = 0
n=len(newData)
for x in newData:
    total+=x
mean = total/n
print('Mean: ' + str(mean))