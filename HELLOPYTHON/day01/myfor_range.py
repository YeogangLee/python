arr = range(3)
#=> arr = [0,1,2]
arr2 = range(1, 3)

for i in arr:
    print(i)
    
for i in arr2:
    print(i)

print()

names = ["김소희","이여강","백지혜"]

#가능
print("-- 배열 출력 --")
for i in names:
    print(i) 

#불가능                    압축을 풀기에 너무 많은 값
#오류 메세지 - ValueError: too many values to unpack (expected 2)
# for i, item in names:
#     print(i, item) 

#가능
for i, item in enumerate(names):
    print(i, item)
    