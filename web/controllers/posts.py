from api_services import posts as post_data

posts = post_data.get_posts()

# groups post by type
def get_post_types():
    post_types = {}
    for post in posts:
        if post['post_type'] in post_types.keys():
            post_types[post['post_type']]+=1
        else:
            post_types[post['post_type']] = 1
    return post_types


def get_count():
    return len(posts)