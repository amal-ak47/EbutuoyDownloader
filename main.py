from kivy.app import App
from kivy.lang import Builder
from splash_screen import SplashScreen

Builder.load_file('splash_screen.kv')

class EbutuoyDownloaderApp(App):
    def build(self):
        return SplashScreen()

if __name__ == "__main__":
    EbutuoyDownloaderApp().run()