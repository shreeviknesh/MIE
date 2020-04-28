from bs4 import BeautifulSoup
import requests
import pickle

response = requests.get('http://www.cs.utsa.edu/~wagner/laws/FFM.html')
data = response.text
soup = BeautifulSoup(data, 'lxml')
table = soup.find_all('center')[-1].find('table')

#The list that will hold the 2^8 multiplicative inverse values
mulInv = []
for row in table.find_all('tr')[4:]:
    temp = []
    for val in row.find_all('td'):
        value = val.text.replace('\xa0', '')
        if value == 'XX':
            value = '0'
        temp.append(int(value, 16))
    mulInv = mulInv + temp

#Saving the list to a file so that it can be used in other programs
with open('Multiplicative-Inverse', 'wb') as file:
    pickle.dump(mulInv, file)
