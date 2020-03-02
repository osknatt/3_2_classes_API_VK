# Задача №1
# Пользователя нужно описать с помощью класса и реализовать метод поиска общих друзей, используя API VK.
#
# Задача №2
# Поиск общих друзей должен происходить с помощью оператора &, т.е. user1 & user2 должен выдать список общих друзей пользователей user1 и user2, в этом списке должны быть экземпляры классов.
#
# Задача №3
# Вывод print(user) должен выводить ссылку на профиль пользователя в сети VK


from urllib.parse import urlencode
import requests
from pprint import pprint
# APP_ID = 7341562
# mTccCu4PBZHbDvTwBDk1v
# OAUTH_URL = 'https://oauth.vk.com.authorize'
# OAUTH_PARAMS = {
#     'client_id' : APP_ID,
#     'display' : 'page',
#     'scope' : 'friends',
#     'response_type': 'token',
#     'v' : '5.52'
# }
TOKEN = 'bc9e546b5505741d7bb05f3745eb54fd987739f3d5d8e920bb713239aa92fef25aed27b8e59500a8b431a'

class User:
    def __init__(self, user_id):
        self.user_id = user_id
        try:
            self.friends = self.get_friends(self.user_id)
        except:
            # Реакция на недоступных пользователей
            self.friends = {}

    def get_friends(self, user_id):
        response = requests.get(
            'https://api.vk.com/method/friends.get',
            params={
                'access_token': TOKEN,
                'v': '5.52',
                'user_id' : user_id
            }
        )
        response = response.json()
        return set(response['response']['items'])

    def __and__(self, other):
        common_friends = list(self.friends & other.friends)
        return [User(u) for u in common_friends]

    def __str__(self):
        return f"vk.com/id{self.user_id}"


user1 = User('976463')
user2 = User('54444173')

# print(user1.friends)
common_friends = user1 & user2
print(common_friends)
print(common_friends[0])