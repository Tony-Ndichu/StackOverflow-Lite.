def check_if_already_exists(list_name, title , description):
    
    for question in list_name:
        if question['title'] == title or question['description'] == description:
            return True
        return False

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
