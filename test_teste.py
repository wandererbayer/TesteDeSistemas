def soma(a, b):
        return a+b

def subtracao(a, b):
        return  a - b

def multiplicacao(a, b):
        return  a * b

def divisao(a, b):
        if(b == 0):
            return "Impossível dividir."
        else:
            return  a / b

def teste_se_a_mais_b_eh_igual():
        assert soma(8,9) == 17
        assert soma(10,5) == 15
        assert soma(8,5) == 13

def teste_se_a_menos_b_eh_igual():
        assert subtracao(5,3) == 2 
        assert subtracao(3,3) == 0
        assert subtracao(5,4) == 1

def teste_se_a_vezes_b_eh_igual():
        assert multiplicacao(5,5) == 25 
        assert multiplicacao(5,6) == 30
        assert multiplicacao(10,7) == 70

def teste_se_a_divide_com_b_eh_igual():
        assert divisao(5,5) == 1 
        assert divisao(8,2) == 4
        assert divisao(3,0) == "Impossível dividir."