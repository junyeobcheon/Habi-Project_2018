import calendar
import re
from oxygen import sentence_generator as sg
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

key_word4 = [i for i in zip(key_kor, key_math, key_soc, key_sci)]
# key_word4 = [i for i in zip(key_math, key_soc)]
key_word4 = key_word4[::-1]
# key_word4_1 = key_word4_1[::-1]

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

key_word5 = [i for i in zip(key_kor, key_math, key_soc, key_sci)]
# key_word5 = [i for i in zip(key_math, key_soc)]
key_word5 = key_word5[::-1]
# key_word5 = key_word5_1[::-1]

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

key_word6 = [i for i in zip(key_kor, key_math, key_soc, key_sci)]
# key_word6_1 = [i for i in zip(key_math, key_soc)]
key_word6 = key_word6[::-1]
# key_word6_1 = key_word6_1[::-1]
# print(calendar.prmonth(2018, 2))
# print(calendar.monthrange(2018, 2)) (첫요일, 마지막날)

f = open("수업일지csv.txt", "w", encoding = "utf-8")
i = 0
key_seed4 = random.randint(0, len_sg-1)
rand_seed4 = random.randint(0, 1)
sub_seed4 = random.randint(0,3)
key_seed5 = random.randint(0, len_sg-1)
rand_seed5 = random.randint(0, 1)
sub_seed5 = random.randint(0,3)
key_seed6 = random.randint(0, len_sg-1)
rand_seed6 = random.randint(0, 1)
sub_seed6 = random.randint(0,3)
header_key = ["1월", "2월", "3월", "4월", "5월", "6월", "7월", "8월", "9월", "10월", "11월", "12월"]
for month in range(first_month, last_month + 1):
    calndr = calendar.monthrange(year, month)
    day_key = calndr[0]
    num_days = 0
    week_key = 1
    row_elements = []
    des4 = []
    des5 = []
    des6 = []
    for day in range(1, calndr[1]+1):
        if (week_key == 1):
            kor4 = kor_contents4[i//7]
            kor5 = kor_contents5[i//7]
            kor6 = kor_contents6[i//7]
            math4 = math_contents4[i//7]
            math5 = math_contents5[i//7]
            math6 = math_contents6[i//7]
            soc4 = soc_contents4[i//7]
            soc5 = soc_contents5[i//7]
            soc6 = soc_contents6[i//7]
            sci4 = sci_contents4[i//7]
            sci5 = sci_contents5[i//7]
            sci6 = sci_contents6[i//7]
        row_elements = [header_key[month-1], kor4, math4, soc4,
         sci4, kor5, math5, soc5, sci5, kor6, math6, soc6, sci6]
        if (day_key%7 == 0):
            # line = str(month) + "월" + str(day) + "일" + str(what_day[day_key])
            # row_elements = [line, kor_contents4[i//7], kor_contents5[i//7], kor_contents6[i//7], math_contents4[i//7],
            # math_contents5[i//7], math_contents6[i//7], soc_contents4[i//7], soc_contents5[i//7], soc_contents6[i//7],
            # sci_contents6[i//7], sci_contents5[i//7], sci_contents6[i//7],
            # sg(key_seed4, key_word4[i//7][sub_seed4]),
            # sg(key_seed5, key_word5[i//7][sub_seed5]),
            # sg(key_seed6, key_word6[i//7][sub_seed6])]
            des4.append(sg(key_seed4, key_word4[i//7][sub_seed4]))
            des5.append(sg(key_seed5, key_word5[i//7][sub_seed5]))
            des6.append(sg(key_seed6, key_word6[i//7][sub_seed6]))
            # row = '@'.join(row_elements)
            # f.write(row)
            # f.write("\n")
        if (num_days%7 == 6):
            key_seed4 = random.randint(0, len_sg-1)
            rand_seed4 = random.randint(0, 1)
            sub_seed4 = random.randint(0, 3)
            key_seed5 = random.randint(0, len_sg-1)
            rand_seed5 = random.randint(0, 1)
            sub_seed5 = random.randint(0, 3)
            key_seed6 = random.randint(0, len_sg-1)
            rand_seed6 = random.randint(0, 1)
            sub_seed6 = random.randint(0, 3)
            week_key += 1
        i += 1
        day_key += 1
        num_days += 1
        if (day == calndr[1]):
            row_elements.extend(des4)
            row_elements.append(" ")
            row_elements.extend(des5)
            row_elements.append(" ")
            row_elements.extend(des6)
            row = '@'.join(row_elements)
            f.write(row)
            f.write("\n")
f.close()
