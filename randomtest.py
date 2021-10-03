userInput = input('Let Reverse your Word : ')
def reverse(txt):
    temp=''
    for words in txt:
        temp=words+temp
    return temp
print(reverse(userInput))