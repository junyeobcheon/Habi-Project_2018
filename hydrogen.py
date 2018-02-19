import re

words = []
f = open("kor4-1.txt", "r", encoding = "utf-8")
contents = str(f.readlines())
result = re.findall(r"(<w>)([\s\S]+?)(</w>)", contents)
for i in range(len(result)):
    words.append(result[i][1])
f.close()
words = words[::-1]
# print(words)


def sentence_generator(key, str_word):
    if(key == 0):
        return "\'" + str_word + "\'" + "에서 내용을 확실히 이해하였다."
    elif(key == 1):
        return "\'" + str_word + "\'" + "에서 아이들이 이해하는데 어려움을 느껴한다."
    elif(key == 2):
        return "\'" + str_word + "\'" + "에 관해서 추가적으로 보충학습을 했고 덕분에 아이들의 이해도를 높이는데 도움이 됐다."
    elif(key == 3):
        return "아이들이 긴 글을 읽을 때 집중을 못한다."
    elif(key == 4):
        return "\'" + str_word + "\'" + "에 관해서 아이들이 큰 흥미를 느끼는 것으로 보였다."
    elif(key == 5):
        return "학교시험에 철저하게 대비할 수 있도록 기본개념을 확실하게 파악한다."
    elif(key == 6):
        return "교과서에 담긴 내용을 파악할 수 있도록 지도한다."
    elif(key == 7):
        return "주요개념을 확실하게 파악하도록 지도한다."
    elif(key == 8):
        return "단원학습을 마무리하고 보완할 부분을 파악한다."
    elif(key == 9):
        return "기본개념을 중시하는 학습습관을 갖도록 지도한다."
    elif(key == 10):
        return "교과서에 담긴 내용을 빈틈없이 학습한다."
    elif(key == 11):
        return "보완할 점을 파악하여 단원학습에 반영한다."
    elif(key == 12):
        return "공부할 내용에 흥미를 느낄 수 있도록 지도한다."
    elif(key == 13):
        return "다양한 유형의 문제를 풀어서 학교시험에 대비할 수 있도록 한다."
    elif(key == 14):
        return "핵심개념을 분명하게 이해할 수 있도록 지도한다."
    elif(key == 15):
        return "학습정리를 통해 학생이 본인의 이해도를 파악할 수 있도록 한다."
    elif(key == 16):
        return "배운 내용을 바로바로 복습하도록 지도한다."
    elif(key == 17):
        return "자주 틀리는 문제를 다음에 틀리지 않도록 유형을 철저히 학습한다"
    elif(key == 18):
        return "간단한 문제를 틀리지 않도록 꼼꼼히 확인한다."
    elif(key == 19):
        return "아이들이 긴 글을 읽을 때 대충 읽어서 내용을 제대로 파악하지 못하는 경우가 종종 있다."
    elif(key == 20):
        return "학습한 내용을 노트에 정리하도록 지도한다."
    elif(key == 21):
        return "\'" + str_word + "\'" + "에 관한 문제에 아이들이 자신감을 보인다."
    elif(key == 22):
        return "수업에 참고하기 위해" + "\'" + str_word + "\'" + "에 관한 인터넷 동영상을 시청했다. 아이들의 반응이 매우 좋았다."
    elif(key == 23):
        return "교과서에" + "\'" + str_word + "\'" + "에 관한 내용이 자세히 서술돼 있어서 교과서를 참고하여 지도했다."
    elif(key == 24):
        return "학교시험에 대비할 수 있도록 기본개념을 철저히 학습시킨다."
    elif(key == 25):
        return "\'" + str_word + "\'" + "에 관해서 흥미를 느끼지 못하고 있다."
    elif(key == 26):
        return "수학공부를 하면서 단순연산에서 실수를 줄일 수 있게 지도한다."
    elif(key == 27):
        return "아이들이 인터넷에 올라와있는 다양한 학습자료를 이용하면 더 높은 학습효율을 보인다."
    elif(key == 28):
        return "\'" + str_word + "\'" + "에 관련된 문제를 자주 틀려서 추가학습을 했다."
    elif(key == 29):
        return "\'" + str_word + "\'" + "에 대해서 토론학습을 진행했다."
    elif(key == 30):
        return ""
    elif(key == 31):
        return ""
    elif(key == 32):
        return ""
    elif(key == 33):
        return ""
    elif(key == 34):
        return ""

    else:
        return ""
