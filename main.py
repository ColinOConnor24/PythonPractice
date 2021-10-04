word = input("What word would you like me to spell? ")
x = len(word)
y = len(word)
while y > 0:
    print(word[x - y])
    y -= 1