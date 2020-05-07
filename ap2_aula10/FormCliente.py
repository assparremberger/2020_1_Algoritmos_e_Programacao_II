import PySimpleGUI as gui 
from Cliente import Cliente
class FormCliente:
    def __init__(self):
        conteudo = [
            [ gui.Text("Nome: ") , gui.Input(size=(30, 0), key='txtNome') ] ,
            [ gui.Checkbox("Aceita receber e-mail", key='aceitaEmail') ] ,
            [ gui.Text("Sexo: ")  ] , 
            [   gui.Radio("Feminino",'sexo', key='feminino') , 
                gui.Radio("Masculino", 'sexo', key='masculino')  , 
                gui.Radio("Não Informar", 'sexo', key='naoInformado')  ] ,
            [ gui.Text("Idade: ") , gui.Slider(range=(0,150), orientation='h' , key='idade', default_value=18)] ,
            [ gui.Button("Salvar") ] 
        ]
        self.tela = gui.Window("Formulário de Produto").layout( conteudo )
    def show(self):
        self.button , self.valores = self.tela.Read()
        cliente = Cliente()
        cliente.nome = self.valores['txtNome']
        cliente.aceitaEmail = self.valores['aceitaEmail']
        if  self.valores['feminino'] :
            cliente.sexo = "Feminino"
        elif self.valores['masculino']: 
            cliente.sexo = "Masculino"
        else:
            cliente.sexo = "Não Informado"
        cliente.idade = self.valores['idade']
        return cliente

