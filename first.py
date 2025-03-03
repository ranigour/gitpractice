i=1
n=int(input("enter the num:"))
fact=1
sum_fact=0
while(i<=n):i
if(i%2==0):
    sum_fact=sum_fact-fact*i
else:
  sum_fact=sum_fact+fact*i
i+=1 
print(sum_fact)
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
print("pizza: Rs50/n chai: Rs40/n partha:30: Rs30/n coffe: Rs80/n burger: Rs60/n ")