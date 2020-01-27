

class BayesNet:

    def __init__(self, ldep=None):  # Why not ldep={}? See footnote 1.
        if not ldep:
            ldep = {}
        self.dependencies = ldep

    # Os dados estao num dicionario (var,dependencies)
    # em que as dependencias de cada variavel
    # estao num dicionario (mothers,prob);
    # "mothers" e' um frozenset de pares (mothervar,boolvalue)
    def add(self,var,mothers,prob):
        self.dependencies.setdefault(var,{})[frozenset(mothers)] = prob

    # Probabilidade conjunta de uma dada conjuncao 
    # de valores de todas as variaveis da rede
    def jointProb(self,conjunction):
        prob = 1.0
        for (var,val) in conjunction:
            for (mothers,p) in self.dependencies[var].items():
                if mothers.issubset(conjunction):
                    prob*=(p if val else 1-p)
        return prob


    # Probabilidade individual de variavel var assumir o valor val
    def individual_prob(self, var, val):
        variaveis = self.dependencies.keys()

        todas_conj = self.genConjunctions([v for v in variaveis if v != var])

        return sum(self.jointProb(conj + [(var, val)]) for conj in todas_conj)
       
    def genConjunctions(self, var_lista):
        if len(var_lista) == 1:
            return [[(var_lista[0], True), (var_lista[0], False)]]
        
        l = []
        for r in self.genConjunctions(var_lista[1:]):
            l.append(r + [(var_lista[0], True)])
            l.append(r + [(var_lista[0], False)])
        return l



# Footnote 1:
# Default arguments are evaluated on function definition,
# not on function evaluation.
# This creates surprising behaviour when the default argument is mutable.
# See:
# http://docs.python-guide.org/en/latest/writing/gotchas/#mutable-default-arguments

