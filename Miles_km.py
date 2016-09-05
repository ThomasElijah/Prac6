from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

class MilesToKilometre(App):
    """This is a tool for converting mi to km"""
    def build(self):
        Window.size = (300, 150)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file("Miles_km.kv")
        return self.root

    def handle_increment(self, value, increment):
        result = value + increment
        self.root.ids.input_number.text = str(result)

    def calculate_km(self, value):
        km = value * 1.60934
        self.root.ids.km_output.text = str(km)

    def check_valid(self):
        try:
            value = float(self.root.ids.input_number.text)
            return value
        except ValueError:
            return 0

MilesToKilometre().run()

