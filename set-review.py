music_tags = {'pop', 'warm', 'happy', 'electronic', 'synth', 'dance', 'upbeat'}

# Checkpoint 1
my_tags = frozenset(['pop', 'electronic', 'relaxing', 'slow', 'synth'])

# Checkpoint 2
frozen_tag_union = frozenset(music_tags | my_tags)
#print(frozen_tag_union)

# Checkpoint 3
regular_tag_intersect = set(music_tags) & set(my_tags)
#print(regular_tag_intersect)

# Checkpoint 4
frozen_tag_difference = my_tags - music_tags
#print(frozen_tag_difference)

# Checkpoint 5
regular_tag_sd = music_tags ^ my_tags
print(regular_tag_sd)