import pytube
from tkinter import *
import tkinter.ttk as ttk

def write(string):
	text_box.config(state=NORMAL)
	text_box.insert("end", string + "\n")
	text_box.see("end")
	text_box.config(state=DISABLED)

def STREAMS():
	try:
		yt=pytube.YouTube(link.get())
		write("\nTITLE : "+str(yt.title))
		write("\nThumbnail Url : "+str(yt.thumbnail_url))
		stream=yt.streams.first()
		write("\nAvailable first stream : "+str(stream))
	except:
		write("CONNECTION ERROR!!!!!")

def DOWNLOAD():
	yt=pytube.YouTube(link.get())
	stream=yt.streams.first()
	if(destination.get()!=None):
		try:
			stream.download(destination.get())
			
			write("Download Successful")
		except:
			write("Connection Error!!!")
			write("Destination not Found!!!")
	else:
		try:
			stream.download()
			
			write("Download Successful!!!")
		except:
			write("Connection Error!!!!!")


root=Tk()
root.title("Youtube Downloader")

ft=ttk.Frame()
#ft.pack(expand=True,fill=BOTH,side=TOP)
ft.grid(row=4,column=0)

text_box=Text(root,height=20,width=100)
text_box.grid(row=0,column=0,columnspan=4)

Pbar=ttk.Progressbar(ft,orient='horizontal',mode='determinate')
Pbar.pack(expand=True,fill=BOTH,side=TOP)
Pbar.start(100)

L1=Label(root,text="Youtube Link ")
L1.grid(row=1,column=0)

link=Entry(root,bd=10)
link.grid(row=1,column=1)

L2=Label(root,text="Destination")
L2.grid(row=2,column=0)

destination=Entry(root,bd=10)
destination.grid(row=2,column=1)

B1=Button(root,text='Details',command=STREAMS)
B1.grid(row=3,column=0)

B2=Button(root,text='Download',command=DOWNLOAD)
B2.grid(row=3,column=1)

root.mainloop()

