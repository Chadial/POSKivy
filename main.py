from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from admin.admin import AdminWindow
from signin.signin import SigninWindow
from t_operator.t_operator import OperatorWindow


class MainWindow(BoxLayout):
    admin_widget = AdminWindow()
    signin_widget = SigninWindow()
    operator_widget = OperatorWindow()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class MainApp(App):
    def build(self):

        return MainWindow()


if __name__ == "__main__":
    MainApp().run()