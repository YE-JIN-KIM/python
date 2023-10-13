from pack02.test34_etc import Employee

class Temporary(Employee):
    def __init__(self, irum, nai, ilsu, ildang):
        super().__init__(irum, nai)
        self.ilsu = int(ilsu)
        self.ildang = int(ildang)
        
    def pay(self):
        return self.ilsu * self.ildang
        
    def data_print(self):
        print('이름 : ' + self.irum, '나이 : ' + str(self.nai), '월급 : ' + str(self.pay()))
        
           
class Regular(Employee):
    def __init__(self, irum, nai, salary):
        super().__init__(irum, nai)
        self.salary = int(salary)
    
    def pay(self):
        return self.salary
    
        
    def data_print(self):
        print('이름 : ' + self.irum, '나이 : ' + str(self.nai), '급여 : ' + str(self.pay()))
        
         
class Salesman(Regular):
    def __init__(self, irum, nai, salary, sales, commission):
        super().__init__(irum, nai, salary)
        self.sales = int(sales)
        self.commission = float(commission)
    
    def pay(self):
        return super().pay() + (self.sales * self.commission)
    
    def data_print(self):
        print('이름 : ' + self.irum, '나이 : ' + str(self.nai), '급여 : ' + str(round(self.pay())))
        
        
t = Temporary('홍길동', 25, 20, 15000)
r = Regular('한국인', 27, 3500000)
s = Salesman('손오공', 29, 1200000, 5000000, 0.25)
t.data_print()
r.data_print()
s.data_print()




class Temporary2(Employee):
    def __init__(self, irum, nai, ilsu, ildang):
        super().__init__(irum, nai)
        self.ilsu = ilsu
        self.ildang = ildang
        
    def pay(self):
        return self.ilsu * self.ildang

    def data_print(self):
        self.pay()
        self.irumnai_print()
        print (", 월급 : {}".format(self.pay()))

class Regular2(Employee):
    def __init__(self, irum, nai, salary):
        super().__init__(irum, nai)
        self.salary = salary
        
    def pay(self):
        return self.salary
        
    def data_print(self):
        self.irumnai_print()
        print (", 급여 : {}".format(self.pay()))

class Salesman2(Regular2):
    def __init__(self, irum, nai, salary, sales, commission):
        super().__init__(irum, nai, salary)
        self.sales = sales
        self.commission = commission
    
    def pay(self):
        return super().pay() + (self.sales * self.commission)
    
    def data_print(self):
        self.irumnai_print()
        print (", 수령액 : {}".format(round(self.pay())))


t = Temporary2('홍길동', 25, 20, 15000)
t.data_print()
r = Regular2('한국인', 27, 3500000)
r.data_print()
s = Salesman2('손오공', 29, 1200000, 5000000, 0.25)
s.data_print()






