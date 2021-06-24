from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import ttk
import sqlite3
import pickle
import pandas as pd
from kmodes.kprototypes import KPrototypes
from sklearn import preprocessing

class Products:

    def __init__(self,name,price,category,image):
        super().__init__()
        self.name=name
        self.price = price
        self.category = category
        self.image = image


cart=[]
window = Tk()

#importing product images   
shirt_image = ImageTk.PhotoImage(Image.open('D:\School\Minor Project\GUI\images\\shirt.png').resize((350, 350), Image.ANTIALIAS))
jeans_image = ImageTk.PhotoImage(Image.open('D:\School\Minor Project\GUI\images\\jeans.png').resize((350, 350), Image.ANTIALIAS))
lipstick_image = ImageTk.PhotoImage(Image.open('D:\School\Minor Project\GUI\images\\lipstick.png').resize((350, 350), Image.ANTIALIAS))
sugar_image = ImageTk.PhotoImage(Image.open('D:\School\Minor Project\GUI\images\\sugar.png').resize((350, 350), Image.ANTIALIAS))
apple_image = ImageTk.PhotoImage(Image.open('D:\School\Minor Project\GUI\images\\apple.png').resize((350, 350), Image.ANTIALIAS))
rice_image = ImageTk.PhotoImage(Image.open('D:\School\Minor Project\GUI\images\\rice.png').resize((350, 350), Image.ANTIALIAS))
notebook_image = ImageTk.PhotoImage(Image.open('D:\School\Minor Project\GUI\images\\notebook.png').resize((350, 350), Image.ANTIALIAS))
pen_image = ImageTk.PhotoImage(Image.open('D:\School\Minor Project\GUI\images\\pen.png').resize((350, 350), Image.ANTIALIAS))
phone_image = ImageTk.PhotoImage(Image.open('D:\School\Minor Project\GUI\images\\phone.png').resize((350, 350), Image.ANTIALIAS))
laptop_image = ImageTk.PhotoImage(Image.open('D:\School\Minor Project\GUI\images\\laptop.png').resize((350, 350), Image.ANTIALIAS))
painkiller_image = ImageTk.PhotoImage(Image.open('D:\School\Minor Project\GUI\images\\painkiller.png').resize((350, 350), Image.ANTIALIAS))
vaccine_image = ImageTk.PhotoImage(Image.open('D:\School\Minor Project\GUI\images\\vaccine.png').resize((350, 350), Image.ANTIALIAS))
fridge_image = ImageTk.PhotoImage(Image.open('D:\School\Minor Project\GUI\images\\fridge.png').resize((350, 350), Image.ANTIALIAS))
ac_image = ImageTk.PhotoImage(Image.open('D:\School\Minor Project\GUI\images\\ac.png').resize((350, 350), Image.ANTIALIAS))
microwave_image = ImageTk.PhotoImage(Image.open('D:\School\Minor Project\GUI\images\\microwave.png').resize((350, 350), Image.ANTIALIAS))
car_image = ImageTk.PhotoImage(Image.open('D:\School\Minor Project\GUI\images\\car.png').resize((350, 350), Image.ANTIALIAS))
rc_image = ImageTk.PhotoImage(Image.open('D:\School\Minor Project\GUI\images\\rc.png').resize((350, 350), Image.ANTIALIAS))
nerf_image = ImageTk.PhotoImage(Image.open('D:\School\Minor Project\GUI\images\\nerf.png').resize((350, 350), Image.ANTIALIAS))
bike_image = ImageTk.PhotoImage(Image.open('D:\School\Minor Project\GUI\images\\bike.png').resize((350, 350), Image.ANTIALIAS))
perfume_image = ImageTk.PhotoImage(Image.open('D:\School\Minor Project\GUI\images\\perfume.png').resize((350, 350), Image.ANTIALIAS))


#clothes
shirt = Products("Shirt", 499, "clothes", shirt_image)
jeans = Products("Jeans", 799, "clothes", jeans_image)

#cosmetics
lipstick = Products("Lipstick", 299, "cosmetics", lipstick_image)
perfume = Products("Perfume", 599, "cosmetics", perfume_image)

#groceries
sugar = Products("Sugar(1kg)", 89, "groceries", sugar_image)
apple = Products("Apples(1kg)", 99, "groceries", apple_image)
rice = Products("Rice(1kg)", 49, "groceries", rice_image)

#stationery
notebook = Products("Notebook", 49, "stationery", notebook_image)
pen = Products("Pens(Bundle of 10)", 99, "stationery", pen_image)

#electronics
phone = Products("Phone", 14999, "electronics", phone_image)
laptop = Products("Laptop", 39999, "electronics", laptop_image)

#medicines
painkiller = Products("Painkillers(10)", 75, "medicines", painkiller_image)
vaccine = Products("Vaccine", 1250, "medicines", vaccine_image)

#appliances
fridge = Products("Refrigerator", 44999, "appliances", fridge_image)
ac = Products("AC", 49999, "appliances", ac_image)
microwave = Products("Microwave Oven", 25999, "appliances", microwave_image)

#vehicles
car = Products("Car", 500000, "vehicles", car_image)
bike=Products("Bike", 90000, "vehicles", bike_image)

#toys
rc = Products("RC Car", 2999, "toys", rc_image)
nerf = Products("Nerf Gun", 1299, "toys", nerf_image)


def productScreen(window, username, cart):
    
    # clearing screen
    for widgets in window.winfo_children():
        widgets.destroy()

    window.geometry("1500x750+0+0")
    window.iconbitmap("D:\School\Minor Project\GUI\images\\logo.ico")
    window.resizable(False, False)
    back_img = ImageTk.PhotoImage(Image.open('D:\School\Minor Project\GUI\images\\FlipcartFrame2.png'))
    back_image_panel = Label(window, image=back_img)
    back_image_panel.pack(fill='both', expand='yes')
    window.title("Flipcart")

    frame = Frame(window, height=610, width=1300, bg="#ffffff")
    frame.place(x=230, y=200)

    #fill survey
    data = sqlite3.connect("D:\\School\Minor Project\\GUI\\NewCustomers.db")
    cursor = data.cursor()
    
    cursor.execute("SELECT isFillSurvey FROM customers WHERE username=?", (username,))
    survey_check = cursor.fetchall()
    
    if survey_check[0][0] == 1:
        Label(window, text="Discount Applied!", bg="#f19849", fg="#ffffff",
                           font=("yu gothic ui", 24, "bold")).place(x=625, y=78)        
    else:
        fill_survey_image=ImageTk.PhotoImage(Image.open('D:\School\Minor Project\GUI\images\\FillSurvey.png'))
        fill_survey_button = Button(window, image=fill_survey_image, relief=FLAT, activebackground="#f19849", borderwidth=0, background="#f19849", cursor="hand2",command= lambda: survey(window,username,cart))
        fill_survey_button.place(x=700, y=85)

    cursor.execute("SELECT segment FROM customers WHERE username=?", (username,))
    segment = cursor.fetchall()
    segment = segment[0][0]
    
    data.commit()
    data.close()

    
    add_to_cart_image=ImageTk.PhotoImage(Image.open('D:\School\Minor Project\GUI\images\\Addtocart.png'))
    #add to cart button def
    def AddToCart(cart, product):
        if len(cart)==0:
            cart.append([product, 1])
        else:
            for i in cart:
                if product == i[0]:
                    i[1]+=1
                    break
            else:
                cart.append([product, 1])
                
        info=product.name+" has been added to your cart!"
        messagebox.showinfo("Item added",info)


    #button functions
    def appliances():

        # clearing screen
        for widgets in frame.winfo_children():
            widgets.destroy()

        Label(frame, image=fridge.image).place(x=0, y=0)
        Label(frame, text=fridge.name, bg="#ffffff", fg="#f19849",
                           font=("yu gothic ui", 24, "bold")).place(x=90, y=355)
        Label(frame, text=fridge.price, bg="#ffffff", fg="#f19849",
                           font=("yu gothic ui", 14, "bold")).place(x=50, y=405)
        Button(frame, image=add_to_cart_image,
                           relief=FLAT, activebackground="#f19849", borderwidth=0, background="#f19849", cursor="hand2",command=lambda: AddToCart(cart,fridge)).place(x=120,y=405)

        Label(frame, image=ac.image).place(x=360, y=0)
        Label(frame, text=ac.name, bg="#ffffff", fg="#f19849",
                           font=("yu gothic ui", 24, "bold")).place(x=510, y=355)
        Label(frame, text=ac.price, bg="#ffffff", fg="#f19849",
                           font=("yu gothic ui", 14, "bold")).place(x=410, y=405)
        Button(frame, image=add_to_cart_image,
                           relief=FLAT, activebackground="#f19849", borderwidth=0, background="#f19849", cursor="hand2",command=lambda: AddToCart(cart,ac)).place(x=480, y=405)
                           
        Label(frame, image=microwave.image).place(x=710, y=0)
        Label(frame, text=microwave.name, bg="#ffffff", fg="#f19849",
                           font=("yu gothic ui", 24, "bold")).place(x=770, y=355)
        Label(frame, text=microwave.price, bg="#ffffff", fg="#f19849",
                           font=("yu gothic ui", 14, "bold")).place(x=770, y=405)
        Button(frame, image=add_to_cart_image,
                           relief=FLAT, activebackground="#f19849", borderwidth=0, background="#f19849", cursor="hand2",command=lambda: AddToCart(cart,microwave)).place(x=840,y=405)

    def clothes():
        # clearing screen
        for widgets in frame.winfo_children():
            widgets.destroy()

        Label(frame, image=shirt.image).place(x=0, y=0)
        Label(frame, text=shirt.name, bg="#ffffff", fg="#f19849",
                           font=("yu gothic ui", 24, "bold")).place(x=140, y=355)
        Label(frame, text=shirt.price, bg="#ffffff", fg="#f19849",
                           font=("yu gothic ui", 14, "bold")).place(x=70, y=405)
        Button(frame, image=add_to_cart_image,
                           relief=FLAT, activebackground="#f19849", borderwidth=0, background="#f19849", cursor="hand2",command=lambda: AddToCart(cart,shirt)).place(x=120,y=405)

        Label(frame, image=jeans.image).place(x=360, y=0)
        Label(frame, text=jeans.name, bg="#ffffff", fg="#f19849",
                           font=("yu gothic ui", 24, "bold")).place(x=510, y=355)
        Label(frame, text=jeans.price, bg="#ffffff", fg="#f19849",
                           font=("yu gothic ui", 14, "bold")).place(x=430, y=405)
        Button(frame, image=add_to_cart_image,
                           relief=FLAT, activebackground="#f19849", borderwidth=0, background="#f19849", cursor="hand2",command=lambda: AddToCart(cart,jeans)).place(x=480, y=405)

    def cosmetics():
        
        # clearing screen
        for widgets in frame.winfo_children():
            widgets.destroy()

        Label(frame, image=lipstick.image).place(x=0, y=0)
        Label(frame, text=lipstick.name, bg="#ffffff", fg="#f19849",
                           font=("yu gothic ui", 24, "bold")).place(x=120, y=355)
        Label(frame, text=lipstick.price, bg="#ffffff", fg="#f19849",
                           font=("yu gothic ui", 14, "bold")).place(x=70, y=405)
        Button(frame, image=add_to_cart_image,
                           relief=FLAT, activebackground="#f19849", borderwidth=0, background="#f19849", cursor="hand2",command=lambda: AddToCart(cart,lipstick)).place(x=120,y=405)

        Label(frame, image=perfume.image).place(x=360, y=0)
        Label(frame, text=perfume.name, bg="#ffffff", fg="#f19849",
                           font=("yu gothic ui", 24, "bold")).place(x=480, y=355)
        Label(frame, text=perfume.price, bg="#ffffff", fg="#f19849",
                           font=("yu gothic ui", 14, "bold")).place(x=430, y=405)
        Button(frame, image=add_to_cart_image,
                           relief=FLAT, activebackground="#f19849", borderwidth=0, background="#f19849", cursor="hand2",command=lambda: AddToCart(cart,perfume)).place(x=480, y=405)
    
    def electronics():
        
        # clearing screen
        for widgets in frame.winfo_children():
            widgets.destroy()

        Label(frame, image=phone.image).place(x=0, y=0)
        Label(frame, text=phone.name, bg="#ffffff", fg="#f19849",
                           font=("yu gothic ui", 24, "bold")).place(x=120, y=355)
        Label(frame, text=phone.price, bg="#ffffff", fg="#f19849",
                           font=("yu gothic ui", 14, "bold")).place(x=40, y=405)
        Button(frame, image=add_to_cart_image,
                           relief=FLAT, activebackground="#f19849", borderwidth=0, background="#f19849", cursor="hand2",command=lambda: AddToCart(cart,phone)).place(x=110,y=405)

        Label(frame, image=laptop.image).place(x=360, y=0)
        Label(frame, text=laptop.name, bg="#ffffff", fg="#f19849",
                           font=("yu gothic ui", 24, "bold")).place(x=480, y=355)
        Label(frame, text=laptop.price, bg="#ffffff", fg="#f19849",
                           font=("yu gothic ui", 14, "bold")).place(x=400, y=405)
        Button(frame, image=add_to_cart_image,
                           relief=FLAT, activebackground="#f19849", borderwidth=0, background="#f19849", cursor="hand2",command=lambda: AddToCart(cart,laptop)).place(x=470, y=405)

    def groceries():
        
        # clearing screen
        for widgets in frame.winfo_children():
            widgets.destroy()

        Label(frame, image=sugar.image).place(x=0, y=0)
        Label(frame, text=sugar.name, bg="#ffffff", fg="#f19849",
                           font=("yu gothic ui", 24, "bold")).place(x=100, y=355)
        Label(frame, text=sugar.price, bg="#ffffff", fg="#f19849",
                           font=("yu gothic ui", 14, "bold")).place(x=90, y=405)
        Button(frame, image=add_to_cart_image,
                           relief=FLAT, activebackground="#f19849", borderwidth=0, background="#f19849", cursor="hand2",command=lambda: AddToCart(cart,sugar)).place(x=120,y=405)

        Label(frame, image=apple.image).place(x=360, y=0)
        Label(frame, text=apple.name, bg="#ffffff", fg="#f19849",
                           font=("yu gothic ui", 24, "bold")).place(x=460, y=355)
        Label(frame, text=apple.price, bg="#ffffff", fg="#f19849",
                           font=("yu gothic ui", 14, "bold")).place(x=450, y=405)
        Button(frame, image=add_to_cart_image,
                           relief=FLAT, activebackground="#f19849", borderwidth=0, background="#f19849", cursor="hand2",command=lambda: AddToCart(cart,apple)).place(x=480, y=405)

        Label(frame, image=rice.image).place(x=710, y=0)
        Label(frame, text=rice.name, bg="#ffffff", fg="#f19849",
                           font=("yu gothic ui", 24, "bold")).place(x=820, y=355)
        Label(frame, text=rice.price, bg="#ffffff", fg="#f19849",
                           font=("yu gothic ui", 14, "bold")).place(x=790, y=405)
        Button(frame, image=add_to_cart_image,
                           relief=FLAT, activebackground="#f19849", borderwidth=0, background="#f19849", cursor="hand2",command=lambda: AddToCart(cart,rice)).place(x=820,y=405)

    def medicines():
        
        # clearing screen
        for widgets in frame.winfo_children():
            widgets.destroy()

        Label(frame, image=painkiller.image).place(x=0, y=0)
        Label(frame, text=painkiller.name, bg="#ffffff", fg="#f19849",
                           font=("yu gothic ui", 24, "bold")).place(x=80, y=355)
        Label(frame, text=painkiller.price, bg="#ffffff", fg="#f19849",
                           font=("yu gothic ui", 14, "bold")).place(x=90, y=405)
        Button(frame, image=add_to_cart_image,
                           relief=FLAT, activebackground="#f19849", borderwidth=0, background="#f19849", cursor="hand2",command=lambda: AddToCart(cart,painkiller)).place(x=120,y=405)

        Label(frame, image=vaccine.image).place(x=360, y=0)
        Label(frame, text=vaccine.name, bg="#ffffff", fg="#f19849",
                           font=("yu gothic ui", 24, "bold")).place(x=490, y=355)
        Label(frame, text=vaccine.price, bg="#ffffff", fg="#f19849",
                           font=("yu gothic ui", 14, "bold")).place(x=430, y=405)
        Button(frame, image=add_to_cart_image,
                           relief=FLAT, activebackground="#f19849", borderwidth=0, background="#f19849", cursor="hand2",command=lambda: AddToCart(cart,vaccine)).place(x=480, y=405)

    def stationery():
        
        # clearing screen
        for widgets in frame.winfo_children():
            widgets.destroy()

        Label(frame, image=notebook.image).place(x=0, y=0)
        Label(frame, text=notebook.name, bg="#ffffff", fg="#f19849",
                           font=("yu gothic ui", 24, "bold")).place(x=110, y=355)
        Label(frame, text=notebook.price, bg="#ffffff", fg="#f19849",
                           font=("yu gothic ui", 14, "bold")).place(x=90, y=405)
        Button(frame, image=add_to_cart_image,
                           relief=FLAT, activebackground="#f19849", borderwidth=0, background="#f19849", cursor="hand2",command=lambda: AddToCart(cart,notebook)).place(x=120,y=405)

        Label(frame, image=pen.image).place(x=360, y=0)
        Label(frame, text=pen.name, bg="#ffffff", fg="#f19849",
                           font=("yu gothic ui", 24, "bold")).place(x=400, y=355)
        Label(frame, text=pen.price, bg="#ffffff", fg="#f19849",
                           font=("yu gothic ui", 14, "bold")).place(x=450, y=405)
        Button(frame, image=add_to_cart_image,
                           relief=FLAT, activebackground="#f19849", borderwidth=0, background="#f19849", cursor="hand2",command=lambda: AddToCart(cart,pen)).place(x=480, y=405)

    def toys():
        
        # clearing screen
        for widgets in frame.winfo_children():
            widgets.destroy()

        Label(frame, image=rc.image).place(x=0, y=0)
        Label(frame, text=rc.name, bg="#ffffff", fg="#f19849",
                           font=("yu gothic ui", 24, "bold")).place(x=140, y=355)
        Label(frame, text=rc.price, bg="#ffffff", fg="#f19849",
                           font=("yu gothic ui", 14, "bold")).place(x=70, y=405)
        Button(frame, image=add_to_cart_image,
                           relief=FLAT, activebackground="#f19849", borderwidth=0, background="#f19849", cursor="hand2",command=lambda: AddToCart(cart,rc)).place(x=120,y=405)

        Label(frame, image=nerf.image).place(x=360, y=0)
        Label(frame, text=nerf.name, bg="#ffffff", fg="#f19849",
                           font=("yu gothic ui", 24, "bold")).place(x=480, y=355)
        Label(frame, text=nerf.price, bg="#ffffff", fg="#f19849",
                           font=("yu gothic ui", 14, "bold")).place(x=430, y=405)
        Button(frame, image=add_to_cart_image,
                           relief=FLAT, activebackground="#f19849", borderwidth=0, background="#f19849", cursor="hand2",command=lambda: AddToCart(cart,nerf)).place(x=480, y=405)

    def vehicles():
        
        # clearing screen
        for widgets in frame.winfo_children():
            widgets.destroy()

        Label(frame, image=car.image).place(x=0, y=0)
        Label(frame, text=car.name, bg="#ffffff", fg="#f19849",
                           font=("yu gothic ui", 24, "bold")).place(x=150, y=355)
        Label(frame, text=car.price, bg="#ffffff", fg="#f19849",
                           font=("yu gothic ui", 14, "bold")).place(x=40, y=405)
        Button(frame, image=add_to_cart_image,
                           relief=FLAT, activebackground="#f19849", borderwidth=0, background="#f19849", cursor="hand2",command=lambda: AddToCart(cart,car)).place(x=120,y=405)

        Label(frame, image=bike.image).place(x=360, y=0)
        Label(frame, text=bike.name, bg="#ffffff", fg="#f19849",
                           font=("yu gothic ui", 24, "bold")).place(x=510, y=355)
        Label(frame, text=bike.price, bg="#ffffff", fg="#f19849",
                           font=("yu gothic ui", 14, "bold")).place(x=410, y=405)
        Button(frame, image=add_to_cart_image,
                           relief=FLAT, activebackground="#f19849", borderwidth=0, background="#f19849", cursor="hand2",command=lambda: AddToCart(cart,bike)).place(x=480, y=405)



    #categories images
    appliances_image = ImageTk.PhotoImage(Image.open('D:\School\Minor Project\GUI\images\\appliances.png'))
    clothes_image = ImageTk.PhotoImage(Image.open('D:\School\Minor Project\GUI\images\\clothes.png'))
    cosmetics_image = ImageTk.PhotoImage(Image.open('D:\School\Minor Project\GUI\images\\cosmetics.png'))
    electronics_image = ImageTk.PhotoImage(Image.open('D:\School\Minor Project\GUI\images\\electronics.png'))
    groceries_image = ImageTk.PhotoImage(Image.open('D:\School\Minor Project\GUI\images\\groceries.png'))
    medicines_image = ImageTk.PhotoImage(Image.open('D:\School\Minor Project\GUI\images\\medicines.png'))
    stationery_image = ImageTk.PhotoImage(Image.open('D:\School\Minor Project\GUI\images\\stationery.png'))
    toys_image = ImageTk.PhotoImage(Image.open('D:\School\Minor Project\GUI\images\\toys.png'))
    vehicles_image = ImageTk.PhotoImage(Image.open('D:\School\Minor Project\GUI\images\\vehicles.png'))
    
    #categories
    Button(window, image=appliances_image, relief=FLAT, activebackground="#f19849", borderwidth=0, background="#f19849", cursor="hand2",command=appliances).place(x=50, y=220)
    Button(window, image=clothes_image, relief=FLAT, activebackground="#f19849", borderwidth=0, background="#f19849", cursor="hand2",command=clothes).place(x=50, y=280)
    Button(window, image=cosmetics_image, relief=FLAT, activebackground="#f19849", borderwidth=0, background="#f19849", cursor="hand2",command=cosmetics).place(x=50, y=340)
    Button(window, image=electronics_image, relief=FLAT, activebackground="#f19849", borderwidth=0, background="#f19849", cursor="hand2",command=electronics).place(x=50, y=400)
    Button(window, image=groceries_image, relief=FLAT, activebackground="#f19849", borderwidth=0, background="#f19849", cursor="hand2",command=groceries).place(x=50, y=460)
    Button(window, image=medicines_image, relief=FLAT, activebackground="#f19849", borderwidth=0, background="#f19849", cursor="hand2",command=medicines).place(x=50, y=520)
    Button(window, image=stationery_image, relief=FLAT, activebackground="#f19849", borderwidth=0, background="#f19849", cursor="hand2",command=stationery).place(x=50, y=580)
    Button(window, image=toys_image, relief=FLAT, activebackground="#f19849", borderwidth=0, background="#f19849", cursor="hand2",command=toys).place(x=50, y=640)
    Button(window, image=vehicles_image, relief=FLAT, activebackground="#f19849", borderwidth=0, background="#f19849", cursor="hand2",command=vehicles).place(x=50, y=700)

    
    minus_image = ImageTk.PhotoImage(Image.open('D:\School\Minor Project\GUI\images\\minus.png'))
    plus_image=ImageTk.PhotoImage(Image.open('D:\School\Minor Project\GUI\images\\plus.png'))
    place_order_image= ImageTk.PhotoImage(Image.open('D:\School\Minor Project\GUI\images\\PlaceOrder.png'))
    #view cart button def
    def viewCart(cart,segment):
        
        # clearing screen
        for widgets in frame.winfo_children():
            widgets.destroy()
            
        #printing index
        Label(frame, text="Product", bg="#ffffff", fg="#f19849",
                           font=("yu gothic ui", 30, "bold")).place(x=100, y=30)
        Label(frame, text="Price", bg="#ffffff", fg="#f19849",
                           font=("yu gothic ui", 30, "bold")).place(x=500, y=30)
        Label(frame, text="Quantity", bg="#ffffff", fg="#f19849",
                           font=("yu gothic ui", 30, "bold")).place(x=750, y=30)
        Label(frame, text="Total", bg="#ffffff", fg="#f19849",
                           font=("yu gothic ui", 30, "bold")).place(x=1050, y=30)

        #minus button def
        def quantityMinus(cart, product,quantity,segment):
            
            if quantity == 1:
                for products in cart:
                    if products[0] == product:
                        cart.remove(products)
                        break

            else:
                for products in cart:
                    if products[0] == product:
                        products[1] -= 1
                        break

            viewCart(cart,segment)

        #plus button def
        def quantityPlus(cart, product,quantity,segment):
            
            for products in cart:
                if products[0] == product:
                    products[1] += 1
                    break

            viewCart(cart,segment)
            

        #printing cart items
        count=0
        total = 0
        for i in cart:
            
            product=i[0]
            quantity=i[1]

            Label(frame, text=product.name, bg="#ffffff", fg="#f19849",
                           font=("yu gothic ui", 18, "bold")).place(x=100, y=(100+count*40))
            Label(frame, text=str(product.price), bg="#ffffff", fg="#f19849",
                           font=("yu gothic ui", 18, "bold")).place(x=505, y=(100 + count * 40))
            Label(frame, text=quantity, bg="#ffffff", fg="#f19849",
                           font=("yu gothic ui", 18, "bold")).place(x=820, y=(100+count*40))
            Label(frame, text=str(product.price*quantity), bg="#ffffff", fg="#f19849",
                           font=("yu gothic ui", 18, "bold")).place(x=1055, y=(100+count*40))

            total = total + product.price * quantity
            count+=1

        #plus/minus buttons
        if count != 0:
            Button(frame, image=minus_image, relief=FLAT, activebackground="#ffffff", borderwidth=0, background="#ffffff", cursor="hand2",command=lambda:quantityMinus(cart,product,quantity,segment)).place(x=790, y=(110+(count-1)*40))
            Button(frame, image=plus_image, relief=FLAT, activebackground="#ffffff", borderwidth=0, background="#ffffff", cursor="hand2",command=lambda:quantityPlus(cart,product,quantity,segment)).place(x=843, y=(110+(count-1)*40))

        #coupon
        if segment == -1:
            coupon_text = "Coupon: N/A"
        elif segment == 0:
            coupon_text = "Coupon: 15% off on Cosmetics, Clothes, Groceries!"
        elif segment == 1:
            coupon_text = "Coupon: 10% off on Stationery, Electronics, Medicines!"
        elif segment == 2:
            coupon_text = "Coupon: 5% off on Appliances, Vehicles, Toys!"
        
        
        #discount
        discount=0
        if segment == -1:
            discount = 0
        if segment == 0:
            for i in cart:
                product2 = i[0]
                quantity2 = i[1]

                if product2.category == "cosmetics" or product2.category == "clothes" or product2.category == "groceries":
                    discount = discount + int(product2.price*quantity2*0.15)

        elif segment == 1:
            for i in cart:
                product2 = i[0]
                quantity2 = i[1]

                if product2.category == "stationery" or product2.category == "electronics" or product2.category == "medicines":
                    discount = discount + int(product2.price * quantity2 * 0.10)
                    
        elif segment == 2:
            for i in cart:
                product2 = i[0]
                quantity2 = i[1]

                if product2.category == "appliances" or product2.category == "vehicles" or product2.category == "toys":
                    discount = discount + int(product2.price*quantity2*0.05)


        #printing coupon,dicount,grand total
        Label(frame, text=coupon_text, bg="#ffffff", fg="#f19849",
                           font=("yu gothic ui", 18, "bold")).place(x=100, y=410)
        Label(frame, text="Discount:", bg="#ffffff", fg="#f19849",
                           font=("yu gothic ui", 18, "bold")).place(x=930, y=410)
        Label(frame, text=str(discount), bg="#ffffff", fg="#f19849",
                           font=("yu gothic ui", 18, "bold")).place(x=1057, y=410)

        Label(frame, text="Grand Total:", bg="#ffffff", fg="#f19849",
                           font=("yu gothic ui", 30, "bold")).place(x=100, y=440)
        Label(frame, text=str(total-discount), bg="#ffffff", fg="#f19849",
                           font=("yu gothic ui", 30, "bold")).place(x=1055, y=440)        

        
        def PlaceOrder():
            messagebox.showinfo("Order Placed!", "Order Placed!")
            
        Button(frame, image=place_order_image, relief=FLAT, activebackground="#ffffff", borderwidth=0, background="#ffffff", cursor="hand2",command=PlaceOrder).place(x=550, y=490)
        

    #view cart
    view_cart_image=ImageTk.PhotoImage(Image.open('D:\School\Minor Project\GUI\images\\ViewCart.png'))
    view_cart_button = Button(window, image=view_cart_image,
                          font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="#f19849", borderwidth=0, background="#f19849", cursor="hand2",command=lambda:viewCart(cart,segment))
    view_cart_button.place(x=1250, y=85)

          
    window.mainloop()


def loginwindow(window):

    # clearing screen
    for widgets in window.winfo_children():
        widgets.destroy()
        
    login_frame = ImageTk.PhotoImage(Image.open('D:\School\Minor Project\GUI\images\\login_frame.png'))
    image_panel = Label(window, image=login_frame)
    image_panel.pack(fill='both', expand='yes')

    login_img = ImageTk.PhotoImage(Image.open(
        'D:\School\Minor Project\GUI\images\\login2.png'))
    signup_img = ImageTk.PhotoImage(Image.open(
        'D:\School\Minor Project\GUI\images\\signup.png'))

    # login/signup buttons
    login_button = Button(window, image=login_img,
                          font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white", borderwidth=0, background="white", cursor="hand2", command=lambda: loginwindow(window))
    login_button.place(x=495, y=200)

    signup_button = Button(window, image=signup_img,
                           font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white", borderwidth=0, background="white", cursor="hand2", command=lambda: signupwindow(window))
    signup_button.place(x=635, y=200)

    # username
    username_label = Label(window, text="Username ", bg="white", fg="#4f4e4d",
                           font=("yu gothic ui", 13, "bold"))
    username_label.place(x=495, y=255)

    username_entry = Entry(window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                           font=("yu gothic ui semibold", 12))
    username_entry.place(x=530, y=290, width=380)

    # password
    password_label = Label(window, text="Password ", bg="white", fg="#4f4e4d",
                           font=("yu gothic ui", 13, "bold"))
    password_label.place(x=495, y=370)

    password_entry = Entry(window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                           font=("yu gothic ui semibold", 12), show="*")
    password_entry.place(x=530, y=405, width=355)

    def login():
        while(True):
            if username_entry.get() == '':
                messagebox.showerror("Invalid username",
                                     "Please enter a username")
                break
            if password_entry.get() == '':
                messagebox.showerror("Invalid password",
                                     "Please enter a password")
                break
            
            if username_entry.get() == "admin":
                if password_entry.get() != "11":
                    messagebox.showerror("Invalid password",
                                     "Entered password is incorrect")
                    break
                else:
                    admin(window)
            else:
                
                data = sqlite3.connect("D:\\School\Minor Project\\GUI\\NewCustomers.db")
                cursor = data.cursor()
                cursor.execute(
                    "SELECT username FROM customers WHERE username=?", (str(username_entry.get()),))
                username_check = cursor.fetchall()
                cursor.execute(
                    "SELECT isFillSurvey FROM customers WHERE username=?", (str(username_entry.get()),))
                survey_check = cursor.fetchall()
                survey_check=survey_check[0][0]
                if len(username_check) == 0:
                    messagebox.showerror("Invalid Username",
                                        "Username doesnt exist")
                    break
                else:
                    cursor.execute(
                        "SELECT password FROM customers WHERE username=?", (str(username_entry.get()),))
                    password_check = cursor.fetchall()
                    if password_entry.get() != password_check[0][0]:
                        messagebox.showerror(
                            "Incorrect password", "Entered password is incorrect")
                        break
                    else:
                        if survey_check == 0:
                            response = messagebox.askquestion("Survey", "Would you like to fill a survey for a discount coupon?")
                            if response == "yes":
                                survey(window, str(username_entry.get()), cart)
                            else:
                                productScreen(window,str(username_entry.get()),cart)
                        else:
                            productScreen(window, str(username_entry.get()), cart)
                            
                data.commit()
                data.close()
    # login
    login_button = Button(window, image=login_img,
                          font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white", borderwidth=0, background="white", cursor="hand2", command=login)
    login_button.place(x=640, y=450)

    window.mainloop()


def signupwindow(window):

    # clearing screen
    for widgets in window.winfo_children():
        widgets.destroy()

    signup_frame = ImageTk.PhotoImage(Image.open(
        'D:\School\Minor Project\GUI\images\\register_frame2.png'))
    image_panel = Label(window, image=signup_frame)
    image_panel.pack(fill='both', expand='yes')

    login_img = ImageTk.PhotoImage(Image.open(
        'D:\School\Minor Project\GUI\images\\login2.png'))
    signup_img = ImageTk.PhotoImage(Image.open(
        'D:\School\Minor Project\GUI\images\\signup.png'))

    # login/signup buttons
    login_button = Button(window, image=login_img,
                          font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white", borderwidth=0, background="white", cursor="hand2", command=lambda: loginwindow(window))
    login_button.place(x=480, y=160)

    signup_button = Button(window, image=signup_img,
                           font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white", borderwidth=0, background="white", cursor="hand2", command=lambda: signupwindow(window))
    signup_button.place(x=620, y=160)

    # username
    username_label = Label(window, text="Username ", bg="white", fg="#4f4e4d",
                           font=("yu gothic ui", 13, "bold"))
    username_label.place(x=480, y=215)

    username_entry = Entry(window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                           font=("yu gothic ui semibold", 12))
    username_entry.place(x=520, y=250, width=380)

    # password
    password_label = Label(window, text="Password ", bg="white", fg="#4f4e4d",
                           font=("yu gothic ui", 13, "bold"))
    password_label.place(x=480, y=330)

    password_entry = Entry(window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                           font=("yu gothic ui semibold", 12), show="*")
    password_entry.place(x=520, y=365, width=355)

    # re-enter password
    repassword_label = Label(window, text="Confirm Password ", bg="white", fg="#4f4e4d",
                             font=("yu gothic ui", 13, "bold"))
    repassword_label.place(x=480, y=445)

    repassword_entry = Entry(window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                             font=("yu gothic ui semibold", 12), show="*")
    repassword_entry.place(x=520, y=478, width=355)

    def signup():
        while(True):
            if username_entry.get() == '':
                messagebox.showerror("Invalid username",
                                     "Please enter a username")
                break
            if password_entry.get() == '':
                messagebox.showerror("Invalid password",
                                     "Please enter a password")
                break
            if repassword_entry.get() != password_entry.get():
                messagebox.showerror("Password mismatch",
                                     "The passwords don't match")
                break

            try:
                data = sqlite3.connect(
                    "D:\\School\Minor Project\\GUI\\NewCustomers.db")
                cursor = data.cursor()
                cursor.execute("INSERT INTO customers VALUES (:username,:password,:segment,:isFillSurvey)",
                               {"username": username_entry.get(),
                                "password": password_entry.get(),
                                "segment": -1,
                                "isFillSurvey": 0
                                }
                               )
                data.commit()
                data.close()
                messagebox.showinfo("Successful", "Registered successfully!")
                loginwindow(window)
            except sqlite3.IntegrityError:
                messagebox.showerror(
                    "Username already taken", "Please try another username")
                break

    # signup
    signup_button = Button(window, image=signup_img,
                           font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white", borderwidth=0, background="white", cursor="hand2", command=signup)
    signup_button.place(x=615, y=525)

    window.mainloop()


def login_signup(window):

    window.title("Flipcart")
    window.geometry("1366x786")
    window.iconbitmap("D:\School\Minor Project\GUI\images\\logo.ico")
    window.resizable(False, False)
    loginwindow(window)

def survey(window, username,cart):
    
    # clearing screen
    for widgets in window.winfo_children():
        widgets.destroy()

    window.title("Survey")
    window.geometry("1081x606+0+0")
    window.iconbitmap("D:\School\Minor Project\GUI\images\\logo.ico")
    window.resizable(False, False)

    survey_frame = ImageTk.PhotoImage(Image.open('D:\School\Minor Project\GUI\images\\SurveyFrame5.png'))
    image_panel = Label(window, image=survey_frame)
    image_panel.pack(fill='both', expand='yes')

    # name
    name = Entry(window, highlightthickness=0, relief=FLAT, bg="white", fg="#4f4e4d",
                           font=("yu gothic ui semibold", 12,"bold"))
    name.place(x=330, y=162)

    # age
    age = Entry(window, highlightthickness=0, relief=FLAT, bg="white", fg="#4f4e4d",
                          font=("yu gothic ui semibold", 12,"bold"))
    age.place(x=312, y=210)
    
    # gender
    gender = StringVar()
    gender.set("aa")
    Radiobutton(window, variable=gender,value="M",bg="white").place(x=580,y=212)
    Radiobutton(window, variable=gender, value="F", bg="white").place(x=650, y=212)


    # Dependant count
    dep_count = IntVar()
    dep_count.set(6)
    Radiobutton(window, variable=dep_count,value=0,bg="white").place(x=435, y=318)
    Radiobutton(window, variable=dep_count,value=1,bg="white").place(x=480, y=318)
    Radiobutton(window, variable=dep_count,value=2,bg="white").place(x=525, y=318)
    Radiobutton(window, variable=dep_count,value=3,bg="white").place(x=572, y=318)
    Radiobutton(window, variable=dep_count,value=4,bg="white").place(x=619, y=318)
    Radiobutton(window, variable=dep_count, value=5, bg="white").place(x=663, y=318)
    
    # marital status
    mar_status = StringVar()
    mar_status.set("aa")
    Radiobutton(window, variable=mar_status,value="Single",bg="white").place(x=412, y=270)
    Radiobutton(window, variable=mar_status,value="Married",bg="white").place(x=513, y=270)
    Radiobutton(window, variable=mar_status, value="Divorced", bg="white").place(x=624, y=270)
    
    # education level
    education = StringVar()
    education.set("")
    options=["Uneducated", "High School", "College", "Graduate", "Post-Graduate", "Doctorate"]
    OptionMenu(window, education,*options ).place(x=390, y=370)
    

    # income
    inc_cat=StringVar()
    inc_cat.set("")
    options2 = ["Less than $40K", "$40K - $60K", "$60K - $80K", "$80K - $120K", "$120K +"]
    OptionMenu(window,inc_cat,*options2).place(x=650,y=370)
    


    def submit(window,username,cart):

        while (True):
            if name.get() == '':
                messagebox.showerror("Invalid name", "Please enter your name")
                break
            if age.get() == '' or int(age.get()) < 1 or int(age.get()) > 100:
                messagebox.showerror("Invalid age", "Please enter a valid age")
                break
            if gender.get() == "aa":
                messagebox.showerror(
                    "Invalid info", "Please select your gender")
                break
            if dep_count.get() == 6:
                messagebox.showerror(
                    "Invalid info", "Please select a number of dependents")
                break
            if education.get() == "":
                messagebox.showerror(
                    "Invalid info", "Please select your education level")
                break
            if mar_status.get() == "aa":
                messagebox.showerror(
                    "Invalid info", "Please select your marital status")
                break
            if inc_cat.get() == "":
                messagebox.showerror(
                    "Invalid info", "Please select an income category")
                break

            data = sqlite3.connect(
                "D:\\School\Minor Project\\GUI\\NewCustomers.db")
            cursor = data.cursor()
            cursor.execute("INSERT INTO survey VALUES (:name,:age,:gender,:dependant_count,:income_category,:marital_status,:education_level)",
                           {"name": name.get(),
                            "age": age.get(),
                            "gender": gender.get(),
                            "dependant_count": dep_count.get(),
                            "income_category": inc_cat.get(),
                            "marital_status": mar_status.get(),
                            "education_level": education.get()
                            }
                           )
            data.commit()
            data.close()

            pickle_in = open("D:\School\Minor Project\GUI\kproto.pickle", "rb")
            kproto = pickle.load(pickle_in)

            customers = pd.read_csv(
                "D:\School\Minor Project\Codes\customers.csv")

            newCustomer = pd.DataFrame({"Age": [int(age.get())], "Gender": [gender.get()], "Dependent_count": [int(dep_count.get(
            ))], "Education_Level": [education.get()], "Marital_Status": [mar_status.get()], "Income_Category": [inc_cat.get()]})
            customers = customers.append(newCustomer)

            customers_norm = customers.copy()
            scaler = preprocessing.MinMaxScaler()
            customers_norm[['Age', 'Dependent_count']] = scaler.fit_transform(
                customers_norm[['Age', 'Dependent_count']])

            clusters = kproto.predict(customers_norm, categorical=[1, 3, 4, 5])

            labeledCustomers = customers.copy()
            labeledCustomers["cluster"] = clusters

            segment = labeledCustomers['cluster'].iloc[-1]

            data = sqlite3.connect(
                "D:\\School\Minor Project\\GUI\\NewCustomers.db")

            cursor = data.cursor()
            cursor.execute("UPDATE customers SET segment=?,isFillSurvey=1 WHERE username=?", (int(segment),username,))
            
            data.commit()
            data.close()

            messagebox.showinfo(
                "Succesful", "Thank you for taking part in the survey!")

            pickle_in.close()

            productScreen(window,username,cart)

    # submit
    submit_image=ImageTk.PhotoImage(Image.open('D:\School\Minor Project\GUI\images\\Submit2.png'))
    Button(window,image=submit_image,relief=FLAT,activebackground="white", borderwidth=0, background="white", cursor="hand2",command=lambda:submit(window,username,cart)).place(x=450,y=440)


    window.mainloop()

def admin(window):

    # clearing screen
    for widgets in window.winfo_children():
        widgets.destroy()

    window.geometry("1500x750+0+0")
    window.iconbitmap("D:\School\Minor Project\GUI\images\\logo.ico")
    window.resizable(False, False)
    back_img = ImageTk.PhotoImage(Image.open('D:\School\Minor Project\GUI\images\\FlipcartAdminFrame.png'))
    back_image_panel = Label(window, image=back_img)
    back_image_panel.pack(fill='both', expand='yes')
    window.title("Flipcart Admin")

    frame = Frame(window, height=610, width=1300, bg="#ffffff")
    frame.place(x=230, y=200)

    #importing button images
    plots_image = ImageTk.PhotoImage(Image.open('D:\School\Minor Project\GUI\images\\Plots.png'))
    customers_image = ImageTk.PhotoImage(Image.open('D:\School\Minor Project\GUI\images\\Customers.png'))
    coupons_image = ImageTk.PhotoImage(Image.open('D:\School\Minor Project\GUI\images\\Coupons.png'))


    #plot button def
    plot1 = ImageTk.PhotoImage(Image.open('D:\School\Minor Project\GUI\images\\plot1.png').resize((740, 500), Image.ANTIALIAS))
    plot2 = ImageTk.PhotoImage(Image.open('D:\School\Minor Project\GUI\images\\plot2.png').resize((740, 500), Image.ANTIALIAS))
    plot3 = ImageTk.PhotoImage(Image.open('D:\School\Minor Project\GUI\images\\plot3.png').resize((740, 500), Image.ANTIALIAS))
    plot4 = ImageTk.PhotoImage(Image.open('D:\School\Minor Project\GUI\images\\plot4.png').resize((740, 500), Image.ANTIALIAS))
    plot5 = ImageTk.PhotoImage(Image.open('D:\School\Minor Project\GUI\images\\plot5.png').resize((740, 500), Image.ANTIALIAS))
    plots=[plot1,plot2,plot3,plot4,plot5]
    next_image = ImageTk.PhotoImage(Image.open('D:\School\Minor Project\GUI\images\\next.png'))
    prev_image = ImageTk.PhotoImage(Image.open('D:\School\Minor Project\GUI\images\\previous.png'))

    i=0
    def plot(i):

        # clearing screen
        for widgets in frame.winfo_children():
            widgets.destroy()

        def previous(i):
            if i == 0:
                plot(i)
            else:
                i -= 1
                plot(i)

        def next(i):
            if i == 4:
                plot(i)
            else:
                i += 1
                plot(i)

        Label(frame, image=plots[i]).place(x=0, y=0)
        Label(frame,text="Plot "+str(i+1)+"/5",bg="#ffffff",fg="#f19849",font=("yu gothic ui", 14, "bold")).place(x=350,y=505)

        Button(frame, image=prev_image, relief=FLAT, activebackground="#f19849", borderwidth=0, background="#f19849", cursor="hand2", command=lambda:previous(i)).place(x=0, y=505)
        Button(frame, image=next_image, relief=FLAT, activebackground="#f19849", borderwidth=0, background="#f19849", cursor="hand2", command=lambda:next(i)).place(x=610, y=505)


    def customers():

        # clearing screen
        for widgets in frame.winfo_children():
            widgets.destroy()

        Label(frame, text="""Segment 0 : Low Income,
                    Female,
                    Moderate Dependent Count""" , bg="#ffffff", fg="#4c72b0", font=("yu gothic ui", 22, "bold"), justify=LEFT,borderwidth=0).place(x=0, y=0)
        
        Label(frame, text="""Segment 1 : Extreme Ages(Low and High),
                    Mostly Male,
                    Moderate Tncome,
                    Low Depedents
                    Single""" , bg="#ffffff", fg="#dd8452", font=("yu gothic ui", 22, "bold"), justify=LEFT, borderwidth=0).place(x=0, y=130)
        
        Label(frame, text="""Segment 2 : High Income,
                    Male,
                    Middle-Aged,
                    Many Depedents
                    Married""",bg="#ffffff",fg="#55a868",font=("yu gothic ui", 22, "bold"),justify=LEFT,borderwidth=0).place(x=0,y=340)

    
    def coupons():

        # clearing screen
        for widgets in frame.winfo_children():
            widgets.destroy()
            
        Label(frame, text="""Segment 0 : "15% off on Cosmetics, Clothes, Groceries":-
                    Lipstick, Perfume,
                    Shirt, Jeans,
                    Sugar, Apples, Rice""" , bg="#ffffff", fg="#4c72b0", font=("yu gothic ui", 22, "bold"), justify=LEFT,borderwidth=0).place(x=0, y=0)
        
        Label(frame, text="""Segment 1 : "10% off on Stationery, Electronics, Medicines":-
                    Notebooks, Pens,
                    Phone, Laptop,
                    Painkillers, Vaccine""" , bg="#ffffff", fg="#dd8452", font=("yu gothic ui", 22, "bold"), justify=LEFT, borderwidth=0).place(x=0, y=170)
        
        Label(frame, text="""Segment 2 : "5% off on Appliances, Vehicles, Toys":-
                    Refrigerator, Air Conditioner, Microwave Oven,
                    Car, Bike,
                    Rc Car, Nerf Gun""",bg="#ffffff",fg="#55a868",font=("yu gothic ui", 22, "bold"),justify=LEFT,borderwidth=0).place(x=0,y=350)



    Button(window, image=plots_image, relief=FLAT, activebackground="#f19849", borderwidth=0, background="#f19849", cursor="hand2",command=lambda:plot(i)).place(x=50, y=300)
    Button(window, image=customers_image, relief=FLAT, activebackground="#f19849", borderwidth=0, background="#f19849", cursor="hand2",command=customers).place(x=50, y=450)
    Button(window, image=coupons_image, relief=FLAT, activebackground="#f19849", borderwidth=0, background="#f19849", cursor="hand2",command=coupons).place(x=50, y=600)

    window.mainloop()


login_signup(window)
