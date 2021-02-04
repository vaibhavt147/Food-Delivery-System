class resto:
	
	def __init__(self,restos, menu, orders, i):
		self.orders = orders
		self.restos = restos
		self.i = i
		self.menu = menu

	def add_menu(self, dish_name,price,cuisine=None):
		self.menu.loc[len(self.menu.index)] = [self.restos['resto_name'][self.i] , dish_name, cuisine, price]
		self.menu.to_csv('menu.csv',index=False)

	def remove_menu(self, dish_name):

		condition1 = self.menu['dish_name'] == dish_name
		resto_name = self.restos['resto_name'][self.i]
		condition2 = self.menu['resto_name'] == resto_name
		
		temp = self.menu.index[ condition1 & condition2 ].tolist()
		self.menu.drop(temp, inplace=True)
		self.menu.to_csv('menu.csv',index=False)
	
	def update(self):

		print('\nIf you want to set restaurant Name, type it in below window. to skip press enter')
		temp = str(input())
		if temp!="":
			old_name = self.restos['resto_name'][self.i]
			self.menu['resto_name'] = self.menu['resto_name'].replace([old_name],temp)
			self.restos['resto_name'][self.i] = temp
		
		print('\nIf you want to change password, type it in below window. to skip press enter')
		temp = input().strip()
		if temp!="":
			self.restos['password'][self.i]=temp
		
		print('\nIf you want to change max_n, type it in below window. to skip press enter')
		temp = input().strip()
		if temp!="":
			self.restos['max_n'][self.i]= int(temp)
		
		print('\nIf you want to change curr_n, type it in below window. to skip press enter')
		temp = input().strip()
		if temp!="":
			self.restos['curr_n'][self.i]=int(temp)
		
		self.restos.to_csv('restos.csv', index = False)
		self.menu.to_csv('menu.csv', index = False)

	def pending_orders(self):

		condition1 = self.orders['resto_name'] == self.restos['resto_name'][self.i]
		condition2 = self.orders['status'] != 'Delivered'
		temp = self.orders.index[condition2 & condition1].tolist()
		print('Here are pending orders:\n')
		print(self.orders.loc[temp])

	## Every time when a restaurant wants to change status of orders, it must need to run pending_orders first to get to know the index of each order
	# Restaurants can change status to "Success" >> "Out for Delivery" >> "Delivered" only

	def change_status(self, order_index, new_status):

		if new_status != 'Delivered' & new_status!= 'Success':
			
			self.restos['curr_n'][self.i] = self.restos['curr_n'][self.i] - 1
			# condition1 = self.orders['resto_name'] == self.restos['resto_name'][self.i]
			# condition2 = self.orders['status'] == 'Waiting'
			# temp = self.orders.index[condition2 & condition1].tolist()
			# if len(temp)==0:
			# 	self.restos['curr_n'][self.i] = self.restos['curr_n'][self.i] - 1
			# else:
			# 	self.orders['status'][temp[0]]='Success'	
	
		elif new_status == 'Success':
			self.restos['curr_n'][self.i] = self.restos['curr_n'][self.i] + 1
		else:
			pass

		# print("Current orders to be prepared are ",self.restos['curr_n'][self.i])
		print("Check pending orders by typing profile.pending_orders()")	
		self.orders['status'][order_index] = new_status
		self.orders.to_csv('orders.csv',index = False)
