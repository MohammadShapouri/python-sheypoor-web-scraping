import requests
from bs4 import BeautifulSoup
import pandas as pd 

url = 'https://www.sheypoor.com/s/iran/car'

# send request
session = requests.Session()
session.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'
response = session.get(url)

# check response
print("Status code:", response.status_code)

soup = BeautifulSoup(response.content, 'html.parser')

# create empty lists to store car data
car_names = []
car_prices = []


#search car
car_items = soup.find_all('div', class_='YPVjY _11d2x rj9VX Vt9Bv')
# found car
if car_items:
    try:
        print('-----------------------')
        for car in car_items:
            #extract car name
            name = car.find('h3', class_='_-8djc').text.strip()


            # extract car price and mileage
            # !!!!!!!!! price1 = car.find_all('div', class_='WQyDR') !!!!!!!!!
            price1 = car.find('div', class_='WQyDR')

            # !!!!!!!!! price = price1[1].text.strip() !!!!!!!!!
            price = price1.text.strip()

            # add data to lists
            car_names.append(name)
            car_prices.append(price)


            print('نام:', name)
            print('قیمت:', price)
            print('-----------------------')
    except AttributeError:
        print('Done!')
    else:
        print('Done!')
else:
    print('WARNING!', "No car found!")

# create a dictionary with the data
data = {'نام': car_names, 'قیمت': car_prices}

# create a dataframe from the dictionary
df = pd.DataFrame(data)

# save the dataframe to a csv file
df.to_csv('cars0.csv', index=False, encoding='utf-8-sig')
