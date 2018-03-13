import random

num_cir = 190
num_tri = 15
tot_char = 271
# x 한 개 당 o과 세모의 갯수 입력하기
def rand_eval(cir, tri):
    key = random.randint(0, cir+tri)
    if (key == 0):
        return "×"
    elif (key >= 0 and key <= tri):
        return "△"
    else:
        return "○"

f = open("기본생활.txt", "w", encoding = "utf-8")
for i in range(0, tot_char):
    linee = []
    for col in range(0,4):
        linee.append(rand_eval(num_cir, num_tri))
    line = ",".join(linee)
    f.write(line)
    f.write("\n")
f.close()
