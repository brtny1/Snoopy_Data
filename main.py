#PLOTTING SNOOPY DATA

#convert TXT to CSV:
import csv

#Read tab-delimited file:
with open("FilterOff_OpenWindow.TXT" , 'r') as txt:
  txt2csv = csv.reader(txt, delimiter = "\t")
