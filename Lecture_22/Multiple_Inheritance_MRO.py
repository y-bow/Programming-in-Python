class A:
    def details(self):
        print("From Class A")

class B:
    def details(self):
        print("From Class B")

class C(A,B):
    def details(self):
        super().details()
        print("From Class C")

c1 = C()
c1.details()