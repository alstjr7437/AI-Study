readfile = open("article.txt", "r", encoding='utf-8')
f = readfile.read()
s = f.lower()
alpha = []
zero = []

#알파벳 갯수 담기
for i in range(97,123):
    alpha.append(i)
    zero.append(0)

for i in range(len(s)):
    if(ord(s[i]) in alpha) :
        zero[ord(s[i]) - 97] +=1

for i in range(len(alpha)):
    print(chr(alpha[i]) + ' : ' + str(zero[i]))

#print(' '.join(map(str, zero)))

#print(alpha)
#print(s)
