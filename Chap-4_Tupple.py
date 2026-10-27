a=(1,45,876,3467,False,True,"Ashraf",45)

no=a.count(45) 
print(no) #We can count the number of occurrences of an element in a tuple using count() method.  
repeated=a.index(45)
print(repeated) #We can find the index of an element in a tuple using index() method. It returns the index of the first occurrence of the element. If the element is not found, it raises a ValueError.
repeated=a*3
print(repeated) #We can repeat the elements of a tuple using * operator. It returns a new tuple with the elements repeated the specified number of times.

print(1 in a) #We can print the elements of a tuple using print() function. It returns the elements of the tuple in the order they were defined.
print(2 in a) #We can check if an element is present in a tuple using in operator. It returns True if the element is present, otherwise it returns False.

print(min(a)) #We can find the minimum value in a tuple using min() function. It returns the smallest element in the tuple.
print(max(a)) #We can find the maximum value in a tuple using max() function.
print(sum(a)) #We can find the sum of all elements in a tuple using sum() function. It returns the sum of all elements in the tuple
print(len(a)) #We can find the length of a tuple using len() function. It returns the number of elements in the tuple.
slice=a[1:5] #We can slice a tuple using slicing operator. It returns a new tuple with the elements from the specified start index to the specified end index.
print(slice) #We can print the elements of a tuple using print() function. It returns

my_tuple=(1,2,3)
a,b,c=my_tuple #We can unpack a tuple using unpacking operator. It assigns the values of the tuple to the variables in the order they were defined.
print(a,b,c) #We can print the values of the variables using print() function. It returns the values of the variables in the order they were defined.
#Ans is 1 2 3

