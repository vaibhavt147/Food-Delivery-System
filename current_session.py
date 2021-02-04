#Start with python3 set.py You need to do it only for the first time you open the terminal. For next times, don't run this commmand
#ipython
#Comments are inputs provided

import pandas as pd
from resto import resto
from user import user
from log_sign_in import login, sign_in,logout

restos = pd.read_csv('restos.csv')
users = pd.read_csv('users.csv')
menu = pd.read_csv('menu.csv')
orders = pd.read_csv('orders.csv')
import pandas as pd
from resto import resto
from user import user
from log_sign_in import login, sign_in

restos = pd.read_csv('restos.csv')
users = pd.read_csv('users.csv')
menu = pd.read_csv('menu.csv')
orders = pd.read_csv('orders.csv')

i = sign_in(restos,users,menu,orders)
# hotel_vaibhav hotel@vaibhav
# 0
profile = resto(restos,menu,orders,i)
profile.update()
# Hotel Vaibhav
# Press enter to skip
# 2
# 0
profile.add_menu("Zunka Bhakar",150,"Maharashtrian")
profile.add_menu("Puran Poli",100,"Maharashtrian")
profile.add_menu("Dosa",100,"South Indian")
profile.add_menu("Idli",100,"South Indian")
profile.add_menu("Dal Makhani",100,"North Indian")
profile.add_menu("Dal Bati",100,"North Indian")
del profile

i = sign_in(restos,users,menu,orders)
# hotel_parag hotel@parag
# 0
profile = resto( restos, menu, orders, i)
profile.update()
# Hotel Parag
# Press Enter
# 3
# 0
profile.add_menu('Chole Kulche',100,'Punjabi')
profile.add_menu('Tandoori Chicken',100,'Punjabi')
profile.add_menu('Dal Bati',60,'North Indian')
profile.add_menu('Paratha',30,'North Indian')
del profile

i = sign_in(restos,users,menu,orders)
# vaibhav_takale vaibhav@takale
# 1
profile = user(users, restos, menu, orders, i) 
profile.update()
# Vaibhav Takale
# Press Enter
# 9876543210
# Pandharpur
# vafdasjkl@dfas.com
profile.get_profile()
profile.search("Hotel Vaibhav")
profile.search("Hotel Parag")
profile.search("North Indian")
profile.search("Dal Bati")
profile.order(5)
profile.get_profile()
profile.get_profile(8)
profile.order(8)
profile.get_profile()
profile.search("")
profile.order(1)
profile.order(2)
profile.get_profile()
del profile

i = login(restos,users,menu,orders)
# hotel_vaibhav hotel@vaibhav
profile = resto(restos, menu, orders, i)
profile.pending_orders()
profile.change_status(2,'Out for Delivery')
profile.pending_orders()
profile.change_status(2,'Delivered')
profile.pending_orders()
profile.pending_orders(3,'Success')
profile.change_status(3,'Success')
profile.pending_orders()
del profile

i = login(restos,users,menu,orders)
# vaibhav_takale vaibhav@takale
profile = user(users, restos, menu, orders, i)
profile.get_profile()
profile.update()
# Press Enter
# takale@vaibhav
# Press Enter
# Press Enter
# Press Enter
del profile

i = login(restos,users,menu,orders)
# vaibhav_takale takale@vaibhav
profile = user(users, restos, menu, orders, i)
del profile

i = sign_in(restos,users,menu,orders)
# nitin_takale nitin@takale
profile = user(users, restos, menu, orders, i)
profile.update()
# Nitin Takale
# Press enter
# 1234567890
# Pune
# fdaslk@er.com
profile.search("")
profile.order(6)
profile.order(7)
profile.order(8)
profile.get_profile()
profile.order(1)
profile.get_profile()
del profile

i = login(restos,users,menu,orders)
# hotel_parag hotel@parag
profile = resto(restos, menu, orders, i)
profile.pending_orders()
profile.change_status(4,'Out for Delivery')
profile.change_status(5,'Out for Delivery')
profile.change_status(4,'Delivered')
profile.change_status(5,'Delivered')
profile.pending_orders()
profile.change_status(6,'Success')
profile.pending_orders()
profile.change_status(6,'Out for Delivery')
profile.change_status(1,'Out for Delivery')
profile.change_status(1,'Delivered')
profile.change_status(6,'Delivered')
profile.pending_orders()
del profile

i = login(restos,users,menu,orders)
# vaibhav_takale takale@vaibhav
profile = user(users, restos, menu, orders, i)
profile.get_profile()
del profile

i = login(restos,users,menu,orders)
# hotel_vaibhav hotel@vaibhav
profile = resto(restos, menu, orders, i)
profile.pending_orders()
profile.change_status(0,'Out for Delivery')
profile.change_status(3,'Out for Delivery')
profile.change_status(3,'Delivered')
profile.change_status(0,'Delivered')
profile.change_status(7,'Success')
profile.change_status(7,'Out for Delivery')
profile.change_status(7,'Delivered')
profile.pending_orders()
del profile

i = login(restos,users,menu,orders)
# nitin_takale nitin@takale
profile = user(users, restos, menu, orders, i)
profile.get_profile()
del profile

i = login(restos,users,menu,orders)
# vaibhav_takale takale@vaibhav
profile = user(users, restos, menu, orders, i)
profile.get_profile()
# get_ipython().run_line_magic('save', 'current_session ~0/')
