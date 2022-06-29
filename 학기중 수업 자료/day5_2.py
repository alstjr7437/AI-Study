while 1:
    value = int(input("정수입력:"))
    if value < 10 and value > 1 :
        if value % 2 == 0 :
            if value == 2 :
                print("소수입니다.")
            else :
                print("소수 아닙니다.")
        elif value % 3 == 0 :
            if value == 3 :
                print("소수입니다.")
            else :
                print("소수 아닙니다.")
        else :
            print("소수입니다.")
    else :
        print("범위 내의 수를 입력하세요.  " )