import tkinter as tk

from dashboard import Dashboard
from ventas import Ventas


class Container(tk.Frame):
    def __init__(self, padre, controlador, user=None):
        super().__init__(padre)
        self.controlador = controlador
        self.user = user
        self.place(x=0, y=0, relwidth=1, relheight=1)
        self.frames = {}
        self.widgets()

        for frame_class in (Dashboard, Ventas):
            frame = frame_class(self)
            self.frames[frame_class] = frame
            frame.config(
                bg="#dcdcdc",
                highlightbackground="gray",
                highlightthickness=1,
            )
            frame.place(x=200, y=50, width=900, height=600)

        self.show_frames(Dashboard)

    def show_frames(self, frame_class):
        self.frames[frame_class].tkraise()

    def dashboard(self):
        self.show_frames(Dashboard)

    def ventas(self):
        self.show_frames(Ventas)

    def widgets(self):
        tk.Label(self, text="Frame principal").place(x=20, y=20)
        tk.Button(self, text="Dashboard", command=self.dashboard).place(
            x=20, y=70, width=160, height=35
        )
        tk.Button(self, text="Ventas", command=self.ventas).place(
            x=20, y=115, width=160, height=35
        )
