import api_services.questions as questions_data
import api_services.articles as articles_data
import api_services.posts as posts_data


# gets totals for each API entity
# [entities] take type 
# returns a dictionary of totals
def get_counts(): 
    totals = {
        "questions": len(questions_data.get_questions()),
        "posts": len(articles_data.get_articles()),
        "articles": len(posts_data.get_posts()),
    }
    return totals 

print(get_counts())