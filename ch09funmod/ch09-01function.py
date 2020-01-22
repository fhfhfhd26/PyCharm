# 전역변수
coffee = 0

# 함수선언
def coffee_machine(button):
    print()
    # 물, 컵을 준비한다
    print("#1. (자동으로) 뜨거운 물을 준비한다")
    print("#1. (자동으로) 종이컵을 준비한다")
    print()

    # 버튼에 따라서 커피를 탄다.
    if button == 1:
        print("#1. (자동으로) 보통커피를 탄다")
    elif button == 2:
        print("#1. (자동으로) 설탕커피를탄다")
    elif button == 3:
        print("#1. (자동으로) 블랙커피를탄다")
    else:
        print("#3. 아무거나 탄다")
    print()

def coffee_machine():
    button = 1
    print()
    # 물, 컵을 준비한다
    print("#1. (자동으로) 뜨거운 물을 준비한다")
    print("#1. (자동으로) 종이컵을 준비한다")
    print()

    # 버튼에 따라서 커피를 탄다.
    if button == 1:
        print("#1. (자동으로) 보통커피를 탄다")
    elif button == 2:
        print("#1. (자동으로) 설탕커피를탄다")
    elif button == 3:
        print("#1. (자동으로) 블랙커피를탄다")
    else:
        print("#3. 아무거나 탄다")
    print()

# main
# 사용자가 커피 선택
coffee = int(input("커피선택 (1:보통, 2:설탕, 3:블랙, 4: 랜덤) : "))
# 기계가 커피를 탄다. -> 뒤에것을 호출해서 오류가 없다.
coffee_machine(coffee)

# coffee_machine() -> 요구되어지는 매개변수의 값이 없다. 오류
# coffee_machine(coffee, coffee) -> 요구되어지는 매개변수의 값이 많다. 오류

# 뒤에 것 coffee_machine(button)을 호출하기 때문에 오류
coffee_machine()

# 내준다.
