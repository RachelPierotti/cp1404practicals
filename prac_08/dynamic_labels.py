"""Dynamic Labels - simple app"""
# Create a very simple app that has a list of names (strings)
# and dynamically creates a separate Label for each one.

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty


class DynamicLabelsApp(App):
    status_text = StringProperty()

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.list_of_names = ["Bob Brown", "Cat Cyan", "Oren Ochre"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create labels for names"""
        for name in self.list_of_names:
            # create a label for each name
            temp_label = Button(text=name)
            # add to layout
            self.root.ids.main.add_widget(temp_label)


DynamicLabelsApp().run()

# commit properly