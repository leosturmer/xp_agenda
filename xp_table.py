from textual.app import App, ComposeResult
from textual.widgets import DataTable, Label, Input, Button

class Tx_Table(App):

    def on_mount(self):
        tabela = self.query_one(DataTable)
        tabela.add_columns('Código', 'Nome', 'Preço', 'Quantidade')

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

        
    
        yield DataTable() 

    def limpar_formulario(self):
        for tx in self.query('Input'):
                tx.value = ''

    def on_button_pressed(self, evento: Button.Pressed):

        if evento.button.id == 'bt_cadastrar':
            codigo = self.query_one("#tx_cod", Input).value
            nome = self.query_one("#tx_nome", Input).value
            preco = self.query_one("#tx_preco", Input).value
            quantidade = self.query_one("#tx_quantidade", Input).value

            self.limpar_formulario()

            self.query_one(DataTable).add_row(codigo, nome, preco, quantidade)

            self.query_one("#tx_cod").focus()


if __name__ == '__main__':
    app = Tx_Table()
    app.run()