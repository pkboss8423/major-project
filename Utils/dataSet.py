import csv
import os

from requests import head

from Utils.createFolder import create_data_sets

#this functions reads the compression ratio column of the dataset and converts it into an array
def check_cr(path):
    filename = open(path)
    file = csv.DictReader(filename)
    Comp_ratio = []
    for col in file:
        Comp_ratio.append(col['Compression ratio'])
    return Comp_ratio

#to reduce duplication
def check(path):
    filename=open(path)
    file = csv.DictReader(filename)
    files = []
    
    for col in file:
        files.append(col['File Name'])
        
    return files


#this function adds another row to an existing dataset or creates a new dataset if not present    
def add_row(row,type):
    header = ['File Name', 'Original Size(MB)',
              'Compressed Size(MB)', 'Compression ratio']
    x=create_data_sets()
    filename = f"{type}_dataset.csv"
    path=os.path.join(x,filename)
    if os.path.exists(path)==True:
        l=check(path)
        with open(path, 'a') as csvfile:
            # creating a csv writer object
            
             
            csvwriter = csv.writer(csvfile)
            # writing the data rows
            if row[0] not in l:
                csvwriter.writerow(row)
            csvfile.close()
      
        
    else:
        with open(path, 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)

            writer.writerow(header)

            writer.writerow(row)
       
        
    return path