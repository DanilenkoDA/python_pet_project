import base as j
import peewee
#import inter as abc
from tkinter import messagebox as mb
class Truck():
    def __init__(self):
        self.name = 'not_stated'
        self.gruz = 0
        self.bron = False
        self.order = 0
    def rename(self, name):
        self.name = name
    def change_gruz(self, gruz):
        self.gruz = gruz
    def change_bron(self, bron):
        self.bron = bron
    def state_order(self, order):
        self.order = order


class Record():
    def __init__(self, mas, num):
        self.massa = mas
        self.number = num
    def change_brn(self, brn):
        self.brn = brn

def check_for_int(abc):
    if str(abc).isdigit():
        return True
    return False

def check_for_bul(abc):
    if abc == 'True' or abc == 'False':
        return True
    return False


class Shake():
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def shk(self):
        self.first.name = self.second.name
        self.first.gruz = self.second.gruz
    def sav(self):
        j.Car.save(self.first)

def show_list():
    a = list(j.Car.select())
    vsp = []
    for i in range(len(a)):
        vsp.append([a[i].id, a[i].name, a[i].gruz, a[i].bron_car, a[i].id_of_order_id])
    return vsp

def sort_for_gruz():
    my_list = show_list()
    for elem in my_list:
        my_list.sort(key = lambda elem: elem[2] )
    return my_list

def resort():
    my_list = sort_for_gruz()
    my_list.reverse()
    return my_list

def add_order(massa, number):
    if check_for_int(massa):
        record = j.Order(massa = int(massa), number_of_klient = number, bron = False)
        j.Order.save(record)
        connect()
        mb.showinfo('Действие', 'Заявка успешно добавлена!')
    else:
        error()

def show_order():
    a = j.Order.select()
    vsp = []
    for i in range(len(a)):
        vsp.append([a[i].id, a[i].massa, a[i].number_of_klient, a[i].bron])
    return vsp

def non_bron():
    my_list = show_order()
    non_bron_list = []
    for i in my_list:
        if i[3] == False:
            non_bron_list.append(i)
    return non_bron_list

def for_connect(zapis):
    car_list1 = resort()
    car_list = []
    for i in car_list1:
        if i[3] == False:
            car_list.append(i)
    neob_massa = zapis[1]
    cars_for_bron = []
    for i in car_list:
        if neob_massa > 0:
            neob_massa -= i[2]
            cars_for_bron.append(i[0])
        else:
            break
    if neob_massa <= 0:
        for i in cars_for_bron:
            hs = i
            a = j.Car.get(j.Car.id == hs)
            a.bron_car = True
            a.id_of_order_id = zapis[0]
            j.Car.save(a)
            b = j.Order.get(j.Order.id == zapis[0])
            b.bron = True
            j.Order.save(b)


def connect():
    my_list1 = show_order()
    my_list = []
    for i in my_list1:
        if i[3] == False:
            my_list.append(i)
    for i in my_list:
        for_connect(i)

def in_null():
    my_list = show_list()
    for i in my_list:
        a = j.Car.get(j.Car.id == i[0])
        a.id_of_order_id = 0
        j.Car.save(a)

def error():
    mb.showerror('Ошибка!', 'Проверьте правильность введенных данных.')

def add_car(nam, gruz):
    if check_for_int(gruz):
        record = j.Car(name = nam, gruz = gruz, bron_car = False, id_of_order_id = 0)
        j.Car.save(record)
        mb.showinfo('Успех!', 'Вы успешно выполнили действие')
    else:
        error()

def delete_car(id):
    if check_for_int(id):
        try:
            record = j.Car.get(j.Car.id == id)
            j.Car.delete_instance(record)
            mb.showinfo('Действие', 'Действие успешно совершено!')
        except peewee.DoesNotExist:
            error()
    else:
        error()

def delete_order(id):
    if check_for_int(id):
        try:
            record = j.Order.get(j.Order.id == id)
            j.Order.delete_instance(record)
            mb.showinfo('Действие', 'Действие успешно совершено!')
        except peewee.DoesNotExist:
            error()
    else:
        error()

def free_cars():
    my_list1 = show_list()
    my_list = []
    for i in my_list1:
        if i[3] == False:
            my_list.append(i)
    return my_list
def unfree_cars():
    my_list1 = show_list()
    my_list = []
    for i in my_list1:
        if i[3] == True:
            my_list.append(i)
    return my_list







