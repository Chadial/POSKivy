"""
From Samuel Courses - "Building a POS System with Python and Kivy" Playlist on Youtube
https://www.youtube.com/watch?v=53Jtx3v9ZZU&list=PLW062AfleDZbWPQXjyMeLOlcL8aQ4aLeP&index=7
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

Builder.load_file('admin/admin.kv')


class AdminWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class AdminApp(App):
    def build(self):

        return AdminWindow()


if __name__ == "__main__":
    aa = AdminApp()
    aa.run()