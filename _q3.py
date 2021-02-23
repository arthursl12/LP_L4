class Node:
    def  __init__(self):
        self.n = 0
        self.e = ''
    
    def __eq__(self, other):
        return type(other) == Node and self.n == other.n and self.e == other.e


class Queue:
    def __init__(self):
        self.initial = Node()
    
    def add(self, item):
        if (self.initial == Node()):
            # Se file estiver vazia
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
            # Fila já está vazia
            pass
        else:
            if (self.initial.n == 0):
                # Fila possui só um elemento
                nodeInicial = self.initial
                self.initial = Node()
                return nodeInicial.e
            else:
                # Fila possui mais de um elemento
                nodeInicial = self.initial
                nodeProx = self.initial.n
                self.initial = nodeProx
                return nodeInicial.e
    
    def getSmaller(self):
        if (self.initial == Node()):
            # Fila vazia, retorna None
            return None
        
        menor = None
        
        # Itera por todos os nodes
        nodeAtual = self.initial
        if ((menor is None) or (nodeAtual.e < menor)):
            # Primeiro pode ser o menor
            menor = nodeAtual.e
        while (nodeAtual.n != 0):
            if ((menor is None) or (nodeAtual.e < menor)):
                # Intermediário pode ser o menor
                menor = nodeAtual.e
            nodeAtual = nodeAtual.n
        if ((menor is None) or (nodeAtual.e < menor)):
            # Último pode ser o menor
            menor = nodeAtual.e
        
        return menor