# 자료형 
# int, float, boole, complex : 객체 값 하나를 참조. Immutable 객체(수정 불가능)
# str, list, tuple, set, dict :  묶음형 객체 값 참조 
from erfa.core import fama03

# str : 문자열 자료형 : 순서O - 인덱싱,슬라이싱 가능 , 변경X
s = 'sequence'
# 문자열 관련 함수
print(len(s))
print('포함 횟수 :',s.count('e'))
print('검색 위치 :',s.find('e'), s.find('e', 3), s.rfind('e'))
# ...ddddd

ss = 'mbc'
print('mbc', ss, id(ss))   # id = Hashcode
ss = 'abc'
print('mbc', ss, id(ss))   # id = Hashcode

print(s, s[0], s[-7])  # 인덱싱 
print(s, s[0:5], s[-7:-5], s[5:], s[:5], s[::2], s[0:7:3])   # 슬라이싱
print(s[0:5] + 'good')
print()
sss = ' mbc kbs sbs  '
print(sss)
print(sss.strip())  # 문자열 공백자르기 
print(sss.lstrip()) # 왼쪽 공백 자르기 
print(sss.rstrip())
ssss = sss.split(sep= ' ')
print(ssss)
s5 = sss.replace('kbs', '공영방송')
print(s5)

print("\n\nlist -----------------")
# list : 배열과 유사, 중복 자료 허용, 여러 종류의 값 기억. 순서O, 변경O
a = [1, 2, 3]
print(a, type(a))
b = [10, a, 12.3, 'good', False]
print(b)
c = list();
print(c, type(c))
print()
family = ['준수', '예진','정혜']
family.append('준호')    # 추가 
family.insert(0,'민규')  # 삽입
family.extend(['tom', 'oscar'])
family += ['지원', '국인']
family.remove('tom')
# family.clear()
print(family, len(family), family[0])

print()
aa = [1,2,3,['a', 'b', 'kbs'],4,5]  # 중첩리스트
print(aa, aa[0], aa[0:3])
print(aa[3], ' ', aa[3][2])

aa.remove(2)   # 값에 의한 삭제
del aa[3]      # 순서에 의한 삭제
print(aa)

print()
bb = aa       # 주소 치환 : 같은 객체를 참조. 얕은 복사 
print(aa, ' ', bb, ' ', id(aa), id(bb))
bb[0] = 'nice'
print(aa, ' ', bb, ' ', id(aa), id(bb))

import copy
cc = copy.deepcopy(aa)   # 주소 치환 : 새로운 공간이 확보. 깊은 복사
print(aa, ' ', cc, ' ', id(aa), id(cc))
print(aa == cc, aa is cc)  # 내용은 같으나 주소는 다름
cc[0] = '쉬고할까?'
print(aa, ' ', cc)

























