def ask_user(message, right_answer):
	while True:
		user_answer = input(message)
		if user_answer == right_answer:
			print('Bye Bye')
			break

ask_user('How are you?', 'Fine!')