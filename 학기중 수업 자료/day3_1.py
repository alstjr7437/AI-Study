#한 변의 크기와 변의 수를 입력받아 다각형 그리기

#1. 변의 크기와 변의 수를 입력받는다.
size = int(input("변의 크기를 입력하세요!"))
num = int(input("변의 수를 입력하세요!"))
# 각도를 위한 go 변수 선언
go = 360 // num

#2. 변을 그리면서 각도 수정
import turtle as t
t.shape("turtle")

#반복문으로 변의수 만큼 반복
for i in range(0, num) :
    t.forward(size)
    t.left(go)
t.done()
