import os
import sys
import requests
from openpyxl import load_workbook




def downloadImage(url , index):
        
    image = requests.get(url)

    file = open("image_" + str(index) + ".jpeg" , "wb")
    file.write(image.content)
    file.close()

par_path = "/Users/rthre/Desktop/Alan_Gamez"

ex_file = 'propiedades.xlsx'
wb = load_workbook(ex_file)
sheet = wb.get_sheet_by_name('Worksheet1')

for x in range(55):
    
    path = "/Users/rthre/Desktop/Alan_Gamez/Propiedad_"+str(x+1)

    


    links = sheet['AC' + str(x+2)].value.split(',')

    os.mkdir(path)
    os.chdir(path)


    i=1
    for link in links:
        downloadImage(link , i)
        i = i+1

    os.chdir(par_path)