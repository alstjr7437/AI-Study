# 파일 복사 및 출력

readfile = open("article.txt", "r", encoding='utf-8')
writefile = open("article_copy.txt", "w", encoding='utf-8')

for aline in readfile :
    writefile.write(aline)
print("한 줄을 읽고 출력하였습니다.")

readfile.close()
writefile.close()
'''
alpha = []
zero = []

for i in range(97,123):
    alpha.append(i)
    zero.append(0)
for i in range(len(fi)):
    if(ord(len[i]) in alpha) :
        zero[ord(fi[i]) - 97] +=1
print(' '.join(map(str, zero)))

print(fi)
'''
