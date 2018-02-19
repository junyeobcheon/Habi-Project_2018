import re

line1 = []
line2 = []
line3 = []

f = open("코딩일지.txt", "r", encoding = "utf-8")
contents = str(f.readlines())
result1 = re.findall(r"(<d>)([\s\S]+?)(</d>)", contents)
result2 = re.findall(r"(<con>)([\s\S]+?)(</con>)", contents)
result3 = re.findall(r"(<eval>)([\s\S]+?)(</eval>)", contents)

print(len(result1))

# result1 = result1[::-1]
# result2 = result2[::-1]
# result3 = result3[::-1]
# f.close()
# for i in range(len(result1)):
#     print(result1[i][1])
# f = open("coding_record.txt", "w", encoding = "utf-8")
# for i in range(len(result1)):
#     if (result2[i][1] != "jump"):
#         f.write(str(result1[i][1]) + "\n")
#         f.write(str(result2[i][1]) + "\n")
#         f.write(str(result3[i][1]) + "\n")
# f.close()
