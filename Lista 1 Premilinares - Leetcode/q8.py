"""(Troco da Limonada) Em uma barraca de limonada, cada limonada custa R$ 5. Os
clientes est ̃ao em uma fila para comprar de vocˆe e pedir uma limonada de cada vez (na ordem
especificada nas notas). Cada cliente comprar ́a apenas uma limonada e pagar ́a com uma
nota de R$ 5, R$ 10 ou R$ 20. Vocˆe deve fornecer o troco correto a cada cliente para que a
transa ̧c ̃ao l ́ıquida seja de R$ 5. Observe que vocˆe n ̃ao tem troco em m ̃aos inicialmente. Dado
um vetor de inteiros contas, onde contas[i]  ́e a conta que o i- ́esimo cliente paga, retorne true
se vocˆe puder fornecer a cada cliente o troco correto, ou false caso contr ́ario."""

def trocolimonada(contas):
    cinco=0
    dez=0
    for conta in contas:
        if conta == 5:
            cinco+=1
        elif conta == 10:
            if cinco==0:
                return False
            cinco-=1
            dez+=1
        elif conta == 20:
            if cinco>0 and dez>0:
                cinco-=1
                dez-=1
            elif cinco>=3:
                cinco-=3
            else:
                return False
        else:
            return False
    return True

#complexidade O(n) pois pecorre cada lista de cliente 1 vez

print(trocolimonada([5, 5, 5, 10, 20]))   
print(trocolimonada([5, 5, 10, 10, 20]))  
print(trocolimonada([5, 10, 5, 20]))     
print(trocolimonada([10, 5]))  