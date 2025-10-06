'''Exerc ́ıcio: 10.
(Encontre o Vencedor do Jogo Circular) H ́a n amigos jogando. Os amigos est ̃ao sentados
em c ́ırculo e s ̃ao numerados de 1 a n no sentido hor ́ario. Mais formalmente, movendo-se no
sentido hor ́ario a partir do i- ́esimo amigo, vocˆe chega ao (i + 1)- ́esimo amigo para 1 ≤ i < n,
e movendo-se no sentido hor ́ario a partir do n- ́esimo amigo, vocˆe chega ao primeiro amigo.
As regras do jogo s ̃ao as seguintes:
1. Comece no primeiro amigo.
2. Conte os pr ́oximos k amigos no sentido hor ́ario, incluindo o amigo com o qual vocˆe
come ̧cou. A contagem se repete ao longo do c ́ırculo e pode contar alguns amigos mais
de uma vez.
3. O  ́ultimo amigo que vocˆe contou sai do c ́ırculo e perde o jogo.
4. Se ainda houver mais de um amigo no c ́ırculo, volte para a etapa 2, come ̧cando pelo
amigo imediatamente no sentido hor ́ario do amigo que acabou de perder e repita.
5. Caso contr ́ario, o  ́ultimo amigo no c ́ırculo vence o jogo.
Dado o n ́umero de amigos, n, e um inteiro k, retorne o vencedor do jogo.
Exemplo 1. Entrada: n = 5, k = 2. Sa ́ıda: 3. Explica ̧c ̃ao: Aqui est ̃ao os passos
do jogo:
1. Comece com o amigo 1.
2. Conte 2 amigos no sentido hor ́ario, que s ̃ao os amigos 1 e 2.
3. O amigo 2 sai do c ́ırculo. O pr ́oximo a come ̧car  ́e o amigo 3.
4. Conte 2 amigos no sentido hor ́ario, que s ̃ao os amigos 3 e 4.
5. O amigo 4 sai do c ́ırculo. O pr ́oximo a come ̧car  ́e o amigo 5.
6. Conte 2 amigos no sentido hor ́ario, que s ̃ao os amigos 5 e 1.
7. O amigo 1 sai do c ́ırculo. O pr ́oximo a come ̧car  ́e o amigo 3.
8. Conte 2 amigos no sentido hor ́ario, que s ̃ao os amigos 3 e 5.

6

9. O amigo 5 sai do c ́ırculo. Restou apenas o amigo 3, ent ̃ao ele  ́e o vencedor.
Exemplo 2. Entrada: n = 6, k = 5. Sa ́ıda: 1. Explica ̧c ̃ao: Os amigos saem nesta
ordem: 5, 4, 6, 2, 3. O vencedor  ́e o amigo 1.'''

def encontrevencedor(amigos,contagem):
    fila = []               
    for i in range(1, amigos + 1):
        fila.append(i)
    
    while len(fila)>1:
        for i in range(contagem-1):
            amigo = fila.pop(0)
            fila.append(amigo)

        eliminado = fila.pop(0)
        print(f"Amigo {eliminado} saiu, fila agora: {fila}")

    return fila[0]

print(encontrevencedor(5, 2))
print(encontrevencedor(6, 5))
