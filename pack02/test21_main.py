import pack02.test21_singer

def process():
    jungkuk = pack02.test21_singer.Singer()
    print('타이틀 송 : ', jungkuk.title_song)
    jungkuk.sing()
    jungkuk.title_song = '정국 찬양가'
    jungkuk.co = '하이브'
    print('소속사가 ' + jungkuk.co + '인 가수의 노래 ' + jungkuk.title_song)
    
    print()
    iu = pack02.test21_singer.Singer()
    print('타이틀 송 : ', iu.title_song)
    iu.sing()
    # print('소속사가 ' + iu.co + '인 가수의 노래 ' + iu.title_song)  # error co는 정국만 가짐 
    print(id(pack02.test21_singer.Singer), id(iu))
    
    print()
    bp = pack02.test21_singer.Singer   # 인스턴스를 불러오기위해 괄호를 넣어야한다 
    print(id(pack02.test21_singer.Singer), id(bp))  
    print(bp.sing())   # error 
    print('타이틀 송 : ', bp.title_song)
 
if __name__ == '__main__':
    process()