from bs4 import BeautifulSoup
import requests
import pickle

#A function that takes a decimal (0-16) and returns hex value (0-f)
def singleHex(decimal):
    return '0123456789abcdef'[decimal]

response = requests.get('http://www.cs.utsa.edu/~wagner/laws/FFM.html')
data = response.text
soup = BeautifulSoup(data, 'lxml')
table = soup.find_all('center')[-1].find('table')

#The dictionary that will hold the 2^8 multiplicative inverse values
mulInv = {}

rowKey = 0
for row in table.find_all('tr')[4:]:
    temp = {}

    colKey = 0
    for val in row.find_all('td'):
        temp[singleHex(colKey)] = val.text.replace('\xa0', '')
        colKey += 1
    mulInv[singleHex(rowKey)] = temp
    rowKey += 1

#0 has no inverse so let it be 0
mulInv['0']['0'] = '00'

#Saving the dictionary to a file so that it can be used in other programs
with open('Multiplicative-Inverse', 'wb') as file:
    pickle.dump(mulInv, file)
