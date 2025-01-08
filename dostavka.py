import uuid

class Menu:
    def __init__(self):
        self.oqatlar = []

    def append_oqat(self, oqat, price):
        self.oqatlar.append({oqat: price})
        return f'{oqat} menuda bor price -> {price}'
     
    def menu(self):
        for i in self.oqatlar:
            for oqat, price in i.items():
                print(f'{oqat}: {price}')

    
class Zakaz:
    def __init__(self):
        self.zakaz_num = str(uuid.uuid4())[:4]
        self.zakazlar = []
        self.summa = 0

    def append_zakaz(self, oqat):
        self.zakazlar.append(oqat)
        return 'buyurtma qabul qilindi'
    

    def zakaz(self):
        print(self.zakaz_num)
        print(self.zakazlar)


class Odam:
    def __init__(self, ism ,number):
        self.ism = ism
        self.number = number

    def __str__(self):
        return f'{self.ism} -- {self.number}'
    

class Delivery:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'dostavshik ismi {self.name}'
    

menu = Menu()
zakaz = Zakaz()
klient = Odam('Nodirbek','944242909')
dostavshik = Delivery('qwerty')
menu.append_oqat('burger', '35000')
menu.append_oqat('pizza', '110000')
menu.menu()
print(zakaz.append_zakaz('pizza'))
zakaz.zakaz()

