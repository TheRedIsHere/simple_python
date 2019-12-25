# task 1
years_list = [1997, 1998, 1999, 2000, 2001]
# task 2
print(years_list[2])
# task 3
print(max(years_list))
# task 4
things = ['mozzarella', 'cinderella', 'salmonella']
# task 5
things[1] = things[2].capitalize()
print(things)
# task 6
things[0] = things[0].upper()
print(things)
# task 7
things.remove('salmonella')
print(things)
# task 8
surprise = ['Groucho', 'Chico', 'Harpo']
# task 9
surprise[-1] = surprise[-1].lower().swapcase().capitalize()
print(surprise)
# task 10
e2f = {
    'dog': 'chien',
    'cat': 'chat',
    'walrus': 'morse'
}
# task 11
print(e2f['walrus'])
# task 12
f2e = {}
for key, value in e2f.items():
    f2e[value] = key
print(f2e)
# task 13
print(f2e['chien'])
# task 14
english_words = set(e2f.keys())
print(english_words)
# task 15
kinds = ['Henri', 'Grumply', 'Lucy']
cat = {
    'cats': kinds,
    'octopi': '',
    'emus' : ''
}
life = {
    'animals': cat,
    'plants': {},
    'other': {}
}
print(life)
# task 16
print(life.keys())
# task 17
print(life['animals'].keys())
# task 18
print(life['animals']['cats'])