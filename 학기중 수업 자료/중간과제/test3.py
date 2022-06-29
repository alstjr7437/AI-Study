readfile = open("article.txt", "r", encoding='utf-8')
writefile = open("article.txt", "r", encoding='utf-8')
for aline in readfile:
    aline = aline.lower()

    for c in aline:
        if c.isalnum() or c.isspace():
            writefile.write(c)

print("rr")

readfile.close()
writefile.close()