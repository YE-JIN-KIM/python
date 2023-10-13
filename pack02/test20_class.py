# class 멤버 호출 관련

kor = 100

def abc():
    print('모듈의 멤버 함수')

class MyClass:
    kor = 90
    
    def abc(self):
        print('abc method')
        
    def show(self):
        kor = 80
        print(self.kor)
        print(kor)    # 변수 호출 순서 : 지역변수 > 모듈변수 
        self.abc()    # method를 호출 
        abc()         # function을 호출 
        
my = MyClass()
my.show()

from pack02.test20_other import Our
print(Our.a)
print('our1 - - -')
our1 = Our()
print(our1.a)
our1.a = 2
print(our1.a)
print('our2 - - -')
our2= Our()
print(our2.a)





























