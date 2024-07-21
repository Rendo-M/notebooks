from bs4 import BeautifulSoup
import requests

url = 'https://benchmark.best/ru/cpu_table.html'
columns = [
'yearofprod',
'cpusocket',
'cpucore', 
'numofcores,numofthreads',
'basefreq',
'turbofreq',
'cachel1',
'cachel2',
'cachel3',
'graphics',
'memorycontroller',
'pciecontroller',
'lithography',
'tdp',
'cpucategory'
]

results = []
col1 = columns[0]
col2 = columns[1]
col3 = columns[2]
req_url = url +f'?td2={col1}&td3={col2}&td4=tdp{col3}'
page = requests.get(req_url)
soup = BeautifulSoup(page.text, "html.parser")
soup = soup.find('tbody', id='cpus')
all_rows = soup.find_all('tr')
s = ('position;name;cheke;perfomance;'+col1+';'+col2+';'+col3)
results.append(s)
for row in (all_rows):
        data_list = row.find_all('td')
        s = ';'.join([data.text for data in data_list])
        results.append(s)
      

for i in range(3,15,3):
    col1 = columns[i]
    col2 = columns[i+1]
    col3 = columns[i+2]
    req_url = url +f'?td2={col1}&td3={col2}&td4={col3}'
    page = requests.get(req_url)
    soup = BeautifulSoup(page.text, "html.parser")
    soup = soup.find('tbody', id='cpus')
    all_rows = soup.find_all('tr')
    s = (';'+col1+';'+col2+';'+col3)
    results[0]+= s
    j = 1
    for row in all_rows:
            data_list = row.find_all('td')
            s = ';'+';'.join([data.text for data in data_list][4:])
            results[j] += ''.join(char for char in s if ord(char) >= 30)   
            j += 1
results = [s+'\n' for s in results]            
with open('processors.csv', 'w', encoding='utf-8') as f:
    f.writelines(results)            