1# A function is a block of code which only runs when it is called. 
1#A car's efficiency in terms of miles per gallon of gasoline 

2#The method operates the data in the class, while a function is used to return or pass the data 

3#Python's implementation of a data structure that is more generally known as an associative array.
3#to look up the meaning of any words that you don't understand.   

4#a code hosting platform for version control and collaboration. 

5#A dictionary is an arbitrary mapping. An object is a special mapping from names to variables and methods. A class is a language construct that gathers together objects with similar structure and helps to create objects. Objects and classes can be simulated in a straightforward way using functions and dictionaries 

Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print(Dict) 

dict1 ={'Name':'Steve', 'Age':30, 'Designation':'Programmer'}
 
print("Dictionary:", dict1)
print("Length of dictionary:", len(dict1)) 

class Bank_Account:
    def __init__(self):
        self.balance=0
        print("Hello!!! Welcome to the Deposit & Withdrawal Machine")
 
    def deposit(self):
        amount=float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\n Amount Deposited:",amount)
 
    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance>=amount:
            self.balance-=amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance  ")
 
    def display(self):
        print("\n Net Available Balance=",self.balance)
 
# Driver code
  
# creating an object of class
s = Bank_Account()
  
# Calling functions with that class object
s.deposit()
s.withdraw()
s.display() 

# if you dont space correctly 
