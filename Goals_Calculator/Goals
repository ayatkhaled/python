from tkinter import *
import tkinter 

from pygame import mixer
#from PIL import Image, ImageTk



mixer.init()

def play_music():
    mixer.music.load("sample.ogg")
    mixer.music.play()
    

b8.Button(root, text="Play music", command=play_music).pack()
root.mainloop()

window_1 = Tk() 
bg = PhotoImage(file = "football8.png")
# adding title to the window 

window_1.title("Hello Ayat ")
window_1.geometry('700x500')

num = 0
num2=0
Label(window_1, font =('Helvetica bold',22), text = 'GOOALS',bg
='yellow').place(x=300,y=20)
#callback : function for changing label
label1 = Label(window_1, image=bg,justify=CENTER)
label1.pack()
Label(window_1, font =('Helvetica bold',22), text = 'GOOALS',bg
='yellow').place(x=300-40,y=20)
def increment():

	global num
	if(num<9):
		num += 1
		lbl.configure(text=num) 
	else:
		num=9
def increment2():

	global num2
	if(num2<9):
		num2 += 1
		lb2.configure(text=num2) 
	else:
		num=9
def zero():
		global num2 
		global num
		num2=0
		num=0
		lb2.configure(text=num2)
		lbl.configure(text=num) 		

photo_1 = PhotoImage(file='moroco.png')
photo_2 = PhotoImage(file='brazil.png')

# editing of the image resizing of it 
# resizing decreased by increasing the number 
photo_1 = photo_1.subsample(2,2)
photo_2 = photo_2.subsample(2,2)
re  =Button(window_1 , text = "Time OFF " , bd = '5',background="black" , command = zero)
re.place(x=300,y=400)
B_1  =Button(window_1 , text = "Increment The button " , bd = '5',background="green" ,image=photo_1, command = increment)

#B_1.pack(side=LEFT,pady=100)
B_1.place(x=170,y=190)
lbl=Label(window_1, text=num,font = ('Verdana', 15),bd = '5',background="black",fg="red")
#lbl.place(relx=6.0, rely=1.0, anchor='sw')
lbl.place(x=195+20,y=290+40+20)

B_2  =Button(window_1 , text = "Increment The button " , bd = '5',background="green" ,image=photo_2, command = increment2)

#B_1.pack(side=LEFT,pady=100)
B_2.place(x=400,y=190)
lb2=Label(window_1, text=num2,font = ('Verdana', 15),bd = '5',background="black",fg="red")
#lbl.place(relx=6.0, rely=1.0, anchor='sw')
lb2.place(x=195+20+150+70+20,y=290+40+20)
b2 =Button(window_1 , text = "Close the window" , bd = '10' , command = window_1.destroy)
b2.pack(side = BOTTOM)
window_1.mainloop()
