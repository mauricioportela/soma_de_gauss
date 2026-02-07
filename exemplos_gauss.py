"""Exemplos da soma de Gauss (1 até 100) em diferentes abordagens."""


def soma_com_for(n: int) -> int:
    """Soma usando múltiplas iterações com for (complexidade O(n))."""
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


def soma_com_while(n: int) -> int:
    """Soma usando while (complexidade O(n))."""
    total = 0
    i = 1
    while i <= n:
        total += i
        i += 1
    return total


def soma_com_sum(n: int) -> int:
    """Soma usando função embutida sum + range (complexidade O(n))."""
    return sum(range(1, n + 1))


def soma_de_gauss(n: int) -> int:
    """Soma usando a fórmula de Gauss: n * (n + 1) // 2 (complexidade O(1))."""
    return n * (n + 1) // 2


def mostrar_exemplos(n: int = 100) -> None:
    """Mostra os exemplos com descrição de abordagem e complexidade."""
    exemplos = [
        ("For (múltiplas iterações)", "O(n)", soma_com_for),
        ("While (múltiplas iterações)", "O(n)", soma_com_while),
        ("sum(range(...))", "O(n)", soma_com_sum),
        ("Fórmula de Gauss", "O(1)", soma_de_gauss),
    ]

    print(f"Soma de 1 até {n}\n")
    for nome, complexidade, func in exemplos:
        resultado = func(n)
        print(f"{nome}: resultado = {resultado} | complexidade = {complexidade}")


if __name__ == "__main__":
    mostrar_exemplos(100)
