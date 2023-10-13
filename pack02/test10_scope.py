# 변수의 생존 범위 : global, local
# Local > Enclosing function > Global > Builtin (LEGB순서)

player = '국가대표'  # 전역변수 (모듈의 어디서든 공유 가능)

def funcSports():
    name = '신기루'  # 지역변수 (함수 내에서만 유효)
    player = '지역대표'
    print(name, player)
    
funcSports()

print()
a = 1; b = 2; c = 3
print('출력1 -- a:{}, b:{}, c:{}'.format(a,b,c))
def outerfunc():
    a = 4
    b = 5
    def innerfunc():
        global c    # 많이쓰임
        nonlocal b  # 자주 안쓰임 
        #c = 6
        print('출력2 -- a:{}, b:{}, c:{}'.format(a,b,c))
        c = 6  # local variable 'c' where it is not 선언을 나중에 하고 찍으면 문제발생 그래서 global
        b = 7
    innerfunc()
    print('출력3 -- a:{}, b:{}, c:{}'.format(a,b,c))      
    
outerfunc()
print('출력4 -- a:{}, b:{}, c:{}'.format(a,b,c))

print('\n인수와 매개변수 키워드 매칭 - - - - -')
def showGugu(start = 1, end = 5):
    for dan in range(start, end + 1):
        print(str(dan) + '단 출력', end = " ")
    print()
        
showGugu(2, 3)  # 위치 매개변수 
showGugu(2)     # 기본값 매개변수 
showGugu()
# showGugu(2, 3, 4)
showGugu(start=5, end=7)  # 키워드 매개변수
showGugu(end=9, start=8)
showGugu(2, end=4)
# showGugu(start=2, 4) SyntaxError: positional argument follows keyword argument
# showGugu(end=9, 8)   SyntaxError: positional argument follows keyword argument

print()
# 가변 매개변수 : 인수의 갯수가 동적 
# * a, b = [1,2,3,4,5]
def fu1(*ar):  # 패키지 연산자 
    print(ar)
    for a in ar:
        print('밥 : ' + a)
    
fu1('공기밥','주먹밥')
fu1('공기밥','주먹밥','김밥')

print()
def fu2(bap, *ar): 
#def fu2(*ar, bap): error
    print(bap)  
    print(ar)
    for a in ar:
        print('밥 : ' + a)
    
fu2('공기밥','주먹밥')
fu2('공기밥','주먹밥','김밥')

print()
def selectCalc(choice, *ar):
    if choice == '+':
        imsi = 0
        for i in ar:
            imsi += i
    elif choice == '*':
        imsi = 1
        for i in ar:
            imsi *= i
    return imsi


print(selectCalc('+', 1,2,3,4,5))   # tuple 자료 
print(selectCalc('*', 1,2,3,4,5))

print()
# dict를 인수로 전달
def fu3(w, h, **etc):   # **을 넣어주면 dict로 처리됨 
    print('몸무게:{}, 키:{}'.format(w, h))
    print(etc)

fu3(66, 177, irum='홍길동')
fu3(77, 178, irum='고길동', nai=22)

print()
def fuFinal(a,b,*c,**d):
    print(a, ' ', b)
    print(c)
    print(d)

fuFinal(1, 2)
fuFinal(1, 2, 3, 4, 5)
fuFinal(1, 2, 3, 4, 5, m = 6, n = 7)


























