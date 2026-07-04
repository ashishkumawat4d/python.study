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





#                              1.INHERITANCE







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