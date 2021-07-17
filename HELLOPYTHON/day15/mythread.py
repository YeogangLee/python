def printNumber():
    for i in range(55000):
        if i % 100 == 0:
            print()
        print(i, end="")
        
def printChar():
    for i in range(55000) :
        print(i,chr(i),end="")
        
if __name__ == '__main__':
    printNumber()
    printChar()