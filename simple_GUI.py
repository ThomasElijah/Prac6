from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

class SimpleGUI(App):
    def build(self):
        Window.size = (300,150)
        self.title = "Pass or Fail?"
        self.root = Builder.load_file('simple_GUI.kv')
        return self.root

    def check_result(self, result):
        if 0 <= result < 40:
            self.root.ids.output_mark.text = 'Fail'
        elif 40 <= result <= 64:
            self.root.ids.output_mark.text = 'Pass'
        elif 65 <= result <= 74:
            self.root.ids.output_mark.text = 'Credit'
        elif 75 <= result <= 84:
            self.root.ids.output_mark.text = 'Distinction'
        elif 85 <= result <= 100:
            self.root.ids.output_mark.text = 'High Distinction'
        else:
            self.root.ids.output_mark.text = 'Invalid Result'

    def clear_input(self):
        self.root.ids.input_result.text = ''
        self.root.ids.output_mark.text = ''

SimpleGUI().run()