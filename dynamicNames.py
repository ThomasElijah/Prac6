from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty
from kivy.core.window import Window

class AgeDisplayer(App):
    status_text = StringProperty()

    def __init__(self):
        super().__init__()
        self.nameFile = open("names", "r")
        self.name_dict = {}
        for line in self.nameFile:
            name, age = line.strip().split(',')
            self.name_dict[name] = age


    def build(self):
        self.title = "Name -> Age"
        self.root = Builder.load_file('dynamicNames.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for key in self.name_dict:
            new_button = Button(text=key)
            new_button.bind(on_release=self.handle_button_press)
            self.root.ids.entriesBox.add_widget(new_button)

    def handle_button_press(self, instance):
        name = instance.text
        self.status_text = "{}".format(self.name_dict[name])


AgeDisplayer().run()
