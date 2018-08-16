def check_if_already_exists(list_name, title , description):
    
    for item in list_name:
        if item['title'] == title or item['description'] == description:
            return True
    
def check_for_answer(list_name , answer):

	for item in list_name:
		if item['answer'] == answer:
			return True   

def question_verification(title, description):
    '''check the quality of questions sent to the platform'''
    if len(title)< 1:
        return 'You cannot post an empty title, Please add a title'
    if len(description)< 1:
        return 'You cannot post an empty description, Please add a description'
    if title.isdigit():
    	return 'You cannot have a title with digits only, Please describe with some words'
    if description.isdigit():
    	return 'You cannot have a description with digits only, Please describe with some words'

def check_using_id(list_name , other_id):

	my_item = next((item for item in list_name if item['question_id'] == other_id), None)

	if my_item:
		return my_item
	return False

def check_quality(item):
	
	if len(item) < 1:
		return 'Too Short, Please add more input'

def find_answers_to_a_question(list_name, question_id):	
	answers = []
	for answer in list_name:
		if answer['question_id'] == int(question_id):
			answers.append(answer)

	return answers