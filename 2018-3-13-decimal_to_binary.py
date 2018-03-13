print("숫자를 입력하세요. 2진수로 변환해드립니다.")
user_input=int(input())
result=""
while (user_input > 0):
    remainder = user_input % 2
    user_input = user_input // 2
    result = str(remainder) + result
print(result)
