from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.lang import Builder
import os
from functools import partial
from kivy.uix.modalview import ModalView

Window.size = (300,600)

# Obter o caminho absoluto do diretório onde o script está localizado
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construir o caminho absoluto para o arquivo KV
kv_file = os.path.join(current_dir, 'login.kv')

# Verificar se o arquivo KV existe
if not os.path.exists(kv_file):
    print(f"Arquivo KV não encontrado: {kv_file}")
    raise FileNotFoundError(f"Arquivo KV não encontrado: {kv_file}")

# Carregar o arquivo KV
Builder.load_file(kv_file)

class TelaLogin(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.clearcolor = (1, 1, 1, 1)
        self.arg1 = None  # Inicializando arg1 como None
        self.arg2 = None  # Inicializando arg2 como None

    def on_kv_post(self, base_widget):
        # Widgets são acessíveis após o arquivo KV ser carregado
        self.texto_senha = self.ids.texto_senha
        self.texto_email = self.ids.texto_email
        self.login = self.ids.login
        self.cadastro = self.ids.cadastro
        self.cadastro.bind(on_release=partial(self.entrar_cadastro))

    def entrar_cadastro(self, instance):
        cadastro = Cadastro()
        cadastro.open()

    def open(self):
        self._window = ModalView(size_hint=(1, 1))
        self._window.add_widget(self)
        self._window.background_color = (1, 1, 1, 1)  # Definir o fundo do ModalView como preto
        self._window.open()

class Cadastro(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.clearcolor = (1, 1, 1, 1)
        self.arg1 = None  # Inicializando arg1 como None
        self.arg2 = None  # Inicializando arg2 como None

    def on_kv_post(self, base_widget):
        # Widgets são acessíveis após o arquivo KV ser carregado
        self.voltar = self.ids.voltar
        self.voltar.bind(on_release=partial(self.voltar_login))
        self.texto_senhac = self.ids.texto_senhac
        self.texto_emailc = self.ids.texto_emailc
        self.cadastro = self.ids.cadastroc

    def voltar_login(self, instance):
        voltar = TelaLogin()
        voltar.open()

    def open(self):
        self._window = ModalView(size_hint=(1, 1))
        self._window.add_widget(self)
        self._window.background_color = (1, 1, 1, 1)  # Definir o fundo do ModalView como preto
        self._window.open()

class MyApp(App):
    def build(self):
        return TelaLogin()
        
if __name__ == '__main__':
    MyApp().run()