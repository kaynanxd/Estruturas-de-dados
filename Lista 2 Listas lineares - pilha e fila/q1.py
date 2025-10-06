"""(Parˆenteses V ́alidos) Dada uma string s contendo apenas os caracteres (, ), {, }, [ e ],
determine se a string de entrada  ́e v ́alida. Uma string de entrada  ́e v ́alida se:
 Os colchetes de abertura devem ser fechados pelo mesmo tipo de colchete.
 Os colchetes de abertura devem ser fechados na ordem correta.
 Cada colchete de fechamento tem um colchete de abertura correspondente do mesmo
tipo.
Exemplo 1. Entrada: s = (). Sa ́ıda: verdadeiro.
Exemplo 2. Entrada: s = ()[]. Sa ́ıda: verdadeiro.
Exemplo 3. Entrada: s = (]. Sa ́ıda: falso.
Exemplo 4. Entrada: s = ([]). Sa ́ıda: verdadeiro.
Exemplo 5. Entrada: s = ([)]. Sa ́ıda: falso."""

#aplicacao usando pilha(primeiro a entrar ultimo a sair)

def parentesesvalidos(lista):
    pilha =[]

    for char in lista:
        if char in '({[':
            pilha.append(char) # adiciona o abre-colchete correspondente
        elif char in ']})': #se o fecha colchete apareceu e nao tem um abre colchete referente da erro na msm hora
            if not pilha:
                return False
            
            topo = pilha[-1] #aqui definimos o topo da pilha

            if ((char == ')' and topo != '(') or          #nesses ifs e comparado a entrada junto com o topo, se for igual ao fecha colchete e o abrecolchete for diferente no topo da erro
               (char == '}' and topo != '{') or 
               (char == ']' and topo != '[')):
                return False  

            pilha.pop()        # remove o abre-colchete correspondente

    return len(pilha) == 0      # válido se pilha vazia

#complexidade O(n) 

print(parentesesvalidos("()"))       # True
print(parentesesvalidos("()[]"))     # True
print(parentesesvalidos("(]"))       # False
print(parentesesvalidos("([])"))     # True
print(parentesesvalidos("([)]"))     # False