"""
From Samuel Courses - "Building a POS System with Python and Kivy" Playlist on Youtube
https://www.youtube.com/watch?v=53Jtx3v9ZZU&list=PLW062AfleDZbWPQXjyMeLOlcL8aQ4aLeP&index=8
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.lang import Builder

import re

Builder.load_file('t_operator/operator.kv')


class OperatorWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cart = []
        self.qty = []
        self.total = 0.00

    def update_purchases(self):
        pcode = self.ids.code_inp.text
        products_container = self.ids.products
        if pcode == "1234" or pcode == "2345":
            c_val = (.06, .45, .45, 1)
            details = BoxLayout(size_hint_y=None,
                                height=30,
                                pos_hint={'top': 1})
            products_container.add_widget(details)

            code  = Label(text=pcode, size_hint_x=.2, color=c_val)
            name  = Label(text='Product One', size_hint_x=.3, color=c_val)
            qty   = Label(text='1', size_hint_x=.1, color=c_val)
            disc  = Label(text='0.00', size_hint_x=.1, color=c_val)
            price = Label(text='0.00', size_hint_x=.1, color=c_val)
            total = Label(text='0.00', size_hint_x=.2, color=c_val)
            details.add_widget(code)
            details.add_widget(name)
            details.add_widget(qty)
            details.add_widget(disc)
            details.add_widget(price)
            details.add_widget(total)

            #Update Preview
            pname = "Product One"
            if pcode == "2345":
                pname = "Product Two"
            pprice = 1.00
            pqty = str(1)
            self.total += pprice
            purchase_total = '`\n\nTotal\t\t\t\t\t\t\t\t'+str(self.total)
            self.ids.cur_product.text = pname
            self.ids.cur_price.text = str(pprice)
            preview = self.ids.receipt_preview
            prev_text = preview.text
            _prev = prev_text.find('`')
            if _prev > 0:
                prev_text = prev_text[:_prev]

            ptarget = -1
            for i, c in enumerate(self.cart):
                if c == pcode:
                    ptarget = i

            if ptarget >= 0:
                pqty = self.qty[ptarget]+1
                self.qty[ptarget] = pqty
                expr = '%s\t\tx\d\t'%(pname)
                rexpr = pname+'\t\tx'+str(pqty)+'\t'
                nu_text = re.sub(expr, rexpr, prev_text)
                preview.text = nu_text + purchase_total
            else:
                self.cart.append(pcode)
                self.qty.append(1)
                nu_preview = '\n'.join([prev_text, pname+'\t\tx'+pqty+'\t\t'+str(pprice), purchase_total])
                preview.text = nu_preview


class OperatorApp(App):
    def build(self):
        return OperatorWindow()


if __name__ == "__main__":
    oa = OperatorApp()
    oa.run()
