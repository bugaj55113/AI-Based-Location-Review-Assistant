with open('input/f.txt', 'r') as f:
    data = f.read().lower()

frequency_map = {x: data.count(x) for x in set(data)}
popular = max(frequency_map, key=frequency_map.get)

keyword = input("Enter your character, word or sentence: ")

r = data.count(keyword)

print(f"Keyword {keyword} has occurred {r} times")
print(f"The most popular character in the file is {popular}")