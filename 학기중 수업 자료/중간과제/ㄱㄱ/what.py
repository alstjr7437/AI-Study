file = open('shit.txt', "r")
text = file.read()
text = text.lower()
wordList = text.split()
wordCount = {}

for word in wordList:
    wordCount[word] = wordCount.get(word, 0) + 1
    keys = sorted(wordCount.keys())

for word in keys:
    print(word + ':' + str(wordCount[word])) 
