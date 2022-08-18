import ntplib
import datetime, time
from datetime import timedelta
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import askyesno
import string
import os
import base64
from random import *

try:
    #pravimo prozor i konektujemo sa na server za trenutno vreme
    glavni_prozor = Tk()
    glavni_prozor.geometry("400x250")

    def uzmi_vreme():
        client = ntplib.NTPClient()
        response = client.request('pool.ntp.org')
        Internet_date_and_time = datetime.datetime.fromtimestamp(response.tx_time)
        return Internet_date_and_time

    #biramo duzinu u satima za timer
    def timer(a):
        if a=='':messagebox.showinfo("selektuj", "selektuj broj")
        else:
            vreme_otkljucavanja=uzmi_vreme()+timedelta(hours=int(a))
            file = open("vreme.txt", "w")
            file.truncate(0)
            vreme_otkljucavanja=str(vreme_otkljucavanja)
            vreme_bytes = vreme_otkljucavanja.encode('ascii')
            base64_bytes = base64.b64encode(vreme_bytes)
            base64_vreme = base64_bytes.decode('ascii')
            file.write(base64_vreme)
            file.close

    #dobijamo sifru ako je vreme isteklo
    def otkljucaj():
        try:
            file = open("vreme.txt", "r")
            base64_vreme = file.readline()
            base64_bytes =  base64_vreme.encode('ascii')
            vreme_bytes = base64.b64decode(base64_bytes)
            vreme = vreme_bytes.decode('ascii')
            file.close
            lines_conv = datetime.datetime.strptime(vreme, '%Y-%m-%d %H:%M:%S.%f')
            file = open("sifra64.txt", "r")
            base64_sifra = file.readline()
            file.close
        except:messagebox.showerror("greska","Morate imati sifru i zadati timer")

        base64_bytes =  base64_sifra.encode('ascii')
        sifra_bytes = base64.b64decode(base64_bytes)
        sifra = sifra_bytes.decode('ascii')

        if lines_conv<uzmi_vreme():messagebox.showinfo("sifra", sifra)
        else:
            aa=lines_conv-uzmi_vreme()
            messagebox.showinfo("sifra", "sacekajte jos "+str(aa).split(".")[0])

    #generisemo sifru i encodujemo je
    def generisi():
        characters = string.ascii_lowercase + string.digits
        password =  "".join(choice(characters) for x in range(randint(10, 15)))
        sifra_bytes = password.encode('ascii')
        base64_bytes = base64.b64encode(sifra_bytes)
        base64_sifra = base64_bytes.decode('ascii')
        if os.stat("sifra64.txt").st_size == 0:
            file = open("sifra64.txt", "w")
            file.write(base64_sifra)
            file.close
        else:
            odgovor = askyesno(title='UPOZORENJE',message='Ako generisete novu sifru stara ce se obrisati!')
            if odgovor==TRUE:
                file = open("sifra64.txt", "w")
                file.write(base64_sifra)
                file.close
    #pravimo elemente
    Ispis=Label(text="Izaberi koliko sati ce tajmer trajati")
    Ispis.pack()
    izbor_combobox = ttk.Combobox(glavni_prozor,width=5,state='readonly')
    izbor_combobox['values']=('','3','5','7','12','24')
    izbor_combobox.place(x=200,y=35,anchor=CENTER)
    DugmeTimer=Button(text="Ukljuci Timer", bg="orange", font=('Myriad',11,'bold'),  width=12, command=lambda:timer(izbor_combobox.get()))
    DugmeTimer.place(x=200,y=70,anchor=CENTER)
    DugmeOtkljucaj=Button(text="Otkljucaj", bg="lightgreen", font=('Myriad',11,'bold'),  width=12, command=otkljucaj)
    DugmeOtkljucaj.place(x=200,y=140,anchor=CENTER)
    generisi_dugme=Button(text="Generisi", bg="lightgreen", font=('Myriad',11,'bold'),  width=12, command=generisi)
    generisi_dugme.place(x=200,y=180,anchor=CENTER)


    glavni_prozor.mainloop()

except OSError:
    glavni_prozor.destroy()
    print('\n')
    print('Vreme nije moguce preuzeti sa servera')
