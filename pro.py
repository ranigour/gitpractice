menu={
    'pizza':50,
    'chai':40,
    'partha':30,
    'coffe':80,
    'burger':60,
}
print(menu)
#greet
print("welcome to rani hotel")
print("pizza: Rs50\nchai: Rs40\npartha: Rs30\ncoffe: Rs80\nburger: Rs60\n ")
order_total=0
item_1=input("Enter the name of item you want to order=  ")
if item_1 in menu:
    order_total+= menu[item_1]
    print(f"your item{item_1} has been  added your order")
else:
    print(f"order item{item_1}is not available yet!")
    
    another_order =input("do you want add another item ?(yes/no)")
    
    if another_order == "Yes":
       item_2 =input("enter the name of second item=")
       if item_2 in menu:
             order_total+=menu[item_2]
             print(f"item{item_2}has been added to order")
    else:
             print("ordered item{item_2}is not available!")
             print(f"the total amount of item to pay is{order_total}")
             
  