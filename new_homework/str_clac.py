def str_clac(user_input):

    digits_dic = {"один": 1, "два": 2, "три": 3, "четыре": 4,
              "пять": 5, "шесть": 6, "семь": 7, "восемь": 8,
              "девять": 9, "десять": 10}

    user_input = user_input.lower().strip()
    user_input = user_input.replace("сколько будет", "")
    user_input_list = user_input.split(" ")
    if len(user_input_list) == 4:
        x = digits_dic.get(user_input_list[1])
        y = digits_dic.get(user_input_list[3])
        if user_input_list[2] == "плюс":
            result = x+y
            return result
        elif user_input_list[2] == "минус":
            result = x-y
            return result
        
    else:
        x = digits_dic.get(user_input_list[1])
        y = digits_dic.get(user_input_list[4])
        if user_input_list[2] == 'делить':
            result = x/y
            return result
        else:
            result = x*y
            return result