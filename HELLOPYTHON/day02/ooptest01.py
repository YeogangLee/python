class Animal:
    
    # 생성자가 클래스명과 다르다
    # 충격! 
    def __init__(self):
        self.age = 0
    
    def aging(self):
        self.age += 1

class Human(Animal):
    def __init__(self):
        # pass
        print("생성자 constructor")
        super().__init__()
        self.skill_speack = 0
    
    def learnSpeak(self, step=1):
        # 파라미터가 없으면 step을 1로 인식
        # 파라미터가 있으면 그건 그걸로 인식
        self.skill_speack += step
        
    def __del__(self):
        print("소멸자 destroyer")
        
    def __str__(self):
        return "{}, {}".format(self.age, self.skill_speack)
    
if __name__ == "__main__":
    # ani = Animal()
    # print(ani.age)
    # ani.aging()
    # print(ani.age)
    # print()
    
    hum = Human()
    # print(hum.age)
    # print(hum.skill_speack)
    print(hum)
    hum.aging()
    # hum.learnSpeak() # 파라미터가 없는 경우
    hum.learnSpeak(5)  # 파라미터가 있는 경우
    # print(hum.age)
    # print(hum.skill_speack)
    print(hum)