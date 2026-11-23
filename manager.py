from tkinter import *
from tkinter import ttk,messagebox
from container import Container

class Manager(Tk):
    def __int__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.title("sistema de punto de venta")
        self.resizable(False,False)
        self.geometry("1150x650+120+50")
        
        self.container = Frame(self, bg="#dcdcdc")
        self.container.pack(fill=BOTH, expand=True)
        
        self.frames = {}
        for i in (Container):
            frame = i(self.container, self)
            self.frames[i] = frame
            
    def show_frame(self, frame_class, user=None):
        frame = self.frames[frame_class]
        
        if user is not None:
            frame.set_User(user)
        
        frame.tkraise
        
    def main():
        app = Manager
        app.mainloop()
        
    if __name__ == "__main__":
        main()