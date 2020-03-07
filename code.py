from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
window = Tk()
window.geometry("700x700+120+60")
window.title("Billing")

# entered_s_name = StringVar()
# entered_s_qty = StringVar()
# entered_mc_name = StringVar()
# entered_mc_qty = StringVar()
# entered_d_name = StringVar()
# entered_d_qty = StringVar()
usernameVar = StringVar()
paswordVar = StringVar()



def admin():
    
    top = Tk()
    window.destroy()
    top.title("Admin")
    top.geometry("700x700+120+60")
    titleLabel = Label(top,text="Admin",font="35")
    titleLabel.grid(row=0,column=0,columnspan=2,padx=(40,0),pady=(10,0))
    
    logoutLabel = Label(top,text="Logout")
    logoutLabel.grid(row=1,column=0,padx=(600,0))

    top.geometry("700x700+120+60")
    conn = sqlite3.connect('orders.db')
    c = conn.cursor()
    c.execute("SELECT * ,oid FROM orders")
    
    #saving the data
    
    bills_tree = ttk.Treeview(top,columns=('Item name','Quantity','Price'),show='headings')

    # scrollbills = ttk.Scrollbar(top,orient="vertical",command=bills_tree.yview)
    # scrollbills.grid(row=1,column=3,sticky="NS")
    
    #bills_tree.configure(yscrollcommand=scrollbills.set)
    bills_tree.heading("#1",text="Item name")
    bills_tree.heading("#2",text="Quantity")
    bills_tree.heading("#3",text="Price")

    rec = c.fetchall()
    #display_str = ''
    for record in rec:
        #display_str += str(record[0]) + " " + str(record[1]) + " " + str(record[2]) + "\n"
        bills_tree.insert("",END,values=record)
    bills_tree.grid(row=2,column=0)

    #saving the data
    conn.commit()
    conn.close()


def auth_user():
    conn = sqlite3.connect('login.db')
    c = conn.cursor()
    #c.execute(''' CREATE TABLE login(usernname text,password text)''')
    
    #c.execute("INSERT INTO login VALUES('admin','rest')")
    
    c.execute("SELECT *,oid FROM login")
    rec = c.fetchall()
    uname = ''
    pword = ''
    print(rec)
    for record in rec:
        uname += str(record[0])
        pword += str(record[1])
        
    if usernameEntry.get() == uname and passwordEntry.get() == pword:
        admin()
    else:
        adminLogin()
        messagebox.askretrycancel("Login failed","Incorrect username or password.Please try again")
        usernameEntry.delete(0,END)
        passwordEntry.delete(0,END)
        
        

    #saving the data
    conn.commit()
    conn.close()


def adminLogin():
    global usernameEntry,passwordEntry
    top = Toplevel()
    top.geometry("700x700+120+60")
    top.title("Login")
    titleLabel = Label(top,text="Restaurant Billing",fg="blue",font="35")
    titleLabel.grid(row=0,column=0,columnspan=2,padx=(40,0),pady=(10,0))

    loginLabel = Label(top,text="Admin login",font="25",fg="green")
    loginLabel.grid(row=1,column=2,columnspan=2,padx=(40,0),pady=(10,0))
    
    usernameLabel = Label(top,text="Username")
    usernameLabel.grid(row=2,column=2,padx=20,pady=7)

    passwordLabel = Label(top,text="Password")
    passwordLabel.grid(row=3,column=2,padx=20,pady=7)

    usernameEntry = Entry(top)
    usernameEntry.grid(row=2,column=3,padx=20,pady=7)

    passwordEntry = Entry(top,show="*")
    passwordEntry.grid(row=3,column=3,padx=20,pady=7)
    
    
    Login = Button(top,text="Login",width=15,height=3,command=auth_user)
    
    Login.grid(row=4,column=2,columnspan=2,pady=(40,0))

#DB fro menu
def menu():
    conn = sqlite3.connect('menu.db')
    c = conn.cursor()
    c.execute(''' CREATE TABLE menu(item_name text,price integer)''')
    menu = [('Spring roll',100),('Hara bhara kebab',120),('Paneer tikka',130),('Chicken lollipop',150),('Chicken platter',300),('Chilli Paneer',130),('Veg Manchurian',100)
    ('Lorem',150),('ipsum',160),('dolor',140),('sit',170),('amet',200),('consectetur',175),('adipiscing',180)]

#adding item to DB
def add_starter():
    conn = sqlite3.connect('orders.db')
    c = conn.cursor()
    # c.execute(''' CREATE TABLE starter(Item_name text,Qty integer,Price real)''')
    #c.execute(''' CREATE TABLE orders(Item_name text,Qty integer,Price integer)''')
    
    c.execute("INSERT INTO orders VALUES(:name,:qty,100)",
    {
        'name':starter.get(),
        'qty':s_qty.get(),
         
        
    })
    c.execute("SELECT * ,oid FROM orders")
    record1 = c.fetchall()
    print(record1)
    #saving the data
    conn.commit()
    conn.close()

def add_mc():
    conn = sqlite3.connect('orders.db')
    c = conn.cursor()
    #c.execute(''' CREATE TABLE starter(Item_name text,Qty integer,Price real)''')
    #c.execute(''' CREATE TABLE orders(Item_name text,Qty integer,Price integer)''')
    c.execute("INSERT INTO orders VALUES(:name,:qty,200)",
    {
        'name':mc.get(),
        'qty':mc_qty.get(),
        
    })
    c.execute("SELECT * ,oid FROM orders")
    record2 = c.fetchall()
    print(record2)
    #saving the data
    conn.commit()
    conn.close()

def add_dessert():
    conn = sqlite3.connect('orders.db')
    c = conn.cursor()
    #c.execute(''' CREATE TABLE starter(Item_name text,Qty integer,Price real)''')
    #c.execute(''' CREATE TABLE orders(Item_name text,Qty integer,Price integer)''')
    c.execute("INSERT INTO orders VALUES(:name,:qty,150)",
    {
        'name':d.get(),
        'qty':d_qty.get(),
        
    })
    c.execute("SELECT * ,oid FROM orders")
    record3 = c.fetchall()
    print(record3)
    #saving the data
    conn.commit()
    conn.close()

def view_currentBill():
    top = Toplevel()
    top.title("View Bills")
    top.geometry("700x700+120+60")
    conn = sqlite3.connect('orders.db')
    c = conn.cursor()
    c.execute("SELECT * ,oid FROM orders")
    
    #saving the data
    
    bills_tree = ttk.Treeview(top,columns=('Item name','Quantity','Price'),show='headings')

    # scrollbills = ttk.Scrollbar(top,orient="vertical",command=bills_tree.yview)
    # scrollbills.grid(row=1,column=3,sticky="NS")
    
    #bills_tree.configure(yscrollcommand=scrollbills.set)
    bills_tree.heading("#1",text="Item name")
    bills_tree.heading("#2",text="Quantity")
    bills_tree.heading("#3",text="Price")

    rec = c.fetchall()
    #display_str = ''
    for record in rec:
        #display_str += str(record[0]) + " " + str(record[1]) + " " + str(record[2]) + "\n"
        bills_tree.insert("",END,values=record)
    bills_tree.pack()

    #saving the data
    conn.commit()
    conn.close()


def add_new():
    #global variables for entries
    global s_qty
    global starter
    global mc
    global mc_qty
    global d
    global d_qty

    window1=Tk()
    window1.title("Add new order")
    window1.geometry("700x700+120+60")
    #starters
    starters = ['Spring roll','Hara bhara kebab','Paneer tikka','Chicken lollipop','Chicken platter','Chilli Paneer','Veg Manchurian']
    starter = StringVar(window1)
    starter.set(starters[0]) #default value to be displayed

    s_dropdown = OptionMenu(window1,starter,*starters) #dropdown for starters
    starterLabel = Label(window1,text="Starters")
    starterLabel.grid(row=0,column=0,padx=30)
    s_dropdown.grid(row=1,column=0,padx=30,pady=5)
    
    s_qty = Entry(window1)
    starterQty = Label(window1,text="Qty",padx=30)
    starterQty.grid(row=0,column=1)
    s_qty.grid(row=1,column=1,padx=10,pady=5)
    
    
    add_s = Button(window1,text="Add",width=15,height=2,command=add_starter)
    add_s.grid(row=1,column=2,padx=10)

    #Main course
    mcourse = ['Lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur', 'adipiscing' ,'elit', 'sed do']
    mc = StringVar(window1)
    mc.set(mcourse[0]) #default value to be displayed

    mc_dropdown = OptionMenu(window1,mc,*mcourse) #dropdown for maincourse
    mcLabel = Label(window1,text="Main Course",pady=25)
    mcLabel.grid(row=2,column=0,padx=30)
    mc_dropdown.grid(row=3,column=0,padx=30,pady=10)
    
    mc_qty = Entry(window1)
    mc_qty.grid(row=3,column=1,padx=10,pady=5)
    mcQtyLabel = Label(window1,text="Qty",padx=30,pady=25)
    mcQtyLabel.grid(row=2,column=1)
    
    addbutton_mc = Button(window1,text="Add",width=15,height=2,command=add_mc)
    addbutton_mc.grid(row=3,column=2,padx=10)


    #Dessert
    desserts = ['Lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur', 'adipiscing' ,'elit', 'sed do']
    d = StringVar(window1)
    d.set(desserts[0]) #default value to be displayed

    d_dropdown = OptionMenu(window1,d,*desserts) #dropdown for maincourse
    dLabel = Label(window1,text="Desserts",pady=25)
    dLabel.grid(row=4,column=0,padx=30)
    d_dropdown.grid(row=5,column=0,padx=30,pady=10)
    
    d_qty = Entry(window1)
    d_qty.grid(row=5,column=1,padx=10,pady=5)
    dQtyLabel = Label(window1,text="Qty",padx=30,pady=25)
    dQtyLabel.grid(row=4,column=1)
    
    addbutton_d = Button(window1,text="Add",width=15,height=2,command=add_dessert)
    addbutton_d.grid(row=5,column=2,padx=10)

    viewButton = Button(window1,text="View current bill",width=20,height=2,command= view_currentBill)
    viewButton.grid(row=6,column=0,padx=75,pady=20)

    

    
def current_orders():
    adminLogin()

def today_sales():
    adminLogin()

def main_page():
    addButton = Button(window,text="Add new order",width=20,height=3,command=add_new)
    currentOrders = Button(window,text="View Current orders",width=20,height=3,command=current_orders)
    todaySales = Button(window,text="View today's sales",width=20,height=3,command=today_sales)
    
    addButton.grid(row=0,column=0,padx=50,pady=35)
    currentOrders.grid(row=0,column=1,padx=20,pady=35)
    todaySales.grid(row=0,column=2,padx=20,pady=35)

main_page()
window.mainloop()