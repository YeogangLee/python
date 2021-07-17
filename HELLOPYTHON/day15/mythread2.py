#Python Thread 예제1
import threading
 
def execute():
    """
    쓰레드에서 실행 할 함수
    """
    print(threading.currentThread().getName())
     
def printNumber():
    for i in range(55000):
        if i % 100 == 0:
            print()
        print(i, end="")
        
def printChar():
    for i in range(55000) :
        print(i,chr(i),end="")


if __name__ == '__main__':
    my_t1 = threading.Thread(target=printNumber)
    my_t2 = threading.Thread(target=printChar)
    my_t1.start()
    my_t2.start()
    
    # for i in range(1,8): # 1 ~ 7 실행
    #     my_thread = threading.Thread(target=execute, args=(i,))
    #     my_thread.start()
    

