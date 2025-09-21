import mysql.connector as ms
import tabulate
import pyttsx3


# class sfx:
#     engine = pyttsx3.init()
#     def welcome_voice(self):
#         self.engine.say("Welcome to the Restaurants")
#         self.engine.runAndWait()
# cur.execute("create table if not exists price(item_code int  ,item_name char(25) not null ,price int not null, foreign key (item_code) references menu (item_code));")
# cur.execute("select * from info")
# a = cur.fetchall()
# print(a)

# creating parent class resturant
class resturant:

    # creating and connecting database
    con = ms.connect(host = "localhost",user = "root",password = "root") 
    cur = con.cursor()
    cur.execute("create database if not exists hotel")
    cur.execute("use hotel")


    class menu ():
        
        def __init__(self):
            resturant.cur.execute("create table if not exists menu(item_code int primary key ,item_name char(25) not null ,price int not null);" ) #making table if not exits
            
        class menu_update:
            def __init__(self):
                # Question = input("what you want to update \n1.item name\n2.item price\n3.item code")
                pass

            def item_price(self,itemcode,newvalue):
                resturant.cur.execute(f"update menu set item_price = {newvalue} where item_code = {itemcode}")

            def itme_name(self,itemcode,newvalue):
                resturant.cur.execute(f"update menu set item_name = {newvalue} where item_code = {itemcode}")

            def item_code(self,itemcode,newvalue):
                resturant.cur.execute(f"update menu set item_code = {newvalue} where item_code = {itemcode}")
                

            def itme_insert(self,item_code,item_name,item_price):
                resturant.cur.execute(f"insert into table menu values ({item_code},{item_name},{item_price})")

            def item_delete(self):
                resturant.cur.execute(f"")

        def __str__(self):
                resturant.cur.execute("select * from menu")
                data = resturant.cur.fetchall()
                return tabulate.tabulate(data,["ITEM CODE","ITEM NAME","ITEM PRICE"],tablefmt= "grid")

    class sales:
        def print_sale():
            pass
        def print_analysis():
            pass

        def saving_data():
            pass
        class modifying_sales_data():
            def inserting_data():
                pass
            def deleting_data():
                pass

    class bill:
        def generate():
            pass
        def print():
            pass
        def adding_items():
            pass
        def removing_items():
            pass

    # a = sfx()
    # a.welcome_voice(
print(resturant.menu())