#WAP TO STORE 7 FURITS IN A LIST ENTERED BY USER AND PRINT THE LIST IN REVERSE ORDER.
fruits=[]


f1=input("Enter fruit 1: ")
fruits.append(f1)
f2=input("Enter fruit 2: ")
fruits.append(f2)
f3=input("Enter fruit 3: ")
fruits.append(f3)
f4=input("Enter fruit 4: ")
fruits.append(f4)
f5=input("Enter fruit 5: ")
fruits.append(f5)
f6=input("Enter fruit 6: ")
fruits.append(f6)
f7=input("Enter fruit 7: ")
fruits.append(f7)

print(fruits)

reverse_fruits=fruits[::-1]
print(reverse_fruits)

#WAP TO ACCEPT MARKS OF 6 STUDENTS AND DISPLAY THEM IN A SORTED MANNER.
Marks=[]

m1=int(input("Enter marks of student 1: "))
Marks.append(m1)
m2=int(input("Enter marks of student 2: "))
Marks.append(m2)
m3=int(input("Enter marks of student 3: "))
Marks.append(m3)
m4=int(input("Enter marks of student 4: "))
Marks.append(m4)
m5=int(input("Enter marks of student 5: "))
Marks.append(m5)
m6=int(input("Enter marks of student 6: "))
Marks.append(m6)

print(Marks)
Marks.sort()
print(Marks)

#WAP to sum a list with 4 numbers entered by user and print the sum.
numbers=[]
n1=int(input("Enter number 1: "))
numbers.append(n1)
n2=int(input("Enter number 2: "))   
numbers.append(n2)
n3=int(input("Enter number 3: "))
numbers.append(n3)
n4=int(input("Enter number 4: "))
numbers.append(n4)
print(numbers)
sum=sum(numbers)
print("The sum of the numbers is: ",sum)

#Problem 4: WAP TO COUNT THE NUMBER OF ZEROS IN THE FOLLOWING TUPLE: a=[7,0,8,0,0,9)

a=(7,0,8,0,0,9)
zero_count=a.count(0)
print("The number of zeros in the tuple is: ",zero_count)       
