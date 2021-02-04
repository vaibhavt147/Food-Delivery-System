#Initialising database
#Run this file only at time==0, when this app is brought into the market.

import pandas as pd

menu = pd.DataFrame(columns = ['resto_name', 'dish_name', 'cuisine', 'price'])

orders = pd.DataFrame(columns = ['resto_name', 'dish_name', 'username', 'status'])

users = pd.DataFrame(columns = ['username', 'password', 'name', 'phone', 'address', 'email_id'])

restos = pd.DataFrame(columns = ['username', 'password', 'resto_name', 'max_n', 'curr_n'])

menu.to_csv('menu.csv',index = False)
orders.to_csv('orders.csv',index = False)
users.to_csv('users.csv',index = False)
restos.to_csv('restos.csv',index = False)
