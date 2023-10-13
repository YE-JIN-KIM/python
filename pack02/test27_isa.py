# 상속 연습
print('클래스는 모듈의 멤버')

class Person:
    say = '난 사람이야~'        # public 
    nai = '20'
    __my = 'private member'  # private
    
    def __init__(self, nai):
        print('Person 생성자')
        self.nai = nai
    
    def printInfo(self):
        print('나이:{}, 이야기:{}'.format(self.nai, self.say))
        
    def hello(self):
        print('안녕')
        print(self.__my)
           
    @staticmethod  
    def kbs(tel):
        print('kbs_static method(클래스 소속) :', tel)

        
print(Person.say, Person.nai)
# Person.printInfo()
p = Person('25')
print(p.say, p.nai)
p.printInfo()

p.hello()
p.kbs('111-1234')       # 비권장
Person.kbs('111-1234')  # 권장 

print('*****' * 20)
class Employee(Person):
    subject = '근로자'
    
    def __init__(self):
        print('Employee 생성자')
        
    def printInfo(self):   # method overriding
        print('Employee의 오버라이딩된 printinfo')
        
    def eprintInfo(self):
        print(self.say, super().say)   # self.say : Employee부터 찾고 없으면 올라감 , super().say : 처음부터 Person으로 가서 찾음
        self.hello()
        self.printInfo()     # 현재없으면 상위클래스로 올라감 
        super().printInfo()  # 바로 상위클래스로 올라감 
        
e = Employee()
print(e.say, e.subject)
e.eprintInfo()

print('***' * 5)
class Worker(Person):
    say = 'worker의 say'
    
    def __init__(self, nai):
        print('Worker 생성자')
        super().__init__(nai)     # Bound method call, 생성자 나중에 적어줘도 가능
        
    def printInfo(self):
        print('Worker에 선언된 printInfo')
        
    def wprintInfo(self):
        self.printInfo()
        super().printInfo()

w = Worker('30')
print(w.say, w.nai)
w.wprintInfo()

print('^^^' * 10)
class Programmer(Worker):
    def __init__(self, nai):
        print('Programmer 생성자')
        #super().__init__(nai)      # Bound call
        Worker.__init__(self, nai)  # UnBound call
        
    def pprintInfo(self):
        self.wprintInfo()
        
    def hello2(self):
        print('안녕')
        #print(self.__my)      # err : private 멤버 이므로 호출이 안됨 현재 있는 클래스내에서만 유효함 
   
pr = Programmer(33)
print(pr.say, pr.nai)
pr.pprintInfo()
pr.hello2()
pr.kbs('234-5678')
Programmer.kbs('234-5678')

print('\n클래스 타입 확인 ----')
print(type(1.2))
print(type(pr))
print(Programmer.__bases__)
print(Worker.__bases__)
print(Person.__bases__)     # (<class 'object'>,)















