import ephem
def full_moon(user_text):
    user_text = user_text.replace("когда ближайшее полнолуние после ", "")
    date_list = user_text.split("-")
    result = "{}/{}/{}".format(date_list[0], date_list[1], date_list[2])
    full_moon = ephem.next_full_moon(result)
    return str(full_moon)
