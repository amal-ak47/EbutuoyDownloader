from kivy.uix.screenmanager import Screen
from kivy.animation import Animation
from kivy.metrics import sp
from kivy.clock import Clock

class SplashScreen(Screen):
    def animate_text(self):
        Clock.schedule_once(self._do_animate, 1)
        Clock.schedule_once(self._go_to_main, 5)

    def _do_animate(self, dt):
        pop_text = self.ids.pop_text
        anim = (
            Animation(duration=0.1) +
            Animation(opacity=1, width=sp(280), duration=0.6, t='out_bounce')
        )
        anim.start(pop_text)

    def _go_to_main(self, dt):
        self.manager.current = 'main'