def find_person(name, names_list):
    while names_list:
        item = names_list.pop()
        if item == name:
            print("Here is the", name)
            break

list_of_names = ['Wo', 'Cao', 'Ni', 'Ma']
find_person('Cao', list_of_names)


input()