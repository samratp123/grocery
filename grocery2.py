
a = "Hello!"
b = input("What's your name?")
print(a, b)
c = (input("Do you want to buy somethoing?"))
list=[]
y=[]
if c == ("yes"):
    d=("""
    Welcome to our Shop_Basket
----------------------------------
1. Rice
2. Mustard Oil
3. Soap
4. Toothpaste
5. Detergent
6. Shampoo

""")
    print(d)
    def main():
        item = int(input("Enter the Product number which you want to buy: "))
        if item == 1:
            Product ={
                'Basmati': 'Rs.100 per_kg',
                'Lalbaba': 'Rs.90 per_kg',
                'Dawat': 'Rs.85 per_kg'

            }
            print(Product)
            a=(input("Choose your Product_Brand: "))

            x= int(input("Enter your quantity:"))

        elif item == 2:
            Product = {
                'Emami': 'Rs.180',
                'Fortune': 'Rs.185',
                'Dhara': 'Rs.160',
            }
            print(Product)
            a=(input("Choose your Product_Brand: "))
            x = int(input("Enter your quantity:"))

        elif item == 3:
            Product = {
                'Lifebuoy': 'Rs.30',
                'Lux': 'Rs.40',
                'Dettol': 'Rs.35',
                'Wild_Stone': 'Rs.50',
            }
            print(Product)
            a=(input("Choose your Product_Brand: "))

            x = int(input("Enter your quantity:"))

        elif item == 4:
            Product = {
                'Colgate': 'Rs.92',
                'Pepsodent': 'Rs.80',
                'Dabur_red': 'Rs.88',
                'Close_up': 'Rs.95',
            }
            print(Product)
            a=(input("Choose your Product_Brand: "))

            x = int(input("Enter your quantity:"))

        elif item == 5:
            Product = {
                'Sunlight': 'Rs.83',
                'Tide': 'Rs.100',
                'Surf_Excel': 'Rs.120',
                'Wheel': 'Rs.45',
            }
            print(Product)
            a=(input("Choose your Product_Brand: "))

            x = int(input("Enter your quantity:"))

        elif item == 6:
            Product = {
                'head&shoulders': 'Rs.85',
                'Dove': 'Rs.98',
                'Loreal': 'Rs.95',
                'Sunsilk': 'Rs.55',
            }
            print(Product)
            a=(input("Choose your Product_Brand: "))

            x = int(input("Enter your quantity:"))
        a = eval(input('calculate your product price:'))        #manually calcuation
        print(a)
        Repeat=input('Do you want to buy something else?')
        list.append(item)
        y.append(a)

        if Repeat=='yes':
            main()

        else:
            print("your final products are:", list)
            print("your total amount:",y)
            print('THANK YOU VISIT AGAIN!')
            exit()
    main()
else:
    c=="no"
    print("THANK YOU")


