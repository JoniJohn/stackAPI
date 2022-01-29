import api_services.questions as questions_data
questions = questions_data.get_questions()

# counts number of tagged languages in questions
# returns a dictionary of languages and their count
def get_tags(): 
    tags = {}
    for question in questions:
        # check to see if tag is dictionary 
        for tag in question['tags']:
            if tag in tags.keys():
                tags[tag] += 1
            else:
                tags[tag] = 1
    return tags


## is answered
## to see how many questions are not answered
def is_answered_data():  
    res = {
        "Answered": 0,
        "Unanswered": 0
    }
    for question in questions:
        if question['is_answered']:
            res['Answered'] += 1
        else:
            res['Unanswered'] += 1
    return res

## view count
def view_count_data():
    res = []
    # collect data on view count per question
    for question in questions:
        # format data in a simple form
        summ = {
            'question_id': question['question_id'],
            'view_count': question['view_count'],
        }
        # append to list
        res.append(summ)
    return res

def get_count():
    return len(questions)