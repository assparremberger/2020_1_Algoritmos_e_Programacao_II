import PySimpleGUI as gui 
from Produto import Produto

class FormProduto:

    def __init__(self):
        conteudo = [
            [ gui.Text("Nome: ") , gui.Input() ] ,
            [ gui.Text("Preço: ") , gui.Input(key='txtPreco') ] ,
            [ gui.Text("Quantidade: ") , gui.Input(key='txtQtd') ] ,
            [ gui.Button("Salvar") ]
        ]
        self.tela = gui.Window("Formulário de Produto").layout( conteudo )

    def show(self):
        self.button , self.valores = self.tela.Read()
        prod = Produto()
        prod.nome = self.valores[0]
        preco = self.valores['txtPreco']
        preco = float( preco.replace(",", ".") )
        prod.preco = preco
        qtd = self.valores['txtQtd']
        qtd = float( qtd.replace(",", ".") )
        prod.quantidade = qtd
        return prod
