from kivy.metrics import sp
from kivy.uix.boxlayout import BoxLayout
from kivy.animation import Animation
from kivy.clock import Clock

class SplashScreen(BoxLayout):
    def animate_text(self):

        Clock.schedule_once(self._do_animate, 2)

    def _do_animate(self, dt):
        pop_text = self.ids.pop_text

        anim = (
            Animation(duration=0.1) +
            Animation(opacity=1, width=sp(280), duration=0.6, t='out_bounce')
        )
        anim.start(pop_text)