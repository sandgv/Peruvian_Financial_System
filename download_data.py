# -*- coding: utf-8 -*-
"""
Created on Thu Mar 20 10:13:29 2025

@author: sandg
"""

# Import necesary library to download information from URL
import requests


##### Download Banks data from the SBS website

month_info={
    "di": "Diciembre",
    }
for year in [2024]:
    
    for mo,month in month_info.items():
        
        for archi in [2201,2314]:
        
            url=f"https://intranet2.sbs.gob.pe/estadistica/financiera/{year}/{month}/B-{archi}-{mo}{year}.XLS" 
            res=requests.get(url)
        
        
            fh=open(f"Input/B-{archi}-{mo}{year}.xlsx",mode="wb")
            fh.write(res.content)
            fh.close()

month_info={
    "di": "Diciembre",
    }
for year in [2024]:
    
    for mo,month in month_info.items():
        
        url1=f"https://intranet2.sbs.gob.pe/estadistica/financiera/{year}/{month}/B-2359-{mo}{year}.XLS" 
        res=requests.get(url1)
        
        
        fh=open(f"Input/B-2359-{mo}{year}.xls",mode="wb")
        fh.write(res.content)
        fh.close()


######### Download Financial Companies data from the SBS website
month_info={
    "di": "Diciembre",
    }
for year in [2024]:
    
    for mo,month in month_info.items():
        
        for archi in [3101,3254,3272]:
        
            url=f"https://intranet2.sbs.gob.pe/estadistica/financiera/{year}/{month}/B-{archi}-{mo}{year}.XLS" 
            res=requests.get(url)
        
        
            fh=open(f"Input/B-{archi}-{mo}{year}.xlsx",mode="wb")
            fh.write(res.content)
            fh.close()
 
    
######## Download CMACs data  from the SBS website
           
month_info={
     "di": "Diciembre",
     }

for year in [2024]:
     
     for mo,month in month_info.items():
         
         for archi in [1101,1213,1261]:
         
             url=f"https://intranet2.sbs.gob.pe/estadistica/financiera/{year}/{month}/C-{archi}-{mo}{year}.XLS" 
             res=requests.get(url)
         
         
             fh=open(f"Input/C-{archi}-{mo}{year}.xls",mode="wb")
             fh.write(res.content)
             fh.close()
                        

######### Download CRACs data from the SBS website
month_info={
     "di": "Diciembre",
     }

for year in [2024]:
     
     for mo,month in month_info.items():
         
         for archi in [2101,2213,2264]:
         
             url=f"https://intranet2.sbs.gob.pe/estadistica/financiera/{year}/{month}/C-{archi}-{mo}{year}.XLS" 
             res=requests.get(url)
         
         
             fh=open(f"Input/C-{archi}-{mo}{year}.xls",mode="wb")
             fh.write(res.content)
             fh.close()            
            
            
######## Download population by region data from the INEI

import requests

url_inei="https://www.inei.gob.pe/media/MenuRecursivo/indices_tematicos/proy_04_4.xls"

#"https://www.inei.gob.pe/media/MenuRecursivo/indices_tematicos/proy_04_4.xls"
res=requests.get(url_inei)


        
fh=open("Input/proy_04_4.xls",mode="wb")
fh.write(res.content)
fh.close()



            