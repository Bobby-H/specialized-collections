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
## Creating a Frozenset
## Adding to a Set
## Removing From a Set
## Finding Elements in a Set
## Introduction to Set Operations
## Set Union
## Set Intersection
## Set Difference
## Symmetric Difference
## Sets Review
