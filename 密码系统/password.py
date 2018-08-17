import pickle



def register():
	"""
	register
	"""
	data = open_database() if open_database() else {}
	username = input("请输入注册id:")
	while username in data.keys():
		print("此id已存在，请重试")
		username = input("（按q返回）请重新输入注册id:")
		if username == 'q':
			break
	else:
		password = input("请输入注册密码:")
		password2 = input("请再次输入注册密码:")
		while password != password2:
			print("两次输入密码不一致请重新输入")
			if password=='q' or password2=='q':
				break
			password = input("请输入注册密码:")
			password2 = input("请再次输入注册密码:")
		else:
			print("注册成功！")
	data[username] = password 
	update_database(data)


def login():
	"""
	login
	"""
	b = open_database()
	print(b)
	user_name = input("请输入您的id:")
	while not user_name in b.keys():
		print("id不存在")
		user_name = input("（按q返回）请重新输入id:")
		if user_name == 'q':
			break
	else:
		pass_word = input("请输入您的密码:")
		while b[user_name] != pass_word:
			print("密码错误")
			pass_word = input("请重新输入您的密码:")
			if pass_word == 'q':
				break
		else:
			print("登录成功！")


def update_database(user_data):
	with open('mm.pkl', 'wb') as f:
		pickle.dump(user_data, f)


def open_database():
	try:
		with open('mm.pkl', 'rb') as f:
			return pickle.load(f)
	except:
		return False

def main():
	while True:
		get = input('1.注册  2.登录 3.退出:  ')
		if get == '1':
			register()
		elif get == '2':
			login()
		else:
			break

if __name__ == "__main__": 
	main()
	