from peewee import *
import datetime
db = SqliteDatabase('data.db')

class Order(Model):
    class Meta:
        database = db
        order_by = 'id'
        db_table = 'orders'


    id = PrimaryKeyField(unique=True)
    massa = IntegerField()
    number_of_klient = CharField(max_length=70)
    bron = BooleanField()


class Car(Model):
    class Meta:
        database = db
        order_by = 'id'
        db_table = 'cars'


    id = PrimaryKeyField(unique=True)
    name = CharField(max_length=70)
    gruz = IntegerField()
    bron_car = BooleanField()
    id_of_order = ForeignKeyField(Order, default=None)

