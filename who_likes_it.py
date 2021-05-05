"""
You probably know the "like" system from Facebook and other pages.
People can "like" blog posts, pictures or other items.
We want to create the text that should be displayed next to such an item.

Implement a function likes :: [String] -> String, which must take in input array,
containing the names of people who like an item.
It must return the display text as shown in the examples:
    likes([]) # must be "no one likes this"
    likes(["Peter"]) # must be "Peter likes this"
    likes(["Jacob", "Alex"]) # must be "Jacob and Alex like this"
    likes(["Max", "John", "Mark"]) # must be "Max, John and Mark like this"
    likes(["Alex", "Jacob", "Mark", "Max"]) # must be "Alex, Jacob and 2 others like this"
"""


def likes(names):
    count_names = len(names)
    like_this = ' like this'
    likes_this = ' likes this'
    who_like = ''
    if count_names == 0:
        who_like = 'no one'
    elif count_names == 1:
        who_like = names[0]
    elif count_names == 2:
        who_like = f'{names[0]} and {names[1]}'
    elif count_names == 3:
        who_like = f'{names[0]}, {names[1]} and {names[2]}'
    elif count_names > 3:
        who_like = f'{names[0]}, {names[1]} and {count_names - 2} others'
    if count_names < 2:
        return who_like + likes_this
    else:
        return who_like + like_this


"""
Other solutions:

def likes(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this', 
        2: '{} and {} like this', 
        3: '{}, {} and {} like this', 
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)
"""