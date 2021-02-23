from filecmp import cmp

import pytest

from _q8 import FormulaError, evaluate, parse_input


class TestParser:
    def test_parser_correct(self):
        assert parse_input("107.0001 + -20E+4") == (107.0001, "+", -20E+4)
        assert parse_input("    +107.0001 * +204.00 " ) == (107.0001, "*", 204.00)
        assert parse_input("-107  /    -204.00  ") == (-107, "/", -204.00)
        assert parse_input("   107.0001       -  -204") == (107.0001, "-", -204)
        
    def test_parser_error_operator(self):
        with pytest.raises(FormulaError) as e_info:
            parse_input("107.0001 % -204.00")
        assert str(e_info.value) == "% nao e um operador valido"
        with pytest.raises(FormulaError) as e_info:
            parse_input("107.0001 ** -204.00")
        assert str(e_info.value) == "** nao e um operador valido"
        with pytest.raises(FormulaError) as e_info:
            parse_input("107.0001 * * -204.00")
        assert str(e_info.value) == "A entrada nao consiste de 3 elementos"
            

    def test_parser_error_lack(self):
        with pytest.raises(FormulaError) as e_info:
            parse_input("107.0001 * ")
        assert str(e_info.value) == "A entrada nao consiste de 3 elementos"    
        with pytest.raises(FormulaError) as e_info:
            parse_input("107.0001")
        assert str(e_info.value) == "A entrada nao consiste de 3 elementos"
        with pytest.raises(FormulaError) as e_info:
            parse_input(" + -204.00")
        assert str(e_info.value) == "A entrada nao consiste de 3 elementos"
        with pytest.raises(FormulaError) as e_info:
            parse_input("-204.00")
        assert str(e_info.value) == "A entrada nao consiste de 3 elementos"
        with pytest.raises(FormulaError) as e_info:
            parse_input("           ")
        assert str(e_info.value) == "A entrada nao consiste de 3 elementos"
        with pytest.raises(FormulaError) as e_info:
            parse_input("")
        assert str(e_info.value) == "A entrada nao consiste de 3 elementos"
        with pytest.raises(FormulaError) as e_info:
            parse_input("107.0001 -204.00")
        assert str(e_info.value) == "A entrada nao consiste de 3 elementos"
        
    
    def test_parser_error_wrong(self):
        with pytest.raises(FormulaError) as e_info:
            parse_input("     +   -  204.00  ")
        assert str(e_info.value) == "O primeiro e o terceiro valor de entrada devem ser numeros" 
        with pytest.raises(FormulaError) as e_info:
            parse_input("     teste   -  teste2  ")
        assert str(e_info.value) == "O primeiro e o terceiro valor de entrada devem ser numeros"
        with pytest.raises(FormulaError) as e_info:
            parse_input("     101  -  teste3  ")
        assert str(e_info.value) == "O primeiro e o terceiro valor de entrada devem ser numeros"

class TestCalculator:
    def test_evaluate(self):
        # Entrada está correta, pois foi tratada
        assert evaluate(107,"+",-3) == 104
        assert evaluate(-10.5,"-",5.5) == -16
        assert evaluate(-75E2,"/",-30E-1) == 2500
        assert evaluate(2500,"*",-3E0) == -75E2
        
class TestArquivosIguais:
    def test_compara(self):
        assert cmp('_q8.py','8.py',shallow=True)
