"""Convert Miles to Kilometers Program"""
from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root


BoxLayoutDemo().run()
