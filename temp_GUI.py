from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

class TemperatureConverter(App):
    def build(self):
        Window.size = (400,200)
        self.title = 'Temperature Converter'
        self.root = Builder.load_file('temp_GUI.kv')

    def convert_temp(self, type, temp):
        if type == "F":
            celsius = 5 / 9 * (temp - 32)
            self.root.ids.converted_temp.text = "{:.2f}".format(celsius)
        else:
            fahrenheit = temp * 9.0 / 5 + 32
            self.root.ids.converted_temp.text = "{:.2f}".format(fahrenheit)

    def clear_fields(self):
        self.root.ids.temp_input.text = ''
        self.root.ids.converted_temp.text = ''

TemperatureConverter().run()