# 추상 클래스 : 추상 메소드를 한 개라도 가지고 있다면 추상 클래스가 된다.
from abc import abstractmethod, ABCMeta

class AbstractClass(metaclass=ABCMeta):   # 추상 클래스 - 객체 생성 불가 
    @abstractmethod
    def abcMethod(self):    # 추상 메소드
        pass
    
    def normalMethod(self):
        print('추상 클래스 내의 일반 메소드')
        
# parent = AbstractClass()   # error : 인스턴스 불가
# TypeError: Can't instantiate abstract class AbstractClass with abstract method abcMethod

# class Child1(AbstractClass):
#     pass
#
# c1 = Child1()  # 객체 생성 불가 
# TypeError: Can't instantiate abstract class Child1 with abstract method abcMethod

class Child1(AbstractClass):
    name = '난 Child1'
    def abcMethod(self):
        print('Child1 에서 추상 메소드를 오버라이드 함 : 순전히 강요 때문에')
        
c1 = Child1()   
print(c1.name)      
c1.abcMethod()
c1.normalMethod()

print()
class Child2(AbstractClass):
    def abcMethod(self):       # 오버라이드 강요
        print('Child2 에서 추상 메소드를 재정의함')
        print('추상의 마법에서 벗어남')
        
    def normalMethod(self):    # 오버라이드 선택
        print('추상 클래스의 일반 메소드를 재정의 함')
        
c2 = Child2()
c2.abcMethod()
c2.normalMethod()

print('다형성-------')
good = c1
good.abcMethod()
good.normalMethod()
print()
good = c2
good.abcMethod()
good.normalMethod()

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    