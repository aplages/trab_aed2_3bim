class Nodo:
    def __init__(self, chave: int | float) -> None:
        self.chave = chave
        self.esquerda = None
        self.direita = None


    def inserir(self, valor: int | float) -> Nodo | bool:
        """
            Insere um nodo a partir do valor dado.\n
            Retorna o Nodo criado, ou False caso o valor já exista na árvore.
        """
        if (not self.raiz) or (valor == self.chave):
            # Nodo não é raiz ou valor já existe na árvore
            return False

        if valor > self.chave:
            if self.direita == None:
                self.direita = Nodo(valor)
                return self.direita
            else:
                return self.direita._aux_inserir(valor)
            

        else:
            if self.esquerda == None:
                self.esquerda = Nodo(valor)
                return self.esquerda
            else:
                return self.esquerda._aux_inserir(valor)

    def getchave(self):
        return self.chave

    def _aux_inserir(self, valor: int | float) -> Nodo | bool :
        """
            auxilia a função inserir
        """
        if valor == self.chave:
            # valor já existe na árvore
            return False
        if valor > self.chave:
            if self.direita == None:
                self.direita = Nodo(valor)
                return self.direita # retorna o nodo criado
            else:
                return self.direita._aux_inserir(valor)
        
        else:
            if self.esquerda == None:
                self.esquerda = Nodo(valor)
                return self.esquerda # retorna o nodo criado
            else:
                return self.esquerda._aux_inserir(valor)

    def printar(self, printa_tudo=False):
        esquerda_info = None
        direita_info = None
        if self.esquerda:
            esquerda_info = self.esquerda.chave
        if self.direita:
            direita_info = self.direita.chave
        
        print(f'\nNodo:\t\t{self.chave}\nFilhos:\t{esquerda_info}\t\t{direita_info}\n')
        if printa_tudo:
            if self.esquerda:
                self.esquerda.printar(printa_tudo=True)
            if self.direita:
                self.direita.printar(printa_tudo=True)

    def printar_inline(self, printa_tudo=False):
        esquerda_info = None
        direita_info = None
        if self.esquerda:
            esquerda_info = self.esquerda.chave
        if self.direita:
            direita_info = self.direita.chave

        print(f'\nNodo: {self.chave} | Filhos: ({esquerda_info} | {direita_info})')
        if printa_tudo:
            if self.esquerda:
                self.esquerda.printar_inline(printa_tudo=True)
            if self.direita:
                self.direita.printar_inline(printa_tudo=True)

    def buscar(self, valor):
        if self.chave == valor:
            return valor
        if valor > self.chave:
            if self.direita:
                return self.direita.buscar(valor)
            return False
        if self.esquerda:
            return self.esquerda.buscar(valor)
        return False

    def todos_chaves(self) -> list:
        """
            Retorna uma lista com os valores de todos nodos da árvore
        """
        lista_chaves = [self.chave]
        if self.esquerda:
            for i in self.esquerda.todos_chaves():
                lista_chaves.append(i)
        if self.direita:
            for i in self.direita.todos_chaves():
                lista_chaves.append(i)
        return lista_chaves

if __name__ == "__main__":
    raiz = Nodo(10, raiz=True)

    a = raiz.inserir(5)

    b = raiz.inserir(15)

    raiz.inserir(3)
    raiz.inserir(13)
    raiz.inserir(14)
    raiz.inserir(16)

    #print(a, b)
    #raiz.printar()
    raiz.printar_inline(printa_tudo=True)

    print(raiz.buscar(7))

    todos = raiz.todos_chaves()

    print(todos)
    #print(selection_sort_recursivo(todos))


