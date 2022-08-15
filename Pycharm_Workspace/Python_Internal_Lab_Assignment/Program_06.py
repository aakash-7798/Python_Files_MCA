# Written by Aakash Nadupalli

# 6. Write a class Complex for performing arithmetic with complex numbers. The
# constructor for this class should take two floating-point values. Add methods for
# adding, subtracting, and multiplying two complex numbers. Overload the operators.

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        rl = self.real + other.real
        img = self.imag + other.imag
        if img < 0:
            return f'Addition of Complex Numbers --> ({rl}{img}j)'
        else:
            return f'Addition of Complex Numbers --> ({rl}+{img}j)'

    def __sub__(self, other):
        rl = self.real - other.real
        img = self.imag - other.imag
        if img < 0:
            return f'Subtraction of Complex Numbers --> ({rl}{img}j)'
        else:
            return f'Subtraction of Complex Numbers --> ({rl}+{img}j)'

    def __mul__(self, other):
        rl = (self.real * other.real) - (self.imag * other.imag)
        img = (self.real * other.imag) + (self.imag * other.real)
        if img<0:
            return f'Multiplication of Complex Numbers --> ({rl}{img}j)'
        else:
            return f'Multiplication of Complex Numbers --> ({rl}+{img}j)'


cmp1 = Complex(-5, 3)
print(f'Real and Imaginary Values for cmp1  --> ({cmp1.real}+{cmp1.imag}j)')
cmp2 = Complex(4, -2)
print(f'Real and Imaginary Values for cmp2  --> ({cmp2.real}+{cmp2.imag}j)')
print(cmp1.__add__(cmp2))
# print(cmp1+cmp2)    # this is also valid statement
print(cmp1.__sub__(cmp2))
# print(cmp1-cmp2)
print(cmp1.__mul__(cmp2))
# print(cmp1*cmp2)
# print(complex(-5,3)*complex(4,-2))  ## inbuilt function in python

