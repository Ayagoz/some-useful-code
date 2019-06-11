import urllib
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import wget
import sys

itas2017 = 'http://itas2017.iitp.ru/papers/'

data = []
authors=[]
response = urllib.request.urlopen(itas2017)
soup = BeautifulSoup(response, 'html.parser')
papers = soup.text.split('"id"')


path_save = sys.argv[1]
for p in papers[1:]:
    try:
        url = itas2017[:-8] + p.split('"pdf"')[1].split('.pdf')[0][3:] + '.pdf'
        info = p.split('"abstract"')[1].split('"title"')[1]
        info2 = info.split('"all_authors"')
        title = bytes(info2[0], 'utf-8').decode('unicode_escape')
        for t in title.split('"'):
            if len(t)> 7:
                main_title = t
        if len(main_title) > 60:
            main_title = main_title[:60]
        print(main_title)
        wget.download(url, path_save + main_title + '.pdf')
    except:
        pass
