import pytest

def calcular_preco_ingressos(idade, quantidade):
    if quantidade < 1 or quantidade > 5:
        return "Erro: quantidade inválida"
    if idade < 0:
        return "Erro: idade inválida"
    if idade <= 12:
        preco_unitario = 10
    elif idade >= 60:
        preco_unitario = 15
    else:
        preco_unitario = 30
    preco_total = preco_unitario * quantidade
    return f"R$ {preco_total:.2f}"

@pytest.mark.parametrize("idade, quantidade, esperado", [
    # Casos iniciais
    (10, 2, "R$ 20.00"),  # T1
    (30, 1, "R$ 30.00"),  # T2
    (65, 5, "R$ 75.00"),  # T3
    (-3, 2, "Erro: idade inválida"),  # T4
    (20, 0, "Erro: quantidade inválida"),  # T5
    (25, 6, "Erro: quantidade inválida"),  # T6
    (12, 3, "R$ 30.00"),  # T7
    (13, 3, "R$ 90.00"),  # T8
    (59, 2, "R$ 60.00"),  # T9
    (60, 2, "R$ 30.00"),  # T10
    (0, 1, "R$ 10.00"),   # T11 - idade mínima válida (bebê)
    (1, 5, "R$ 50.00"),      # T12 - criança, quantidade máxima
    (11, 4, "R$ 40.00"),     # T13
    (12, 5, "R$ 50.00"),     # T14 - limite superior de criança
    (13, 1, "R$ 30.00"),     # T15 - início adulto
    (29, 4, "R$ 120.00"),    # T16
    (59, 5, "R$ 150.00"),    # T17 - fim adulto
    (60, 1, "R$ 15.00"),     # T18 - início idoso
    (80, 3, "R$ 45.00"),     # T19
    (150, 2, "R$ 30.00"),    # T20 - idade alta
    (5, 0, "Erro: quantidade inválida"),  # T21 - quantidade = 0
    (5, -1, "Erro: quantidade inválida"), # T22
    (5, 6, "Erro: quantidade inválida"),  # T23
    (-1, 3, "Erro: idade inválida"),      # T24
    (-99, 2, "Erro: idade inválida"),     # T25
    (200, 5, "R$ 75.00"),     # T26 - idoso muito idoso
    (14, 5, "R$ 150.00"),     # T27 - adulto jovem
    (35, 2, "R$ 60.00"),      # T28
    (58, 1, "R$ 30.00"),      # T29
    (59, 1, "R$ 30.00"),      # T30
    (60, 5, "R$ 75.00"),      # T31
    (61, 5, "R$ 75.00"),      # T32
    (0, 5, "R$ 50.00"),       # T33 - bebê com máximo
    (2, 2, "R$ 20.00"),       # T34
    (8, 1, "R$ 10.00"),       # T35
    (15, 3, "R$ 90.00"),      # T36
    (55, 4, "R$ 120.00"),     # T37
    (100, 1, "R$ 15.00"),     # T38
    (101, 3, "R$ 45.00"),     # T39
    (90, 5, "R$ 75.00"),      # T40
    (58, 5, "R$ 150.00"),     # T41
    (3, 3, "R$ 30.00"),       # T42
    (11, 2, "R$ 20.00"),      # T43
    (19, 4, "R$ 120.00"),     # T44
    (70, 2, "R$ 30.00"),      # T45
    (30, 5, "R$ 150.00"),     # T46
    (40, 1, "R$ 30.00"),      # T47
    (100, 2, "R$ 30.00"),     # T48
    (6, 4, "R$ 40.00"),       # T49
    (20, 5, "R$ 150.00"),     # T50
])
def test_calcular_preco_ingressos(idade, quantidade, esperado):
    assert calcular_preco_ingressos(idade, quantidade) == esperado