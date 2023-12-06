import tkinter as tk
from tkinter import messagebox
from instaloader import *

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Inicio de sesión de Instagram")

        self.instaloader = Instaloader()
        self.username_entry = tk.StringVar()
        self.password_entry = tk.StringVar()
        self.session_status = ""

        self.create_widgets()

        



    def create_widgets(self):
        # Etiqueta y entradas para el inicio de sesión
        login_label = tk.Label(self, text="Iniciar sesión:")
        login_label.pack()

        username_entry = tk.Entry(self, textvariable=self.username_entry)
        username_entry.pack()

        password_entry = tk.Entry(self, textvariable=self.password_entry, show="*")
        password_entry.pack()

        # Botones para el inicio de sesión y registrarse
        login_button = tk.Button(self, text="Iniciar sesión", command=self.login)
        login_button.pack()

        signup_button = tk.Button(self, text="Registrarse", command=self.signup)
        signup_button.pack()

        # Etiqueta y botón para acceder al feed de Instagram
        status_label = tk.Label(self, textvariable=self.session_status)
        status_label.pack()

        go_to_feed_button = tk.Button(self, text="Acceder al feed de Instagram", command=self.go_to_feed)
        go_to_feed_button.pack()

    def login(self):
        try:
            self.instaloader.context.log_in(self.username_entry.get(), self.password_entry.get())
            self.session_status = f"Sesión iniciada para {self.username_entry.get()}"
        except instagramOAuth2Error:
            self.session_status = "Error en el inicio de sesión. Verifica tus credenciales e intenta de nuevo."

    def signup(self):
        messagebox.showinfo("Información", "Por favor, visita https://www.instagram.com/ para registrarte.")

    def go_to_feed(self):
        if self.session_status == "":
            messagebox.showinfo("Error", "Primero debes iniciar sesión.")
        else:
            profile = self.instaloader.context.search_username(self.username_entry.get())
            profile_id = profile.userid
            posts = self.instaloader.get_profile_pic_urls(profile_id)
            for post in posts:
                messagebox.showinfo("Feed de Instagram", f"{self.username_entry.get()}'s feed: {post}")
def get_profile_pic_urls(self, username):
    profile = self.instaloader.context.search_username(username)
    profile_id = profile.userid
    posts = self.instaloader.get_profile_pic_urls(profile_id)
    return posts

app = Application()
app.mainloop()