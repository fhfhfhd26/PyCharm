# 1. 수식을 작성하면 작성된 수식을 계산해서 출력하자.
# 2. 숫자 2개를 입력받고 숫자 2개 사이의 모든 숫자를 더해서 출력

# 변수 선언
select, answer, numStr, num1, num2 = 0, 0, "", 0, 0

# 메인 코드
select = int(input("1. 입력한 수식 계산  2. 두 수 사이의 모든 숫자 합계 : "))

if select == 1:
    numStr = input("수식을 입력해 주세요 : ")
    answer = eval(numStr)
    print("%s 결과는 %5.1f" % (numStr, answer))

elif select == 2:
    num1 = int(input("시작 숫자를 입력해 주세요 : "))
    num2 = int(input("마지막 숫자를 입력해 주세요 : "))
    for i in range(num1, num2+1):
        answer += i
    print("%d+...+%d는 %d입니다. " % (num1, num2, answer))
else:
    print("1 또는 2만 입력해야 합니다.")

