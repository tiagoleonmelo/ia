import inspect

## Superclass
class Expr:
    def __init__(self, val):
        self.val = val

    def evaluate(self, var):
        return self.val.evaluate(var)

    def simplify(self):
        return self.val.simplify()

    def __str__(self):
        return str(self.val)


class Const(Expr):
    def __init__(self, val):
        Expr.__init__(self, val)

    def evaluate(self, var):
        return self.val

    def simplify(self):
        return self

    def __str__(self):
        return str(self.val)


class Var:
    def __init__(self, name):
        self.name = name 

    def evaluate(self, var):
        return var

    def simplify(self):
        return self

    def __str__(self):
        return self.name


class Soma:
    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2

    def evaluate(self, var):
        return self.val1.evaluate(var) + self.val2.evaluate(var)

    def simplify(self):
        # if self.val1 == 0 and self.val2 == 0:
        #     return Const(0)

        if self.val1.simplify() == Const(0):
            return self.val2

        elif self.val2.simplify() == Const(0):
            return self.val1

        return self

    def __str__(self):
        return self.val1.__str__() + ' + ' + self.val2.__str__()


class Produto:
    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2

    def evaluate(self, var):
        return self.val1.evaluate(var) * self.val2.evaluate(var)

    def simplify(self):
        if self.val1.simplify() == Const(0) or self.val2.simplify() == Const(0):
            return Const(0)

        if self.val1.simplify() == Const(1):
            return self.val2

        if self.val2.simplify() == Const(1):
            return self.val1

        return self

    def __str__(self):
        return self.val1.__str__() + ' * ' + self.val2.__str__()

def var_val(expr, x):    
    return expr.evaluate(x)

def simplifier(expr):
    return expr.simplify()



## Driver code

expr1 = Const(10)
expr2 = Var("x")
expr3 = Soma(expr1, expr1)
expr4 = Produto(expr1, expr1)

expr5 = Expr( Soma( Const(10), Produto( Const(120) , Var("x") ) ) )
expr6 = Expr( Soma( Const(10), Produto( Const(120) , Const(0) ) ) )

print(expr1)
print(expr2)
print(expr3)
print(expr4)
print("")

x = 12
print(expr5)
print("Considering x as " + str(x) + ": ", end='')
print(var_val(expr5, x))
print("")

print(expr6)
print("Simplifying..")
print(simplifier(expr6))

