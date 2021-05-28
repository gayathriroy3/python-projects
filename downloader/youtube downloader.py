import tkinter as tk
from pytube import YouTube


a=tk.Tk()
a.geometry('510x424')
a.configure(bg='red')
a.title('YouTube Downloader')

lb=tk.Label(a,text='YouTube Downloader',font='arial 20 bold',bg='white',fg='black').pack()
lb1=tk.Label(a,text='Paste The Link Here:',font='arial 15 bold',bg='white',fg='black').place(x=20,y=60)
link=tk.StringVar()
entry=tk.Entry(a,textvariable=link,bg='white',font=10).place(x=20,y=100)


def downloader():
     video=YouTube(str(link.get()))
     video=video.streams.get_highest_resolution()
     video.download()
     lb2=tk.Label(a,text='Downloaded',font='arial 10 bold').place(x=180,y=210)

def Reset():
    link.set('')
    
button1=tk.Button(a,text='Download',font='arial 10 bold',bg='white',fg='black',command=downloader,width=10).place(x=25,y=140)
button2=tk.Button(a,text='Reset',font='arial 10 bold',bg='white',fg='black',command=Reset,width=10).place(x=120,y=140)

a.mainloop()
