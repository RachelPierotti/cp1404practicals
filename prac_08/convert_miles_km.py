"""Convert Miles to Kilometres Program"""
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class MilesToKilometres(App):
    "Convert miles to kilometres."

    def build(self):
        "Build app."
        self.title = "Miles To Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_conversion(self):
        """Conversion calculation: miles to kilometres"""
        miles = self.get_valid_miles()
        kilometres = miles * MILES_TO_KM
        self.root.ids.output_kilometres.text = str(kilometres)

    def handle_increment(self, increment):
        """Change miles value by a positive or negative increment of 1"""
        miles = self.get_valid_miles() + increment
        self.root.ids.input_miles.text = str(miles)
        self.handle_conversion()

    def get_valid_miles(self):
        """Get a valid input"""
        try:
            miles = float(self.root.ids.input_miles.text)
            return miles
        except ValueError:
            return 0.0


MilesToKilometres().run()

# commit properly