class FormulaError(Exception):
    pass

def parse_input(input):
    # Separa a entrada por espaços
    items = input.split()
    
    if (len(items) != 3):
        raise FormulaError("A entrada nao consiste de 3 elementos")
    src1, op, src2 = items[0], items[1], items[2]
    
    if (op not in ["+","-","*","/"]):
        raise FormulaError(f"{op} nao e um operador valido")
    
    try:
        src1 = float(src1)
        src2 = float(src2)
    except (ValueError):
        raise FormulaError("O primeiro e o terceiro valor de entrada devem ser numeros")
 
    return src1, op, src2

def evaluate(src1, op, src2):
    if (op == "+"):
        return src1 + src2
    elif (op == "-"):
        return src1 - src2
    elif (op == "*"):
        return src1 * src2
    elif (op == "/"):
        return src1 / src2
    
def main():
    entrada = input()
    src1, op, src2 = parse_input(entrada)
    print(evaluate(src1,op,src2))

if __name__ == "__main__":
    main()