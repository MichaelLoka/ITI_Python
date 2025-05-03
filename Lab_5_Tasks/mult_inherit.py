class A:
    def show(self):
        print("A.show() called")

class B(A):
    def show(self):
        print("B.show() called")
        super().show()

class C(A):
    def show(self):
        print("C.show() called")
        super().show()

class D(B, C):  # D inherits from B and C
    def show(self):
        print("D.show() called")
        super().show()

obj = D()
obj.show()
