#            Data Structures
           
           
#            1.In-build data structures



#            Data structures are used to store, organize, and manipulate
#            data efficiently. Python provides several built-in data
#            structures.
            
            
#            Now in python we have 4 types of in-build data structure
#            List, Tuple, Dictionary, Set.






#           -----------------{1}.List----------------------





#      Before starting we need to understand some of the
#      terminology.


    
#      MUTABLE -
#               Mutability refers to whether an object's value
#      can be changed after creation. And List allows this.
     
      
#      DUOLIATES- 
#               we know data structures are used to store
#      multiple values so duplicates means same value occuring
#      multiple time. List allows this.
     
     
#      ORDERED- 
#              List maintains ordered data structure maintains
#      the sequence of elements as they were inserted. This
#      means you can access elements using their position
#      (index).
      
      
#      HETEROGENOUS-
#                  List have heterogenous nature that means
#      we can have multiple data types inside the list.




#      List Basics

#      syntax of list

a = [1,2,3,3.2,2.6,43.3]

#      list has Indexing and slicing and it is same as string

# 1st way using index

for i in range(len(a)): 
    print(a[i])

# 2nd way directly on values

for i in a:
    print(i)





#     List Traversing and methods



#    list traversing is also similar to string traversing it can
#    be looped using the index values and directly7




#    some of the examples of the methods



n = [1,2,3,4,5]






#1. append() - to add a number in list


n.append(6)  # it will add 6 in list

print(n)











#2. insert(x,y) - inserts y at index x


n.insert(6,7)

print(n)








#3. extend(x,y,z)- adds multiple elements at the end


n.extend([8,9,10])

print(n)







#4 remove(x)- remove the first occurrence of x




n.remove(5)

print(n)








#     popped_item = numbers.pop (3) # Removes and stores the element at index 3
#                 Removes an item using its index and returns it.

n.pop(0)

print(n)








#     index numbers.index(6) # Finds the index of 6


position = n.index(3)

print(f"the index of 3 is {position}")






#     count()-  Counts how many times a value appears.
#     count_5 = numbers.count(5) # Counts occurrences of 5

a = [2,2,2,2,2,1,12,23,3,1]

c = a.count(2)

print(f"occurrences of 2 is {c}")










#     numbers.sort() # Sorts the list in ascending order
#     Sorts the original list in ascending order (smallest to largest)

l = [8,7,6,5,4,3,2,1,0]

l.sort()

print(l)











#     numbers.reverse() # Reverses the list order
#     Simply reverses the current order.


l = [1,2,3,4,5,6,7,8,9]

l.reverse()

print(l)







#     new_numbers = numbers.copy() # Creates a copy of the list
#                  Creates a new list with the same elements.


l = [1,2,3,4,5,6,7,8,9]



new_list = l.copy()

print(new_list)








#     numbers.clear() # Removes all elements from the list



l = [1,2,3,4,5,6,7,8,9]

l.clear()

print(l)



#  Some Questions on List



# Q1 Print positive and negative elements of an List?



l = [1,2,-2,-3,5,-7]

print("POSITIVE ELEMENTS ARE ")
for i in l:
    if i >= 0:
        print(i)

print("NEGSTIVE ELEMENTS ARE ")
for i in l:
    if i < 0:
        print(i)






# Q2  Mean of List elements?

l = [2,23,23,4,34,5,465,567,34,34]


sum = 0

for i in l:
    sum = sum + i

print(sum/len(l))










# Q3  Find the greatest element and print its index too.

l = [12,2,3,34,54,74,6]

largest = 0
index = 0

for i in range(len(l)):
    if l[i] > largest:
        largest = l[i]
        index = i

print(f"largest number is {largest} and its index is {index}")







# Q4  Find the second greatest element?




l = [12,2,3,34,54,74,6]

largest = l[0]
sec_largest = l[0]

for i in l:
    if i >= largest:
        sec_largest = largest
        largest = i
    elif i > sec_largest:
        sec_largest = i

print(f"{sec_largest},{largest}")
    








# Q5 6 Check if List is sorted or not.


l = [1,2,3,4,5,6,7,8,9,]


for i in range(len(a)):
    if a[i] < a[i+1]:
        continue
    else:
        print("your list is not sorted")
        break

else:
    print("your list is shorted")





#       ----------------------{2}.Tuple------------------

 




#                        Tuple Powers



# syntax    t = (1,2,3,4,5,6)


#         IMMUTABLE - Tuples are not mutable you cannot change
#         the values of tuple
         
         
#         DUPLICATES - You can have duplicate values in tuple there
#         are no restriction
         
         
#         ORDERED - Set are ordered and you can access them
#         through index values
         
         
#         HETEROGENOUS- Set also have heterogenous nature and
#         can have different types of data structure in tuple.





#         Tuple Traversing and methods




#         Tuples are traversed in the same manner as List are
#         traversedQ#         

#         But remember tuples are like strings you can’t change
#         anything once it’s made we can’t change them.K





#         Methods of tuple are:



#         1.index = t.index(x) ------> find the index of first occurrence of x




t = (1,2,3,4,5,6)

index = t.index(5)
print(index)






#         2.count = t.count(x) ------> counts occurrences of x

t = (1,5,2,3,4,5,6)

count = t.count(5)

print(count)




#           tuple unpacking

a,b,c,d = (1,2,3,4)

print(a) 





#        ----------{3}.Set-------------------


#        SYNTAX

a = {1,2,3,4,23,234,}








#         Set Powers


#         terminology



#        MUTABLE -
#                 Sets are mutable you can change the values of
#                 set.


#        DUPLICATES - 
#                     You cannot have any duplicate values in set
#                     that means every element will be unique.


#        UNORDERED-
#                   Sets are unordered and you cannot access
#                   them through index values.


#        HETEROGENOUS -
#                      Set is semi-heterogenous it can store
#                      some data types like string, numbers, tuples but not
#                      everything




#           How Set stores value in python

#          Each value in a set is hashed using a hash function (hash() in
#          Python)


#          The hash is used as an index to store the element in memory


#          Since hashing does not maintain order, sets are unordered


#          Only immutable (hashable) objects can be stored in a set
#          (e.g., numbers, strings, tuples). Mutable objects like lists and
#          dictionaries are not allowed.


#          Set Traversing


#          A set cannot be traversed using the index values cause it is
#          unordered and has no index.
#          So many times it will give random values.




#          Set methods

#          Now set methods are very powerful cause you don’t have
#          any indexing you cannot change the values but set is
#          mutable so we use methods for this.



#          For adding and removing the elements you can use methods
#          as follows-




#          1. add(x) - # Adds an element to the set

s = {1,2,3,12,321,12}

s.add(122)

print(s)



#          2. remove(x) - # Removes x (Raises an error if not found)




s = {1,2,3,4,5}

s.remove(2)

print(s)





#          3. discard(x) - # Removes 5 (No error if not found)


s = {1,2,3,4,5,6}

s.discard(5)

print(s)

#          4.pop() -   #Removes a random element

s = {1,3,5,4,2,3}

s.pop() 

print(s)


#          5.clear() # Removes all elements


s = {1,4,2,3,5,3}

s.clear()

print(s)


#          Now these are some of the basic methods but sets also have
#          some special methods for performing some special
#          operations between 2 sets.

#          for example we have

A = {1,2,3}
B = {3,4,5}


#          1. union_set = A.union (B) 

union = A.union(B)

# OR

print( A | B)  # Union

print(union)







#          2. intersection_set = A. intersection (B) 

intersection = A.intersection(B)

# OR

print(A & B)   # Intersection


print(intersection)










#          3. difference_set = A.difference (B) 

difference = A.difference(A)

# OR

print(A - B)   # Difference


print(difference)









#          4. symmetric_diff = A.symmetric_difference (B) 

symmetric_diff = A.symmetric_difference(B)

# OR

print(A ^ B)


print(symmetric_diff)





#   ----------- [4]. Dictionary --------------------




#        Dictionary Powers

#        terminology

#        MUTABLE -
#                Dictionaries are mutable, meaning you can
#                change, add, or remove key-value pairs after creation.



#        DUPLICATES -
#                   Keys must be unique, but you can have
#                   duplicates in values.


#       ORDER -
#              Dictionary follows insertion order.( keys act as index)



#       HETEROGENEOUS -
#                      A dictionary can store different types of
#                      keys and values, like integers, strings, lists, or even
#                      another dictionary.



#       Dictionary syntax and working

#       we have to use key and value pairs to store
#       values in dictionary.

#       the keys in dictionary acts like index values that we use
#       in List.

#       EXAMPLE
       
d = {1:12,2:13,3:14,4:15}
#    ^ ^
#  KEY VALUE

print(d[2]) # ----> OUTPUT 13

student = {"name":"ashish","age":20}

print(student["name"])   #OUTPUT ashish




#         Again telling we can perform CRUD(create, read, update,
#         delete) operations on values but not all on keys cause the
#         keys cannot be changed after creation.


d = {10:100,20:200,30:300}

d[10] = 100 #Updating
d[50] = 500 #Creating
del d[30]   #deleting

print(d)




  

#     Dictionary traversing


#     We can traverse both keys and values in dictionary, but
#     default loop is set on keys and you can access the values
#     because of keys.
     
#     So technically you can traverse on both keys and values at
#     the same time.



d = {10:100,20:200,30:300}

for i in d:
    print(d[i])

# OR

for i in d.values():
    print(i)




#              Dictionary methods


#      Method         | Purpose                                                 |
#      -------------- | ------------------------------------------------------- |
#      `clear()`      | Removes all items                                       |
#      `copy()`       | Creates a copy of the dictionary                        |
#      `fromkeys()`   | Creates a dictionary from given keys                    |
#      `get()`        | Gets a value safely (no `KeyError`)                     |
#      `items()`      | Returns all key-value pairs                             |
#      `keys()`       | Returns all keys                                        |
#      `values()`     | Returns all values                                      |
#      `pop()`        | Removes a specified key                                 |
#      `popitem()`    | Removes the last inserted key-value pair                |
#      `setdefault()` | Returns value or inserts a new key with a default value |
#      `update()`     | Adds or updates key-value pairs                         |



#     Dictionary Questions

#  Q1. Write a Python script to merge two Python dictionaries?


d1 = {10:100,20:200,30:300}
d2 = {40:400,50:500,60:600}

for i in d2:
    d1[i] = d2[i]
 
print(d1)



#  Q2.Write a Python program to sum all the values in a dictionary?

d = {10:100,20:200,30:300}

sum = 0

for i in d:
    sum = sum + d[i]

print(sum)




#  Q3.Count the frequency of each element in list through dictionary

a = [1,2,2,3,3,4,4,4,4,5,6,7,8,9,10]

d = {}

for i in a:
    if i in d.keys():
        d[i] += 1
    else:
        d[i] = 1


print(d)