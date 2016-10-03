def str_clac(user_input):

    digits_dic = {"один": 1, "два": 2, "три": 3, "четыре": 4,
              "пять": 5, "шесть": 6, "семь": 7, "восемь": 8,
              "девять": 9, "десять": 10, "ноль": 0}

    user_input = user_input.lower().strip()
    user_input = user_input.replace("сколько будет", "")
    user_input_list = user_input.split(" ")
    
    if "и" in user_input_list:
        if len(user_input_list) == 8:
            x_first = str(digits_dic.get(user_input_list[1]))
            x_second = str(digits_dic.get(user_input_list[3]))
            x = '{}.{}'.format(x_first, x_second)
            x = float(x)

            y_first = str(digits_dic.get(user_input_list[5]))
            y_second = str(digits_dic.get(user_input_list[7]))
            y = '{}.{}'.format(y_first, y_second)
            y = float(y)

            if user_input_list[4] == "плюс":
                result = x+y
                return result
            elif user_input_list[4] == "минус":
                result = x-y
                return result

        elif len (user_input_list) == 9:
            x_first = str(digits_dic.get(user_input_list[1]))
            x_second = str(digits_dic.get(user_input_list[3]))
            x = '{}.{}'.format(x_first, x_second)
            x = float(x)

            y_first = str(digits_dic.get(user_input_list[6]))
            y_second = str(digits_dic.get(user_input_list[8]))
            y = '{}.{}'.format(y_first, y_second)
            y = float(y)

            if user_input_list[4] == "делить":
                result = x/y
                return result
            elif user_input_list[4] == "умножить":
                result = x*y
                return result


    else:
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