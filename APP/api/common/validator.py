def check_if_already_exists(list_name, title , description):
    
    for question in list_name:
        if question['title'] == title or question['description'] == description:
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