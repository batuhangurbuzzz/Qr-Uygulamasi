import tkinter as tk 
from tkinter import filedialog
import pyqrcode
from pyqrcode import QRCode

# Functions
def createQR():
    url = labelUrl.get()
    
    if url:
        qrUrl = pyqrcode.create(url)
        filePath = filedialog.asksaveasfilename(defaultextension=".svg", filetypes=[("SVG dosyaları", "*.svg")])
        
        if filePath:
            with open(filePath, 'wb') as f:
                qrUrl.svg(f, scale=8)
            statusLabel.config(text="QR kodu oluşturuldu ve kaydedildi.")

# Design

window = tk.Tk()
window.title("QR Kod Oluşturucu")
label = tk.Label(window, text="URL giriniz:")
labelUrl = tk.Entry(window, width=40)
button = tk.Button(window, text="QR Kodu Oluştur", command=createQR)
statusLabel = tk.Label(window, text="")

label.grid(row=0,column=0, padx=10,pady=10)
labelUrl.grid(row=0,column=1,padx=10,pady=10)
button.grid(row=1,column=0,columnspan=2,padx=10,pady=10)
statusLabel.grid(row=2,column=0,columnspan=2,padx=10,pady=10)


window.mainloop()