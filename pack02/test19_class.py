# class : 멤버로 변수와 메소드를 포함한 집합체. 객체 중심의 독립적인 프로그램밍이 가능함. OOP 구현
class Car:
    handle = 0
    speed = 0
    
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        
    def showData(self):
        km = '킬로미터'
        msg = '속도 : ' + str(self.speed) + km
        return msg

print(Car.handle)
#Car.showData()   # TypeError: Car.showData() missing 1 required positional argument: 'self'

car1 = Car('tom',80)
print('car1 : ', car1.handle, car1.name, car1.speed)
car1.color = '보라'    # car1 객체에 color 변수 추가 
print('car1 :', car1.color)
print()
car2 = Car('james',100)
print('car2 : ', car2.handle, car2.name, car2.speed)
print()
print(Car.handle, car1.handle, car2.handle)
print(Car.speed, car1.speed, car2.speed)
print(car1.color)
print(Car, car1, car2)
print(id(Car), id(car1), id(car2))   # 3개 주소가 다름 (객체가 3개 생성됨)
print(car1.__dict__)   # 각 객체의 멤버 확인
print(car2.__dict__)   # 각 객체의 멤버 확인

print('\n메소드 - - - - - ')
print('car1 :', car1.showData())
print('car2 :', car2.showData())

car1.speed = 55
car2.speed = 88
print('car1 :', car1.showData())
print('car2 :', car2.showData())

print()
Car.handle = 1
print('car1 : ', car1.handle, car1.name, car1.speed)
print('car2 : ', car2.handle, car2.name, car2.speed)




















