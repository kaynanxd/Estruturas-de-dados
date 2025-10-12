'''Exerc ́ıcio: 6.
(Primeiro Caractere Unico em uma String)  ́ Dada uma string s, encontre o primeiro
caractere n ̃ao repetido nela e retorne seu  ́ındice. Se n ̃ao existir, retorne -1.
Exemplo 1. Entrada: s = leetcode. Sa ́ıda: 1. Explica ̧c ̃ao: O caractere l no  ́ındice
1  ́e o primeiro caractere que n ̃ao ocorre em nenhum outro  ́ındice.

3

Exemplo 2. Entrada: s = loveleetcode. Sa ́ıda: 3.
Exemplo 3. Entrada: s = aabb. Sa ́ıda: −1.'''

def primeiro_caractere_unico(palavra):
    contador = {}  # para contar ocorrências
    fila = []      # fila para manter ordem

    for i in range(len(palavra)):
        c = palavra[i]
        contador[c] = contador.get(c, 0) + 1
        fila.append((c, i))

    for c, i in fila:
        if contador[c] == 1:
            return i
    return -1

print(primeiro_caractere_unico('leetcode'))
print(primeiro_caractere_unico('loveleetcode'))

print(primeiro_caractere_unico('aabb'))
