#PLOTTING SNOOPY DATA

#convert TXT to CSV:
import csv

#Read tab-delimited file:
with open("FilterOff_OpenWindow.TXT" , 'r') as txtFile:
  txt2list = csv.reader(txtFile, delimiter = "\t")
  #Creating 2D array with data from txt file:
  """ 
  data = []
  for row in txt2list:
      data.append(row)
  print(data)
  """
  #rewriting lines 11 to 13 using list comprehension:
  data = [row for row in txt2list]
    
# write to comma-delimited file:
with open("FilterOff_OpenWindow.csv", 'w') as csvFile:
  # creating csv file:
  list2csv = csv.writer(csvFile, quotechar='', quoting=csv.QUOTE_NONE)
  # adding each sublist from the data array to a seperate row in csvFile:
  list2csv.writerows(data)

# plot data:
import matplotlib.pyplot as plt 
import pandas
#in order to import pandas, first click on the cube in the left pane, type pandas in the search box, and then click the plus sign by 'pandas'

# Create a data frame (df) from the csv file using pandas's read_csv() method:
df = pandas.read_csv("FilterOff_OpenWindow.csv")
#print(df)

minutes = []
pm1 = []
pm2_5 = []
pm10 = []
tvoc = []
co2 = []

# loop over the rows in the data frame using iterrows() method:
for index,row in df.iterrows():
    minutes.append(row["#"])
    pm1.append(row["PM1.0"])
    pm2_5.append(row["PM2.5"]) 
    pm10.append(row["PM10.0"])
    tvoc.append(row["TVOC(ppb)"])
    co2.append(row["CO2(ppm)"])

#plotting pollen:
plt.plot(minutes, pm1, color = "yellow")
plt.plot(minutes, pm2_5, color = "orange")
plt.plot(minutes, pm10, color = "red")
# labels for x and y axis:
plt.xlabel("Minutes")
plt.ylabel("PPM (particles per million parts of air)")
#title of the graph:
plt.title("Pollen & Dust")
plt.show()

