from filecmp import cmp

import pytest

from _q3 import Node, Queue

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

class TestQueue:
    def test_empty(self):
        s = Queue()
        assert s.isNotEmpty() == False
        
        s.add(1)
        assert s.isNotEmpty() == True
        
        s.remove()
        assert s.isNotEmpty() == False
        
    def test_add_remove(self):
        s = Queue()
        s.add("Baltimore")
        s.add("Lord")
        s.add("Sir")
        s.remove()  # Remove Baltimore
        s.remove()  # Remove Lord
        s.add("TheLord")    
        s.add("TheSir")
        assert s.remove() == "Sir"
        assert s.remove() == "TheLord"
        assert s.remove() == "TheSir"
        
    def test_specs(self):
        s = Queue()
        s.add("Baltimore")
        s.add("Lord")
        s.add("Sir")
        assert s.isNotEmpty()
        
        assert s.remove() == "Baltimore"
        assert s.isNotEmpty()
        
        assert s.remove() == "Lord"
        assert s.isNotEmpty()
        
        assert s.remove() == "Sir"
        assert s.isNotEmpty() == False
    
    def test_getSmaller_empty(self):
        s = Queue()
        assert s.getSmaller() is None

    def test_getSmaller_spec(self):
        s = Queue()
        s.add("C")
        s.add("A")
        s.add("B")
        
        assert s.isNotEmpty()
        assert s.getSmaller() == "A"
    
    def test_getSmaller(self):
        s = Queue()
        s.add("C")
        s.add("Y")
        s.add("A")
        s.add("B")
        s.add("D")
        s.add("K")
        s.add("A")
        
        assert s.isNotEmpty()
        assert s.getSmaller() == "A"
    
    def test_getSmaller_all_equal(self):
        s = Queue()
        s.add("ABC")
        s.add("ABC")
        s.add("ABC")
        assert s.isNotEmpty()
        assert s.getSmaller() == "ABC"

class TestArquivosIguais:
    def test_compara(self):
        assert cmp('_q3.py','3.py',shallow=True)