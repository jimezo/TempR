from kivy.app import App
from kivy.uix.button import Button
from kivy.config import Config
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.graphics import Rectangle


from time import sleep

Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 400)
Config.set('graphics', 'height', 500)


class Calculate(App):


    def build(self):

        calc_elements = ['(', ')', 'C', '/',
                        '7', '8', '9', 'X',
                        '4', '5', '6', '-',
                        '1', '2', '3', '+',
                        '<--', '0', '.', '=',]


        gl = GridLayout(cols=4, size_hint = (1, .9))
        bl = BoxLayout(orientation='vertical', padding = [10,10])

        self.app_size = Config.get('graphics', 'width'), Config.get('graphics', 'height')

        self.num_label = Label(halign = 'right',
                            valign = 'middle',
                            font_size = 35,
                            text_size = (int(self.app_size[0]) - 20, int(self.app_size[1])),
                            )

        bl.add_widget( self.num_label )

        for elem in calc_elements:
            if (not elem):
                gl.add_widget( Widget() )
            else:
                gl.add_widget( Button( text = elem,
                                       on_press = self.Pressed,
                                    ))

        bl.add_widget( gl )

        return bl


    def Pressed(self, instance):

        if (self.num_label.text == 'Синтаксическая ошибка'):
            self.num_label.text = self.old_text
            return

        if (self.num_label.text == 'Отсутсвует знак до скобки'):
            self.num_label.text = self.old_text
            return

        # Очистка поля
        if (instance.text == 'C'):
            self.num_label.text = ''
            return

        if (instance.text == '<--'):
            length_text = len(self.num_label.text)
            self.num_label.text = self.num_label.text[:length_text-1]
            return

        # Подсчет результата
        if (instance.text == '='):
            try:
                self.num_label.text = str(eval(self.num_label.text))
            except SyntaxError:
                self.old_text = self.num_label.text
                self.num_label.text = 'Синтаксическая ошибка'
            except TypeError:
                self.old_text = self.num_label.text
                self.num_label.text = 'Отсутсвует знак до скобки'
            return

        if (str(instance.text).lower() == 'x'):
            self.num_label.text += '*'
            return

        self.num_label.text += instance.text


if __name__ == '__main__':
    Calculate().run()
