class A:
    def show(self):
        print("A")


class B(A):
    def show(self):
        print("B")


class C(A):
    def show(self):
        print("C")


class D(C,B):
    pass


obj = D()

obj.show()

print(D.mro())