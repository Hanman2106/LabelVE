import csv
import kivy
kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.widget import Widget


class label(Widget):
    pass

class labelApp(App):

    def build(self):
        return label()


if __name__ == '__main__':
    labelApp().run()





