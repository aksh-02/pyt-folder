from kivy.app import App
from kivy.uix.button import Button

class Hello(App):
  def build(self):
    return Button(text='My first App')
if __name__=='__main__':
  Hello().run()
