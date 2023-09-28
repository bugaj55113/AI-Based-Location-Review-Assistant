with open('input/f.txt', 'r') as f:
    data = f.read().lower()

keyword = input("Enter your character, word or sentence: ")

r = data.count(keyword)

print(f"Keyword {keyword} has occurred {r} times")