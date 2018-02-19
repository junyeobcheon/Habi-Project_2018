import calendar
import re
from hydrogen import sentence_generator as sg
import random

len_sg = 30

what_day = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일",
 "월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일",
 "월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일",
 "월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일",
 "월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일",
 "월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]

key_word4 = []
key_word5 = []
key_word6 = []

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

key_word4 = [i for i in zip(key_kor, key_math, key_soc, key_sci)]
key_word4 = key_word4[::-1]

f = open("kor5-1.txt", "r", encoding = "utf-8")
contents = str(f.readlines())
result = re.findall(r"(<dd>)([\s\S]+?)(</dd>)", contents)
for i in range(len(result)):
    kor_contents5.append(result[i][1])
f.close()
kor_contents5 = kor_contents5[::-1]

f = open("math5-1.txt", "r", encoding = "utf-8")
contents = str(f.readlines())
result = re.findall(r"(<dd>)([\s\S]+?)(</dd>)", contents)
for i in range(len(result)):
    math_contents5.append(result[i][1])
f.close()
math_contents5 = math_contents5[::-1]

f = open("soc5-1.txt", "r", encoding = "utf-8")
contents = str(f.readlines())
result = re.findall(r"(<dd>)([\s\S]+?)(</dd>)", contents)
for i in range(len(result)):
    soc_contents5.append(result[i][1])
f.close()
soc_contents5 = soc_contents5[::-1]

f = open("sci5-1.txt", "r", encoding = "utf-8")
contents = str(f.readlines())
result = re.findall(r"(<dd>)([\s\S]+?)(</dd>)", contents)
for i in range(len(result)):
    sci_contents5.append(result[i][1])
f.close()
sci_contents5 = sci_contents5[::-1]

f = open("kor6-1.txt", "r", encoding = "utf-8")
contents = str(f.readlines())
result = re.findall(r"(<dd>)([\s\S]+?)(</dd>)", contents)
for i in range(len(result)):
    kor_contents6.append(result[i][1])
f.close()
kor_contents6 = kor_contents6[::-1]

f = open("math6-1.txt", "r", encoding = "utf-8")
contents = str(f.readlines())
result = re.findall(r"(<dd>)([\s\S]+?)(</dd>)", contents)
for i in range(len(result)):
    math_contents6.append(result[i][1])
f.close()
math_contents6 = math_contents6[::-1]

f = open("soc6-1.txt", "r", encoding = "utf-8")
contents = str(f.readlines())
result = re.findall(r"(<dd>)([\s\S]+?)(</dd>)", contents)
for i in range(len(result)):
    soc_contents6.append(result[i][1])
f.close()
soc_contents6 = soc_contents6[::-1]

f = open("sci6-1.txt", "r", encoding = "utf-8")
contents = str(f.readlines())
result = re.findall(r"(<dd>)([\s\S]+?)(</dd>)", contents)
for i in range(len(result)):
    sci_contents6.append(result[i][1])
f.close()
sci_contents6 = sci_contents6[::-1]

# print(calendar.prmonth(2018, 2))
# print(calendar.monthrange(2018, 2)) (첫요일, 마지막날)

f = open("수업일지.txt", "w", encoding = "utf-8")
i = 0
for month in range(1, 7):
    calndr = calendar.monthrange(2018, month)
    day_key = calndr[0]
    for day in range(1, calndr[1]+1):
        if (day_key%7 < 4 and day_key%7 >= 0):
            line = str(month) + "월" + str(day) + "일" + str(what_day[day_key]) + "\n"
            f.write(line)
            if (day_key%7 == 0):
                f.write("4학년 \n 국어: " + kor_contents4[i//4] + " \n 과학: " + sci_contents4[i//4] + "\n")
                f.write("5학년 \n 국어: " + kor_contents5[i//4] + " \n 과학: " + sci_contents5[i//4] + "\n")
                f.write("6학년 \n 국어: " + kor_contents6[i//4] + " \n 과학: " + sci_contents6[i//4] + "\n")
                f.write("4학년: " + )
                i += 1
            elif (day_key%7 == 1):
                f.write("4학년 \n 수학: " + math_contents4[i//4] + "\n 사회: " + soc_contents4[i//4] + "\n")
                f.write("5학년 \n 수학: " + math_contents5[i//4] + "\n 사회: " + soc_contents5[i//4] + "\n")
                f.write("6학년 \n 수학: " + math_contents6[i//4] + "\n 사회: " + soc_contents6[i//4] + "\n")
                # f.write(str(i//4))
                f.write("\n")
                i += 1
            elif (day_key%7 == 2):
                f.write("4학년 \n 국어: " + kor_contents4[i//4] + " \n 과학: " + sci_contents4[i//4] + "\n")
                f.write("5학년 \n 국어: " + kor_contents5[i//4] + " \n 과학: " + sci_contents5[i//4] + "\n")
                f.write("6학년 \n 국어: " + kor_contents6[i//4] + " \n 과학: " + sci_contents6[i//4] + "\n")
                # f.write(str(i//4))
                f.write("\n")
                i += 1
            elif (day_key%7 == 3):
                f.write("4학년 \n 수학: " + math_contents4[i//4] + "\n 사회: " + soc_contents4[i//4] + "\n")
                f.write("5학년 \n 수학: " + math_contents5[i//4] + "\n 사회: " + soc_contents5[i//4] + "\n")
                f.write("6학년 \n 수학: " + math_contents6[i//4] + "\n 사회: " + soc_contents6[i//4] + "\n")
                # f.write(str(i//4))
                f.write("\n")
                i += 1
        day_key += 1
f.close()
print(key_word4)
