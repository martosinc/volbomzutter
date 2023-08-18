from api import *

db_api = API(host='192.168.1.75', user='user', db_name='db', password='123')

db_api.add_user(User((1, 'name', 'name', 'bio')))

print(db_api.get_user(1).name)

db_api.add_post(Post((1, 1, 'tittle', 'text')))

print(db_api.get_post(1).tittle)
