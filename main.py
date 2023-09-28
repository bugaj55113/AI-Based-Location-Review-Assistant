f = open('input/f.txt', 'r')
data = f.read()
f.close()

keyword = input("Enter your character, word or sentence: ")

r = data.count(keyword)

print(f"Keyword {keyword} has occurred {r} times")