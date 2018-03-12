import calendar
import re
from hydrogen import sentence_generator as sg
import random

year = 2018
first_month = 1
last_month = 6
len_sg = 30

what_day = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일",
 "월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일",
 "월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일",
 "월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일",
 "월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일",
 "월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]

key_math1 = []
key_math2 = []
key_math3 = []

key_eng1 = []
key_eng2 = []
key_eng3 = []

key_math = []
key_eng = []

math_contents1 = []
eng_contents1 = []

math_contents2 = []
eng_contents2 = []

math_contents3 = []
eng_contents3 = []

f = open("midmath1-1.txt", "r", encoding = "utf-8")
contents = str(f.readlines())
result = re.findall(r"(<dd>)([\s\S]+?)(</dd>)", contents)
result1 = re.findall(r"(<w>)([\s\S]+?)(</w>)", contents)
for i in range(len(result)):
    math_contents1.append(result[i][1])
    key_math1.append(result1[i][1])
f.close()
math_contents1 = math_contents1[::-1]
key_math1 = key_math1[::-1]

f = open("mideng1.txt", "r", encoding = "utf-8")
contents = str(f.readlines())
result = re.findall(r"(<dd>)([\s\S]+?)(</dd>)", contents)
result2 = re.findall(r"(<w>)([\s\S]+?)(</w>)", contents)
for i in range(len(result)):
    eng_contents1.append(result[i][1])
    key_eng1.append(result2[i][1])
f.close()
eng_contents1 = eng_contents1[::-1]
key_eng1 = key_eng1[::-1]

# key_word1 = [i for i in zip(key_math, key_eng)]
# key_word1 = key_word1[::-1]
#
# key_math = []
# key_eng = []

f = open("midmath2-1.txt", "r", encoding = "utf-8")
contents = str(f.readlines())
result = re.findall(r"(<dd>)([\s\S]+?)(</dd>)", contents)
result1 = re.findall(r"(<w>)([\s\S]+?)(</w>)", contents)
for i in range(len(result)):
    math_contents2.append(result[i][1])
    key_math2.append(result1[i][1])
f.close()
math_contents2 = math_contents2[::-1]
key_math2 = key_math2[::-1]

f = open("mideng2.txt", "r", encoding = "utf-8")
contents = str(f.readlines())
result = re.findall(r"(<dd>)([\s\S]+?)(</dd>)", contents)
result2 = re.findall(r"(<w>)([\s\S]+?)(</w>)", contents)
for i in range(len(result)):
    eng_contents2.append(result[i][1])
    key_eng2.append(result2[i][1])
f.close()
eng_contents2 = eng_contents2[::-1]
key_eng2 = key_eng2[::-1]

# key_word2 = [i for i in zip(key_math, key_eng)]
# key_word2 = key_word2[::-1]
#
# key_math = []
# key_eng = []

f = open("midmath3-1.txt", "r", encoding = "utf-8")
contents = str(f.readlines())
result = re.findall(r"(<ex>)([\s\S]+?)(</ex>)", contents)
result1 = re.findall(r"(<kw>)([\s\S]+?)(</kw>)", contents)
for i in range(len(result)):
    math_contents3.append(result[i][1])
    key_math3.append(result1[i][1])
f.close()
math_contents3 = math_contents3[::-1]
key_math3 = key_math3[::-1]

f = open("mideng3.txt", "r", encoding = "utf-8")
contents = str(f.readlines())
result = re.findall(r"(<dd>)([\s\S]+?)(</dd>)", contents)
result2 = re.findall(r"(<w>)([\s\S]+?)(</w>)", contents)
for i in range(len(result)):
    eng_contents3.append(result[i][1])
    key_eng3.append(result2[i][1])
f.close()
eng_contents3 = eng_contents3[::-1]
key_eng3 = key_eng3[::-1]

# key_word3 = [i for i in zip(key_math, key_eng)]
# key_word3 = key_word3[::-1]

# print(calendar.prmonth(2018, 2))
# print(calendar.monthrange(2018, 2)) (첫요일, 마지막날)

f = open("중등수업일지.txt", "w", encoding = "utf-8")
i = 0
key_seed10 = random.randint(0, len_sg-1)
key_seed20 = random.randint(0, len_sg-1)
key_seed30 = random.randint(0, len_sg-1)
key_seed11 = random.randint(0, len_sg-1)
key_seed21 = random.randint(0, len_sg-1)
key_seed31 = random.randint(0, len_sg-1)

for month in range(first_month, last_month + 1):
    calndr = calendar.monthrange(year, month)
    day_key = calndr[0]
    num_days = 0
    for day in range(1, calndr[1]+1):
        if (day_key%7 < 4 and day_key%7 >= 0):
            line = str(month) + "월" + str(day) + "일" + str(what_day[day_key]) + "\n"
            f.write(line)
            if (day_key%7 == 0):
                f.write("1학년: " + math_contents1[i//4] + "\n")
                f.write("2학년: " + math_contents2[i//4] + "\n")
                f.write("3학년: " + math_contents3[i//4] + "\n")
                f.write("\n")
                f.write("지도평가 및 개선점 \n")
                f.write("1학년: " + sg(key_seed10, key_math1[i//4]) + "\n")
                f.write("2학년: " + sg(key_seed20, key_math2[i//4]) + "\n")
                f.write("3학년: " + sg(key_seed30, key_math3[i//4]) + "\n")
                f.write("\n")
                # f.write(str(i//4))
                i += 1
            elif (day_key%7 == 1):
                f.write("1학년: " + eng_contents1[i//4] + "\n")
                f.write("2학년: " + eng_contents2[i//4] + "\n")
                f.write("3학년: " + eng_contents3[i//4] + "\n")
                f.write("\n")
                f.write("지도평가 및 개선점 \n")
                f.write("1학년: " + sg(key_seed11, key_eng1[i//4]) + "\n")
                f.write("2학년: " + sg(key_seed21, key_eng2[i//4]) + "\n")
                f.write("3학년: " + sg(key_seed31, key_eng3[i//4]) + "\n")
                f.write("\n")
                # f.write(str(i//4))
                i += 1
            elif (day_key%7 == 2):
                f.write("1학년: " + math_contents1[i//4] + "\n")
                f.write("2학년: " + math_contents2[i//4] + "\n")
                f.write("3학년: " + math_contents3[i//4] + "\n")
                f.write("\n")
                f.write("지도평가 및 개선점 \n")
                f.write("1학년: " + sg(key_seed10, key_math1[i//4]) + "\n")
                f.write("2학년: " + sg(key_seed20, key_math2[i//4]) + "\n")
                f.write("3학년: " + sg(key_seed30, key_math3[i//4]) + "\n")
                f.write("\n")
                # f.write(str(i//4))
                i += 1
            elif (day_key%7 == 3):
                f.write("1학년: " + eng_contents1[i//4] + "\n")
                f.write("2학년: " + eng_contents2[i//4] + "\n")
                f.write("3학년: " + eng_contents3[i//4] + "\n")
                f.write("\n")
                f.write("지도평가 및 개선점 \n")
                f.write("1학년: " + sg(key_seed11, key_eng1[i//4]) + "\n")
                f.write("2학년: " + sg(key_seed21, key_eng2[i//4]) + "\n")
                f.write("3학년: " + sg(key_seed31, key_eng3[i//4]) + "\n")
                f.write("\n")
                # f.write(str(i//4))
                i += 1
        if (num_days%7 == 6):
            key_seed10 = random.randint(0, len_sg-1)
            key_seed20 = random.randint(0, len_sg-1)
            key_seed30 = random.randint(0, len_sg-1)
            key_seed11 = random.randint(0, len_sg-1)
            key_seed21 = random.randint(0, len_sg-1)
            key_seed31 = random.randint(0, len_sg-1)
        day_key += 1
        num_days += 1
f.close()
