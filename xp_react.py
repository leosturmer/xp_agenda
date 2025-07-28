from textual.app import App, ComposeResult
from textual.widget import Widget
from textual.reactive import reactive
from textual.widgets import Input, Button, Label, Pretty


class ListaDeProdutos(Widget):

    produtos = reactive({
        "prg001" : 
        {"nome" : "sapato", 
         "preco" : 240.00, 
         "quantidade" : 20},
    })

    def render(self):
         return Pretty(self.produtos).render()

    # def render(self) -> str:
    #     listagem = str()
        
    #     for cod, dados in self.produtos.items():
    #         listagem += f"{cod}: {dados['nome']}, {dados['preco']}, {dados['quantidade']}\n"

    #     return listagem


class XP_React(App):
               
    def compose(self) -> ComposeResult:
        yield Label('Código: ')
        yield Input(id="tx_cod")
        yield Label('Nome: ')
        yield Input(id='tx_nome')
        yield Label('Preço: ')
        yield Input(id='tx_preco')
        yield Label('Quantidade: ')
        yield Input(id='tx_quantidade')
        yield Button('Cadastrar', id='bt_cadastrar')

        yield ListaDeProdutos(id='lst_produtos')

    def limpar_formulario(self):
        for tx in self.query('Input'):
                tx.value = ''

    def on_button_pressed(self, evento: Button.Pressed):

        if evento.button.id == 'bt_cadastrar':
            lista = self.query_one("#lst_produtos", ListaDeProdutos)
            #aqui modificamos a propriedade reativa do componente

            produtos_atualizado = lista.produtos.copy()

            codigo = self.query_one("#tx_cod", Input).value
            nome = self.query_one("#tx_nome", Input).value
            preco = self.query_one("#tx_preco", Input).value
            quantidade = self.query_one("#tx_quantidade", Input).value


            produtos_atualizado[codigo] = {
                "nome": nome,
                "preco": preco,
                "quantidade" : quantidade
            }
            
            lista.produtos = produtos_atualizado

            self.limpar_formulario()
            self.query_one("#tx_cod").focus()


if __name__ == "__main__":
    app = XP_React()
    app.run()