from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

class Gerenciador(ScreenManager):
    pass

class Menu(Screen):
    pass

# classe de Lista de Tarefas
class Tarefas(Screen):
    def __init__(self, tarefas=[], **kwargs): #keywords arguments
        super().__init__(**kwargs)
        
        for tarefa in tarefas:
            self.ids.box.add_widget(Tarefa(text=tarefa))
            
    def on_pre_enter(self):
        Window.bind(on_keyboard=self.voltar)
       
    def voltar(self, window, key, *args):
        if key == 27:
            App.get_running_app().root.current = 'menu'
            return True
        
    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.voltar) #desativa a funcionalidade da tecla
        
    def addWidget(self):
        texto = self.ids.texto.text #pega o que o usuário digitou
        self.ids.box.add_widget(Tarefa(text=texto)) #adiciona na lista
        self.ids.texto.text = ''
            
            
# classe Tarefa
class Tarefa(BoxLayout):
    def __init__(self, text='', **kwargs):
        super().__init__(**kwargs)
        self.ids.label.text = text

      
class Test(App):
    def build(self):
        return Gerenciador() 
    
Test().run()