from beautifultable import BeautifulTable
table = BeautifulTable()
from datetime import datetime
from win32com.client import Dispatch
def speak(str):
    spk = Dispatch('SAPI.spvoice')
    spk.speak(str)

table.column_headers=["Dish","Total Price"]
List=[]
sum=0.0

print("\t______________________")
print("\t    Apna Restaurent")
print("\t______________________\n")
speak("Welcome to Apna Restaurent")
speak("Please select menu type")
b=bool(1)
while b:
 print("\t\t\tMenu")     #display main menu
 print("\t***********************")
 print("""\t 1.Starter Menu
         2.Main Course
         3.Dessert
         4.Billing""")
 print("\t***********************\n")
 sel=int(input("Enter your choice : "))
 if sel==1:
    speak("Please select starter food")
    print("\t**********************************************")      #display starter menu
    print("""\t
             1.Peanut Chat          Rs.60.00
             2.Chilli Paneer        Rs.90.00
             3.French Fries         Rs.100.00
             4.Vegetable Soup       Rs.50.00
             """)
    print("\t***********************************************\n")

    ch=int(input("Select Starter Food : "))
    if ch==1:
        name="Peanut Chat"
        q=int(input("Enter Quantity : "))
        t=60.00*q
    elif ch==2:
        name = "Chilli Paneer"
        q = int(input("Enter Quantity : "))
        t = 90.00 * q
    elif ch==3:
        name = "French Fries"
        q = int(input("Enter Quantity : "))
        t = 100.00 * q
    elif ch==4:
        name = "Vegetable Soup"
        q = int(input("Enter Quantity : "))
        t = 50.00 * q
    else:
        print("Item Not Available!")
    list1=[name,t]        #save name and price value in list
    table.append_row(list1)     #append the list items in table
    List.append(t)        #append the price value in list
 elif sel==2:
    speak("select main course menu")
    b1=bool(1)
    while b1:
     print("\t\t\t1.Veg Menu\t\t2.Non-Veg Menu\t\t3.Roti\t\t4.Main Menu")     #display main course menu
     ch=int(input("Enter choice : "))
     if ch==1:
         speak("Please select Veg Food")
         print("\t**********************************************")         #display veg menu
         print("""\t
		     1.Shahi-Paneer             Rs.150.00
                     2.Dal Fry                  Rs.110.00
                     3.Kadai Paneer             Rs.140.00
                     4.Masala Bhindi            Rs.90.00""")
         print("\t***********************************************\n")

         ch = int(input("Select Veg Sabji : "))
         if ch == 1:
            name = "Shahi Paneer"
            q = int(input("Enter Quantity : "))
            t = 150.00 * q
         elif ch == 2:
            name = "Dal Fry"
            q = int(input("Enter Quantity : "))
            t = 110.00 * q
         elif ch == 3:
            name = "Kadai Paneer"
            q = int(input("Enter Quantity : "))
            t = 140.00 * q
         elif ch == 4:
            name = "Masala Bhindi"
            q = int(input("Enter Quantity : "))
            t = 90.00 * q

         else:
            print("Item Not Available!")
         list2 = [name, t]
         table.append_row(list2)
         List.append(t)
     elif ch == 2:
            speak("Please select Non-Veg Food")
            print("\t**************************************************************")    #display non-veg menu
            print("""\t
		     1.Chicken Curry                 Rs.250.00
                     2.Egg Curry                     Rs.120.00
                     3.Chicken Tikka                 Rs.200.00
                     4.Mutton Curry                  Rs.300.00""")
            print("\t**************************************************************\n")

            ch = int(input("Select Non-Veg Sabji : "))
            if ch == 1:
                name = "Chicken Curry"
                q = int(input("Enter Quantity : "))
                t = 250.00 * q
            elif ch == 2:
                name = "Egg Curry"
                q = int(input("Enter Quantity : "))
                t = 120.00 * q
            elif ch == 3:
                name = "Chicken Tikka"
                q = int(input("Enter Quantity : "))
                t = 200.00 * q
            elif ch == 4:
                name = "Mutton Curry"
                q = int(input("Enter Quantity : "))
                t = 300.00 * q
            else:
                print("Item Not Available!")
            list3 = [name, t]
            table.append_row(list3)
            List.append(t)

     elif ch==3:
         speak("Please select Roti")
         print("\t\t*****************************************************************")  #display roti menu
         print("""\t 
			      1.Plain Roti                      Rs.7.00
                              2.Butter Roti                     Rs.12.00
                              3.Butter Nan                      Rs.10.00
                              4.Roomali Roti                    Rs.15.00""")
         print("\t\t*****************************************************************\n")

         ch = int(input("Select Roti : "))
         if ch == 1:
             name = "Plain Roti"
             q = int(input("Enter Quantity : "))
             t = 7.00 * q
         elif ch == 2:
             name = "Butter Roti"
             q = int(input("Enter Quantity : "))
             t = 12.00 * q
         elif ch == 3:
             name = "Butter Nan"
             q = int(input("Enter Quantity : "))
             t = 10.00 * q
         elif ch == 4:
             name = "Roomali Roti"
             q = int(input("Enter Quantity : "))
             t = 15.00 * q
         else:
             print("Item Not Available!")
         list4 = [name, t]
         table.append_row(list4)
         List.append(t)

     elif ch==4:
         b1=bool(0)

     else:
         print("Invalid Choice!")
 elif sel==3:
     speak("Please select Dessert Food")
     print("\t*********************************************************")     #display dessert menu
     print("""\t
		 1.Gulab Jamun              Rs.15.00
                 2.Ras Gulla                Rs.20.00
                 3.Ras Malai                Rs.30.00
                 4.Halwa                    Rs.50.00
                 """)
     print("\t*********************************************************\n")

     ch = int(input("Select Dessert Food : "))
     if ch == 1:
         name = "Gulab Jamun"
         q = int(input("Enter Quantity : "))
         t = 15.00 * q
     elif ch == 2:
         name = "Ras Gulla"
         q = int(input("Enter Quantity : "))
         t = 20.00 * q
     elif ch == 3:
         name = "Ras Malai"
         q = int(input("Enter Quantity : "))
         t = 30.00 * q
     elif ch == 4:
         name = "Halwa"
         q = int(input("Enter Quantity : "))
         t = 50.00 * q
     else:
         print("Item Not Available!")
     list5 = [name, t]
     table.append_row(list5)
     List.append(t)

 elif sel==4:
     b=bool(0)
 else:
     print("Please enter valid choice!")

speak("Your Bill")
print("  ******** YOUR BILL ********")    #bill generation
print(table)
for i in List:
    sum=sum+i
print("_______________________________")
print("\tTotal\t\t ",sum)
print("_______________________________")
print("_______________________________")
print(" ",datetime.now())                 #print date and time
print("_______________________________")
print("\t THANK YOU")
speak("Thank you for come in Apna Restaurent")






