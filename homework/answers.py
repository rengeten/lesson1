conversation = {"hello" : "    Hello to you too!", "how are you?" : "Fine", "bye" : "See you!"}
def get_answer(key, mydict):
	answer = mydict.get(key)
	return str(answer.lower().strip())

def ask_user(answers):
	while True:
		try:
		    user_input = input("Say something: ")
		    answer = get_answer(user_input, conversation)
		    print(answer)

		    if user_input == "bye":
			    break
		except KeyboardInterrupt:
			print("Oh, you are leaving! Good luck!")
			break

if __name__ == "__main__":
    ask_user(conversation)
