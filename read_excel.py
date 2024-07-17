import pandas as pd
import numpy as np
# import requests
# import re

from bookcat.models import Book

xls = pd.read_excel('Vergil.xlsx', header=0)

# out = xls.drop(labels = 'Title/Description (Print – Original):',axis = 1).astype(str).groupby(xls['Title/Description (Print – Original):'].mask(xls['Title/Description (Print – Original):']=='+++++').ffill()).agg(', '.join).reset_index()

for i in range (len(out)):
    if (out['Unnamed: 0'][i].find(",")>=0):
        out.loc[i, "Unnamed: 0"] = out.loc[i, "Unnamed: 0"].split(',')[0]
out['Unnamed: 0'] = pd.to_numeric(out['Unnamed: 0'])
xls = out.sort_values(by='Unnamed: 0')
xls.head(30)

books = []

for i in range (len(xls)):
    loc = xls.loc[i, 'Location:']
    loc_code = xls.loc[i, 'Location Code:']
    call_num = xls.loc[i, 'Call Number:']
    category = xls.loc[i,'Category (Print):']
    title = xls.loc[i, 'Title/Description (Print – Original):']
    
    cont = ''
    if (xls.loc[i, "Author (Modern):"].find('virgil')>=0):
        cont = "Publius Vergilius Maro"
        if (xls.loc[i, "Contributors:"] != ' '):
            cont += ", "
    if (xls.loc[i, "Contributors:"] != ' '):
            cont += xls.loc[i, "Contributors:"]
    if (xls.loc[i, "Publisher:"] != ' '):
        if (cont!=''):
            cont += ", "
        cont += xls.loc[i, "Publisher:"]

    # print(cont)
            
    barcodes = xls.loc[i, 'Barcodes:']
    date = xls.loc[i, 'Date (Print):']
    publisher = xls.loc[i,'Publisher:']
    lang = xls.loc[i,'Language:']
    bmcat = xls.loc[i,'B. M. Cat. (1882):']
    note = xls.loc[i,'Notes:']

    books.append(Book(title_description = title, contributors = cont, date = date, publisher = publisher, category = category, language = lang, call_num = call_num, barcode = barcodes, loc_code = loc_code, BM_cat = bmcat))

for book in books:
    my_product = book
    my_product.save()

    
import pandas as pd
from bookcat.models import Book
xls = pd.read_excel('Vergil.xlsx', header=0)
 for i in range (len(xls)):
     loc = xls.loc[i, 'Location:']
     loc_code = xls.loc[i, 'Location Code:']
     call_num = xls.loc[i, 'Call Number:']
     category = xls.loc[i,'Category (Print):']
     title = xls.loc[i, 'Title/Description (Print – Original):']
     cont = ''
     if (xls.loc[i, "Author (Modern):"].find('virgil')>=0):
             cont = "Publius Vergilius Maro"
             if (xls.loc[i, "Contributors:"] != ' '):
                     cont += ", "
     if (xls.loc[i, "Contributors:"] != ' '):
             cont += xls.loc[i, "Contributors:"]
     if (xls.loc[i, "Publisher:"] != ' '):
             if (cont!=''):
                     cont += ", "
             cont += xls.loc[i, "Publisher:"]
     barcodes = xls.loc[i, 'Barcodes:']
     date = xls.loc[i, 'Date (Print):']
     publisher = xls.loc[i,'Publisher:']
     lang = xls.loc[i,'Language:']
     bmcat = xls.loc[i,'B. M. Cat. (1882):']
     note = xls.loc[i,'Notes:']
     books.append(Book(title_description = title, contributors = cont, date = date, publisher = publisher, category = category, language = lang, call_num = call_num, barcode = barcodes, loc_code = loc_code, BM_cat = bmcat))