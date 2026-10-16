x = int(input("enter a number: "))
temp = x
power = len(str(x))
total = 0
while temp>0:
    digts = temp%10
    total += digts**power
   # print (digts)
    temp //=10

if (x == total):
    print ("This is armstrong number")
print(total)
