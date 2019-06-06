from kivy.app import App
from kivy.uix.image import Image

class TestApp(App):

    def build(self):
        image = Image(source='scw-logo.png')
        return image

if __name__ == '__main__':
    TestApp().run()
