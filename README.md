# specialized-collections
A Python course walkthrough on specialized collections
Explores:
* How to create a set and a frozenset.
* How to add to a set (we won’t be able to mutate a frozenset).
* How to remove from a set (we won’t be able to mutate a frozenset).
* How to find specific elements in a set and a frozenset.
* How to perform set operations such as unions, intersections, and more.

# Sets
## Introduction to Sets

a set is a group of elements that are unordered and do not contain duplicates. Although it may seem that the usefulness of this data structure is limited, it can actually be very helpful for organizing items and performing set mathematics.

## Creating a Set
- In Python, there are multiple ways to create a set.
##### Creating a set with curly braces
```music_genres = {'country', 'punk', 'rap', 'techno', 'pop', 'latin'}```
##### Creating a set from a list using set()
```
music_genres_2 = set(['country', 'punk', 'rap', 'techno', 'pop', 'latin'])
print(music_genres_3)
```
will output:
```
{'country', 'punk', 'pop', 'rap'} # element/index switches are due to sets being un-ordered
```
##### Set Comprehensions:
```
items = ['country', 'punk', 'rap', 'techno', 'pop', 'latin']

music_genres = {category for category in items if category[0] == 'p'}
print(music_genres)
```
Would output a set containing all elements from items starting with the letter 'p':
```
{'punk', 'pop'}
```
## Creating a Frozenset
Unlike a normal set, you can only create a frozenset using its constructor. 
Using a frozenset means that you cannot modify the elements inside of it.
```
# Creating a frozenset from a list
frozen_music_genres = frozenset(['country', 'punk', 'rap', 'techno', 'pop', 'latin'])
```
## Adding to a Set
There are two different ways to add elements to a set:

The .add() method can add a single element to the set.
```
# Create a set to hold the song tags
song_tags = {'country', 'folk', 'acoustic'}
 
# Add a new tag to the set and try to add a duplicate.
song_tags.add('guitar')
song_tags.add('country')
 
print(song_tags)
```
Would output:
```{'country', 'acoustic', 'guitar', 'folk'}```

The .update() method can add multiple elements.
```
# Create a set to hold the song tags
song_tags = {'country', 'folk', 'acoustic'}
 
# Add more tags using a hashable object (such as a list of elements)
other_tags = ['live', 'blues', 'acoustic']
song_tags.update(other_tags)

 
print(song_tags)
```
Would output:

```{'acoustic', 'folk', 'country', 'live', 'blues'}```

There are a few things to note about adding to a set:

Neither of these methods will add a duplicate item to a set.

A frozenset can not have any items added to it and so neither of these methods will work.

Notice that when the elements are printed, they are not printed in the same order in which they entered the set. This is because set and frozenset containers are unordered.

## Removing From a Set
There are two methods for removing specific elements from a set:

The .remove() method searches for an element within the set and removes it if it exists, otherwise, a KeyError is thrown.
```# Given a list of song tags
song_tags = {'guitar', 'acoustic', 'folk', 'country', 'live', 'blues'}
 
# Remove an existing element
song_tags.remove('folk')
print(song_tags)
 
# Try removing a non-existent element
song_tags.remove('fiddle')```

would output:

```
{'blues', 'acoustic', 'country', 'guitar', 'live'}
``` 

followed by: 

``` 
Traceback (most recent call last):
File "some_file_name.py", line 9, in <module>
 song_tags.remove('fiddle')
KeyError: 'fiddle'
```
The .discard() method works the same way but does not throw an exception if an element is not present.
```
 # Given a list of song tags
song_tags = {'guitar', 'acoustic', 'folk', 'country', 'live', 'blues'}
 
# Try removing a non-existent element but with the discard method
song_tags.discard('guitar')
print(song_tags)
 
# Try removing a non-existent element but with the discard method
song_tags.discard('fiddle')
print(song_tags)
 ```
 would output:
``` 
 {'folk', 'acoustic', 'blues', 'live', 'country'}
{'folk', 'acoustic', 'blues', 'live', 'country'}
```

## Finding Elements in a Set
## Introduction to Set Operations
## Set Union
## Set Intersection
## Set Difference
## Symmetric Difference
## Sets Review
