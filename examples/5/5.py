from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.image import Image

class TestApp(App):

    def build(self):
        layout = GridLayout(cols=2,rows=2)
        layout.add_widget(Button(text="1"))
        layout.add_widget(Button(text="2"))
        layout.add_widget(Button(text="3"))
        layout.add_widget(Image(source='scw-logo.png'))
        return layout

if __name__ == '__main__':
    TestApp().run()
