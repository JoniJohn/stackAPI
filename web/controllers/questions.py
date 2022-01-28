import api_services.questions as questions_data

# counts number of tagged languages in questions
# returns a dictionary of languages and their count
def get_tags():
    questions = questions_data.get_questions()
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
    questions = questions_data.get_questions()
    res = {
        "is_answered": 0,
        "not_answered": 0
    }
    for question in questions:
        if question['is_answered']:
            res['is_answered'] += 1
        else:
            res['not_answered'] += 1
    return res

## view count
def view_count_data():
    questions = questions_data.get_questions()
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