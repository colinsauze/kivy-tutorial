from kivy.app import App
from kivy.uix.button import Button

class TestApp(App):

    def build(self):
        button = Button(text='Hello world')
        button.bind(on_press=self.callback)
        return button

    def callback(self,event):
        print("Pressed Button")


if __name__ == '__main__':
    TestApp().run()
