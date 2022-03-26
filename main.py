import Tkinter as tk
import qrcode
from PIL import ImageTk,Image
from resizeimage import resizeimage
from tkinter import messagebox
import random
from datetime import  datetime


class QR:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1000x600+0+0")
        self.root.title("QR code generator")

        self.qr_link = tk.StringVar()

        tk.Label(root, text="QR Generator", bd=10, relief=tk.RIDGE, bg="#e1ff59", pady=2,
              font=("Helvetica", 30, "bold")).pack(fill=tk.X)
        Q = tk.LabelFrame(root, bg="#ebb8ff", font=("Helvetica", 15, "bold"), bd=10, relief=tk.RIDGE)
        Q.place(x=0, y=80,width=500,height=370)
        tk.Label(Q, text="Enter Link:-", font=("Helvetica", 20, "bold"), bg="#ebb8ff").grid(row=0, column=0, padx=5,
                                                                                          pady=10)
        tk.Entry(Q, font=("Helvetica", 15, "bold"), relief=tk.SUNKEN, bd=8,
                 width=10,textvariable=self.qr_link).place(x=70,y=60,width=400,height=80)

        Q1 = tk.LabelFrame(root, bg="#ebb8ff", font=("Helvetica", 15, "bold"), bd=10, relief=tk.RIDGE)
        Q1.place(x=0, y=450, width=500, height=150)

        tk.Button(Q1, text="GENERATE", font=("Helvetica", 15, "bold"), bg="#74f7bf", bd=8, relief=tk.RIDGE, width=10,
                  height=3,command=self.QRcode).grid(row=0,column=0,padx=15,pady=15)
        tk.Button(Q1, text="SAVE", font=("Helvetica", 15, "bold"), bg="#74f7bf", bd=8, relief=tk.RIDGE, width=10,
                  height=3, command=self.save).grid(row=0, column=1, padx=15, pady=15)

        self.Q2 = tk.LabelFrame(root,text ="QR CODE", bg="#ebb8ff", font=("Helvetica", 15, "bold"), bd=10, relief=tk.RIDGE)
        self.Q2.place(x=500, y=80, width=500, height=520)
        self.qrcode = tk.Label(self.Q2,text="No QR code \navailable",font=("Helvetica", 15, "bold"),bd=10)
        self.qrcode.place(x=100,y=100,width=300,height=300)

    def QRcode(self):
        self.qr_code = qrcode.make(self.qr_link.get())
        self.qr_code = resizeimage.resize_cover(self.qr_code, [300, 300])
        self.im=ImageTk.PhotoImage(self.qr_code)




        self.qrcode.config(image=self.im)
    def save(self):
        if self.qr_link.get()=="":
            tk.messagebox.showinfo("WARNING", "Please Enter Link")


        # datetime object containing current date and time
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")

        self.no = tk.IntVar()
        x = random.randint(1000, 9999)
        self.no.set(x)

        self.qr_code.save("QR- "+str(self.no.get())+'.png')

        tk.messagebox.showinfo("SAVED", "QR code saved succesfully")


root = tk.Tk()
obj = QR(root)
root.mainloop()
