import re

def anonimizar_cpf(texto):
    # Encontra o padrão de CPF: 3 números, ponto, 3 números, ponto, 3 números, traço, 2 números.
    # Os parênteses dividem o CPF em 4 grupos.
    padrao_cpf = r'\b(\d{3})\.(\d{3})\.(\d{3})-(\d{2})\b'
    
    # Substitui o 1º e o 4º grupo por asteriscos, mantendo o 2º (\g<2>) e o 3º (\g<3>)
    texto_mascarado = re.sub(padrao_cpf, r'***.\g<2>.\g<3>-**', texto)
    return texto_mascarado

def anonimizar_email(texto):
    padrao_email = r'\b([a-zA-Z0-9])([a-zA-Z0-9_\.\-]+)([a-zA-Z0-9])@([a-zA-Z0-9_\-\.]+)\b'
    
    texto_mascarado = re.sub(padrao_email, r'\g<1>***\g<3>@\g<4>', texto)
    return texto_mascarado

if __name__ == "__main__":
    texto_original = "A cliente Maria (email: maria.silva_2026@gmail.com) possui o CPF 123.456.789-00."
    
    print("=== TEXTO ORIGINAL ===")
    print(texto_original)
    
    texto_processado = anonimizar_cpf(texto_original)
    texto_processado = anonimizar_email(texto_processado)
    
    print("\n=== TEXTO ANONIMIZADO (LGPD) ===")
    print(texto_processado)
