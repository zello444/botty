import tkinter as tk
    
def close_app():
    root.destroy()

def minimize_app():
    root.iconify()

def start_move(event):
    root.x = event.x
    root.y = event.y

def move_app(event):
    x = root.winfo_x() + (event.x - root.x)
    y = root.winfo_y() + (event.y - root.y)
    root.geometry(f"+{x}+{y}")

root = tk.Tk()
root.title("Schwebender Text")
root.geometry("400x300+500+200")
root.attributes('-alpha', 0.2)
root.attributes('-topmost', True)  # Fenster bleibt immer im Vordergrund
root.configure(bg='black')
root.overrideredirect(True)

# Header-Leiste für Steuerung
header = tk.Frame(root, bg='white', height=30)
header.pack(fill=tk.X, side=tk.TOP)
header.bind("<ButtonPress-1>", start_move)
header.bind("<B1-Motion>", move_app)

# Buttons oben rechts
close_btn = tk.Button(header, text="X", command=close_app, fg="red", bg="white", relief="flat")
close_btn.pack(side=tk.RIGHT, padx=5)

minimize_btn = tk.Button(header, text="_", command=minimize_app, fg="red", bg="white", relief="flat")
minimize_btn.pack(side=tk.RIGHT)

# Scrollbarer Textbereich
frame = tk.Frame(root, bg='black')
frame.pack(fill=tk.BOTH, expand=True)

text_widget = tk.Text(frame, wrap="word", font=("Arial", 14), fg="black", bg="white", padx=10, pady=10)
text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(frame, command=text_widget.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
text_widget.config(yscrollcommand=scrollbar.set)

# Beispieltext
text_widget.insert(tk.END, "text text text\n."*100)
text_widget.config(state=tk.DISABLED)

# Escape-Taste zum Schließen

root.mainloop()
