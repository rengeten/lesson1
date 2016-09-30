def answer(user_text):
    user_text = user_text.strip().lower()
    if "!" in user_text:
        return "dont shout on me!"
    if "?" in user_text:
        return "I would not answer any questions without my lawyer"
    dictionary = {'hello':'Hello!', "bye":"Bye!"}
    usrmsg = dictionary.get(user_text, "I dont know!")
    return usrmsg