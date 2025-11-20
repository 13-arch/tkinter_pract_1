import tkinter as tk
from tkinter import ttk
from pkg_resources import resource_stream, resource_exists
window = tk.Tk()
window.title("Плеер")
window.tk.call("source", "breeze-dark/breeze-dark.tcl")
ttk.Style().theme_use("breeze-dark")

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_width = int(screen_width * 0.25)
window_height = int(window_width * (10 / 8))
x_pos = int((screen_width - window_width) / 2)
y_pos = int((screen_height - window_height) / 2)
window.geometry(f"{window_width}x{window_height}+{x_pos}+{y_pos}")
window.configure(bg="#1A1A1A")
window.overrideredirect(True)
window.resizable(False, False)

playlist_panel = None

import pygame

def play_music():
    pygame.mixer.init()
    pygame.mixer.music.load("music\Sabi, MIA BOYKA - Базовый минимум (zaycev.net).mp3") 
    pygame.mixer.music.play()

def toggle_playlist():
    global playlist_panel
    if playlist_panel and playlist_panel.winfo_exists():
        playlist_panel.destroy()
        playlist_panel = None
    else:
        playlist_panel = tk.Toplevel(window)
        playlist_panel.title("Список музыки")
        playlist_panel.geometry(f"{window_width}x{window_height}+{x_pos - window_width}+{y_pos}")
        playlist_panel.configure(bg="#1A1A1A")
        playlist_panel.overrideredirect(True)
        playlist_panel.resizable(False, False)

        add_btn = ttk.Button(playlist_panel, text="+ Добавить музыку")
        add_btn.pack(pady=20)

settings_btn = ttk.Button(window, text="⚙", command=lambda: window.attributes("-alpha", 0.5 if window.attributes("-alpha") == 1.0 else 1.0))
settings_btn.place(relx=0.95, rely=0.02, anchor="ne")

cover = tk.Label(window, text="🎵 Обложка", font=('Segoe UI', 14), bg="#1A1A1A", fg="white")
cover.pack(pady=(20, 5))

progress = ttk.Scale(window, from_=0, to=100, orient="horizontal", length=200)
progress.pack(pady=5)

time_label = tk.Label(window, text="1:00", font=('Segoe UI', 10), bg="#1A1A1A", fg="white")
time_label.pack(pady=(0, 10))

button_frame = tk.Frame(window, bg="#1A1A1A")
button_frame.pack(pady=10)

def create_round_button(parent, label, command=None):
    canvas = tk.Canvas(parent, width=64, height=64, bg="#1A1A1A", highlightthickness=0)
    canvas.create_oval(4, 4, 60, 60, fill="#2A2A2A", outline="#444444")
    canvas.create_text(32, 32, text=label, fill="white", font=("Segoe UI", 12, "bold"))
    if command:
        canvas.bind("<Button-1>", lambda e: command())
    return canvas

btn_music = create_round_button(button_frame, "📁", toggle_playlist)
btn_prev = create_round_button(button_frame, "⏮")
btn_pause = create_round_button(button_frame, "⏸",command=play_music)
btn_next = create_round_button(button_frame, "⏭")
btn_pin = create_round_button(button_frame, "📌", lambda: window.attributes("-topmost", not window.attributes("-topmost")))

btn_music.grid(row=0, column=0, padx=8)
btn_prev.grid(row=0, column=1, padx=8)
btn_pause.grid(row=0, column=2, padx=8)
btn_next.grid(row=0, column=3, padx=8)
btn_pin.grid(row=0, column=4, padx=8)

window.bind("<Escape>", lambda e: window.destroy())

window.mainloop()
