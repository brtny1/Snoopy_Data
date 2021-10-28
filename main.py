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

