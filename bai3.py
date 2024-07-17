import tkinter as tk
from tkinter import ttk

def gui_du_lieu():
    print("Họ:", ho_entry.get())
    print("Tên:", ten_entry.get())
    print("Chức danh:", chuc_danh_entry.get())
    print("Tuổi:", tuoi_spinbox.get())
    print("Quốc tịch:", quoc_tich_entry.get())
    print("Đăng ký:", "Có" if dang_ky_var.get() else "Không")
    print("Số khóa học đã hoàn thành:", hoan_thanh_spinbox.get())
    print("Số học kỳ:", hoc_ky_spinbox.get())
    print("Chấp nhận điều khoản:", "Có" if dieu_khoan_var.get() else "Không")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Biểu mẫu nhập dữ liệu")
root.geometry("500x400")

# Tạo khung thông tin người dùng
khung_tt_nguoi_dung = tk.LabelFrame(root, text="Thông tin người dùng")
khung_tt_nguoi_dung.pack(fill="both", expand="yes", padx=10, pady=10)

tk.Label(khung_tt_nguoi_dung, text="Họ:").grid(row=0, column=0, padx=5, pady=5)
ho_entry = tk.Entry(khung_tt_nguoi_dung)
ho_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(khung_tt_nguoi_dung, text="Tên:").grid(row=0, column=2, padx=5, pady=5)
ten_entry = tk.Entry(khung_tt_nguoi_dung)
ten_entry.grid(row=0, column=3, padx=5, pady=5)

tk.Label(khung_tt_nguoi_dung, text="Chức danh:").grid(row=1, column=0, padx=5, pady=5)
chuc_danh_entry = tk.Entry(khung_tt_nguoi_dung)
chuc_danh_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(khung_tt_nguoi_dung, text="Tuổi:").grid(row=1, column=2, padx=5, pady=5)
tuoi_spinbox = tk.Spinbox(khung_tt_nguoi_dung, from_=0, to=100)
tuoi_spinbox.grid(row=1, column=3, padx=5, pady=5)

tk.Label(khung_tt_nguoi_dung, text="Quốc tịch:").grid(row=2, column=0, padx=5, pady=5)
quoc_tich_entry = tk.Entry(khung_tt_nguoi_dung)
quoc_tich_entry.grid(row=2, column=1, padx=5, pady=5)

# Tạo khung đăng ký
khung_dang_ky = tk.LabelFrame(root, text="Đăng ký")
khung_dang_ky.pack(fill="both", expand="yes", padx=10, pady=10)

dang_ky_var = tk.BooleanVar()
dang_ky_check = tk.Checkbutton(khung_dang_ky, text="Đã đăng ký", variable=dang_ky_var)
dang_ky_check.grid(row=0, column=0, padx=5, pady=5)

tk.Label(khung_dang_ky, text="Số khóa học đã hoàn thành:").grid(row=1, column=0, padx=5, pady=5)
hoan_thanh_spinbox = tk.Spinbox(khung_dang_ky, from_=0, to=100)
hoan_thanh_spinbox.grid(row=1, column=1, padx=5, pady=5)

tk.Label(khung_dang_ky, text="Số học kỳ:").grid(row=2, column=0, padx=5, pady=5)
hoc_ky_spinbox = tk.Spinbox(khung_dang_ky, from_=1, to=10)
hoc_ky_spinbox.grid(row=2, column=1, padx=5, pady=5)

dieu_khoan_var = tk.BooleanVar()
dieu_khoan_check = tk.Checkbutton(khung_dang_ky, text="Chấp nhận điều khoản", variable=dieu_khoan_var)
dieu_khoan_check.grid(row=3, column=0, padx=5, pady=5)

# Nút gửi dữ liệu
nut_gui = tk.Button(root, text="Gửi", command=gui_du_lieu)
nut_gui.pack(pady=20)

# Chạy ứng dụng
root.mainloop()
