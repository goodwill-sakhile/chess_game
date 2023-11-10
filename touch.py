from kivymd.uix.boxlayout import MDBoxLayout
class TouchBox(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def respondToTouch(self):
        pass
    def on_touch_down(self, touch):
        if ((touch.pos[0] > self.pos[0]) and (touch.pos[0] < (self.pos[0] + self.size[0])) and ((touch.pos[1] > self.pos[1]) and (touch.pos[1] < (self.pos[1] + self.size[1])))):
            self.respondToTouch()
        