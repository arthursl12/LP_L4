from filecmp import cmp

import pytest

from _q2 import Node, Stack

class TestNode:
    def test_equals(self):
        assert Node() == Node()
        n1 = Node()
        assert n1 == Node()
        
        n1 = Node()
        n1.n = Node()
        n1.e = "1"
        
        n2 = Node()
        n2.n = Node()
        n2.e = "2"
        
        assert (Node() == n1) == False
        assert (Node() == n2) == False
        assert (n2 == n1) == False
        n2.e = "1"
        assert (n2 == n1)
class TestStack:
    def test_empty(self):
        s = Stack()
        assert s.isEmpty()
        
        s.add(1)
        assert s.isEmpty() == False
        
        s.remove()
        assert s.isEmpty()
        
    def test_add_remove(self):
        s = Stack()
        s.add("Baltimore")
        s.add("Lord")
        s.add("Sir")
        s.remove()
        s.remove()
        s.add("TheLord")
        s.add("TheSir")
        assert s.remove() == "TheSir"
        assert s.remove() == "TheLord"
        assert s.remove() == "Baltimore"
        
    def test_specs(self):
        s = Stack()
        s.add("Baltimore")
        s.add("Lord")
        s.add("Sir")
        assert s.isEmpty() == False
        
        assert s.remove() == "Sir"
        assert s.isEmpty() == False
        
        assert s.remove() == "Lord"
        assert s.isEmpty() == False
        
        assert s.remove() == "Baltimore"
        assert s.isEmpty()

class TestArquivosIguais:
    def test_compara(self):
        assert cmp('_q2.py','2.py',shallow=True)