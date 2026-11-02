from random import randint

def busca_binaria_divisao_conquista(arr, inicio, fim, alvo):
    """
    Algoritmo de Divisão e Conquista executado sobre o arranjo ordenado.\n
    Divide a área de busca ao meio e realiza chamadas recursivas na metade correspondente.
    """
    if inicio > fim:
        return False

    meio = (inicio + fim) // 2

    if arr[meio] == alvo:   # caso base
        return meio

    if alvo < arr[meio]:
        # procura à esquerda
        return busca_binaria_divisao_conquista(arr, inicio, meio-1, alvo)

    # procura à direita
    return busca_binaria_divisao_conquista(arr, meio+1, fim, alvo)

def encontrar_indice_minimo_recursivo(arr, i, j):
    """Localiza recursivamente o índice do menor elemento no sub-arranjo de i até o fim da lista."""
    if i == j:
        return i

    menor_resto = encontrar_indice_minimo_recursivo(arr, i+1, j)

    if arr[i] < arr[menor_resto]:
        return i
    return menor_resto

def selection_sort_recursivo(arr, i=0, n=None):
    """
    Funciona como a estrutura principal do Selection Sort, selecionando o menor elemento da sublista
    não ordenada via encontrar_indice_minimo_recursivo e trocando com a posição i.
    """
    if n is None:
        n = len(arr)

    if i >= (n-1):
        return arr
    
    menor_ind = encontrar_indice_minimo_recursivo(arr, i, n-1)
    
    if i != menor_ind:
        arr[i], arr[menor_ind] = arr[menor_ind], arr[i]

    return selection_sort_recursivo(arr, i+1, n)

class No:
    def __init__(self, chave: int | float) -> None:
        self.chave = chave
        self.esquerda: None | No = None
        self.direita: None | No = None

class ArvoreBinariaBusca:
    def __init__(self, chave_raiz: int | None = None) -> None:
        if chave_raiz:
            self.raiz = No(chave_raiz)
        else:
            self.raiz = None


    def _inserir_recursivo(self, no: No, chave: int) -> No | bool :
        """
            Auxilia a função inserir
        """
        if chave == no.chave:
            # chave já existe na árvore
            return False
        if chave > no.chave:
            if no.direita == None:
                no.direita = No(chave)
                return no.direita # retorna o no criado
            else:
                return self._inserir_recursivo(no.direita, chave)
        
        else:
            if no.esquerda == None:
                no.esquerda = No(chave)
                return no.esquerda # retorna o no criado
            else:
                return self._inserir_recursivo(no.esquerda, chave)

    def inserir(self, chave: int) -> No | bool:
        """
            Insere um no a partir da chave dada.\n
            Retorna o No criado, ou False caso a chave já exista na árvore.
        """
        if not self.raiz:
            self.raiz = No(chave)
            return self.raiz
        
        raiz = self.raiz

        if raiz.chave == chave:
            return False
        
        if chave > raiz.chave:
            if raiz.direita == None:
                raiz.direita = No(chave)
                return raiz.direita
            else:
                return self._inserir_recursivo(raiz.direita, chave)
    
        if raiz.esquerda == None:
            raiz.esquerda = No(chave)
            return raiz.esquerda
        else:
            return self._inserir_recursivo(raiz.esquerda, chave)

    def printar(self, no: No | None=None):
        if self.raiz is None:
            return False
        
        if not no:
            no = self.raiz
        
        esquerda_info = None
        direita_info = None
        if no.esquerda:
            esquerda_info = no.esquerda.chave
        if no.direita:
            direita_info = no.direita.chave

        print(f'\nNo: {no.chave} | Filhos: ({esquerda_info} | {direita_info})')

        if no.esquerda:
            self.printar(no.esquerda)
        if no.direita:
            self.printar(no.direita)

    def buscar(self, chave):
        if self.raiz is None:
            return False
        
        if self.raiz.chave == chave:
            return self.raiz
        
        if chave > self.raiz.chave:
            if self.raiz.direita:
                return self._buscar_recursivo(self.raiz.direita, chave)
            return False
        
        if self.raiz.esquerda:
            return self._buscar_recursivo(self.raiz.esquerda, chave)
        return False

    def _buscar_recursivo(self, no: No, chave) -> No | bool:
        if no.chave == chave:
            return no

        if chave > no.chave:
            if no.direita:
                return self._buscar_recursivo(no.direita, chave)
            return False

        if no.esquerda:
            return self._buscar_recursivo(no.esquerda, chave)
        return False

    def _buscar_antecessor(self, no: No):
            if no.direita:
                return self._buscar_antecessor(no.direita)
            else:
                return no

    def em_ordem(self, no, resultado=None):
        if resultado is None:
            resultado = []
        if no:
            self.em_ordem(no.esquerda, resultado)
            resultado.append(no.chave)
            self.em_ordem(no.direita, resultado)

        return resultado

    def _remover_recursivo(self, chave, no: No | None):
        """
            Auxilia a função remover() de forma recursiva
        """
        if not no:
            return None
        
        if chave < no.chave:
            no.esquerda = self._remover_recursivo(chave, no.esquerda)
        elif chave > no.chave:
            no.direita = self._remover_recursivo(chave, no.direita)

        else:   # chave == no.chave
            if not no.esquerda:
                return no.direita
            if not no.direita:
                return no.esquerda

            antecessor = self._buscar_antecessor(no.esquerda)

            no.chave = antecessor.chave

            no.esquerda = self._remover_recursivo(antecessor.chave, no.esquerda)

        return no

    def remover(self, chave: int):
        if (self.raiz is None) or (not self.buscar(chave)):
            return False
        self.raiz = self._remover_recursivo(chave, self.raiz)
        return True

if __name__ == "__main__":
    testa_arv = False
    testa_funcs = False

    if testa_arv:
        arv = ArvoreBinariaBusca(25)


        for i in range(15):
            arv.inserir(randint(1, 50))

        arv.printar()

        print(arv.em_ordem(arv.raiz))

        print(arv.remover(25))

        print(arv.em_ordem(arv.raiz))

        print(arv.raiz.chave)
        arv.printar()
    if testa_funcs:
        lista = []
        for i in range(10, 0, -1):
            lista.append(randint(1,50))
            #print(i)
        print(lista)
        #print(busca_binaria_divisao_conquista(lista, 0, len(lista)-1, 10))
        #print(encontrar_indice_minimo_recursivo(lista, 0, 1))
        lista_ordenada = selection_sort_recursivo(lista)
        print(lista_ordenada)

        aleatorio = lista_ordenada[randint(0, 10)]

        print(aleatorio)
        print(busca_binaria_divisao_conquista(lista_ordenada, 0, len(lista_ordenada)-1, aleatorio))


    vermelho = '\033[31m'
    verde = '\033[32m'
    amarelo = '\033[33m'
    limpa = '\033[m'
    azul = '\033[34m'
    texto = "\n=== MENU ÁRVORE BINÁRIA DE BUSCA, SELECTION SORT E DIVISÃO E CONQUISTA ===\n" \
            "1. Inserir elemento na BST (Recursivo)\n" \
            "2. Buscar elemento na BST (Recursivo)\n" \
            "3. Remover elemento da BST (Recursivo)\n" \
            "4. Exibir percurso Em-Ordem (Vetor)\n" \
            "5. Ordenar vetor com Selection Sort (Recursivo)\n" \
            "6. Executar Busca Binária por Divisão e Conquista (Vetor)\n" \
            "0. Sair\n" \
            "Digite sua opção:\t"+amarelo

    arv = ArvoreBinariaBusca()
    while True:
        opcao = str(input(texto))
        print(limpa)

        if opcao == '1':
            elem = int(input("Digite um elemento a inserir na árvore:\t"))
            result = arv.inserir(elem)
            if result:
                print(f'Elemento {azul}{result.chave}{limpa} inserido com sucesso.')
            else:
                print(f'O elemento já existe na árvore.')
        
        elif opcao == '2':
            elem = int(input('Digite o elemento que deseja buscar na árvore:\t'))
            result = arv.buscar(elem)
            if result:
                print('Elemento se encontra na árvore')
            else:
                print('Elemento não foi encontrado na árvore')
        
        elif opcao == '3':
            elem = int(input('Digite o elemento que deseja remover da árvore:\t'))

            if arv.remover(elem):
                print(f'Elemento {azul}{elem}{limpa} removido com sucesso.')
            else:
                print(f'Elemento {elem} não foi encontrado na árvore.')

        elif opcao == '4':
            print(f'Percurso Em-Ordem da árvore:\n{azul}{arv.em_ordem(no=arv.raiz)}{limpa}')

        elif opcao == '5':
            vetor_desord = []
            for i in range(randint(7, 21)):
                vetor_desord.append(randint(1, 50))
            print(f'\nAqui tem um exemplo de vetor desordenado:\n{vermelho}{vetor_desord}{limpa}')
            vetor_ord = selection_sort_recursivo(vetor_desord)
            print(f'Aqui está o vetor após ser ordenado por Selection Sort:\n{verde}{vetor_ord}{limpa}\n')

        elif opcao == '6':
            vetor = arv.em_ordem(arv.raiz)
            if not vetor:
                print('Erro. A árvore está vazia.')
            else:
                print(f'Vetor da árvore:\n{vetor}')
                alvo = int(input('Escolha um elemento-alvo para buscar no vetor:\t'))
                result = busca_binaria_divisao_conquista(vetor, 0, len(vetor)-1, alvo)
                if result is not False:
                    print(f'O elemento {alvo} foi encontrado no índice [{result}] do vetor.')
                else:
                    print(f'O elemento {alvo} {vermelho}não{limpa} foi encontrado no vetor.')


        elif opcao == '0':
            break
        else:
            print('Opção inválida.')
        

    print('Encerrando programa...\n')
