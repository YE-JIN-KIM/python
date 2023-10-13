# 사용자 정의 모듈 call

print('뭔가를 하다가 ... 다른 모듈 호출')

# 같은 패키지 내의 모듈 읽기 
import pack02.test14_other

print('score : ', pack02.test14_other.score)
print(pack02.test14_other.__file__)
print(pack02.test14_other.__name__)

list1 = [1,2]
list2 = [3,4]
pack02.test14_other.listHap(list1, list2)

def abc():
    if __name__ == '__main__':
        print('메인 모듈이야 라고 외치다')
        
abc()

print()
pack02.test14_other.kbs()

from pack02.test14_other import kbs, Mbc, score   # 한번에 함수 호출 
kbs()
Mbc()
print(score)

# 다른 패키지 내의 모듈 읽기
import moduleTest.test14_etc2
moduleTest.test14_etc2.Hap(5, 3)

from moduleTest.test14_etc2 import Cha
Cha(5, 3)

import test14_etc2
test14_etc2.Hap(5, 3)
from test14_etc2 import Hap
Hap(5, 3)























