coffee = 200
class Machine:
    def __init__(self):
        self.cupCount = 1
        self.coin = CoinIn()   # 클래스의 포함관계
    
    def showData(self):
        su = int(input('동전을 입력하세요'))
        CoinIn.coin = su
        count = int(input('몇잔을 원하세요'))
        Machine.cupCount = count
            
        total = coffee * count
        if self.coin < total:
            self.coin.change = 0
            print("요금 부족 메세지 출력")
        else:
            self.coin.change = self.coin.coin - total
            print("커피 {count}잔과 잔돈 {self.coin.change}원")

    
            
class CoinIn:
    def __init__(self):
        self.coin = 0 
        self.change = 0 
    
    def culc(self, cupCount):
        total = coffee * cupCount
        
        
        
if __name__ == '__main__':
    Machine().showData()    
            
            
            
            
        