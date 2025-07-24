from textual.app import App
from textual.widgets import Label, Input, Button, Static, Pretty
from textual.screen import Screen

class TelaListagem(Screen):
    def compose(self):
        yield Pretty(XpAgenda.AGENDA)


class XpAgenda(App):

    AGENDA = {
        "nome@email.com": {"nome": "Nome da pessoa", "fone": "51 999999"},
        "Onome@email.com": {"nome": "O Nome da pessoa", "fone": "Dois 51 999999"}
    }

    CSS_PATH = 'xp_agenda.tcss'

    def compose(self):
        yield Static(
            """
-----------------
XP Agenda
-----------------

""")
        yield Static('[i]versão 0.0.1[/]')
        yield Label("Nome: ")
        yield Input(id='tx_nome')

        yield Label("E-mail: ")
        yield Input(id='tx_email')

        yield Label("Telefone: ")
        yield Input(id='tx_fone')

        yield Button("Limpar", id='bt_limpar')
        yield Button("Cadastrar", id='bt_cadastrar')
        yield Button("Agenda de contatos", id='bt_listar')

    def limpar_formulario(self):
        for tx in self.query('Input'):  # retorna todos os Inputs
                tx.value = ''

    def on_button_pressed(self, evento: Button.Pressed):
        if evento.button.id == "bt_listar":
            self.push_screen(TelaListagem())

        if evento.button.id == 'bt_limpar':
            self.limpar_formulario()

    # Ou faz um por um
            # nome = self.query_one('#tx_nome', Input)
            # email = self.query_one('#tx_email', Input)
            # fone = self.query_one('#tx_fone', Input)

            # nome.value = ''
            # email.value = ''
            # fone.value = ''

        if evento.button.id == 'bt_cadastrar':
            nome = self.query_one('#tx_nome', Input).value
            email = self.query_one('#tx_email', Input).value
            fone = self.query_one('#tx_fone', Input).value

            XpAgenda.AGENDA[email] = {"nome": nome, "fone": fone}

            self.limpar_formulario()
            self.notify(f'{XpAgenda.AGENDA[email]['nome']} cadastrado!')

            # colcoar pra limpar dos inputs depois de cadastrado


if __name__ == '__main__':
    app = XpAgenda()
    app.run()
