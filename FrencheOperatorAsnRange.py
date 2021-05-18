#  operateur pas hebergeur 
from types import MappingProxyType
from typing import Text
import requests
from bs4 import BeautifulSoup
import re
import os

FrenchOperator = ["Free", "Orange", "Bouygue", "SFR", #france
"VITI", "PACIFIC MOBILE TELECOM", #polynesie fr 
"WAYSCOM", "GUYACOM", "SOCIETE PUBLIC LOCALE POUR LAMENAGEMENT NUMERIQUE DE LA GUYANE", # guyane fr
"Dauphin Telecom Guadeloupe", "Southern Caribbean Fiber", "Global Caribbean Network", # guadeloupe
"Outremer Telecom SASU", "DIGICEL ANTILLES FRANCAISES GUYANE SA", # martinique
"SOCIETE REUNIONNAISE DU RADIOTELEPHONE SCS", "Reunicable SAS", "TELCO OI SAS",  # reunion 
"Guyana Telephone & Telegraph Co.", "E-Networks Inc.", "U Mobile (Cellular) Inc.", "Atlantic Wireless Network Inc.", # guyane
"STOI Internet", # Mayotte
"Office des Postes et Telecommunications New-Caledonia", "OFFRATEL", "CANL", "TeleNet", "Micro Logic Systems", "Nautile", "" # new caledonie
"SBFWI","ST BARTH TELECOM", # Saint Barthélemy 
"Dauphin Telecom", "THDTEL",   # Saint martin
"SPM TELECOM", # Saint Pierre and Miquelon
"Orange Wallis", # Wallis and Futuna
]
# Free, Bouygue, Orange, SFR,

def cropIP(asline):
    os.system("whois -h whois.radb.net -- '-i origin "+asline.replace('/','')+"' | grep -Eo '([0-9.]+){4}/[0-9]+' | tee output.txt")

def countries():
    frcountries = ["fr", "pf", "gf", "gp", "mq", "re", "gy", "yt", "nc", "bl", "mf", "pm", "wf"]
    for i in frcountries:
        getAS(i)

def getAS(countrie):
    URL_Get_AS = "https://ipinfo.io/countries/"+countrie
    r = requests.get(URL_Get_AS)
    soup = BeautifulSoup(r.text, 'html.parser')
    cpt = 1
    for myas in soup.find_all('td'):
        for line in myas :
            #format : AS nom nbip
            if cpt == 1 :
                soup2 = BeautifulSoup(Text(line), 'html.parser')
                asline = soup2.a.get('href')
                cpt = 2
            elif cpt == 2 :
                nameline = line
                cpt = 3 
            elif cpt == 3 :
                nbipline = line
                cpt = 1
                for name in FrenchOperator:
                    if re.search(name, nameline, re.IGNORECASE):
                        cropIP(asline)

def main():
    countries()

if __name__ == '__main__':
    main()