from api_services import posts as post_data

posts = post_data.get_posts()

def get_post_type():
    pass

def get_count():
    return len(posts)