scores_list = [{'school_class':'4a', 'scores':[3,4,4,4,3,2,5]}, {'school_class':'4b', 'scores':[5,5,5,2,3,2]}]

#average for school

a_scores = scores_list[0].get('scores')
b_scores = scores_list[1].get('scores')
school_scores = a_scores + b_scores
all_scores = 0
for score in school_scores:
	all_scores += score
average = all_scores / len(school_scores)
print('Average school scores: ')
print(average)

#average for each class

all_scores_4a = 0
for score in a_scores:
	all_scores_4a += score
average_4a = all_scores_4a / len(a_scores)
print('4a average is: ')
print(average_4a)

all_scores_4b = 0
for score in b_scores:
	all_scores_4b += score
average_4b = all_scores_4b/ len(b_scores)
print('4b average is: ')
print(average_4b)