class Const:
    def __init__(self, val):
        self.val = val

    def __str__(self):
        return str(self.val)


class Var:
    def __init__(self, name, val):
        self.name = name
        self.val = val

    def __str__(self):
        return self.name + " = " + str(self.val)


class Soma:
    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2


    def __str__(self):
        return str(self.val1 + self.val2)


class Produto:
    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2


    def __str__(self):
        return str(self.val1 * self.val2)

expr1 = Const(10)
expr2 = Var("x",10)
expr3 = Soma(10,10)
expr4 = Produto(10,10)

print(expr1)
print(expr2)
print(expr3)
print(expr4)

