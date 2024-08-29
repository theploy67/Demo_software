#print('Hello, World!')
#print('"ITDS120 Fundamentals of Programming" is fun and easy')
#print('like "1+1=2"')

#base = float(input())
#height = float(input())
#print((0.5)*base*height)

# x1 = float(input())
# x2 = float(input())
# x3 = float(input())
# print(f"The average is {(x1+x2+x3)/3}")

#kW = float(input())
#hr = float(input())
#print(round (kW*60/100,2))

#hr = int(input())
#if hr <= 40 :
#    print(hr*50)
#else :
# print(2000+((hr-40)*75))

#capacity= float(input())
#charge_rate = float(input())
#print(capacity/charge_rate)
#print(round(capacity*4.5,2))

#F = float(input())
#C = ((F-32)/9)*5
#print(f'{round(F,2)} is equal to {round(C,2)}C')

#a = int(input())
#b = int(input())
#print(f'{a} divided by {b} is {a//b} with {a%b} as remainders')

#hr = int(input())
#hh = hr//60
#mm = hr%60
#print(f'{hh}:{mm}')

#x1 = float(input())
#y1 = float(input())
#x2 = float(input())
#y2 = float(input())
#m = (y2-y1)/(x2-x1)
#print(f'This slope is {round(m,2)}')

#hr = int(input())
#x=0
#if hr<=40:
#    print(hr*50)
#else:
#   print(2000+(hr-40)*75)
'''
x = int(input())
if x>0 :
    print(f'x is positive')
else:
    print(f'x is not positive')

if x%3==0 and x%7==0:
    print(f'x is divisible by 3 and 7')
else:
    print(f'x is not divisible by 3 and 7')

if x%10==1:
    print(f'x is ending with 1')
else:
    print(f'x is not ending with 1')
'''
''''
a = float(input())
b = float(input())
c = float(input())

if a==0 or b==0 or c==0:
    print(f'Invalid triangle')
elif a+b>c and a+c>b and b+c>a:
     print(f'Invalid triangle')

if a==b and b==c and c==a:
      print(f'Equilateral')
elif a==b or b==c or a==c :
     print(f'Isosceles')
elif a!=b and b!=c and c!=a:
     print(f'Scalene')
else:
     print(f'Valid triangle')

total = 50.00
member = input()
size = input()
topping = input()

if size =='L' :
    total=total+10

if topping =='N':
    total=total-10

if member =='Y':
    print(f'Total price: {total-(total*0.1)}')

if member =='n':
    print(f'Total price: {total}')
'''