dan = input("출력할 단 수 입력 : ")
int_dan = int(dan)

# print("{}*{}={}".format(2, 1, 2*1))
# print("{}*{}={}".format(2, 2, 2*2))

# for문 많이 쓰면 안 좋다
# 한 눈에 보고, 구구단이라는 걸 알아볼 수 있는 코드가 더 좋은 코드
# 무조건 for문 돌리는 것보다 낫다.
print("{}*{}={}".format(int_dan, 1, int_dan*1))
print("{}*{}={}".format(int_dan, 2, int_dan*2))
print("{}*{}={}".format(int_dan, 3, int_dan*3))
print("{}*{}={}".format(int_dan, 4, int_dan*4))
print("{}*{}={}".format(int_dan, 5, int_dan*5))
print("{}*{}={}".format(int_dan, 6, int_dan*6))
print("{}*{}={}".format(int_dan, 7, int_dan*7))
print("{}*{}={}".format(int_dan, 8, int_dan*8))
print("{}*{}={}".format(int_dan, 9, int_dan*9))
