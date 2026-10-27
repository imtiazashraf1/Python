friends=["Ashraf","Orange","Mango","Banana",5,3.785,False,True]

print(friends[7])
friends[0]="Imtiaz"
print(friends)
print(friends[0]) # So, list is mutable, we can change the value of list.however, we can not change the size of list. We can add or remove elements from list but we can not change the size of list.
print(friends[1:6]) #And string is immutable, we can not change the value of string. We can only create a new string with the new value.
friends.append("Imtiaz") #We can add new element to the list using append() method.
print(friends)
friends.extend(["Imtiaz","Ashraf"]) #We can add multiple elements to the list using extend() method.
print(friends)
friends.remove("Mango") #We can remove an element from the list using remove() method.
print(friends)

friends.insert(2,"Mango") #We can add an element to the list at a specific index using insert() method.
print(friends)  
friends.pop(1) #We can remove an element from the list using pop() method. It removes the element at the specified index.
print(friends)      
#friends.clear() #We can remove all elements from the list using clear() method.
#print(friends) 
friends.reverse()
print(friends) #We can reverse the order of elements in the list using reverse() method.


L1= [1,65,8,98,4,76,567.89,8,-7]  
L1.sort() #We can sort the elements of the list in ascending order using sort() method.
print(L1)
L1.reverse() #We can reverse the order of elements in the list using reverse() method.
print(L1)
L1.sort(reverse=True) #We can sort the elements of the list in descending order using sort() method with reverse=True parameter.
print(L1)
L1.remove(8) #We can remove an element from the list using remove() method.
print(L1)
L1.insert(3,333) #We can add an element to the list at a specific index using insert() method.
print(L1)
L1.pop(5) #We can remove an element from the list using pop() method. It removes the element at the specified index.
print(L1)

