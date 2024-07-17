import tkinter as tk
from tkinter import messagebox

class FrameRecorderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ghi Hình")
        self.root.geometry("600x300")
        self.root.configure(bg='pink')

        self.create_widgets()

    def create_widgets(self):
        title_label = tk.Label(self.root, text="Ghi Hình", font=("Helvetica", 24), bg='pink')
        title_label.pack(pady=20)

        fps_frame = tk.Frame(self.root, bg='pink')
        fps_frame.pack(pady=10)
        fps_label = tk.Label(fps_frame, text="FPS:", bg='pink')
        fps_label.pack(side=tk.LEFT)
        self.fps_entry = tk.Entry(fps_frame)
        self.fps_entry.pack(side=tk.LEFT)

        button_frame = tk.Frame(self.root, bg='pink')
        button_frame.pack(pady=10)
        pause_button = tk.Button(button_frame, text="Tạm dừng", command=self.pause_recording)
        pause_button.pack(side=tk.LEFT, padx=5)
        start_button = tk.Button(button_frame, text="Bắt đầu", command=self.start_recording)
        start_button.pack(side=tk.LEFT, padx=5)
        end_button = tk.Button(button_frame, text="Kết thúc", command=self.end_recording)
        end_button.pack(side=tk.LEFT, padx=5)

        self.status_label = tk.Label(self.root, text="Đang tạm dừng ghi hình", bg='pink', font=("Helvetica", 14))
        self.status_label.pack(pady=10)

    def pause_recording(self):
        self.status_label.config(text="Đang tạm dừng ghi hình")
        messagebox.showinfo("Hành động", "Đã tạm dừng ghi hình")

    def start_recording(self):
        self.status_label.config(text="Đang bắt đầu ghi hình")
        messagebox.showinfo("Hành động", "Đã bắt đầu ghi hình")

    def end_recording(self):
        fps_value = self.fps_entry.get()
        self.status_label.config(text="Đã kết thúc ghi hình")
        messagebox.showinfo("Hành động", f"Đã kết thúc ghi hình\nGiá trị FPS: {fps_value}")

if __name__ == "__main__":
    root = tk.Tk()
    app = FrameRecorderApp(root)
    root.mainloop()
