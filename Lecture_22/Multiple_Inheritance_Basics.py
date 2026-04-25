class A:
    def details_1 (self):
        print("From Class A")

class B:
    def details_2 (self):
        print("From Class B")

class C(A,B):
    def details_3(self):
        print("From Class C")

c1 = C()
c1.details_1()
c1.details_2()
c1.details_3()