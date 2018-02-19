import re

line1 = []
line2 = []
line3 = []

f = open("코딩일지.txt", "r", encoding = "utf-8")
contents = str(f.readlines())
result1 = re.findall(r"(<d>)([\s\S]+?)(</d>)", contents)
result2 = re.findall(r"(<con>)([\s\S]+?)(</con>)", contents)
result3 = re.findall(r"(<eval>)([\s\S]+?)(</eval>)", contents)
for i in range(len(result1)):
    line1.append(result1[i][1])
    line2.append(result2[i][1])
    line3.append(result3[i][1])
f.close()

f = open("coding_record.txt", "w", encoding = "utf-8")
for i in range(len(line1)):
    f.write(str(line1[i]) + "\n")
    f.write("내용: " + str(line2[i]) + "\n")
    f.write("평가: " + str(line3[i]) + "\n")
    f.write("\n")
f.close()
