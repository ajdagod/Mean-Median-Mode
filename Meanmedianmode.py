import csv
with open('Height-Weight.csv',newline='') as f:
    reader=csv.reader(f)
    file_data=list(reader)

file_data.pop(0)

new_data=[]
for i in range(len(file_data)):
    n_numb=file_data[i][1]
    new_data.append(float(n_numb))

n=len(new_data)
total=0
for x in new_data:
    total+=x

mean=total/n

print(" mean or averages "+str(mean))

with open('Height-Weight.csv',newline='') as f:
    reader=csv.reader(f)
    file_data=list(reader)

file_data.pop(0)

new_data=[]
for i in range(len(file_data)):
    n_numb=file_data[i][1]
    new_data.append(float(n_numb))

n=len(new_data)
new_data.sort()

if n%2==0:
    median1=float(new_data[n//2])
    median2=float(new_data[n//2-1])
    median=(median1+median2)/2

else:
    median=new_data[n//2]
    print(n)
    
print(" median is "+str(median))

from collections import Counter
import csv
with open('Height-Weight.csv',newline='') as f:
    reader=csv.reader(f)
    file_data=list(reader)

file_data.pop(0)

new_data=[]
for i in range(len(file_data)):
    n_numb=file_data[i][1]
    new_data.append(float(n_numb))

data=counter(new_data)
mode_data_for_range={
    "50-60":0,
    "60-70":0,
    "70-80":0
    }
for Height,occurence in data.items():
    if 50<float(Height)<60:
        mode_data_for_range["50-60"] += occurence
    elif 60<float(Height)<70:
        mode_data_for_range["60-70"] += occurence
    elif 70<float(Height)<80:
        mode_data_for_range["70-80"] += occurence

mode_range,mode_occurence=0,0
for range,occurence in mode_data_for_range.items():
    if occurence>mode_occurence:
        mode_range,mode_occurence=[int(range.split("-")[0]),int(range.split("-")[1])],occurence
mode=float((mode_range[0]+mode_range[1])/2)
print(f"Mode is -> {mode:2f}")