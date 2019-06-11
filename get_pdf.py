import wget
import pandas as pd
import sys 

path_excel = str(sys.argv[1])
path_save = str(sys.argv[2])
i = 0
data = pd.read_excel(path_excel)
print('Beginning file download with wget module')
for url in data.url[i:]:
	title =  str(data.iloc[i].titles)
	try:
		wget.download(url, path_save +title[:20]+'.pdf')
		i+=1	
	except:
		i+=1
