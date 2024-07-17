import tkinter as tk
from tkinter import messagebox

class AntivirusApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AtarBals Modern Antivirus")
        self.root.geometry("800x500")
        self.root.configure(bg='white')

        self.create_widgets()

    def create_widgets(self):
        # Sidebar
        sidebar = tk.Frame(self.root, width=150, bg='blue', height=500, relief='sunken', borderwidth=2)
        sidebar.pack(expand=False, fill='both', side='left', anchor='nw')

        buttons = ["Trạng thái", "Cập nhật", "Cài đặt", "Phản hồi", "Mua Premium", "Trợ giúp", "Quét ngay"]
        for button in buttons:
            b = tk.Button(sidebar, text=button, bg='green' if button == "Quét ngay" else 'white', fg='black', command=lambda b=button: self.button_click(b))
            b.pack(fill='x', pady=5, padx=5)

        # Main area
        main_area = tk.Frame(self.root, bg='white')
        main_area.pack(expand=True, fill='both', side='right')

        self.title_label = tk.Label(main_area, text="Quét", font=("Helvetica", 24), bg='white')
        self.title_label.pack(pady=20)

        self.subtitle_label = tk.Label(main_area, text="Premium sẽ miễn phí mãi mãi. Bạn chỉ cần nhấn các nút.", bg='white')
        self.subtitle_label.pack(pady=10)

        scan_buttons = ["Quét nhanh", "Bảo vệ web", "Cách ly", "Quét toàn bộ", "Cập nhật đơn giản"]
        for scan_button in scan_buttons:
            b = tk.Button(main_area, text=scan_button, bg='magenta', fg='white', width=20, command=lambda b=scan_button: self.scan_action(b))
            b.pack(pady=5, padx=20)

        self.status_label = tk.Label(main_area, text="Nhận Premium để kích hoạt: (Bảo vệ web), (Quét toàn bộ), (Cập nhật đơn giản)", bg='white', fg='magenta')
        self.status_label.pack(side='bottom', pady=20)

    def button_click(self, button):
        messagebox.showinfo("Nút đã được nhấn", f"Bạn đã nhấn nút '{button}'")
        if button == "Quét ngay":
            self.status_label.config(text="Đang quét...")

    def scan_action(self, action):
        self.status_label.config(text=f"{action} đang tiến hành...")
        messagebox.showinfo("Hành động quét", f"{action} đã bắt đầu")

if __name__ == "__main__":
    root = tk.Tk()
    app = AntivirusApp(root)
    root.mainloop()
