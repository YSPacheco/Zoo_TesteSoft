def calcular_preco_ingressos(idade, quantidade):

    if quantidade < 1 or quantidade > 5:
        return "Erro: A quantidade de ingressos deve ser entre 1 e 5."

    if idade <= 12:
        preco_unitario = 10  # Criança
    elif idade >= 60:
        preco_unitario = 15  # Idoso
    else:
        preco_unitario = 30  # Adulto

    preco_total = preco_unitario * quantidade
    return f"Preço total: R$ {preco_total:.2f}"

idade = int(input("Informe a idade do visitante: "))
quantidade = int(input("Informe a quantidade de ingressos: "))

resultado = calcular_preco_ingressos(idade, quantidade)
print(resultado)
