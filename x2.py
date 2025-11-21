import tkinter as tk
from tkinter import ttk, filedialog
import pygame
import time

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
playlist_box = None
playlist = []
current_index = -1
track_length = 0.0
is_playing = False
is_paused = False
start_time = 0.0
current_offset = 0.0

pygame.mixer.init()

def play_music(file_path, start_pos=0.0):
    global track_length, is_playing, is_paused, start_time, current_offset
    pygame.mixer.music.load(file_path)
    try:
        pygame.mixer.music.play(start=start_pos)
    except:
        pygame.mixer.music.play()
        start_pos = 0.0
    track_length = float(pygame.mixer.Sound(file_path).get_length())
    progress.config(to=int(track_length))
    current_offset = float(start_pos)
    start_time = time.time()
    is_playing = True
    is_paused = False
    if 'btn_pause' in globals() and btn_pause:
        btn_pause.itemconfig("icon", text="⏸")

def add_music():
    global current_index
    file_path = filedialog.askopenfilename(
        title="Выберите аудиофайл",
        filetypes=[("Аудио файлы", "*.mp3 *.wav *.ogg")]
    )
    if file_path:
        playlist.append(file_path)
        if playlist_box:
            playlist_box.insert(tk.END, file_path.split("/")[-1])
        current_index = len(playlist) - 1
        play_music(file_path, 0.0)

def play_selected(event):
    global current_index
    selection = playlist_box.curselection()
    if selection:
        current_index = selection[0]
        file_path = playlist[current_index]
        play_music(file_path, 0.0)

def play_next():
    global current_index
    if playlist and current_index < len(playlist) - 1:
        current_index += 1
        play_music(playlist[current_index], 0.0)
        if playlist_box:
            playlist_box.selection_clear(0, tk.END)
            playlist_box.selection_set(current_index)

def play_prev():
    global current_index
    if playlist and current_index > 0:
        current_index -= 1
        play_music(playlist[current_index], 0.0)
        if playlist_box:
            playlist_box.selection_clear(0, tk.END)
            playlist_box.selection_set(current_index)

def pause_or_resume():
    global is_playing, is_paused, current_offset, start_time
    if is_playing and not is_paused:
        pygame.mixer.music.pause()
        current_offset = get_display_pos()
        is_paused = True
        if 'btn_pause' in globals() and btn_pause:
            btn_pause.itemconfig("icon", text="▶️")
    elif is_playing and is_paused:
        pygame.mixer.music.unpause()
        start_time = time.time()
        is_paused = False
        if 'btn_pause' in globals() and btn_pause:
            btn_pause.itemconfig("icon", text="⏸")
    else:
        if playlist and 0 <= current_index < len(playlist) and track_length > 0:
            try:
                pygame.mixer.music.play(start=current_offset)
            except:
                pygame.mixer.music.play()
                current_offset = 0.0
            start_time = time.time()
            is_playing = True
            is_paused = False
            if 'btn_pause' in globals() and btn_pause:
                btn_pause.itemconfig("icon", text="⏸")

def toggle_playlist():
    global playlist_panel, playlist_box
    if playlist_panel and playlist_panel.winfo_exists():
        playlist_panel.destroy()
        playlist_panel = None
        playlist_box = None
    else:
        playlist_panel = tk.Toplevel(window)
        playlist_panel.title("Список музыки")
        playlist_panel.geometry(f"{window_width}x{window_height}+{x_pos - window_width}+{y_pos}")
        playlist_panel.configure(bg="#1A1A1A")
        playlist_panel.overrideredirect(True)
        playlist_panel.resizable(False, False)
        add_btn = ttk.Button(playlist_panel, text="+ Добавить музыку", command=add_music)
        add_btn.pack(pady=10)
        playlist_box = tk.Listbox(playlist_panel, bg="#1A1A1A", fg="white", selectbackground="#444444")
        playlist_box.pack(fill="both", expand=True, padx=10, pady=10)
        playlist_box.bind("<Double-Button-1>", play_selected)

def toggle_transparency_slider():
    if getattr(window, "transparency_panel", None) and window.transparency_panel.winfo_exists():
        window.transparency_panel.destroy()
        window.transparency_panel = None
    else:
        panel_width = 200
        panel_height = 80
        panel_x = x_pos + window_width // 2 - panel_width // 2
        panel_y = y_pos - panel_height - 10
        window.transparency_panel = tk.Toplevel(window)
        window.transparency_panel.geometry(f"{panel_width}x{panel_height}+{panel_x}+{panel_y}")
        window.transparency_panel.configure(bg="#1A1A1A")
        window.transparency_panel.overrideredirect(True)
        window.transparency_panel.attributes("-topmost", True)
        label = tk.Label(window.transparency_panel, text="Прозрачность", font=("Segoe UI", 10), bg="#1A1A1A", fg="white")
        label.pack(pady=(10, 0))
        def update_alpha(val):
            alpha = float(val) / 100
            window.attributes("-alpha", alpha)
        alpha_slider = ttk.Scale(window.transparency_panel, from_=30, to=100, orient="horizontal", command=update_alpha)
        current_alpha = window.attributes("-alpha") if window.attributes("-alpha") is not None else 1.0
        alpha_slider.set(current_alpha * 100)
        alpha_slider.pack(pady=(5, 10))

def get_display_pos():
    if is_playing and not is_paused:
        return current_offset + (time.time() - start_time)
    else:
        return current_offset

def update_progress():
    pos = get_display_pos()
    if track_length > 0:
        if pos > track_length:
            pos = track_length
        progress.set(pos)
        time_label.config(text=f"{int(pos//60)}:{int(pos%60):02d} / {int(track_length//60)}:{int(track_length%60):02d}")
    window.after(200, update_progress)

def seek_music(val):
    global current_offset, start_time, is_playing, is_paused
    target = float(val)
    if track_length <= 0:
        return
    if target < 0:
        target = 0.0
    if target > track_length:
        target = track_length
    current_offset = target
    if playlist and 0 <= current_index < len(playlist):
        try:
            pygame.mixer.music.play(start=target)
        except:
            pygame.mixer.music.play()
            current_offset = 0.0
        start_time = time.time()
        is_playing = True
        is_paused = False
        if 'btn_pause' in globals() and btn_pause:
            btn_pause.itemconfig("icon", text="⏸")

settings_btn = ttk.Button(window, text="⚙", command=toggle_transparency_slider)
settings_btn.place(relx=0.95, rely=0.02, anchor="ne")

cover = tk.Label(window, text="🎵 Обложка", font=('Segoe UI', 14), bg="#1A1A1A", fg="white")
cover.pack(pady=(20, 5))

progress = ttk.Scale(window, from_=0, to=100, orient="horizontal", length=200, command=seek_music)
progress.pack(pady=5)

time_label = tk.Label(window, text="0:00 / 0:00", font=('Segoe UI', 10), bg="#1A1A1A", fg="white")
time_label.pack(pady=(0, 10))

button_frame = tk.Frame(window, bg="#1A1A1A")
button_frame.pack(pady=10)

def create_round_button(parent, label, command=None):
    canvas = tk.Canvas(parent, width=64, height=64, bg="#1A1A1A", highlightthickness=0)
    canvas.create_oval(4, 4, 60, 60, fill="#2A2A2A", outline="#444444")
    canvas.create_text(32, 32, text=label, fill="white", font=("Segoe UI", 12, "bold"), tags="icon")
    if command:
        canvas.bind("<Button-1>", lambda e: command())
    return canvas

btn_music = create_round_button(button_frame, "📁", toggle_playlist)
btn_prev = create_round_button(button_frame, "⏮", play_prev)
btn_pause = create_round_button(button_frame, "⏸", pause_or_resume)
btn_next = create_round_button(button_frame, "⏭", play_next)
btn_pin = create_round_button(button_frame, "📌", lambda: window.attributes("-topmost", not window.attributes("-topmost")))

btn_music.grid(row=0, column=0, padx=8)
btn_prev.grid(row=0, column=1, padx=8)
btn_pause.grid(row=0, column=2, padx=8)
btn_next.grid(row=0, column=3, padx=8)
btn_pin.grid(row=0, column=4, padx=8)

update_progress()
window.bind("<Escape>", lambda e: window.destroy())
window.mainloop()
    