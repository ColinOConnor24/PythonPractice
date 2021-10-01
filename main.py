word = input("What word would you like me to spell? ")
letters  = len(word)
x = len(word)
len2 = len(word) - 2
while letters > 0:
    print(word[x - len2])
    x += 1
    letters -= 1