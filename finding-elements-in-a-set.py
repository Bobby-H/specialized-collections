allowed_tags = ['pop', 'hip-hop', 'rap', 'dance', 'electronic', 'latin', 'indie', 'alternative rock', 'classical', 'k-pop', 'country', 'rock', 'metal', 'jazz', 'exciting', 'sad', 'happy', 'upbeat', 'party', 'synth', 'rhythmic', 'emotional', 'relationship', 'warm', 'guitar', 'fiddle', 'romance', 'chill', 'swing']

song_data_users = {'Retro Words': ['pop', 'explosion', 'hammer', 'bomb', 'warm', 'due', 'writer', 'happy', 'horrible', 'electric', 'mushroom', 'shed']}

# checkpoint 1
tag_set = set(song_data_users['Retro Words'])

# checkpoint 2
bad_tags =[]
for tag in tag_set:
  if tag not in allowed_tags:
    bad_tags.append(tag)

# checkpoint 3
for tag in bad_tags:
  if tag in tag_set:
    tag_set.remove(tag)

# checkpoint 4
song_data_users['Retro Words'] = tag_set
print(tag_set)