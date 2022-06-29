readfile = open("article.txt", "r", encoding='utf-8')
f = readfile.read()
s = f.lower()
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
zero = []
print(len(alpha))
#알파벳 갯수 담기
for i in range(len(alpha)):
    zero.append(0)

for i in range(len(s)):
    if(s in alpha) :
        zero[i] +=1
print(' '.join(map(str, zero)))

print(alpha)