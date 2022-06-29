# if - else 블록 연습
# 2022.4.5

# 정수를 입력받는다
while 1 :
    value = int(input("정수 입력:"))

    if value > 0 :
        ("양수입니다.")
        if value % 2 == 0:
            print("%d는 짝수입니다." %value)
            break
        else:
            print("양수입니다.")
            break
    else :
        print("양수 입력하세요!")
        continue
# 정수 여부를 확인하고 결과를 출력한다

