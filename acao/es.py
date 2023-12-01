From proc import Acao

def leitora_emissor():
    """lê emissor"""
    emissor = input("Qual o nome da empresa?")
    return emissor

def leitora_codigo():
    "le codigo"
    codigo = input("Qual o codigo na B3?")
    return codigo

def leitora():
    emissor = leitora_emissor()
    codigo = leitora_codigo()
    return [emissor, codigo]

def impressora(acao: Acao):
    """imprime o resultado"""
    print(acao)