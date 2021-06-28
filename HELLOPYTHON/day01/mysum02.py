# range()를 이용해서 1부터 20까지의 수 중 짝수의 합을 구하시오.

sum = 0
for i in range(1, 21):
    if i%2 == 0:
        sum += i
    
print("sum", sum)





    