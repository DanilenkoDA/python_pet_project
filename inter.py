from tkinter import *
import tkinter.ttk as ttk
import classes
from tkinter import messagebox as mb

class Main_window():
    def __init__(self):
        self.root = Tk()
        self.root.geometry('600x600')
        self.lbl_hi = Label(text='Добро пожаловать!')
        self.lbl_hi.pack()
        self.btn_fight = Button(text='Перевезти груз', command=self.add_order)
        self.btn_fight.pack(anchor=NW, padx=6, pady=6)
        self.btn_chng_weight = Button(text='Добавить машину', command = self.add_car_int)
        self.btn_chng_weight.pack(anchor=NW, padx=6, pady=6)
        self.btn_chng_char = Button(text='Посмотреть свободный транспорт', command=self.show_free_cars)
        self.btn_chng_char.pack(anchor=NW, padx=6, pady=6)
        self.btn_dj_info = Button(text='Посмотреть занятый транспорт', command=self.show_unfree_cars)
        self.btn_dj_info.pack(anchor=NW, padx=6, pady=6)
        self.btn_kik_info = Button(text='Посмотреть транспорт по грузоподъемности', command=self.show_gruz_tr)
        self.btn_kik_info.pack(anchor=NW, padx=6, pady=6)
        self.btn_kik_order = Button(text='Удалить заявку', command=self.delete_order)
        self.btn_kik_order.pack(anchor=NW, padx=6, pady=6)
        self.btn_kik_car = Button(text='Удалить машину', command=self.delete_car)
        self.btn_kik_car.pack(anchor=NW, padx=6, pady=6)
        self.btn_ex = Button(text='Выйти', command=self.root.destroy)
        self.btn_ex.pack()
        self.root.mainloop()
    
    
    def add_car_int(self):
        self.wndw_add_car = Toplevel(self.root)
        self.wndw_add_car.geometry('600x600')
        self.lbl_name = Label(self.wndw_add_car, text='Введите название грузовика')
        self.lbl_name.pack()
        self.txt1_name = ttk.Entry(self.wndw_add_car)
        self.txt1_name.pack()
        self.lbl_name = Label(self.wndw_add_car, text='Введите грузоподъемность машины')
        self.lbl_name.pack()
        self.txt2_massa = ttk.Entry(self.wndw_add_car)
        self.txt2_massa.pack()
        self.send_car = Button(self.wndw_add_car, text='Отправить', command= lambda: classes.add_car(self.txt1_name.get(), self.txt2_massa.get()))
        self.send_car.pack()
        self.ex_car = Button(self.wndw_add_car, text='Выйти', command=lambda: self.wndw_add_car.destroy())
        self.ex_car.pack()
        self.wndw_add_car.mainloop()


    def show_free_cars(self):
        self.my_list = classes.free_cars()
        self.wndw_fr = Toplevel(self.root)
        self.wndw_fr.geometry('800x800')
        self.lbl_car = Label(self.wndw_fr, text = 'ID Name Gruz Занят? IDзаявки')
        self.lbl_car.pack()
        for i in range(len(self.my_list)):
            self.car = self.my_list[i]
            self.lbl_car = Label(self.wndw_fr, text=self.car)
            self.lbl_car.pack()
        self.ex_show_cars = Button(self.wndw_fr, text='Выйти', command=self.wndw_fr.destroy)
        self.ex_show_cars.pack()
        self.wndw_fr.mainloop()


    def show_unfree_cars(self):
        self.my_list_un = classes.unfree_cars()
        if len(self.my_list_un) == 0:
            mb.showinfo('Хм', 'Все машины свободны')
        else:
            self.wndw_un = Toplevel(self.root)
            self.wndw_un.geometry('800x800')
            self.lbl_car_u = Label(self.wndw_un, text='ID Name Gruz Занят? IDзаявки')
            self.lbl_car_u.pack()
            for i in range(len(self.my_list_un)):
                self.car = self.my_list_un[i]
                self.lbl_car_u = Label(self.wndw_un, text=self.car)
                self.lbl_car_u.pack()
            self.ex_show_cars = Button(self.wndw_un, text='Выйти', command=self.wndw_un.destroy)
            self.ex_show_cars.pack()
            self.wndw_un.mainloop()


    def show_gruz_tr(self):
        self.new_wndw = Toplevel(self.root)
        self.my_gruz_list = classes.sort_for_gruz()
        self.new_wndw.geometry('800x800')
        for i in range(len(self.my_gruz_list)):
            self.big_car = self.my_gruz_list[i]
            self.lbl_srt = Label(self.new_wndw, text=self.big_car)
            self.lbl_srt.pack()
        self.ex_srt_cars = Button(self.new_wndw, text='Выйти', command=self.new_wndw.destroy)
        self.ex_srt_cars.pack()
        self.new_wndw.mainloop()


    def delete_car(self):
        self.del_wndw = Toplevel(self.root)
        self.del_wndw.geometry('600x600')
        self.lbl = Label(self.del_wndw, text='Введите ID грузовика')
        self.lbl.pack(anchor=NW, padx=6, pady=6)
        self.txt_id = ttk.Entry(self.del_wndw)
        self.txt_id.pack(anchor=NW, padx=6, pady=6)
        self.btn_del = Button(self.del_wndw, text='Удалить', command= lambda : classes.delete_car(self.txt_id.get()))
        self.btn_del.pack(anchor=NW, padx=6, pady=6)
        self.btn_del_ex = Button(self.del_wndw, text='Выйти', command = self.del_wndw.destroy)
        self.btn_del_ex.pack()
        self.del_wndw.mainloop()


    def delete_order(self):
        self.del_ord = Toplevel(self.root)
        self.del_ord.geometry('600x600')
        self.lbl1_for_ord = Label(self.del_ord, text='Введите ID заявки')
        self.lbl1_for_ord.pack(anchor=NW, padx=6, pady=6)
        self.txt_ord = ttk.Entry(self.del_ord)
        self.txt_ord.pack(anchor=NW, padx=6, pady=6)
        self.btn_ord = Button(self.del_ord, text='Удалить', command = lambda: classes.delete_order(self.txt_ord.get()))
        self.btn_ord.pack(anchor=NW, padx=6, pady=6)
        self.btn_for_ex = Button(self.del_ord, text='Выйти', command = self.del_ord.destroy)
        self.btn_for_ex.pack()
        self.del_ord.mainloop()


    def add_order(self):
        self.ord_wndw = Toplevel(self.root)
        self.ord_wndw.geometry('600x600')
        self.lbl1_ord = Label(self.ord_wndw, text='Введите массу груза')
        self.lbl1_ord.pack(anchor=NW, padx=6, pady=6)
        self.entr1 = ttk.Entry(self.ord_wndw)
        self.entr1.pack(anchor=NW, padx=6, pady=6)
        self.lbl2_ord = Label(self.ord_wndw, text='Введите контактный номер')
        self.lbl2_ord.pack()
        self.entr2 = ttk.Entry(self.ord_wndw)
        self.entr2.pack(anchor=NW, padx=6, pady=6)
        self.btn1 = Button(self.ord_wndw, text='Добавить заявку', command= lambda : classes.add_order(self.entr1.get(), self.entr2.get()))
        self.btn1.pack()
        self.btn1_ex = Button(self.ord_wndw, text='Выйти', command=self.ord_wndw.destroy)
        self.btn1_ex.pack()
        self.ord_wndw.mainloop()


a = Main_window()