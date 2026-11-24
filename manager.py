from tkinter import BOTH, Frame, Tk

from container import Container
from login import Login, Registro

class Manager(Tk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.title("sistema de punto de venta")
        self.resizable(False,False)
        self.geometry("1150x650+120+50")
        
        self.container = Frame(self, bg="#dcdcdc")
        self.container.pack(fill=BOTH, expand=True)
        
        self.frames = {}
        for frame_class in (Login, Registro, Container):
            frame = frame_class(self.container, self)
            self.frames[frame_class] = frame
            frame.place(x=0, y=0, relwidth=1, relheight=1)

        self.show_frame(Container)

    def show_frame(self, frame_class, user=None):
        frame = self.frames[frame_class]

        if user is not None:
            if frame_class is Container:
                frame.user = user
            else:
                frame.logged_user = user

        frame.tkraise()