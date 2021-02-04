def login(restos,users,menu,orders):
	
	print("Enter your username and password with only one space in between")
	username , pas = input().strip().split()
	
	x = restos.index[restos['username'] == username].tolist()
	y = users.index[users['username'] == username].tolist()
	
	if len(x)+len(y) == 0:
		print("Username does not exist")
		return login(restos,users,menu,orders)

	elif len(x):
		i = x[0]
		if restos['password'][i]==pas:
			print("Type profile = resto(restos, menu, orders, i)")
			restos.to_csv('restos.csv',index = False)
			return i
			return resto(restos, menu, orders, i)
			
		else:
			print("Wrong Password")
			return login(restos,users,menu,orders)

	elif len(y):
		i = y[0]
		if users['password'][i]==pas:
			print("type profile = user(users, restos, menu, orders, i) ")
			users.to_csv('users.csv',index = False)
			return i
			return user.user(users, restos, menu, orders, i)
			
		else:
			print("Wrong Password")
			return login(restos,users,menu,orders)
	
def sign_in(restos,users,menu,orders):
	
	print("Enter username and password with only one space in between")
	username , pas = input().strip().split()

	x = restos.index[restos['username'] == username].tolist()
	y = users.index[users['username'] == username].tolist()
	
	if len(x)+len(y) == 0:
		print("Enter 0 if you are restaurant, else 1")
		temp = input().strip()
		if int(temp):
			i = len(users.index)
			users.loc[i] = [username,pas,None,None,None,None]
			print("You will be logged in using entered username and password. Kindly update other details using profile.update()")
			print("type profile = user(users, restos, menu, orders, i) ")
			users.to_csv('users.csv',index = False)

			return i
			return user(users, restos, menu, orders, i)
			
		else:
			i = len(restos.index)
			restos.loc[i] = [username,pas,None,None,0]
			print("You will be logged in using entered username and password. Kindly update other details using profile.update()")
			print("Type profile = resto( restos, menu, orders, i)")
			restos.to_csv('restos.csv',index = False)
			return i
			return resto( restos, menu, orders, i)
			
	else:
		print("username already exists, choose different username")
		return sign_in(restos,users,menu,orders)

