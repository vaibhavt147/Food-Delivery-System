class user:

	def __init__(self,users, restos, menu, orders, i)	:
		self.users = users
		self.orders = orders
		self.restos = restos
		self.i = i
		self.menu = menu

	def update(self):
		print('/nIf you want to change your Name, type it in below window. to skip press enter')
		temp = input()
		if temp != '':
			self.users['name'][self.i] = temp
		
		print('\nIf you want to change password, type it in below window. to skip press enter')
		temp = input().strip()
		if temp != '':
			self.users['password'][self.i] = temp
		
		print('\nIf you want to change phone number, type it in below window. to skip press enter')
		temp = input().strip()
		if temp != '':
			self.users['phone'][self.i]=int(temp)

		print('\nIf you want to change address, type it in below window. to skip press enter')
		temp = input()
		if temp != '':
			self.users['address'][self.i]=temp

		print('\nIf you want to change email, type it in below window. to skip press enter')
		temp = input()
		if temp != '':
			self.users['email_id'][self.i]=temp

		self.users.to_csv('users.csv',index = False)
		print("\nProfile updated successfully")

	def delete(self):
		self.users.drop(self.i, inplace=True)

	def search(self,keyword):

		condition1 = self.menu['cuisine'].str.contains(keyword)
		condition2 = self.menu['dish_name'].str.contains(keyword)
		condition3 = self.menu['resto_name'].str.contains(keyword)

		temp = self.menu[ condition1 | condition2 | condition3 ]
		print(temp)

	def order(self,dish_index):
		
		resto_name = self.menu['resto_name'][dish_index]
		dish_name = self.menu['dish_name'][dish_index]
		temp = self.restos.index[self.restos['resto_name'] == resto_name ].tolist()[0]
		
		if int(self.restos['curr_n'][temp]) < int(self.restos['max_n'][temp]):
		
			self.orders.loc[len(self.orders.index)] = [resto_name,dish_name,self.users['username'][self.i],'Success'] 
			self.restos['curr_n'][temp] = self.restos['curr_n'][temp] + 1
			print("Order placed succesful")

		else:
			self.orders.loc[len(self.orders.index)] = [resto_name,dish_name,self.users['username'][self.i],'Waiting']
			print("Your order is in Waiting list")
		
		self.restos.to_csv('restos.csv', index = False)
		self.menu.to_csv('menu.csv', index = False)
		self.orders.to_csv('orders.csv',index = False)

	def get_profile(self):

		print(self.users.iloc[self.i].drop('password'))
		print('\nYour Orders:\n')
		print(self.orders[self.orders['username']==self.users['username'][self.i]].drop(columns=['username']))
		

