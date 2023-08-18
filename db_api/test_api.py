from api import *

db_api = API(host='127.0.0.1', user='user', db_name='db', password='123')

# test user table 
user = User((1, 'name', 'name', 'bio'))
db_api.add_user(user)

print(db_api.get_user(1).name)

# test post table
db_api.add_post(Post((1, 1, None, 'tittle', 'text')))
db_api.add_post(Post((2, 1, None, 'tittle', 'text')))
db_api.add_post(Post((3, 1, None, 'tittle', 'text')))

print(db_api.get_post(1).tittle)

print(db_api.get_posts_by_user(user))

print(db_api.get_posts(2))
print(db_api.get_posts())
