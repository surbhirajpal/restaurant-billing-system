import sqlite3
import tkinter
from tkinter import *
import time
import random
from tkinter import messagebox
from PIL import Image,ImageTk
import os


def second_window():
    first.destroy()
    from PIL import Image, ImageTk

    def HomeWindow():
        second.destroy()
        root = Tk()
        root.geometry("2000x650+0+0")
        root.title("Restaurant Billing System")
        load = Image.open("food2.jpg")
        background_image = ImageTk.PhotoImage(load)
        background_label = Label(root, image=background_image)
        background_label.place(x=0, y=0, relheight=1, relwidth=1)

        # database
        table = sqlite3.connect("bills.db")
        table.execute('''CREATE TABLE IF NOT EXISTS ORDERS
        (ORDER_NUMBER INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,FRIES_MEAL TEXT,LUNCH_MEAL TEXT,BURGER_MEAL TEXT,PIZZA_MEAL TEXT,CHEESE_BURGER TEXT,DRINKS TEXT,MEAL_1 TEXT,MEAL_2 TEXT,COST TEXT,SERVICE_CHARGE TEXT,TAX TEXT,SUBTOTAL TEXT,TOTAL TEXT);''')
        table.commit()

        # price list GUI
        def price():
            master = Tk()
            master.geometry("550x650")
            master.title("Price List")
            f1 = Frame(master)
            f1.pack(side=TOP)
            x = Label(f1, text="PRICE LIST\n", font=("comic sans ms", "15", "underline", "bold"), fg="steel blue")
            x.pack()

            f2 = Frame(master)
            f2.pack(side=LEFT)
            a1 = Label(f2, text="ITEMS\n", font=("comic sans ms", "10", "underline"), fg="steel blue")
            a1.pack()
            a = Label(f2,
                      text="FRIES MEAL\n\nLUNCH MEAL\n\nBURGER MEAL\n\nPIZZA MEAL\n\nCHESSE BURGER\n\nDRINKS\n\nMEAL 1-\nFRIES MEAL+BURGER MEAL+DRINKS\n\nMEAL 2-\nPIZZA MEAL+CHESSE BURGER+DRINKS",
                      font=("comic sans ms", "15"), fg="steel blue")
            a.pack()

            f3 = Frame(master)
            f3.pack(side=RIGHT)
            b1 = Label(f3, text="PRICE\n", font=("comic sans ms", "10", "underline"), fg="steel blue")
            b1.pack()
            b = Label(f3, text="Rs 50\n\nRs 150\n\nRs 50\n\nRs 200\n\nRs 70\n\nRs 30\n\n\nRs 200\n\n\nRs 250",
                      font=("comic sans ms", "15"), fg="steel blue")
            b.pack()

            master.mainloop()

        # -------------------------------------------------------------------------------

        # assigning values to variables
        ran = StringVar()
        fries = StringVar()
        lunch = StringVar()
        burger = StringVar()
        pizza = StringVar()
        cheese_burger = StringVar()
        drinks = StringVar()
        meal_1 = StringVar()
        meal_2 = StringVar()
        cost = StringVar()
        service = StringVar()
        tax = StringVar()
        sub_total = StringVar()
        final = StringVar()

        global order

        # use of class for calculations
        class Calculate:
            def price(self, e2, e3, e4, e5, e6, e7, m1, m2):
                try:
                    global a, b, c, d, e, f, g, h
                    a = int(e2.get())
                    b = int(e3.get())
                    c = int(e4.get())
                    d = int(e5.get())
                    e = int(e6.get())
                    f = int(e7.get())
                    g = int(m1.get())
                    h = int(m2.get())
                    global costoffries, costoflunch, costofburger, costofpizza, costofchesseburger, costofdrinks, costofmeal1, costofmeal2, costofmeal, Service, PaidTax, OverAllCost
                    costoffries = a * 50
                    costoflunch = b * 150
                    costofburger = c * 50
                    costofpizza = d * 200
                    costofchesseburger = e * 70
                    costofdrinks = f * 30
                    costofmeal1 = g * 200
                    costofmeal2 = h * 250
                    costofmeal = ('%.2f' % (
                                costoffries + costoflunch + costofburger + costofpizza + costofchesseburger + costofdrinks + costofmeal1 + costofmeal2))
                    charge = ((
                                          costoffries + costoflunch + costofburger + costofpizza + costofchesseburger + costofdrinks + costofmeal1 + costofmeal2) / 99)
                    pay = ((
                                       costoffries + costoflunch + costofburger + costofpizza + costofchesseburger + costofdrinks + costofmeal1 + costofmeal2) * 0.05)
                    subtotal = (
                                costoffries + costoflunch + costofburger + costofpizza + costofchesseburger + costofdrinks + costofmeal1 + costofmeal2)
                    Service = ('%.2f' % charge)
                    OverAllCost = (charge + pay + subtotal)
                    PaidTax = ('%.2f' % pay)
                    cost.set(costofmeal)
                    service.set(Service)
                    tax.set(PaidTax)
                    sub_total.set(costofmeal)
                    final.set(OverAllCost)

                    table.execute(
                        "INSERT INTO ORDERS(FRIES_MEAL,LUNCH_MEAL,BURGER_MEAL,PIZZA_MEAL,CHEESE_BURGER,DRINKS,MEAL_1,MEAL_2,COST,SERVICE_CHARGE,TAX,SUBTOTAL,TOTAL)VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)",
                        (str(costoffries), str(costoflunch), str(costofburger), str(costofpizza),
                         str(costofchesseburger),
                         str(costofdrinks), str(costofmeal1), str(costofmeal2), str(costofmeal), str(Service),
                         str(PaidTax),
                         str(costofmeal), str(OverAllCost),))
                    table.commit()
                    messagebox.showinfo("Success", "Bill Successfully Saved..")
                    '''
                    print(table.execute("select * from orders"))
                    items=[]
                    for row in table.execute("SELECT * FROM ORDERS ORDER BY ORDER_NUMBER DESC LIMIT 1"):
                        for i in len(row):
                            print(row[i])
                            if row[i]!=0:
                                items.append(i)

                        p=row
                       # print(p)
                       '''
                except:
                    messagebox.showwarning("WARNING", "Invalid Input")

                    # generating bill

            def bill(self):
                localtime = time.strftime('%d-%m-%y   %H:%M:%S')
                file = open("bills.txt", "w")
                file.write(localtime + "\n")
                file.write("order number : " + str(order) + "\n\n\n")
                file.write("ITEM                    QUANTITY                AMOUNT                        TOTAL\n")
                if (costoffries != 0):
                    file.write("Fries                   " + str(
                        a) + "                         Rs 50" + "                       Rs " + str(costoffries) + "\n")
                if (costoflunch != 0):
                    file.write("Lunch                   " + str(
                        b) + "                         Rs 150" + "                      Rs " + str(costoflunch) + "\n")
                if (costofburger != 0):
                    file.write("Burger                  " + str(
                        c) + "                         Rs 50" + "                       Rs " + str(costofburger) + "\n")
                if (costofpizza != 0):
                    file.write("Pizza                   " + str(
                        d) + "                         Rs 200" + "                       Rs " + str(costofpizza) + "\n")
                if (costofchesseburger != 0):
                    file.write("Cheese burger           " + str(
                        e) + "                         Rs 70" + "                       Rs " + str(
                        costofchesseburger) + "\n")
                if (costofdrinks != 0):
                    file.write("Drinks                  " + str(
                        f) + "                         Rs 30" + "                       Rs " + str(costofdrinks) + "\n")
                if (costofmeal1 != 0):
                    file.write("Meal1                   " + str(
                        g) + "                         Rs 200" + "                       Rs " + str(costofmeal1) + "\n")
                if (costofmeal2 != 0):
                    file.write("Meal2                   " + str(
                        h) + "                         Rs 250" + "                       Rs " + str(costofmeal2) + "\n")

                file.write("\n")
                file.write("Cost of Meal : Rs " + str(costofmeal) + "\nService : Rs " + str(Service) + "\nTax : Rs " + str(
                    PaidTax) + "\nToatal : Rs " + str(OverAllCost))

        def amount():
            c = Calculate()
            c.price(e2, e3, e4, e5, e6, e7, m1, m2)

        def call_bill():
            c = Calculate()
            c.bill()
            os.startfile("bills.txt")

        # ------------------------------------------------------------------------

        # order NUMBER
        # x=random.randint(1,500)
        # order=str(x)
        global order
        order = 1
        ran.set(order)
        # ----------------------------------------------------------------

        # giving default values to different variables
        fries.set(0)
        lunch.set(0)
        burger.set(0)
        pizza.set(0)
        cheese_burger.set(0)
        drinks.set(0)
        meal_1.set(0)
        meal_2.set(0)

        # ----------------------------------------------------------------

        # function to reset all values
        def reset():
            global order
            order = order + 1
            ran.set(order)
            fries.set(0)
            lunch.set(0)
            burger.set(0)
            pizza.set(0)
            cheese_burger.set(0)
            drinks.set(0)
            meal_1.set(0)
            meal_2.set(0)
            cost.set(0)
            service.set(0)
            tax.set(0)
            final.set(0)

        def time_display():
            localtime = time.strftime('%d-%m-%y   %H:%M:%S')
            time1.configure(text=localtime)
            frame1.after(200, time_display)

        # ------------------------------------------------------------------------

        # main window GUI representation
        frame1 = Frame(root)
        frame1.pack(side=TOP)

        x = Label(frame1, text="RESTAURANT BILLING SYSTEM", font=("comic sans ms", '30', "bold", "underline"),
                  fg="steel blue", bd=10, anchor=W)
        x.grid(row=0, column=0)

        localtime = time.strftime('%d-%m-%y   %H:%M:%S')
        time1 = Label(frame1, text=localtime, font=("comic sans ms", "20", "bold", "italic"), fg="steel blue", anchor=W)
        time1.grid(row=1, column=0)
        time_display()
        # -----------------------------------------

        frame2 = Frame(root)
        frame2.pack(side=LEFT)

        lbl1 = Label(frame2, text="Order No.", font=("comic sans ms", "15"), fg="steel blue")
        lbl1.grid(row=0)
        e1 = Entry(frame2, textvariable=ran, font=("comic sans ms", "15"), fg="steel blue",state='disabled')
        e1.grid(row=0, column=1)

        lbl2 = Label(frame2, text="Fries Meal", font=("comic sans ms", "15"), fg="steel blue")
        lbl2.grid(row=1)
        e2 = Entry(frame2, textvariable=fries, font=("comic sans ms", "15"), fg="steel blue")
        e2.grid(row=1, column=1)

        lbl3 = Label(frame2, text="Lunch Meal", font=("comic sans ms", "15"), fg="steel blue")
        lbl3.grid(row=2)
        e3 = Entry(frame2, textvariable=lunch, font=("comic sans ms", "15"), fg="steel blue")
        e3.grid(row=2, column=1)

        lbl4 = Label(frame2, text="Burger Meal", font=("comic sans ms", "15"), fg="steel blue")
        lbl4.grid(row=3)
        e4 = Entry(frame2, textvariable=burger, font=("comic sans ms", "15"), fg="steel blue")
        e4.grid(row=3, column=1)

        lbl5 = Label(frame2, text="Pizza Meal", font=("comic sans ms", "15"), fg="steel blue")
        lbl5.grid(row=4)
        e5 = Entry(frame2, textvariable=pizza, font=("comic sans ms", "15"), fg="steel blue")
        e5.grid(row=4, column=1)

        lbl6 = Label(frame2, text="Cheese Burger", font=("comic sans ms", "15"), fg="steel blue")
        lbl6.grid(row=5)
        e6 = Entry(frame2, textvariable=cheese_burger, font=("comic sans ms", "15"), fg="steel blue")
        e6.grid(row=5, column=1)

        meal1 = Label(frame2, text="Meal 1", font=("comic sans ms", "15"), fg="steel blue")
        meal1.grid(row=6)
        m1 = Entry(frame2, textvariable=meal_1, font=("comic sans ms", "15"), fg="steel blue")
        m1.grid(row=6, column=1)
        # ------------------------------------

        frame3 = Frame(root)
        frame3.pack(side=RIGHT)

        meal2 = Label(frame3, text="Meal 2", font=("comic sans ms", "15"), fg="steel blue")
        meal2.grid(row=0)
        m2 = Entry(frame3, textvariable=meal_2, font=("comic sans ms", "15"), fg="steel blue")
        m2.grid(row=0, column=1)

        lbl7 = Label(frame3, text="Drinks", font=("comic sans ms", "15"), fg="steel blue")
        lbl7.grid(row=1)
        e7 = Entry(frame3, textvariable=drinks, font=("comic sans ms", "15"), fg="steel blue")
        e7.grid(row=1, column=1)

        lbl8 = Label(frame3, text="Cost", font=("comic sans ms", "15"), fg="steel blue")
        lbl8.grid(row=2)
        e8 = Entry(frame3, textvariable=cost, font=("comic sans ms", "15"), fg="steel blue", state='disabled')
        e8.grid(row=2, column=1)

        lbl9 = Label(frame3, text="Service Charge", font=("comic sans ms", "15"), fg="steel blue")
        lbl9.grid(row=3)
        e9 = Entry(frame3, textvariable=service, font=("comic sans ms", "15"), fg="steel blue", state='disabled')
        e9.grid(row=3, column=1)

        lbl10 = Label(frame3, text="Tax", font=("comic sans ms", "15"), fg="steel blue")
        lbl10.grid(row=4)
        e10 = Entry(frame3, textvariable=tax, font=("comic sans ms", "15"), fg="steel blue", state='disabled')
        e10.grid(row=4, column=1)

        lbl11 = Label(frame3, text="Subtotal", font=("comic sans ms", "15"), fg="steel blue")
        lbl11.grid(row=5)
        e11 = Entry(frame3, textvariable=cost, font=("comic sans ms", "15"), fg="steel blue", state='disabled')
        e11.grid(row=5, column=1)

        lbl12 = Label(frame3, text="Total", font=("comic sans ms", "15"), fg="steel blue")
        lbl12.grid(row=6)
        e12 = Entry(frame3, textvariable=final, font=("comic sans ms", "15"), fg="steel blue", state='disabled')
        e12.grid(row=6, column=1)

        # ------------------------------------------------------------------

        # buttons and their working
        frame4 = Frame(root)
        frame4.pack(side=BOTTOM)
        price = Button(frame4, text="price \n list", height=2, width=7, font=("comic sans ms", "11"), fg="steel blue",
                       command=price)
        price.grid(row=0, column=0, padx=7, pady=7)
        total = Button(frame4, text="total \n amount", height=2, width=7, font=("comic sans ms", "11"), fg="steel blue",
                       command=amount)
        total.grid(row=0, column=5, padx=7, pady=7)
        reset = Button(frame4, text="reset", height=2, width=7, font=("comic sans ms", "11"), fg="steel blue",
                       command=reset)
        reset.grid(row=0, column=10, padx=7, pady=7)
        exit = Button(frame4, text="exit", height=2, width=7, font=("comic sans ms", "11"), fg="steel blue",
                      command=quit)
        exit.grid(row=0, column=15, padx=7, pady=7)
        bill = Button(frame4, text="generate \n bill", height=2, width=7, font=("comic sans ms", "11"), fg="steel blue",
                      command=call_bill)
        bill.grid(row=0, column=20, padx=7, pady=7)

        # --------------------------------------------------------

        # end of mainloop
        root.mainloop()

    def Login(event=None):
        Database()
        if USERNAME.get() == "" or PASSWORD.get() == "":
            lbl_text.config(text="Please complete the required field!", fg="red")
        else:
            cursor.execute("SELECT * FROM `member` WHERE `username` = ? AND `password` = ?",
                           (USERNAME.get(), PASSWORD.get()))
            if cursor.fetchone() is not None:
                HomeWindow()
                USERNAME.set("")
                PASSWORD.set("")
                lbl_text.config(text="")
            else:
                lbl_text.config(text="Invalid username or password", fg="red")
                USERNAME.set("")
                PASSWORD.set("")
        cursor.close()
        conn.close()

    second = Tk()
    second.title(" Login ")
    second.geometry("{0}x{1}+0+0".format(second.winfo_screenwidth(),second.winfo_screenheight()))
    load2 = Image.open("login.jpg")
    background_image2 = ImageTk.PhotoImage(load2)
    background_label2 = Label(second, image=background_image2)
    background_label2.place(x=0, y=0, relheight=1, relwidth=1)

    # ==============================VARIABLES======================================
    USERNAME = StringVar()
    PASSWORD = StringVar()

    # ==============================FRAMES=========================================
    # Top = Frame(root)
    # Top.pack(side=TOP, fill=X,pady=50)
    # Top.place(relx=0.4,rely=0.2)
    Form = Frame(second, height=500, width=500, bg='white',borderwidth=2,relief='solid')
    # Form.pack(side=TOP, pady=100)
    # Form.pack(side=TOP,padx=40,pady=40)
    Form.place(relx=0.33, rely=0.2)
    # ==============================LABELS=========================================
    lbl_title = Label(Form, text="Enter \n Username  and  Password  \n to  Login ", font=('Lucida Handwriting', 15), bg='white',fg='LightSkyBlue3')
    lbl_title.grid(row=0, pady=30, columnspan=2)
    empty = Label(Form, text="", bg='white')
    empty.grid(row=1)
    empty = Label(Form, text="", bg='white')
    empty.grid(row=2)

    lbl_username = Label(Form, text="Username:", font=('Lucida Handwriting', 12), bd=15, bg='white')
    lbl_username.grid(row=3, sticky='w', padx=20)
    lbl_password = Label(Form, text="Password:", font=('Lucida Handwriting', 12), bd=15, bg='white')
    lbl_password.grid(row=5, sticky='w', padx=20)
    lbl_text = Label(Form, bg='white')
    lbl_text.grid(row=7, columnspan=2)

    # ==============================ENTRY WIDGETS==================================
    username = Entry(Form, textvariable=USERNAME, font=('Lucida Handwriting',10), width=30,bg="gray99")
    username.grid(row=4, column=0, pady=5)
    password = Entry(Form, textvariable=PASSWORD, show="*", font=('Lucida Handwriting',10), width=30,bg='gray99')
    password.grid(row=6, column=0, pady=5)

    # ==============================BUTTON WIDGETS=================================
    btn_login = Button(Form, text="Log In", font=('Lucida Handwriting',15), width=30, command=Login,bg='LightSkyBlue3')
    btn_login.grid(pady=25, padx=30, row=8, columnspan=2, sticky='w')
    btn_login.bind('<Return>', Login)

    def Database():
        global conn, cursor
        conn = sqlite3.connect("pythontut.db")
        cursor = conn.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS `member` (mem_id INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT, username TEXT, password TEXT)")
        cursor.execute("SELECT * FROM `member` WHERE `username` = 'admin' AND `password` = 'admin' and username='surbhi' and password='surbhi123'and username='rollno' and password='ue168108'")
        if cursor.fetchone() is None:
            cursor.execute("INSERT INTO `member` (username, password) VALUES('admin', 'admin123')")
            cursor.execute("INSERT INTO `member` (username, password) VALUES('surbhi', 'surbhi123')")
            cursor.execute("INSERT INTO `member` (username, password) VALUES('rollno', 'ue168108')")
            conn.commit()
    second.mainloop()


first=Tk()
first.geometry("{0}x{1}+0+0".format(first.winfo_screenwidth(), first.winfo_screenheight()))
load3=Image.open("fd1.jpg")
background_image3=ImageTk.PhotoImage(load3)
background_label3=Label(first, image=background_image3)
background_label3.place(x=0,y=0,relheight=1,relwidth=1)
background_label3.config(bg="white")

welcome=Label(first,text="        Welcome to Restaurant Billing System ",font=("comic sans ms",'30',"bold"),fg="orange",bd=10,anchor=W,bg="white")
welcome.grid(row=5,column=10)
login=Button(first,text="LOGIN",bg="white",font=("comic sans ms",'20',"bold"),fg="orange",command=second_window)
login.place(relx=0.15, rely=0.4, anchor=NE)
login.config(cursor="heart")

cancel=Button(first,text="CANCEL",bg="white",font=("comic sans ms",'20',"bold"),fg="orange",command=exit)
cancel.place(relx=0.4, rely=0.4, anchor=NE)
cancel.config(cursor="heart")




first.mainloop()