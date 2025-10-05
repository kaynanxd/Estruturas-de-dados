"""Exerc ́ıcio: 9.
(Ultimo Peso de Pedra)  ́ Vocˆe recebe um vetor de pedras inteiras, onde pedras[i]  ́e o peso
da i- ́esima pedra. Estamos jogando um jogo com as pedras. Em cada jogada, escolhemos as
duas pedras mais pesadas e as quebramos. Suponha que as duas pedras mais pesadas tenham
pesos x e y, com x ≤ y. O resultado dessa quebra  ́e:
 Se x = y, ambas as pedras s ̃ao destru ́ıdas, e
 Se x ̸= y, a pedra de peso x  ́e destru ́ıda, e a pedra de peso y tem um novo peso y − x.
No final do jogo, resta no m ́aximo uma pedra. Retorna o peso da  ́ultima pedra restante. Se
n ̃ao houver mais pedras, retorna 0."""

def ultima_pedra(pedras):
    while True:
        # encontrar os dois maiores > 0
        max1 = max2 = -1
        idx1 = idx2 = -1
        for i in range(len(pedras)):
            if pedras[i] > max1:
                if max1 > 0:
                    max2, idx2 = max1, idx1
                max1, idx1 = pedras[i], i
            elif pedras[i] > max2:
                max2, idx2 = pedras[i], i

        # se não houver duas pedras positivas, parar
        if max1 <= 0 or max2 <= 0:
            break

        # quebrar pedras
        if max1 == max2:
            pedras[idx1] = pedras[idx2] = 0
        else:
            pedras[idx1] = max1 - max2
            pedras[idx2] = 0

    # retornar pedra restante ou 0
    for p in pedras:
        if p > 0:
            return p
    return 0


print(ultima_pedra([2, 7, 4, 1, 8, 1]))  # 1
print(ultima_pedra([1]))                  # 1
print(ultima_pedra([10, 4, 2, 10]))       # 2