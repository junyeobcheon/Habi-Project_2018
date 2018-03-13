print("구구단 게임 시작(1~9). 0을 입력하면 종료합니다.")
user_input = int(input())
while (user_input is not 0):
    if (user_input > 9 or user_input < 0):
        print("다시 입력해주세요.")
        user_input = int(input())
    else:
        print(user_input, "단을 시작합니다.")
        for i in range(1, 10):
            print(user_input, "*", i, "=", user_input*i)
        print("이번엔 몇단을 할까요?")
        user_input = int(input())
else:
    print("EOP")
