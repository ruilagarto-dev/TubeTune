import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import os
import re

class TubeTuneApp:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.initialize()
        self.controller = None
        
        default_path = "downloads_music"
        os.makedirs(default_path, exist_ok=True)

        self.destinationPath = tk.StringVar(value=default_path)
        self.link_entry = None
        
    def initialize(self):
        self.app = tk.Tk()
        self.app.title("YouTube Audio Downloader")
        self.app.geometry(f"{self.width}x{self.height}")
        self.app.resizable(False, False)

    def run(self):
        self.app.mainloop()

    def set_controller(self, controller):
        self.controller = controller
        self.createWidgets()

    def createWidgets(self):
        # Frame principal
        main_frame = tk.Frame(self.app)
        main_frame.pack(pady=10)

        # Link do YouTube
        tk.Label(main_frame, text="Insira o link do YouTube:").pack()
        self.link_entry = tk.Entry(main_frame, width=50)
        self.link_entry.pack(pady=5)

        # Pasta destino
        tk.Label(main_frame, text="Pasta Destino:").pack()
        path_frame = tk.Frame(main_frame)
        path_frame.pack()
        
        tk.Entry(path_frame, textvariable=self.destinationPath, width=40).pack(side=tk.LEFT, padx=5)
        tk.Button(path_frame, text="...", command=self.selectPath, width=3).pack(side=tk.LEFT)

        # Botões de ação
        button_frame = tk.Frame(main_frame)
        button_frame.pack(pady=10)
        
        tk.Button(button_frame, text="Baixar Música", command=self.controller.download_music).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Baixar Playlist", command=self.controller.download_playlist).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Limpar", command=self.clearFields).pack(side=tk.LEFT, padx=5)

    def selectPath(self):
        path = filedialog.askdirectory()
        if path:
            self.destinationPath.set(path)

    def clearFields(self):
        self.link_entry.delete(0, tk.END)

    def show_message(self, msg_type, text):
        messagebox.showinfo(msg_type, text) if msg_type == "Info" else \
        messagebox.showwarning(msg_type, text) if msg_type == "Warning" else \
        messagebox.showerror(msg_type, text)

    def get_link(self):
        return self.link_entry.get().strip()

    def get_destination(self):
        return self.destinationPath.get().strip()
