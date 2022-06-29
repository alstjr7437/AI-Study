# 파일 복사 및 출력

readfile = open("article.txt", "r", encoding='utf-8')
writefile = open("article_copy.txt", "w", encoding='utf-8')

writefile.write(readfile.readline())
print("한 줄을 읽고 출력하였습니다.")

readfile.close()
writefile.close()
'''

'''
