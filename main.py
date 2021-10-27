#PLOTTING SNOOPY DATA

#convert TXT to CSV:
import csv

#Read tab-delimited file:
with open("FilterOff_OpenWindow.TXT" , 'r') as txt:
    txt2csv = csv.reader(txt, delimiter = "\t")
    #Creating 2D array with data from txt file:
    """ 
    data = []
    for row in txt2csv:
        data.append(row)
    print(data)
    """
    #rewriting lines 11 to 13 using list comprehension:
    data = [row for row in txt2csv]
    
