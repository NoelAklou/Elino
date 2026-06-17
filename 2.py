class Node:
    """Classe que representa um único nó da árvore."""
    def __init__(self, chave):
        self.valor = chave
        self.esquerda = None
        self.direita = None


class ArvoreBinaria:
    """Classe que gerencia a estrutura da árvore."""
    def __init__(self):
        self.raiz = None

    def inserir(self, chave):
        """Método público para inserir um novo valor."""
        if self.raiz is None:
            self.raiz = Node(chave)
        else:
            self._inserir_recursivo(self.raiz, chave)

    def _inserir_recursivo(self, no_atual, chave):
        """Auxiliar recursivo para encontrar a posição correta e inserir."""
        if chave < no_atual.valor:
            if no_atual.esquerda is None:
                no_atual.esquerda = Node(chave)
            else:
                self._inserir_recursivo(no_atual.esquerda, chave)
        else:
            if no_atual.direita is None:
                no_atual.direita = Node(chave)
            else:
                self._inserir_recursivo(no_atual.direita, chave)

    def exibir_em_ordem(self, no):
        """Caminhamento Em-Ordem (Esquerda, Raiz, Direita) - Retorna os dados ordenados."""
        if no:
            self.exibir_em_ordem(no.esquerda)
            print(no.valor, end=" ")
            self.exibir_em_ordem(no.direita)

    def exibir_pre_ordem(self, no):
        """Caminhamento Pré-Ordem (Raiz, Esquerda, Direita)"""
        if no:
            print(no.valor, end=" ")
            self.exibir_pre_ordem(no.esquerda)
            self.exibir_pre_ordem(no.direita)

    def exibir_pos_ordem(self, no):
        """Caminhamento Pós-Ordem (Esquerda, Direita, Raiz)"""
        if no:
            self.exibir_pos_ordem(no.esquerda)
            self.exibir_pos_ordem(no.direita)
            print(no.valor, end=" ")


# --- Testando a Árvore Binária ---
if __name__ == "__main__":
    arvore = ArvoreBinaria()
    
    # Inserindo valores
    # A estrutura gerada terá o 50 como raiz
    valores = [50, 30, 70, 20, 40, 60, 80]
    for v in valores:
        arvore.inserir(v)

    print("=== Caminhamentos na Árvore ===")
    
    print("\nEm-ordem (valores ordenados):")
    arvore.exibir_em_ordem(arvore.raiz)
    
    print("\n\nPré-ordem:")
    arvore.exibir_pre_ordem(arvore.raiz)
    
    print("\n\nPós-ordem:")
    arvore.exibir_pos_ordem(arvore.raiz)
    print()