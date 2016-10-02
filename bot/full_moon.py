import ephem
def full_moon(user_text):
    user_text = user_text.replace("когда ближайшее полнолуние после ", "")
    date_list = user_text.split("-")
    result = ephem.next_full_moon(date_list[0]+'/'+date_list[1]+'/'+date_list[2])
    return str(result)