from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.codeinput import CodeInput
from pygments.lexers import HtmlLexer

from kivy.config import Config
Config.set('graphics', 'resizable', '0');
Config.set('graphics', 'width', '640');
Config.set('graphics', 'height', '480');

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter

class MyApp(App):
  def build(self):

      s =  Scatter()
      fl = FloatLayout(size=(300, 300))
      s.add_widget(fl)
      fl.add_widget(Button(text = "Knopka!",
        font_size = 16,
        on_press = self.btn_press,
        background_color = [1, 0, 0, 1],
        background_normal = '' ,
        size_hint = (.5, .25),
        pos = (640 / 2 - 160, 480 / 2 - (480 * 0.25 / 2)))); #(160,180)

      return s

  def btn_press(self, instance):
    print("Knopka Natysnuta!")
    instance.text = "Ja natysnuta"

if __name__ == "__main__":
  MyApp().run()
