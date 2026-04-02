from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from splash_screen import SplashScreen
from main_screen import MainScreen

Builder.load_file('splash_screen.kv')
Builder.load_file('main_screen.kv')

class EbutuoyDownloaderApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(SplashScreen(name='splash'))
        sm.add_widget(MainScreen(name='main'))
        return sm

    def on_start(self):
        self.root.current = 'splash'
        self.root.get_screen('splash').animate_text()

EbutuoyDownloaderApp().run()