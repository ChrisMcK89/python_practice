ages = [5, 15, 64, 27, 84, 26]

odd_ages = [number for number in ages if number % 2 != 0]

print(odd_ages)

chicken_names = ["Hen Solo", "Cluck Norris", "Hennifer Lopez", "ChewPekka", "Feather Locklear"]

chickens_long = [name for name in chicken_names if len(name) > 10]

print(chickens_long)

chickens_h = [name for name in chicken_names if name[0] == 'H']

print(chickens_h)

words = ["The", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]

new_word = [word[0].lower() for word in words]


print(new_word)