# 클래스의 상속관계 연습문제 : 다형성
from pack02.test30_etc import ElecProduct

class ElecTv(ElecProduct):
    def volumeControl(self, volume):
        self.volume += volume
        print('TV 소리 크기는 ' + str(self.volume))
        
    
class ElecRadio(ElecProduct):
    def showProduct(self):
        print('라디오 고유 메소드')
        
    def volumeControl(self, volume):
        vol = volume
        self.volume += vol
        print('라디오 볼륨은 ', self.volume)      
        
tv = ElecTv()
tv.volumeControl(7)
tv.volumeControl(-3)
print()
radio = ElecRadio()
radio.volumeControl(3)
radio.volumeControl(2)

print('\n~~~~~~~~~~~~~~~~~~~~~~~')
product = tv
product.volumeControl(10)
print()
product = radio
product.volumeControl(10)


















