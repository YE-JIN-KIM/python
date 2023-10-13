# 반복문 for
# for target in object: ...

for i in [1, 2, 3, 4, 5]:
    print(i, end=' ')

print()
for i in {1, 2, 3, 4, 5}:
    print(i, end=' ')
    
print()
for i in 1, 2, 3, 4, 5:
    print(i, end=' ')
    
print()
soft = {'java':'웹용언어', 'python':'만능언어', 'js':'웹용스크립트'}
for i in soft.items():
    # print(i)  # ('java', '웹용언어')
    print(i[0] + '^^;' + i[1])

for k, v in soft.items():
    print(k)
    print(v)
    
print()
for aa in soft.keys():
    print(aa, end=' ')
    
print()
for bb in soft.keys():
    print(bb, end=' ')
        
print()
numbers = [1, 3, 5, 7, 9]
numbers = [-3, 5, 7, 12]
tot = 0
for a in numbers:
    tot += a
    
print('합은 ' + str(tot) + ', 평균은 ' + str((tot / len(numbers))))

print()
li = ['a', 'b', 'c']
for k, d in enumerate(li):
    print(k, d)

print()
for n in [2, 3]:
    print('---------{}단--'.format(n))
    for i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        print('{} * {} = {}'.format(n, i, n * i), end=' ')
    print()

print()
datas = [1, 2, 3, 4, 5]
for i in datas:
    if i == 2: continue
    if i == 4: break
    print(i, end=' ')
else:
    print('for 정상 종료')
    
print()
jumsu = [95, 70, 60, 55, 100]  # 70점 이상만 합격 
num = 0
for jum in jumsu:
    num += 1;
    if jum < 70:continue
    print('%d번쨰 합격! ' % num)
    
print('for + 정규 표현식 연습 ----------')
import re
ss = """민주당 내부에선 강경파 의원들을 중심으로 한 장관을 탄핵해야 한다는 주장이 나오고 있다.
‘친명계’ 민형배 의원은 지난 6일 국회 본회의에서 “검찰을     심판대에 세워야 한다. 
그 첫 단계가 한 장관 탄핵”이라며 “이 대표 체포동의안 제안설명 때 두 번 모두 피의사실을 
공표해 형법을 위반했다”고 주장했다. 홍익표 민주당 원내대표도  
지난 8일 방송에 출연해 한 장관 탄핵 소추와 관련해 “10월 중하순쯤에 대통령의 국정운영 기조의 변화 여부를 보면서 
판단할 것”이라며 “대통령 국정기조의 가장 큰 문제가 검찰을 활용한 검찰 정치”라고 주장했다.
그 첫 단계가 한 장관 탄핵”이라며 “이 대표 체포동의안 제안설명 때 두 번 모두 피의사실을 
공표해 형법을 위반했다”고 주장했다. 홍익표 민주당 원내대표도."""
print(type(ss))
ss2 = re.sub(r'[^가-힣\s]','', ss)  
print(ss2)
ss3 = ss2.split(' ')
print(ss3)

cou = {}  # 단어의 발생 횟수를 dict로 저장
for i in ss3:
    if i in cou:
        cou[i] += 1
    else:
        cou[i] = 1
print(cou)

print()
for ss in ['1111-1234','일이삼-이이이', '234-6789']:
    if re.match(r'^\d{3,4}-\d{4}$', ss):
        print(ss, '전화번호 맞아요')
    else:
        print(ss, '전화번호 아닌 듯')

# 리스트 컴프리헨션(List Comprension)은 직관적으로 리스트를 생성하는 방법이다.
# 대괄호 "[", "]"로 감싸고 내부에 for문과 if 문을 사용하여 반복하며 조건에 만족하는 것만 리스트로 생성할 수 있습니다.
a = 1,2,3,4,5,6,7,8,9,10
li = []
for i in a:
    if i % 2 == 0:
        li.append(i)
print(li)
print(list(i for i in a if i % 2 == 0))

print()
i1 = [3,4,5]
i2 = [0.5, 1, 2]
result = []
for a in i1:
    for b in i2:
        result.append(a + b)
print(result)
print('----')
datas = [a + b for a in i1 for b in i2]
print(datas)

print()
temp = [1,2,3]
for i in temp:
    print(i, end = ' ')
print()
print([i for i in temp])
print({i for i in temp})

print()
datas = [1,2,'a', True, 3]
li = [i * i for i in datas if type(i) == int]
print(li)

datas = {1,1,2,2,3,2,1}
imsi = {i * i for i in datas}
print(imsi)

print()
id_name = {1:'tom', 2:'oscar'}
print(id_name)
name_id = {val:key for key, val in id_name.items()}
print(name_id)

print()
aa = [(1,3), (2,4), (5,6)]
for a, b in aa:
    print(a + b)

# sum([1,2,3])
print('과일 값 계산 ---')
price = {'사과' : 5000, '감':500, '배': 1000}  # 오늘 과일 가격
guest = {'사과':3, '감':2}
bill = sum(price[f] * guest[f] for f in guest)
print('고객이 구매한 과일 총액은 {}원'.format(bill))

print('---- range 함수 : 수열 생성 -------')
print(list(range(0, 11, 1)))
print(list(range(-10, -100, -20)))
print(set(range(1, 11, 2)))
print(tuple(range(1, 11, 2)))

print()
for i in range(6):     # 0 이상 6 미만 증가치 1
    print(i, end = ' ')
    
print()
tot = 0
for su in range(1, 11):
    tot += su
print('결과 : ' + str(tot))
print('내장함수 : ' + str(sum(range(1,11))))

for _ in range(6):
    print('돌자')
    
for i in range(1, 10):
    print('{0} * {1} = {2}'.format(2, i, 2 * i))

# 문1 : 2 ~ 5단 출력
for a in range(2, 6):
    for b in range(1, 10):
        print('{} * {} = {}'.format(a, b, a * b))
    print()

print('\n---문제2---')
# 문2 : 1 ~ 100 사이의 정수 중 3의 배수이면서 5의 배수의 합 출력 
tot = 0
for a in range(1, 100):
    if a % 3 == 0 and a % 5 == 0:
        print(a)
        tot += a
print('합 : ' + str(tot))
        
print('\n---문제3---')
# 문3 : 주사위를 두 번 던져 나온 숫자들의 합이 4의 배수가 되는 경우만 출력 
# 1 3
# 2 6
# ...
for a in range(1, 7):
    for b in range(1, 7):
        if (a + b) % 4 == 0:
            print(a, b)











