# In 2017~2018, I taught middle school students how to code. 
# I made this code to show them the programming is not a fancy technique but one can easily develop the code and use it in an useful way.
# When users give several vocabularies as an input, the output will be a vocab test which tells whether the users memorize it correctly or not.  
# I and teenagers have a lot of fun out of it, even though the person being excited most is me. :)

def help():
    print("시험을 보고 싶다면 커맨드 창에 \'voca_test.test(\"시험지파일명\", 합격점수)\' 를 입력하세요.")
    print("파일의 단어를 셔플하고 싶다면 \'voca_test.shuffle(\"파일명\")\'을 입력하세요.")
def shuffle(file_name):
    import random
    eng_voca = []
    kor_voca = []
    new = []

    f = open(file_name, "r")
    g = open("voca_shuffled.csv", "w")
    while 1:
        content = f.readline()
        if not content: break
        data = content.split(",")
        eng_voca.append(data[0])
        kor = [j for i, j in enumerate(data) if i >=1]
        kor_voca.append(",".join(kor))
    indexes = list(range(len(eng_voca)))
    random.shuffle(indexes)
    for index in indexes:
        new = [eng_voca[index], kor_voca[index]]
        new_line = ",".join(new)
        g.write(new_line)
    f.close()
    g.close()

def test(file_name, cut_line):
    import os
    import datetime as dt

    os.system("cls")
    eng_voca = []
    kor_voca = []
    score = 0
    is_passed = ""
    tester_id = str(input("당신의 이름을 입력하세요."))

    f = open(file_name, "r")
    while 1:
        contents = f.readline()
        if not contents: break
        data = contents.split(",")
        eng_voca.append(data[0])
        kor = [j for i, j in enumerate(data) if i >=1]
        kor_voca.append(",".join(kor))

    if (len(eng_voca) != len(kor_voca)):
        raise ValueError("단어장에 단어와 뜻의 개수가 다릅니다. 다시 확인해주세요.")

    for i in range(len(kor_voca)):
        print(i+1, kor_voca[i])
        user_answer = input("다음의 뜻을 가진 영어 단어는 무엇인가요?")
        if(user_answer == eng_voca[i]):
            print("정답입니다!", "\n")
            score += 1
        else:
            print("오답입니다.", "\n")
    print("당신의 점수는:", score, "\n")
    print("정답은:", eng_voca)
    if (score >= int(cut_line)):
        print("통과입니다. 축하합니다.")
        is_passed = "pass"
    else:
        print("다시 공부하세요.")
        is_passed = "fail"
    f.close()
    if not os.path.isdir("log"):
        os.mkdir("log")
    if not os.path.exists("log/test_taker_record.txt"):
        f = open("log/test_taker_record.txt", "w")
        f.write("본 기록에는 하비 학생들의 시험기록이 저장됩니다. \n")
        f.close()
    f = open("log/test_taker_record.txt", "a")
    stamp = str(dt.datetime.now())
    line = stamp + "\t" + tester_id + "\t" + str(score) + "\t" + is_passed + "\n"
    f.write(line)
    f.close()
