import matplotlib.pyplot as plt
import pandas as pd
import json
import numpy as np
import csv

csvFilePath = "csvData.csv"


# reading csv file and append to the file_data..
filter_data = []
with open(csvFilePath) as  csvfile:
    csvReader = csv.DictReader(csvfile)
    for csvRow in csvReader:
      del csvRow['sr.no']
      del csvRow['Cmpany']
      del csvRow['Data1']
      del csvRow['Data2']
      del csvRow['Data3']
      del csvRow['Data4']
      del csvRow['Data5']
      del csvRow['Data6']
      

      data7 = int(csvRow['Data'])
      csvRow["Int_data"] = data7
      del csvRow['Data']
      
      filter_data.append(csvRow)



with open('main.json', 'w') as jsonFile:
    jsonFile.write(json.dumps(filter_data, indent=4))  
    
f = open('main.json')
jsondata_file = json.load(f)
        
### store all data into dataFram ..

df = pd.DataFrame.from_dict(jsondata_file)

#convert data  into numpy array.. 
np_array = df.to_numpy()


Name = []
Performance = []

for i in np_array:
  name = (i[0])
  Name.append(name)

for i in np_array:
    data_1= (i[1])
    Performance.append(data_1)


x = Name
y = Performance
##########################for pie chart########################


plt.subplot(121)
plt.pie(y,labels=x,radius=1.2,autopct='%0.02f%%',shadow=True,explode = None)

#############################for bar chart ###################


plt.subplot(122)
plt.bar(x,y)

plt.show()


