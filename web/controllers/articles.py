import api_services.articles as articles_data


articles = articles_data.get_articles()

# counts number of tagged languages in questions
# returns a dictionary of languages and their count
def get_tags(): 
    tags = {}
    for article in articles:
        # check to see if tag is dictionary 
        for tag in article['tags']:
            if tag in tags.keys():
                tags[tag] += 1
            else:
                tags[tag] = 1
    return tags

def get_count():
    return len(articles)