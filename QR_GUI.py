import customtkinter
import tkinter as tk
from qr0_get_matrix import get_qr_matrix
import os


customtkinter.set_appearance_mode("dark")

customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()

root.geometry("700x600")

root.title("QR-GEN")



frametop = customtkinter.CTkFrame(master=root)
frametop.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)


qr = customtkinter.CTkFrame(master=frametop)
qr.grid(row=1, column=1, sticky="", padx=10, pady=10)


root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

def rowconfig_frametop():
  frametop.grid_rowconfigure(0, weight=1)
  frametop.grid_rowconfigure(1, weight=1)
  frametop.grid_rowconfigure(2, weight=1)
  frametop.grid_rowconfigure(3, weight=1)
  frametop.grid_rowconfigure(4, weight=1)

  frametop.grid_columnconfigure(0, weight=1)
  frametop.grid_columnconfigure(1, weight=1)
  frametop.grid_columnconfigure(2, weight=1)

rowconfig_frametop()


qr.grid_rowconfigure(0, weight=1)
qr.grid_columnconfigure(0, weight=1)

def show_qr():
   global url_global
   url = entry1.get()
   if url.strip() == "":
      ...
   else:
      entry1.delete(0, "end")
      button1.configure(state="normal")
      generate_code(url)
      url_global = url


def generate_code(url):
    qr_matrix = get_qr_matrix(url)
    display(qr_matrix)


def lagre():
    from PIL import ImageGrab
    x = qr.winfo_rootx()
    y = qr.winfo_rooty()
    width = qr.winfo_width()
    height = qr.winfo_height()



    screenshot = ImageGrab.grab(bbox=(x, y, x + width, y + height))
    os.makedirs("qr_koder", exist_ok=True)
    screenshot.save(f"qr_koder\qr_kode_{url_global}.png")



def display(matrix):
    from qr1_draw import draw_qr
    canvas = tk.Canvas(qr, width=400, height=400, bg='white')
    canvas.grid(row=0, column=0, sticky="", padx=10, pady=10)
    draw_qr(canvas, 25, 25, 350, matrix)



# Tom qr kode
from qr1_draw import draw_qr
canvas = tk.Canvas(qr, width=400, height=400, bg='white')
canvas.grid(row=0, column=0, sticky="", padx=10, pady=10)
draw_qr(canvas, 25, 25, 350, ([0, 0], [0, 0]))




label = customtkinter.CTkLabel(master=frametop, text="QR kode generator", font=("roboto", 24, "bold"))
label.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)




entry1 = customtkinter.CTkEntry(master=frametop, placeholder_text= "Skriv inn en link", font=("roboto", 12, "bold"), width=200)
entry1.grid(row=2, column=1, sticky="ews", padx=10, pady=5)


button = customtkinter.CTkButton(master=frametop, text="Generer", command=show_qr, fg_color="green", font=("roboto", 12, "bold"),
                                  corner_radius=32, width=20)

button.grid(row=3, column=1, padx=10, pady=5, sticky="n")


button1 = customtkinter.CTkButton(master=frametop, text="Lagre", command=lagre, fg_color="purple", font=("roboto", 12, "bold"),
                                  corner_radius=32, width=20, state="disabled")

button1.grid(row=3, column=1, padx=10, pady=5, sticky="s")




entry1.bind("<Return>", lambda event: show_qr())


root.mainloop()