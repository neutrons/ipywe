# coding: utf-8


import traitlets
import ipywidgets as ipyw
from IPython.display import display, HTML, clear_output
from ._utils import js_alert


class Context:
    pass


class Step(traitlets.HasTraits):

    layout = ipyw.Layout(border="1px lightgray solid",
                         margin='5px', padding='15px')
    button_layout = ipyw.Layout(margin='10px 5px 5px 5px')

    def __init__(self, context):
        super(Step, self).__init__()
        self.context = context
        self.panel = self.createPanel()
        return

    def createPanel(self):
        raise NotImplementedError

    def show(self):
        display(self.panel)

    def remove(self):
        close(self.panel)

    def handle_next_button_click(self, s):
        if not self.validate():
            return
        self.remove()
        self.nextStep()

    def validate(self):
        raise NotImplementedError

    def nextStep(self):
        raise NotImplementedError


def close(w):
    "recursively close a widget"
    if hasattr(w, 'children'):
        for c in w.children:
            close(c)
            continue
    w.close()
    return
