#
# class Animal:
#     @classmethod
#     def dog(cls):
#         print("From Animal class Dog method.")
#
#     @classmethod
#     def cat(cls):
#         print("From Animal class Cat method")
#
# class Dog(Animal):
#     # def dog(self):
#     #     print("From Dog Class.")
#     pass
#
# class Cat(Animal):
#
#     def cat(self):
#         print("From Cat class")
#
# c = Cat()
# c.cat()
# d = Dog()
# d.dog()

class A:
    def m1(self):
        print("Class A method")
    def m2(self):
        print("Class A method")
class B(A):
    def m1(self):
        print("Class B method")
    def m2(self):
        print("Class B method")
class E(B):
    def m1(self):
        print("Class E method")
    # def m2(self):
    #     print("Class E method")

class C(A):
    def m1(self):
        print("Class C method")
    def m2(self):
        print("Class C method")
class D(E,C):
    def m1(self):
        print("Class D method")
d = D()
d.m2()









