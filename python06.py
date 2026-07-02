# Q6 - Print the sum of all even & odd numbers in a range
#      separately






n = int(input("enter your number"))

even = 0
odd = 0
for i in range(1,n+1):
    if i%2 == 0:
        even = even + i
    else:
        odd = odd + i
        
print(f"your even and odd sum are {even} , {odd}")




    


#  Q7- Print all the factors of a number





n = int(input("which number factors you want"))

for i in range(1,n+1):
    if n%i == 0:
        print(i)








    

#    Q8- Accept a number and check if it a perfect number or not.
#        (A number whose sum of factors is equal to the number itself)
#         example 6 = 1+2+3






n = int(input("check your number is perfect or not"))

sum = 0
for i in range(1,n):
    if n%i == 0:
        sum = sum + i

if sum == n:
    print("your number is perfect")
else:
    print("not a perfect number")




#Q9- Check wether the number is prime or not


n = int(input("check your number is prime or not :"))

count = 0

for i in range(1,n+1):
    if n%1 == 0:
        count = count + 1

if count == 2:
    print("your number is prime")
else: 
    print("your number is not prime")


#  Q10-Reverse a string without using in build functions.


a = "ASHISH"

print(a[::-1])

# USING FOR LOOP

a = "ASHISH"
b = ""
for i in range(len(a)-1,-1,-1):
    b = b + a[i]
   
print(b)



# Q11- Check string is Pallindrome or not





a = "naman"
b = ""
for i in range(len(a)-1,-1,-1):
    b = b + a[i]
   
if b == a:
    print("your string is paliandrome")
else:
    print("its not a paliandrome")



# Q12 Count all letters, digits, and special symbols from a given
#     string

a = "ASHISH"

char = 0
alpha = 0
dig = 0

for i in a:
    if i.isdigit():
        dig +=1
    elif i.isalpha:
        alpha +=1
    else:
        char +=1
print(f"{alpha} alphabet,{char} character,{dig} digits")
