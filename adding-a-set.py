song_data = {'Retro Words': ['pop', 'warm', 'happy', 'electric']}

user_tag_1 = 'warm'
user_tag_2 = 'exciting'
user_tag_3 = 'electric'
all_user_tags = [user_tag_1, user_tag_2, user_tag_3]
# checkpoint 1
tag_set = set(song_data['Retro Words'])
tag_set.update(all_user_tags)