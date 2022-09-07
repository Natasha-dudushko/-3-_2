# 2.	Разработайте программу, имитирующую работу транспортного агентства.
# Транспортное агентство имеет сеть филиалов в нескольких городах. Транспортировка грузов E3232
# осуществляется между этими городами тремя видами транспорта: автомобильным, железнодорожным
# и воздушным. Любой вид транспортировки имеет стоимость единицы веса на единицу пути и
# скорость доставки. Воздушный транспорт можно использовать только между крупными городами,
# этот вид самый скоростной и самый дорогой.  Железнодорожный транспорт можно использовать
# между крупными и средними городами, этот вид самый дешевый. Автомобильный транспорт можно
# использовать между любыми городами. Заказчики через случайные промежутки времени
# обращаются в один из филиалов транспортного агентства с заказом на перевозку
# определенной массы груза и возможным пожеланием о скорости/цене доставки.
# Транспортное агентство организует отправку грузов одним из видов транспорта
# с учетом пожеланий клиента.
#
# -Доход транспортного агентства, в том числе с разбивкой по видам транспорта и городам.
# -Среднее время доставки груза, в том числе с разбивкой по видам транспорта и городам.
# -Список исполняемых заказов с возможность сортировки по городам, видам транспорта,
# стоимости перевозки.
class Transport_agency():
    nun = 0
    speed_car = 35
    speed_train = 40
    speed_plane = 600

    koef_car = 50.1
    koef_train = 70
    koef_plane = 120.5

    def __init__(self, city, distans, massa):
        self.city = city
        self.distans = distans
        self.massa = massa
        self.transport = ''
        Transport_agency.nun += 1



    def choice_transport(self):
        if self.massa <= 20 and self.distans <= 100:
            print("Вы можете использовать авто")
            self.info_auto()
            self.transport = 'авто'
            Auto.info_car()
        elif self.massa <= 20 and 100 <= self.distans < 500:
            print("Вы можете использовать авто и поезд")
            self.info_auto()
            self.info_train()
            self.transport = input('Выберите транспорт(авто, поезд): ')
        elif self.massa <= 20 and self.distans >= 500:
            print('Вы можете использовать авто, поезд и авиа')
            self.info_auto()
            self.info_train()
            self.info_plane()
            self.transport = input('Выберите транспорт(авто, поезд, авиа): ')
        elif 20 < self.massa <= 50 and 100 < self.distans <= 500:
            print('Вы можете использовать поезд')
            self.info_train()
            self.transport = 'поезд'
        elif 20 < self.massa <= 50 and self.distans >= 500:
            print('Вы можете использовать авиа и поезд')
            self.info_train()
            self.info_plane()
            self.transport = input('Выберите транспорт(поезд, авиа): ')
        elif 50 < self.massa <= 100 and self.distans > 500:
            print('Вы можете использовать только авиа')
            self.info_plane()
            self.transport = 'авиа'
        else:
            print('ничем не можем помочь')
            if self.massa > 100:
                print('слишком больная масса груза')

    def info_auto(self):
        print(f'Стоимость авто-перевозки {self.massa * self.koef_car}, время {self.distans / self.speed_car}')
    def info_train(self):
        print(f'Стоимость ж/д перевозки {self.massa * self.koef_train}, время {self.distans / self.speed_train}')
    def info_plane(self):
        print(f'Стоимость авиа-перевозки {self.massa * self.koef_plane}, время {self.distans / self.speed_plane}')

    def auto(self):
        self.count = self.massa * self.koef_car
        self.time = self.distans / self.speed_car
    def train(self):
        self.count = self.massa * self.koef_train
        self.time = self.distans / self.speed_train
    def plane(self):
        self.count = self.massa * self.koef_plane
        self.time = self.distans / self.speed_plane


class Minsk(Transport_agency):
    num_order = 0

    def __init__(self, city, distans, massa):
        super().__init__(city, distans, massa)
        self.count = 0
        self.time = 0
        Minsk.num_order += 1

    def info(self):
        if self.transport == 'авто':
            self.auto()
        elif self.transport == 'поезд':
            self.train()
        elif self.transport == 'авиа':
            self.plane()

        print(f'заказ №{Transport_agency.nun}: город {self.city}, транспорт {self.transport},стоимость {self.count}, время {self.time}')


class Moskow(Transport_agency):
    num_order = 0

    def __init__(self, city, distans, massa):
        super().__init__(city, distans, massa)
        self.count = 0
        self.time = 0
        Moskow.num_order += 1

    def info(self):
        if self.transport == 'авто':
            self.auto()
        elif self.transport == 'поезд':
            self.train()
        elif self.transport == 'авиа':
            self.plane()
        print(f'заказ №{Transport_agency.nun}: город {self.city}, транспорт {self.transport},стоимость {self.count}, время {self.time}')

class Brest(Transport_agency):
    num_order = 0

    def __init__(self, city, distans, massa):
        super().__init__(city, distans, massa)
        self.count = 0
        self.time = 0
        Brest.num_order += 1

    def info(self):
        if self.transport == 'авто':
            self.auto()
        elif self.transport == 'поезд':
            self.train()
        elif self.transport == 'авиа':
            self.plane()
        print(f'заказ №{Transport_agency.nun}: город {self.city}, транспорт {self.transport},стоимость {self.count}, время {self.time}')

oder1 = Minsk('Брест', 510, 13)
oder1.choice_transport()
oder1.info()
print('-----')
oder2 = Minsk("Москва", 720, 35)
oder2.choice_transport()
oder2.info()
print('-----')
oder3 = Moskow('Минск', 720, 55)
oder3.choice_transport()
oder3.info()
print('----')
oder4 = Brest('Москва', 1020, 35)
oder4.choice_transport()
oder4.info()
print('----')
orders = [oder1, oder2, oder3, oder4]

agenstvo_count_auto = agenstvo_count_train = agenstvo_count_plane = 0
order_auto = order_train = order_plane = 0
time_auto = time_train = time_plane = 0

agenstvo_count_minsk = agenstvo_count_moskow = agenstvo_count_brest = 0
order_minsk = order_moskow = order_brest = 0
time_minsk = time_moskow = time_brest = 0

for elem in orders:
    if elem.transport == 'авто':
        order_auto += 1
        agenstvo_count_auto += elem.count
        time_auto += elem.time
    elif elem.transport == 'поезд':
        order_train += 1
        agenstvo_count_train += elem.count
        time_train += elem.time
    elif elem.transport == 'авиа':
        order_plane += 1
        agenstvo_count_plane += elem.count
        time_plane += elem.time

    if elem.city == 'Минск':
        order_minsk += 1
        agenstvo_count_minsk += elem.count
        time_minsk += elem.time
    elif elem.city == 'Москва':
        order_moskow += 1
        agenstvo_count_moskow += elem.count
        time_moskow += elem.time
    elif elem.city == 'Брест':
        order_brest += 1
        agenstvo_count_brest += elem.count
        time_brest += elem.time


print('Доход агенства', agenstvo_count_train + agenstvo_count_auto + agenstvo_count_plane)
print(f'Автотранспорт: количество заказов {order_auto}, доход {agenstvo_count_auto}, cреднее время доставки {time_auto /order_auto}')
print(f'Ж/д транспорт: количество заказов {order_train},доход {agenstvo_count_train}, cреднее время доставки {time_train / order_train}')
print(f'Авиатранспорт: количество заказов {order_plane},доход {agenstvo_count_plane}, cреднее время доставки {time_auto / order_plane}')

print(f'Минск: количество заказов {order_minsk}, доход {agenstvo_count_minsk}, cреднее время доставки {time_minsk /order_minsk}')
print(f'Москва: количество заказов {order_moskow},доход {agenstvo_count_moskow}, cреднее время доставки {time_moskow / order_moskow}')
print(f'Брест: количество заказов {order_brest},доход {agenstvo_count_brest}, cреднее время доставки {time_brest / order_brest}')
