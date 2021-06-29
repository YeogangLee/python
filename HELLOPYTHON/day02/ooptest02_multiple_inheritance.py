class Dog:
    def __init__(self):
        self.flag_bark = True
    
    def do_surgery(self):
        self.flag_bark = False
        
class Bird:
    def __init__(self):
        self.skill_fly = 0
        
    def learn(self):
        self.skill_fly += 1 
    
class GaeSae(Dog, Bird):
    def __init__(self):
        # Parent의 생성자 호출
        # 멀티 상속은 super를 사용하지 않는다
        Dog.__init__(self)
        Bird.__init__(self)
    
    def __str__(self):
        return "{}, {}".format(self.flag_bark, self.skill_fly)
    
    
if __name__ == "__main__":
    gs = GaeSae()
    print("기본 GaeSae")
    print(gs)
    print(gs.flag_bark)
    print(gs.skill_fly)
    print()
    gs.do_surgery()
    print("수술 후")
    print(gs)
    print(gs.flag_bark)
    print(gs.skill_fly)
    print()
    gs.learn()
    print("공부 후")
    print(gs)
    print(gs.flag_bark)
    print(gs.skill_fly)
    print()