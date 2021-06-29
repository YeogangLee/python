from random import random
mine = input("가위바위보 입력 : ")
com = ""
result = ""

#print(mine)

rnd = random()
if rnd > 0.66 :
    com = "가위"
elif rnd > 0.33 :
    com = "바위"
else:
    com = "보"
    
if (com == "가위" and mine == "가위") or (com == "바위" and mine == "바위") or (com == "보" and mine == "보") :
    result = "무승부"
elif (com == "가위" and mine == "바위") or (com == "바위" and mine == "보") or (com == "보" and mine == "가위") :
    result = "사람 승"
elif (com == "가위" and mine == "보") or (com == "바위" and mine == "가위") or (com == "보" and mine == "바위") :
    result = "컴퓨터 승"

print("mine", mine)
print("com", com)
print("result", result)
