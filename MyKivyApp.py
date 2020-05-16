from kivy.app import App
from kivy.uix.button import *
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import AsyncImage
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
import random
from kivy.uix.popup import Popup

class MyLayout(GridLayout):

    url_ans_dict = {
        "https://homepages.cae.wisc.edu/~ece533/images/airplane.png": ("airplane", "bird"),
        "https://homepages.cae.wisc.edu/~ece533/images/baboon.png": ("Baboon", "Human"),
        "https://homepages.cae.wisc.edu/~ece533/images/cat.png": ("Cat", "Tiger"),
        "https://homepages.cae.wisc.edu/~ece533/images/girl.png": ('Girl', "Car")
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.load_new_image(url=list(self.url_ans_dict.keys())[0])

    def ans_correct_callback(self, url, instance):
        print(f"This button was called - {instance.text}")
        if self.url_ans_dict.get(url)[0] == instance.text:
            print("Correct answer")
            correct = True
        else:
            print("Wrong Answer")
            correct = False
        self.show_popup(correct)
        self.clear_widgets()
        rand_int = random.randint(1, len(list(self.url_ans_dict.keys()))-1)
        self.load_new_image(list(self.url_ans_dict.keys())[rand_int])

    def show_popup(self, correct):
        layout = GridLayout(cols=1, padding=10)
        label = Label(text="Correct") if correct else Label(text="Wrong Answer")
        layout.add_widget(label)
        popup = Popup(title="", content=layout, size_hint=(None, None), size=(200, 200), auto_dismiss=True)
        popup.open()

    def load_new_image(self, url):

        self.ans_button = self.url_ans_dict.get(url)
        self.add_widget(AsyncImage(source=url))
        self.bottom_layout = FloatLayout(size=(600, 600))
        self.ans_1 = Button(text=self.ans_button[0],
                   background_color=(0.1, 0.5, 0.3, 1),
                   size_hint=(0.2, 0.2),
                   pos_hint={'x': 0.3, 'y': 0.5}
                   )
        buttoncallback = lambda *args: self.ans_correct_callback(url, *args)
        self.ans_1.bind(on_press=buttoncallback)
        self.bottom_layout.add_widget(
            self.ans_1
        )
        self.ans_2 = Button(
            text=self.ans_button[1],
            background_color=(0.1, 0.5, 0.3, 1),
            size_hint=(0.2, 0.2),
            pos_hint={'x': 0.5, 'y': 0.5}

        )
        self.ans_2.bind(on_press=buttoncallback)
        self.bottom_layout.add_widget(self.ans_2)
        self.add_widget(self.bottom_layout)


class MyKivyApp(App):

    def build(self):
        Window.clearcolor = (1,1,1,1)
        return MyLayout()

    def on_start(self):
        print("This method on start is fired!!!!!!!!")

    def on_stop(self):
        print("This method is called after the app ends")


if __name__ == '__main__':
    MyKivyApp().run()


