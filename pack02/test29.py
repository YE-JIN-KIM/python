# 다중 상속
class Tiger:
    data = '호랑이 세상'
    
    def cry(self):
        print('호랑이가 소리를 ...')
        
    def eat(self):
        print('맹수는 고기를 무척 좋아한다')
        

class Lion:
    def cry(self):
        print('사자의 울부짖음')
        
    def hobby(self):
        print('백수의 왕은 채팅을 즐긴다')

class Liger1(Tiger, Lion):    # 다중 상속 (중복될 시 먼저 적어준 멤버로 호출)
    pass

obj1 = Liger1()
obj1.cry()
obj1.eat()
obj1.hobby()
print(obj1.data)

print('- - - - - -- - - - -- - ')
def hobby():
    print('모듈의 멤버인 함수')
    
class Liger2(Lion, Tiger):
    data = '라이거 만세'
    
    def play(self):
        print('라이거 고유 메소드')
        
    def hobby(self):
        print('라이거는 운동을 좋아한다')
        
    def showHobby(self):
        self.hobby()
        super().hobby()
        hobby()
        print(self.data + ", " + super().data)
    
obj2 = Liger2()
obj2.cry()
obj2.showHobby()





























