import tkinter as tk

#Warna
WARNA_BG = "#2A1A0E"
WARNA_INPUT = "#D4621A"
WARNA_TEKS = "#FEF3E2"
WARNA_HASIL = "#F4AE52"

root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("420x680")

root.config(bg=WARNA_BG)

#Label judul
label_judul = tk.Label(
    root,
    text="Aplikasi Prediksi Prodi Pilihan",
    font=("Arial", 18, "bold"),
    bg=WARNA_BG,
    fg=WARNA_TEKS
)
label_judul.pack(pady=20)

root.mainloop()

#Frame untuk 10 input nilai
frame_input = tk.Frame(root, bg=WARNA_BG)
frame_input.pack()

for i in range(10):
    label_nilai = tk.Label(
        frame_input,
        text="Nilai Mata Pelajaran " + str(i + 1) + ":",
        font=("Arial", 12),
        bg=WARNA_BG,
        fg=WARNA_TEKS
    )
    label_nilai.grid(row=i, column=0, sticky="e", padx=10, pady=4)