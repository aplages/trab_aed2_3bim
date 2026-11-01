from random import randint

class Nodo:
    def __init__(self, chave: int | float) -> None:
        self.chave = chave
        self.esquerda: None | Nodo = None
        self.direita: None | Nodo = None

class ArvoreBinariaBusca:
    def __init__(self, chave_raiz: int | float) -> None:
        self.raiz = Nodo(chave_raiz)

    def inserir(self, chave: int | float) -> Nodo | bool:
        """
            Insere um nodo a partir da chave dada.\n
            Retorna o Nodo criado, ou False caso a chave já exista na árvore.
        """
        raiz = self.raiz

        if raiz.chave == chave:
            return False
        
        if chave > raiz.chave:
            if raiz.direita == None:
                raiz.direita = Nodo(chave)
                return raiz.direita
            else:
                return self._inserir_recursivo(chave, raiz.direita)
    
        if raiz.esquerda == None:
            raiz.esquerda = Nodo(chave)
            return raiz.esquerda
        else:
            return self._inserir_recursivo(chave, raiz.esquerda)

    def _inserir_recursivo(self, chave: int | float, nodo: Nodo) -> Nodo | bool :
        """
            Auxilia a função inserir
        """
        if chave == nodo.chave:
            # chave já existe na árvore
            return False
        if chave > nodo.chave:
            if nodo.direita == None:
                nodo.direita = Nodo(chave)
                return nodo.direita # retorna o nodo criado
            else:
                return self._inserir_recursivo(chave, nodo.direita)
        
        else:
            if nodo.esquerda == None:
                nodo.esquerda = Nodo(chave)
                return nodo.esquerda # retorna o nodo criado
            else:
                return self._inserir_recursivo(chave, nodo.esquerda)

    def printar(self, nodo: Nodo | None=None):
        if not nodo:
            nodo = self.raiz
        
        esquerda_info = None
        direita_info = None
        if nodo.esquerda:
            esquerda_info = nodo.esquerda.chave
        if nodo.direita:
            direita_info = nodo.direita.chave

        print(f'\nNodo: {nodo.chave} | Filhos: ({esquerda_info} | {direita_info})')

        if nodo.esquerda:
            self.printar(nodo.esquerda)
        if nodo.direita:
            self.printar(nodo.direita)

    def buscar(self, chave):
        if self.raiz.chave == chave:
            return chave
        
        if chave > self.raiz.chave:
            if self.raiz.direita:
                return self._buscar_recursivo(chave, self.raiz.direita)
            return False
        
        if self.raiz.esquerda:
            return self._buscar_recursivo(chave, self.raiz.esquerda)
        return False

    def _buscar_recursivo(self, chave, nodo: Nodo):
        if nodo.chave == chave:
            return chave

        if chave > nodo.chave:
            if nodo.direita:
                return self._buscar_recursivo(chave, nodo.direita)
            return False

        if nodo.esquerda:
            return self._buscar_recursivo(chave, nodo.esquerda)
        return False

    def todas_chaves(self):
        """
            Retorna uma lista com os chavees de todos nodos da árvore
        """
        lista_chaves = [self.raiz]
        pass

    def em_ordem(self) -> list:
        """
            Retorna um arranjo com os chavees da árvore (já ordenados)
        """
        esq = []
        dir = []
        if self.raiz.esquerda:
            esq = self._aux_em_ordem(self.raiz.esquerda)
        if self.raiz.direita:
            dir = self._aux_em_ordem(self.raiz.direita)

        return esq+[self.raiz.chave]+dir

    def _aux_em_ordem(self, nodo: Nodo) -> list:
        """
            Auxilia a função em_ordem()
        """
        esq = []
        dir = []
        if nodo.esquerda:
            #print(nodo.esquerda.chave)
            esq = self._aux_em_ordem(nodo.esquerda)
        if nodo.direita:
            dir = self._aux_em_ordem(nodo.direita)

        return esq+[nodo.chave]+dir
    
    def remover(self, chave):
        """
            Remove um nodo a partir de uma chave dado
        """        
        if chave < self.raiz.chave:
            self.raiz.esquerda = self._aux_remover(chave, self.raiz.esquerda)
        elif chave > self.raiz.chave:
            self.raiz.direita = self._aux_remover(chave, self.raiz.direita)

        else:   # chave == self.raiz.chave
            if not self.raiz.esquerda:
                return self.raiz.direita
            if not self.raiz.direita:
                return self.raiz.esquerda

            antecessor = self._buscar_antecessor(self.raiz.esquerda)

            self.raiz.chave = antecessor.chave

            self.raiz.esquerda = self._aux_remover(antecessor.chave, self.raiz.esquerda)

    def _aux_remover(self, chave, nodo: Nodo | None):
        """
            Auxilia a função remover() de forma recursiva
        """
        if not nodo:
            return None
        
        if chave < nodo.chave:
            nodo.esquerda = self._aux_remover(chave, nodo.esquerda)
        elif chave > nodo.chave:
            nodo.direita = self._aux_remover(chave, nodo.direita)

        else:   # chave == nodo.chave
            if not nodo.esquerda:
                return nodo.direita
            if not nodo.direita:
                return nodo.esquerda

            antecessor = self._buscar_antecessor(nodo.esquerda)

            nodo.chave = antecessor.chave

            nodo.esquerda = self._aux_remover(antecessor.chave, nodo.esquerda)

        return nodo

    def localizaPai(self, chave, retornaChave=False):
        """
        Localiza o pai de um nodo a partir de uma chave dada
        """
        raiz = self.raiz

        if raiz.chave == chave:
            return False

        if not retornaChave:
            if raiz.esquerda:
                if raiz.esquerda.chave == chave:
                    return raiz
                esq = self._aux_localizaPai(chave, raiz.esquerda)
                if esq:
                    return esq
        
            if raiz.direita:
                if raiz.direita.chave == chave:
                    return raiz
        
                dir = self._aux_localizaPai(chave, raiz.direita)
                if dir:
                    return dir
        
            return None

        # retorna Chave
        if raiz.esquerda:
            if raiz.esquerda.chave == chave:
                return raiz.chave
            esq = self._aux_localizaPai(chave, raiz.esquerda)
            if esq:
                return esq.chave
    
        if raiz.direita:
            if raiz.direita.chave == chave:
                return raiz.chave
    
            dir = self._aux_localizaPai(chave, raiz.direita)
            if dir:
                return dir.chave
        return None

    def _aux_localizaPai(self, chave, nodo: Nodo):
        """
            Auxilia a função localizaPai()
        """ 
        if nodo.esquerda:
            if nodo.esquerda.chave == chave:
                return nodo
            esq = self._aux_localizaPai(chave, nodo.esquerda)
            if esq:
                return esq

        if nodo.direita:
            if nodo.direita.chave == chave:
                return nodo
            
            dir = self._aux_localizaPai(chave, nodo.direita)
            if dir:
                return dir
        
        return None

    def _buscar_antecessor(self, nodo: Nodo):
        if nodo.direita:
            return self._buscar_antecessor(nodo.direita)
        else:
            return nodo
        
if __name__ == "__main__":
    arv = ArvoreBinariaBusca(25)


    for i in range(15):
        arv.inserir(randint(1, 50))

    arv.printar()

    print(arv.em_ordem())

    print(arv.remover(25))

    print(arv.em_ordem())

    arv.printar()