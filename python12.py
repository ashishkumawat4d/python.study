#             OOPS IN PYTHON




#             What is OOPS
             
#             OOPS (Object-Oriented Programming System) is a
#             programming paradigm based on the concept of "objects",
#             which can contain data (attributes) and code (methods).




#             CLASSES in OOPS


#             A class is like a blueprint or template for creating objects.


#             Syntax of class
    

#             A class is also created with a basic keyword class and a name
#             in front of it.

#             EXAMPLE:

class  Car:
    brand = "BMW" 
    


#            There are 2 types of things inside class Attributes and
#            Methods.


#            1.Attributes - Variables defined inside the class are Attribute.

#            2.Methods - Functions defined inside a class are Methods.



#            EXAMPLE:

class Animal:

    species = "dog"  # Attribute

    def make_sound(self):     # Method
        print("Bark!") 






#            Accessing attributes and methods





#            A class is initialised only one time when we first run the
#            program. and for accessing the attributes and methods we
#            have to first access the class and then attributes and
#            methods.


class Animal:
    type = "cat"  #  Attribute


    def sound(self):   # Method
        print("Meow!")

# DIrectly accessing attribute and method using the class

print(Animal().type)     # Access attribute
Animal().sound()       # Call method





#              Objects in OOPS-

#              An object is a real-world entity or an instance of a class that contains data (attributes) and behavior (methods).

#              EXAMPLE

class factory:
    a = 12 

    def hello(self):
        print("how are you ")

obj = factory()

obj2 = factory()

obj3 = factory()

print(obj.a)

obj.hello()






#                Constructor




#              A constructor is a method that runs automatically when we
#              call a class and this constructor function will target the
#              objects location.

 



#              A constructor is a special method named __init__().
                 
#              It is called automatically when an object is created.
                
#              It is used to initialize object attributes.
                 
#              Every class can have one __init__() method.
                 
#              The first parameter is always self.
                 
#              Constructors can take additional parameters or none at all.







class Animals:
    def __init__(self,species,height,sound):
        
      self.species = species   #  self targets the location of object
      self.height = height
      self.sound = sound

    def show(self):
        print(f"your object details are {self.species},{self.height},{self.sound}")

dog = Animals("DOG",30,"Bark!")

cat = Animals("Cat",20,"MEOW!")

print(dog.sound)

dog.show()














#             ---------   Attributes and Methods    ----------------
       
       
       
#                          Types of Attribute
       
       
       
       
#           1.CLASS ATTRIBUTE
#                            -A normal variable created inside a class is
#                           is a class attribute.




#          Example:





class car:
    brand = "BMW"  #<-------- Class attribute















#         2.INTANCE ATTRIBUTE -
#                                A attribute created using an instance like
#                                self.name, self.age etc. It is known as
#                                instance attribute.


#          Example:






class car:
    def __init__(self,brand,price):
        self.brand = brand           #<---------- Intence attribute
        self.price = price
        











#                      Types of Methods




#         1.INTANCE METHOD- 
#                           An instance method Works with instance
#                           (object) of the class. This method can
#                           access and modify instance attributes.




class car:
    def __init__(self,brand,price):
        self.brand = brand           #<------------Intence attribute
        self.price = price

    def show(self):       #<-----------Instance Method
        print("this is Instance Method") 


    


#         2.CLASS METHOD -         
#                          This method works with the class itself it will
#                          not target the instance (object). we have to
#                          use @classmethod decorator for creating the
#                          class method and it takes cls as their first
#                          parameter.
          

#          Example






class car:
    def __init__(self,brand,price):
        self.brand = brand           #<------------Intence attribute
        self.price = price

    def show(self):       #<-----------Instance Method
        print("this is Instance Method") 

    @classmethod   #<-----we have to use @classmethod decorator for creating the class method 
    
    def hello(cls):  #<----------cls targets the location of our class 
        print("this is Class Method")     #<-------------Class Method

        






#        3.STATIC METHOD -
#                         This method doesn’t access class or instance
#                         directly it also uses a decorator @staticmethod
#                         it just acts like a regular function placed inside a
#                         class. 






#        Example:

class car:
    def __init__(self,brand,price):
        self.brand = brand           #<------------Intence attribute
        self.price = price

    def show(self):       #<-----------Instance Method
        print("this is Instance Method") 

    @classmethod   #<-----we have to use @classmethod decorator for creating the class method 
    
    def hello(cls):  #<----------cls targets the location of our class 
        print("this is Class Method")     #<-------------Class Method

        


    @staticmethod   #<-----------we have to use @staticmethod decorator for creating the class method 

    def static():
        print("this is Static Method")










#    ---------------------THE FOUR PILLERS OF OOPs IN PYTHON   ------------------------------





#    ----------------------------------- 1.INHERITANCE ---------------------------------------







#        Inheritance -
#                     Inheritance works between classes,Inheritance allows a class (child class) to inherit properties and
#                     behaviors (attributes and methods) from another class (parent
#                     class).







#     Benefits of using inheritance is :

#                                         Code reusability
#                                         Organized structure
#                                         Easy to maintain and extend






#             Syntax of Inheritance


#            FOR EXAMPLE





class factory:  #<----------------Parent Class/superclass
    a = "hello i am an attribute mentioned inside factory"
    def hello(self):
        print("hello i am an Method mentioned inside factory ")




class carfactory(factory):    #<--------------Child Class/subclass
    pass



obj = carfactory()

print(obj.a)

print(obj.hello())




#         Now the inherited class has all the powers of parent class that
#         means all the methods, attributes can be accessed by the
#         instance of child class as well.





#                    Constructor in Inheritance


#        Lets say we have created a parent class with a constructor
#        function inside it and then this class is inherited by another class
#        then the constructor function of parent class will work for the
#        child class as well.


class car:
    def __init__(self,Model,price):    #<------ constructer
        self.Model = Model
        self.price = price
        pass
    def show(self):
        print(f"hello your car model is {self.Model},and price is {self.price}")

class bmw(car):
    pass

obj = bmw("M5",120)

print(obj.price)
print(obj.Model)

obj.show()

         






#            Now lets say you need a new parameter in your child class you
#            have to create a constructor function for your child class but the
#            parameters that can be initialized in the parent class will be
#            initialized using the super() function. Super function will target the
#            parent class.)






class cars:
    def __init__(self,model):
        self.model = model
        pass
    def show(self):
        print(f"hello your car model is {self.model}")


class BMW(cars):
    def __init__(self, model,price):
        super().__init__(model)
        self.price = price

    def show(self):
        print(f"the price is {self.price}")

obj = cars("m5")
obj = BMW("m5",120)


obj.show()






#                    Types of Inheritance



#         1.Single Inheritance -
#                                All the inheritance we saw above was single level.

   



#         2.Multiple Inheritance -
#                                 Multiple Inheritance means there will be 2 parent classes and
#                                 only 1 child class and the child class will inherit all the
#                                 attributes and methods of both parents.


#        Note - The constructor function will be inherited of the first
#        class that has been Inherited. This is MRO(Method Resolution
#        Order) followed by python.




class Animal:
    def __init__(self,name):
        pass
       
class Human:
    def __init__(self,name ,age):
        pass

class robots(Human,Animal):
    pass


obj = robots("Ashish",20)








    

#            3.MULTILEVEL INHERITANCE

#       This is a basic case where we will have
#       grandparent class → parent class → child class

#       The attributes and methods are passed on through all the
#       classes.





class factory:
    def __init__(self,material,zips):
        self.material = material
        self.zips = zips
        

class factorymumbai(factory):
    def __init__(self, material, zips,color):
        super().__init__(material, zips)
        self.color = color

class factorydelhi(factorymumbai):
    def __init__(self, material, zips, color,pockets):
        super().__init__(material, zips, color)
        self.pockets = pockets


obj = factorydelhi("corton",3,"blue",2)

print(obj.material)













#    -------------------- 2. POLYMORPHISM -----------------------------




#   Polymorphism - 
#                  Polymorphism is a core concept in Object-Oriented Programming
#                  (OOP). The word means "many forms" — and in programming, it
#                  allows the same interface or method name to behave differently
#                  depending on the object or context.




#  Types of Polymorphism -

#                  Polymorphism can be achieved in python in two ways well if we
#                  talk about compile time languages there are 3 ways but python
#                  does not support Method overloading.

#                  Method overloading means having same name methods inside a
#                  class but parameters will be different but in python the latest
#                  definition will overwrite the previous one.



#      1.METHOD OVERRIDING -

#                   This is where a child class overrides a method of the parent
#                   class, and Python decides at runtime which method to call,
#                   based on the object type.

#         EXAMPLE:




class Animal:
    def sound(self):
        print("Animal makes a sound")


class Dog:
    def sound(self):
        print("dog barks!!")   #<---------this will overwrite the previous method

    




#     2.DUCK TYPING -

#                   Python follows the philosophy:
                  
#                   "If it walks like a duck and quacks like a duck, it must be a
#                   duck."


#                   Duck typing is a concept in Python where an object's suitability
#                   is determined by what it can do (its methods and attributes),
#                    not by what class it belongs to.



class Duck:
    def speak(self):
        print("Quack Quack")

class Dog:
    def speak(self):
        print("Woof Woof")

def make_sound(animal):
    animal.speak()

duck = Duck()
dog = Dog()

make_sound(duck)
make_sound(dog)






#     -------------- 3. ENCAPSULATION  ------------------------------



#    Encapsulation -

#      Encapsulation means putting data (variables) and code (functions)
#      together in one place — inside a class.
     
     
#      It also means hiding the internal details of how things work, and
#      only showing what is needed.
     
#      It keeps data safe from being changed by mistake.
#      It makes your code clean and easy to use.
#      It gives control over what others can access or change.




#   Access modifiers in python -

#     Access modifiers means how we give access of our attributes
#     and methods to the object or inherited classes. There are 3 types

 

#  1.Public Attributes and Methods-



#     Till now every attribute and methods we have created are
#     public means the inherited classes and objects can access
#     them no matter what.




#  2.protected Attributes and Methods.


#    python protected members are created using a single
#    underscore but it still can be accessed from outside the
#    class so you might wonder whats the point of using them
#    Python doesn’t enforce protected access like other
#    languages (e.g., Java or C++). But it uses a naming
#    convention to tell developers.




#  3.Private Attributes and Method

#    A private variable or method means:
#    It cannot be accessed from outside the class — only from
#    inside the class where it is defined.

#    In Python, we use two underscores (__) before the name to
#    make it private.



#  Example:

class Factory:
    __a = "mumbai"

    def __show(self):
       print("mumbai")     #<-------- now It cannot be accessed from outside the class




# so how TO access these private attribute  and methods --

class Factory:
    __a = "mumbai"

    def show(self):
       print(Factory.__a)     #<-------- now It cannot be accessed 


obj = Factory()

obj.show()








#  ----------------4.Abstraction ----------------------



#        Abstraction
       
#        Abstraction does not exist in python but we can achieve it using a
#        library we will see what is a library later.
       
#        Abstraction is used to simplifying complex systems by focusing
#        on essential features and hiding unnecessary details
       
#        It is used to define a common interface for different subclasses.
       
       
       
       
       
#        Abstract classes and methods
       
#        Abstract classes are classes that contains one or more abstract
#        methods.
       
#        A method that is defined but not implemented in the abstract
#        class. subclasses must provide the implementation.


#     Explanation 

# Example:

class Square:
    def __init__(self,side):
        self.side = side

    
class circle:
    def __init__(self,radius):
        self.radius = radius
        

#      Now we want all classes to have a common structure and follow 
#      the same set of rules. To achieve this, we create an abstract
#      class and make the other classes inherit from it. This ensures
#      that every derived class follows the rules defined in the abstract class.




from abc import ABC, abstractmethod


class abstract(ABC):
    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass





#we will make the other classes inherit from it


class Square(abstract):
    def __init__(self,side):
        self.side = side
    def perimeter(self):
        print("now i have created the method")

    def area(self):
        print("i have created this area method")
    
class circle(abstract):
    def __init__(self,radius):
        self.radius = radius

    def perimeter(self):
        print("i have created")

    def area(self):
        print("i have created this area method")
        

obj = circle(9)
obj2 = Square(9)







#            What are Dunder methods



#        Dunder methods are special methods in Python that start and
#        end with double underscores, like __init__, __str__, __add__, etc.

#        these methods let you define how your objects behave with buil in python operations>

#        They automatically get called when you perform certain actions
#        on an object.


#        They help us -

#        Customize behavior of your class
#        Make our class objects behave like built-in data types (like
#        strings, lists, etc.




#  Examples:


class Animal:
    def __init__(self,age,name):
        self.age = age
        self.name = name

    def __str__(self):
        return f"hello this is a dunder method and your name is {self.name}"
    

obj = Animal(12,"lion")

print(obj)








class Animal:
    def __init__(self,age,name):
        self.age = age
        self.name = name

    def __str__(self):
        return f"hello this is a dunder method and your name is {self.name}"
    
    def __add__(self, other):
        return f"your sum of ages are {self.age + other.age}"
        pass


obj = Animal(12,"lion")
obj2 = Animal(11,"tiger")

print(obj + obj2)




# sum for three objects





class Animal:
    def __init__(self,age,name):
        self.age = age
        self.name = name

    def __str__(self):
        return f"hello this is a dunder method and your name is {self.name}"
    
    def __add__(self, other):
        sum = 0
        for i in other:
            sum = sum + i.age
        return f"your sum of ages are {self.age + sum}"
        pass


obj1 = Animal(12,"lion")
obj2 = Animal(11,"tiger")
obj3 = Animal(23,"elephent")


print(obj1 + (obj2,obj3))





#         Most Important Dunder (Magic) Methods in Python

#      1. __init__()      → Constructor; initializes an object.
#      2. __str__()       → Returns a user-friendly string representation.
#      3. __repr__()      → Returns an official string representation for developers.
#      4. __len__()       → Returns the length of an object.
#      5. __getitem__()   → Accesses an item using indexing (obj[index]).
#      6. __setitem__()   → Sets an item using indexing (obj[index] = value).
#      7. __delitem__()   → Deletes an item using indexing (del obj[index]).
#      8. __contains__()  → Checks membership using the `in` operator.
#      9. __iter__()      → Returns an iterator object.
#      10. __next__()     → Returns the next item during iteration.
#      11. __add__()      → Overloads the `+` operator.
#      12. __sub__()      → Overloads the `-` operator.
#      13. __mul__()      → Overloads the `*` operator.
#      14. __truediv__()  → Overloads the `/` operator.
#      15. __eq__()       → Overloads the `==` operator.
#      16. __lt__()       → Overloads the `<` operator.
#      17. __gt__()       → Overloads the `>` operator.
#      18. __call__()     → Makes an object callable like a function.
#      19. __getattr__()  → Called when an attribute is not found.
#      20. __setattr__()  → Called whenever an attribute is assigned.
#      21. __enter__()    → Executed when entering a `with` block.
#      22. __exit__()     → Executed when exiting a `with` block.
#      23. __new__()      → Creates a new object before `__init__()`.
#      24. __del__()      → Destructor; called when an object is about to be destroyed.
#      25. __hash__()     → Returns the hash value of an object.
#      26. __bool__()     → Returns the Boolean value of an object.
 







