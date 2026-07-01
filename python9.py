#            Data Structures
           
           
#            1.In-build data structures



#            Data structures are used to store, organize, and manipulate
#            data efficiently. Python provides several built-in data
#            structures.
            
            
#            Now in python we have 4 types of in-build data structure
#            List, Tuple, Dictionary, Set.






#            A.List



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

