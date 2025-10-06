'''Exerc ́ıcio: 5.

(Prefixo Reverso da Palavra) Dada uma string word e um caractere ch, inverta o seg-
mento de word que come ̧ca no  ́ındice 1 e termina no  ́ındice da primeira ocorrˆencia de ch

(inclusive). Se o caractere ch n ̃ao existir em word, n ̃ao fa ̧ca nada.
Por exemplo, se word = abcdef d e ch = d, vocˆe deve inverter o segmento que come ̧ca em 1 e
termina em 4 (inclusive). A string resultante ser ́a dcbaef d.
Retorne a string resultante.
Exemplo 1. Entrada: word = abcdef d, ch = d. Sa ́ıda: dcbaef d. Explica ̧c ̃ao: A
primeira ocorrˆencia de d est ́a no  ́ındice 4. Inverta a parte da palavra de 1 a 4 (inclusive),
a string resultante  ́e dcbaef d.
Exemplo 2. Entrada: word = xyxzxe, ch = z. Sa ́ıda: zxyxxe.
Exemplo 3. Entrada: word = abcd, ch = z. Sa ́ıda: abcd.'''

def prefixoreverso(palavra,letra):
    if letra not in palavra: #se a letra nao ta na palavra so retorna ela
        return palavra
    
    indice=palavra.index[letra] #pega o indicie da letra alvo
    
    pilha=[]
    invertido=[]

    for i in range(indice+1):  #adiciona todos elementos ate o indice na pilha
        pilha.append[palavra[i]]

    while pilha: #enquanto tiver elementos na pilha eles seram adicionados em invertido, como o primeiro a entrar e o ultimo a sair entao ele ficaram invertidos
        invertido+= pilha.pop()

    return invertido + palavra[indice+1] #concatena a palavra invertida ate o indice + o que restou da palavra depois do indice marcado

#complexidade O de N

print(prefixoreverso(['xyxzxe'],['z']))