'''
class Student:
    def getStudent(self):
        self.r=int(input("Enter roll no."))
        self.name=(input("Enter your name :"))
        self.age=int(input("Enter your age :"))
    def show(self):
        print("Roll no. is ",self.r)
        print("Name is",self.name)
        print("Age is ",self.age)
vijay=Student()
vijay.getStudent()
vijay.show()
'''

# Create a class BankAccount with private attributes balance and account_number.
#Provide methods to set and get these attributes with proper validation.

class BankAccount:
    def customer(self):
        self.name=input("Name :")
        self.__account_number=input("What is your account number :")
        self.__balance=int(input("Enter your balance :"))
    def show(self):
        print("Name is ",self.name)
        print("Your Account Number is",self.__account_number)
        print("Current balance is ₹",self.__balance)
        
joker=BankAccount()
joker.customer()
joker.show()

#Write a class Student that encapsulates the attributes name and grade. Ensure grade can
#only be accessed through a getter and modified through a setter that checks if the grade
#is within 0 to 100.

