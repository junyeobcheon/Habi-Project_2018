# I taught middle school students how to code. This is for writing the report on its progress.

import re

line1 = []
line2 = []
line3 = []

file_output = "코딩_record.txt"
file_source = "코딩일지.txt"

f = open(file_source, "r", encoding = "utf-8")
contents = str(f.readlines())
result1 = re.findall(r"(<date>)([\s\S]+?)(</date>)", contents)
result2 = re.findall(r"(<contents>)([\s\S]+?)(</contents>)", contents)
result3 = re.findall(r"(<evaluation>)([\s\S]+?)(</evaluation>)", contents)
for i in range(len(result1)):
    line1.append(result1[i][1])
    line2.append(result2[i][1])
    line3.append(result3[i][1])
f.close()

f = open(file_output, "w", encoding = "utf-8")
for i in range(len(line1)):
    f.write(str(line1[i]) + "\n")
    f.write("내용: " + str(line2[i]) + "\n")
    f.write("평가: " + str(line3[i]) + "\n")
    f.write("\n")
f.close()
