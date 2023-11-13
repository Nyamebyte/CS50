vowels = list('aeiouAEIOU')
line = input('Type anything here: ')
text = ''
for c in line:
    if c not in vowels:
        text += c
print(text)
