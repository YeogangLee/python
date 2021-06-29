# 물어보는 것은 항상 문자열로 받는다.
a = input("시작 숫자 입력 : ")
b = input("끝 숫자 입력 : ")

int_a = int(a)
int_b = int(b)

sum = 0
for i in range(int_a, int_b+1):
    sum += i
    
print("sum", sum)