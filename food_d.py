import pandas as pd
from resto import resto
from user import user
from log_sign_in import login, sign_in

restos = pd.read_csv('restos.csv')
users = pd.read_csv('users.csv')
menu = pd.read_csv('menu.csv')
orders = pd.read_csv('orders.csv')

i = sign_in(restos,users,menu,orders)