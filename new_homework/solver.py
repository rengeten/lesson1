def solver(user_text):
    print("solver is workin!")
    new_text = user_text.replace('=', '')
    if "+" in new_text:
        numbers = new_text.split("+")
        print(numbers)
        x, y = numbers
        result = int(x)+int(y)
        result = str(result)
        print(result)
        return result
    elif "-" in new_text:
        numbers = new_text.split('-')
        x, y = numbers
        result = int(x)-int(y)
        result = str(result)
        return result
    elif "*" in new_text:
        numbers = new_text.split('*')
        x, y = numbers
        result = int(x)*int(y)
        result = str(result)
        return result
    elif "/" in new_text:
        numbers = new_text.split('/')
        x, y = numbers
        result = int(x)/int(y)
        result = str(result)
        return result
