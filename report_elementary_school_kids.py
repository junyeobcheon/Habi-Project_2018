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

key_word4_0 = []
key_word4_1 = []
key_word5_0 = []
key_word5_1 = []
key_word6_0 = []
key_word6_1 = []

key_kor = []
key_math = []
key_soc = []
key_sci = []

kor_contents4 = []
math_contents4 = []
soc_contents4 = []
sci_contents4 = []

kor_contents5 = []
math_contents5 = []
soc_contents5 = []
sci_contents5 = []

kor_contents6 = []
math_contents6 = []
soc_contents6 = []
sci_contents6 = []

f = open("kor4-1.txt", "r", encoding = "utf-8")
contents = str(f.readlines())
result = re.findall(r"(<dd>)([\s\S]+?)(</dd>)", contents)
result1 = re.findall(r"(<w>)([\s\S]+?)(</w>)", contents)
for i in range(len(result)):
    kor_contents4.append(result[i][1])
    key_kor.append(result1[i][1])
f.close()
kor_contents4 = kor_contents4[::-1]

f = open("math4-1.txt", "r", encoding = "utf-8")
contents = str(f.readlines())
result = re.findall(r"(<dd>)([\s\S]+?)(</dd>)", contents)
result2 = re.findall(r"(<w>)([\s\S]+?)(</w>)", contents)
for i in range(len(result)):
    math_contents4.append(result[i][1])
    key_math.append(result2[i][1])
f.close()
math_contents4 = math_contents4[::-1]

f = open("soc4-1.txt", "r", encoding = "utf-8")
contents = str(f.readlines())
result = re.findall(r"(<dd>)([\s\S]+?)(</dd>)", contents)
result3 = re.findall(r"(<w>)([\s\S]+?)(</w>)", contents)
for i in range(len(result)):
    soc_contents4.append(result[i][1])
    key_soc.append(result3[i][1])
f.close()
soc_contents4 = soc_contents4[::-1]

f = open("sci4-1.txt", "r", encoding = "utf-8")
contents = str(f.readlines())
result = re.findall(r"(<dd>)([\s\S]+?)(</dd>)", contents)
result4 = re.findall(r"(<w>)([\s\S]+?)(</w>)", contents)
for i in range(len(result)):
    sci_contents4.append(result[i][1])
    key_sci.append(result4[i][1])
f.close()
sci_contents4 = sci_contents4[::-1]

key_word4_0 = [i for i in zip(key_kor, key_sci)]
key_word4_1 = [i for i in zip(key_math, key_soc)]
key_word4_0 = key_word4_0[::-1]
key_word4_1 = key_word4_1[::-1]

key_kor = []
key_math = []
key_soc = []
key_sci = []

f = open("kor5-1.txt", "r", encoding = "utf-8")
contents = str(f.readlines())
result = re.findall(r"(<dd>)([\s\S]+?)(</dd>)", contents)
result1 = re.findall(r"(<w>)([\s\S]+?)(</w>)", contents)
for i in range(len(result)):
    kor_contents5.append(result[i][1])
    key_kor.append(result1[i][1])
f.close()
kor_contents5 = kor_contents5[::-1]

f = open("math5-1.txt", "r", encoding = "utf-8")
contents = str(f.readlines())
result = re.findall(r"(<dd>)([\s\S]+?)(</dd>)", contents)
result2 = re.findall(r"(<w>)([\s\S]+?)(</w>)", contents)
for i in range(len(result)):
    math_contents5.append(result[i][1])
    key_math.append(result2[i][1])
f.close()
math_contents5 = math_contents5[::-1]

f = open("soc5-1.txt", "r", encoding = "utf-8")
contents = str(f.readlines())
result = re.findall(r"(<dd>)([\s\S]+?)(</dd>)", contents)
result3 = re.findall(r"(<w>)([\s\S]+?)(</w>)", contents)
for i in range(len(result)):
    soc_contents5.append(result[i][1])
    key_soc.append(result3[i][1])
f.close()
soc_contents5 = soc_contents5[::-1]

f = open("sci5-1.txt", "r", encoding = "utf-8")
contents = str(f.readlines())
result = re.findall(r"(<dd>)([\s\S]+?)(</dd>)", contents)
result4 = re.findall(r"(<w>)([\s\S]+?)(</w>)", contents)
for i in range(len(result)):
    sci_contents5.append(result[i][1])
    key_sci.append(result4[i][1])
f.close()
sci_contents5 = sci_contents5[::-1]

key_word5_0 = [i for i in zip(key_kor, key_sci)]
key_word5_1 = [i for i in zip(key_math, key_soc)]
key_word5_0 = key_word5_0[::-1]
key_word5_1 = key_word5_1[::-1]

key_kor = []
key_math = []
key_soc = []
key_sci = []

f = open("kor6-1.txt", "r", encoding = "utf-8")
contents = str(f.readlines())
result = re.findall(r"(<dd>)([\s\S]+?)(</dd>)", contents)
result1 = re.findall(r"(<w>)([\s\S]+?)(</w>)", contents)
for i in range(len(result)):
    kor_contents6.append(result[i][1])
    key_kor.append(result1[i][1])
f.close()
kor_contents6 = kor_contents6[::-1]

f = open("math6-1.txt", "r", encoding = "utf-8")
contents = str(f.readlines())
result = re.findall(r"(<dd>)([\s\S]+?)(</dd>)", contents)
result2 = re.findall(r"(<w>)([\s\S]+?)(</w>)", contents)
for i in range(len(result)):
    math_contents6.append(result[i][1])
    key_math.append(result2[i][1])
f.close()
math_contents6 = math_contents6[::-1]

f = open("soc6-1.txt", "r", encoding = "utf-8")
contents = str(f.readlines())
result = re.findall(r"(<dd>)([\s\S]+?)(</dd>)", contents)
result3 = re.findall(r"(<w>)([\s\S]+?)(</w>)", contents)
for i in range(len(result)):
    soc_contents6.append(result[i][1])
    key_soc.append(result3[i][1])
f.close()
soc_contents6 = soc_contents6[::-1]

f = open("sci6-1.txt", "r", encoding = "utf-8")
contents = str(f.readlines())
result = re.findall(r"(<dd>)([\s\S]+?)(</dd>)", contents)
result4 = re.findall(r"(<w>)([\s\S]+?)(</w>)", contents)
for i in range(len(result)):
    sci_contents6.append(result[i][1])
    key_sci.append(result4[i][1])
f.close()
sci_contents6 = sci_contents6[::-1]

key_word6_0 = [i for i in zip(key_kor, key_sci)]
key_word6_1 = [i for i in zip(key_math, key_soc)]
key_word6_0 = key_word6_0[::-1]
key_word6_1 = key_word6_1[::-1]
# print(calendar.prmonth(2018, 2))
# print(calendar.monthrange(2018, 2)) (첫요일, 마지막날)

f = open("수업일지.txt", "w", encoding = "utf-8")
i = 0
key_seed4 = random.randint(0, len_sg-1)
rand_seed4 = random.randint(0, 1)
key_seed5 = random.randint(0, len_sg-1)
rand_seed5 = random.randint(0, 1)
key_seed6 = random.randint(0, len_sg-1)
rand_seed6 = random.randint(0, 1)
for month in range(first_month, last_month + 1):
    calndr = calendar.monthrange(year, month)
    day_key = calndr[0]
    num_days = 0
    for day in range(1, calndr[1]+1):
        if (day_key%7 < 4 and day_key%7 >= 0):
            line = str(month) + "월" + str(day) + "일" + str(what_day[day_key]) + "\n"
            f.write(line)
            if (day_key%7 == 0):
                f.write("4학년 \n 국어: " + kor_contents4[i//4] + " \n 과학: " + sci_contents4[i//4] + "\n")
                f.write("5학년 \n 국어: " + kor_contents5[i//4] + " \n 과학: " + sci_contents5[i//4] + "\n")
                f.write("6학년 \n 국어: " + kor_contents6[i//4] + " \n 과학: " + sci_contents6[i//4] + "\n")
                f.write("\n")
                f.write("지도평가 및 개선점 \n")
                f.write("4학년: " + sg(key_seed4, key_word4_0[i//4][rand_seed4]) + "\n")
                f.write("5학년: " + sg(key_seed5, key_word5_0[i//4][rand_seed5]) + "\n")
                f.write("6학년: " + sg(key_seed6, key_word6_0[i//4][rand_seed6]) + "\n")
                f.write("\n")
                # f.write(str(i//4))
                i += 1
            elif (day_key%7 == 1):
                f.write("4학년 \n 수학: " + math_contents4[i//4] + "\n 사회: " + soc_contents4[i//4] + "\n")
                f.write("5학년 \n 수학: " + math_contents5[i//4] + "\n 사회: " + soc_contents5[i//4] + "\n")
                f.write("6학년 \n 수학: " + math_contents6[i//4] + "\n 사회: " + soc_contents6[i//4] + "\n")
                # f.write(str(i//4))
                f.write("\n")
                f.write("지도평가 및 개선점 \n")
                f.write("4학년: " + sg(key_seed4, key_word4_1[i//4][rand_seed4]) + "\n")
                f.write("5학년: " + sg(key_seed5, key_word4_1[i//4][rand_seed5]) + "\n")
                f.write("6학년: " + sg(key_seed6, key_word6_1[i//4][rand_seed6]) + "\n")
                f.write("\n")
                i += 1
            elif (day_key%7 == 2):
                f.write("4학년 \n 국어: " + kor_contents4[i//4] + " \n 과학: " + sci_contents4[i//4] + "\n")
                f.write("5학년 \n 국어: " + kor_contents5[i//4] + " \n 과학: " + sci_contents5[i//4] + "\n")
                f.write("6학년 \n 국어: " + kor_contents6[i//4] + " \n 과학: " + sci_contents6[i//4] + "\n")
                # f.write(str(i//4))
                f.write("\n")
                f.write("지도평가 및 개선점 \n")
                f.write("4학년: " + sg(key_seed4, key_word4_0[i//4][rand_seed4]) + "\n")
                f.write("5학년: " + sg(key_seed5, key_word4_0[i//4][rand_seed5]) + "\n")
                f.write("6학년: " + sg(key_seed6, key_word6_0[i//4][rand_seed6]) + "\n")
                f.write("\n")
                i += 1
            elif (day_key%7 == 3):
                f.write("4학년 \n 수학: " + math_contents4[i//4] + "\n 사회: " + soc_contents4[i//4] + "\n")
                f.write("5학년 \n 수학: " + math_contents5[i//4] + "\n 사회: " + soc_contents5[i//4] + "\n")
                f.write("6학년 \n 수학: " + math_contents6[i//4] + "\n 사회: " + soc_contents6[i//4] + "\n")
                # f.write(str(i//4))
                f.write("\n")
                f.write("지도평가 및 개선점 \n")
                f.write("4학년: " + sg(key_seed4, key_word4_1[i//4][rand_seed4]) + "\n")
                f.write("5학년: " + sg(key_seed5, key_word4_1[i//4][rand_seed5]) + "\n")
                f.write("6학년: " + sg(key_seed6, key_word6_1[i//4][rand_seed6]) + "\n")
                f.write("\n")
                i += 1
        if (num_days%7 == 6):
            key_seed4 = random.randint(0, len_sg-1)
            rand_seed4 = random.randint(0, 1)
            key_seed5 = random.randint(0, len_sg-1)
            rand_seed5 = random.randint(0, 1)
            key_seed6 = random.randint(0, len_sg-1)
            rand_seed6 = random.randint(0, 1)
        day_key += 1
        num_days += 1
f.close()
