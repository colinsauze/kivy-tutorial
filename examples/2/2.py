from kivy.app import App
from kivy.uix.label import Label

class TestApp(App):
    def build(self):
        l = Label(text="Hello world")
        return l

if __name__ == '__main__':
    TestApp().run()
