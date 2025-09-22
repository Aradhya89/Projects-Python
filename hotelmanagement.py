import mysql.connector as ms
import tabulate
import pyttsx3


# class sfx:
#     engine = pyttsx3.init()
#     def welcome_voice(self):
#         self.engine.say("Welcome to the Restaurants")
#         self.engine.runAndWait()
            # resturant.cur.execute("create table if not exists sale(order_no int primary key ,date char(15) not null ,time char(15) not null, foreign key (item_code) references menu (item_code));")
# cur.execute("select * from info")

# creating parent class resturant
class resturant:

    # creating and connecting database
    con = ms.connect(host = "localhost",user = "root",password = "root") 
    cur = con.cursor()
    cur.execute("create database if not exists hotel")
    cur.execute("use hotel")


    class menu ():
        
        def __init__(self):
            resturant.cur.execute("create table if not exists menu(item_code int primary key ,item_name char(25) not null ,item_price int not null);" ) #making table if not exits
            
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
                
        
            def item_insert(item_code,item_name,item_price):
                try: #using try block to avoide duplicate entries error
                    resturant.cur.execute(f"insert into menu values ({item_code},\"{item_name}\",{item_price})")
                except ms.errors.IntegrityError:
                    print("ENTERED SAME ITEM_CODE PRESENT IN TABLE")
            
            def item_delete(item_code):
                resturant.cur.execute(f"delete from menu where item_code = {item_code}")

        def __str__(self):
                resturant.cur.execute("select * from menu")
                data = resturant.cur.fetchall()
                return tabulate.tabulate(data,["ITEM CODE","ITEM NAME","ITEM PRICE"],tablefmt= "grid")

    class sales:
        def __init__(self):
            resturant.cur.execute("create table if not exists sale(order_no int primary key ,date char(15) not null ,time char(15) not null, total_sale int not null);")
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
        order = {}

        def generate():
            pass

        def __str__(self): #to print direct bill
            return (tabulate.tabulate(self.order.items(),["ITEM NAME","ITEM PRICE"],tablefmt= "grid",missingval= ""))
        

        @staticmethod
        def gettingitemdetail(item_code) -> int | str:
            resturant.cur.execute(f"select item_price,item_name from menu where item_code = {item_code}")
            data = resturant.cur.fetchall()
            itemprice = data[0][0]  #data[0][1] = item_price
            itemname  = data [0][1]  #the reson behind it was the output was [(itemprice,itemname)]
            return itemprice,itemname


        @classmethod
        def adding_items(cls,item_code, quantity:int):
            price,name = resturant.bill.gettingitemdetail(item_code)
            total_price = price * quantity 
            cls.order[name] = total_price

        @classmethod
        def removing_items(cls,item_code,quantity:int) -> None:
            try:
                price , name = resturant.bill.gettingitemdetail(item_code)
                removing_price = price * quantity
                if (calculated_price := resturant.bill.order[name]- removing_price) >0:
                    cls.order[name] = calculated_price
                else:
                    del cls.order[name]
            except KeyError:
                print("ITEM NOT IN BILL :)")


    # a = sfx()
    # a.welcome_voice(
# print(resturant.menu())
# shriji = resturant()
# bill1 = shriji.bill
# bill1.adding_items(101,2)
# print(bill1(),"\n")
# bill1.removing_items(101,1)
# print(bill1(),"\n")
# bill1.removing_items(101,1)
# print(bill1())
# # a.bill.adding_items(101,2)
# # a.menu.menu_update.item_insert(101,"samosa",20)
# resturant.con.commit()
# # print(a.bill())
