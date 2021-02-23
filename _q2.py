class Node:
    def  __init__(self):
        self.n = 0
        self.e = ''
    
    def __eq__(self, other):
        return type(other) == Node and self.n == other.n and self.e == other.e

class Stack:
    def __init__(self):
        self.initial = Node()
    
    def add(self, item):
        if (self.initial == Node()):
            # Se stack estiver vazia
            self.initial.n = 0
            self.initial.e = item
        else:
            # Cria novo node
            n1 = Node()
            n1.n = 0
            n1.e = item
            
            # Procura último node (que não aponta para o próximo)
            nodeAtual = self.initial
            while (nodeAtual.n != 0):
                nodeAtual = nodeAtual.n
            nodeAtual.n = n1
    
    def isNotEmpty(self):
        return not(self.initial == Node())
    
    def remove(self):
        if (self.initial == Node()):
            # Stack já está vazia
            pass
        else:
            # Procura último node (que não aponta para o próximo)
            nodeAnterior = None
            nodeAtual = self.initial
            while (nodeAtual.n != 0):
                nodeAnterior = nodeAtual
                nodeAtual = nodeAtual.n
                
            if nodeAnterior is not None:
                # Último não é o node inicial
                nodeAnterior.n = 0
                return nodeAtual.e
            else:
                # Último é o node inicial: a stack fica vazia agora
                self.initial = Node()
                return nodeAtual.e