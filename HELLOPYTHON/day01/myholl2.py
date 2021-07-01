from random import random
mine = input("홀 / 짝 입력 : ")

rnd = random()
com = ""
result = ""

if rnd > 0.5 :
    com = "홀"
else:
    com = "짝"
    
if mine == com :
    result = "승리"
else :
    result = "패배"
    
print("컴퓨터 : {}\n사람 : {}".format(com, mine))
# print(result,"하셨습니다.") # 띄어쓰기 무조건 포함...
print("{}하셨습니다.".format(result))

    