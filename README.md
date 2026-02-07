# Soma de Gauss (1 até 100)

Este repositório traz exemplos de como calcular a soma de **1 até 100** usando diferentes estratégias, com descrição e complexidade de tempo.

## 1) Múltiplas iterações com `for` — O(n)

Nesse modo, percorremos todos os números de 1 até 100 e acumulamos em uma variável.

```python
total = 0
for i in range(1, 101):
    total += i
```

- ✅ Fácil de entender.
- ⚠️ Faz várias iterações (cresce linearmente com `n`).

## 2) Múltiplas iterações com `while` — O(n)

Mesma ideia do `for`, mas controlando manualmente o índice.

```python
total = 0
i = 1
while i <= 100:
    total += i
    i += 1
```

- ✅ Útil para entender controle de loop.
- ⚠️ Também percorre todos os elementos.

## 3) Função nativa `sum(range(...))` — O(n)

Usa recursos prontos da linguagem para deixar o código curto.

```python
total = sum(range(1, 101))
```

- ✅ Código enxuto e legível.
- ⚠️ Ainda é uma soma iterativa por baixo dos panos.

## 4) Fórmula da Soma de Gauss — O(1)

Gauss percebeu que a soma de 1 até `n` pode ser calculada diretamente com:

\[
\text{soma} = \frac{n(n+1)}{2}
\]

Para `n = 100`:

\[
\frac{100 \cdot 101}{2} = 5050
\]

Em Python:

```python
total = n * (n + 1) // 2
```

- ✅ Muito eficiente (tempo constante).
- ✅ Melhor opção para desempenho quando só precisamos do resultado final.

---

## Executando o exemplo completo

```bash
python3 exemplos_gauss.py
```

Saída esperada (resumo):

- For: `5050`
- While: `5050`
- sum(range): `5050`
- Fórmula de Gauss: `5050`
