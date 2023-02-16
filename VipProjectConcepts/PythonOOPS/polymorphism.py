#
# # Super() method
# class Person:
#     def __init__(self,name,age,gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#
#     def display(self):
#         print("Name-",self.name)
#         print("Age-",self.age)
#         print("Gender-",self.gender)
#
# class Student(Person):
#     def __init__(self,name,age,gender,roll,marks):
#         super(Student, self).__init__(name,age,gender)
#         self.roll = roll
#         self.marks = marks
#
#     def display(self):
#         super(Student, self).display()
#         print("roll-", self.roll)
#         print("Marks-",self.marks)
#
# s = Student("Mahesh",33,"Male",101,98)
# s.display()

# Method Overloading

# class A:
#     def sum(self,a=None,b=None,c=None):
#         if a!=None and b!=None and c!=None :
#             print("3 args Sum is->",a+b+c)
#         elif a!=None and b!=None:
#             print("2 args Sum is->",a+b)
#         else:
#             print("Please provide more that 1 argument")
#
# a = A()
# a.sum()
# a.sum(10,20)
# a.sum(10,20,30)


# class A:
#     def sum(self,*args):
#         sum = 0
#         for i in args:
#             sum+=i
#         print(sum)
# a = A()
# a.sum()
# a.sum(10,20)
# a.sum(10,20,30)





