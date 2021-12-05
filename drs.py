from tkinter import *
import tkinter
from tkinter import font
import cv2
import PIL.Image,PIL.ImageTk
# to give arguments to the function
from functools import partial 
import threading
import imutils 
import time
set_width=650
set_height=368
window=Tk()
window.title("DRS System")
cv_image=cv2.cvtColor(cv2.imread(r"C:\Users\ROHIT\Desktop\python programms\python gui\welcomp.png"),cv2.COLOR_BGR2RGB)
canvas=tkinter.Canvas(window,width=set_width,height=set_height)
photo=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_image))
image_on_canvas=canvas.create_image(0,0,ancho=tkinter.NW,image=photo)
canvas.pack()

stream=cv2.VideoCapture(r"C:\Users\ROHIT\Desktop\python programms\python gui\clip.mp4")

global flag
def pending(decision):
    # 1.display decision pending image
    frame=cv2.cvtColor(cv2.imread(r"C:\Users\ROHIT\Desktop\python programms\python gui\decision.png"),cv2.COLOR_BGR2RGB)
    frame=imutils.resize(frame,width=set_width,height=set_height)
    frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0,image=frame,anchor=tkinter.NW)

    # 2.wait for 1s
    time.sleep(2)

    # 3.display sponcer image
    frame=cv2.cvtColor(cv2.imread(r"C:\Users\ROHIT\Desktop\python programms\python gui\sponcer.png"),cv2.COLOR_BGR2RGB)
    frame=imutils.resize(frame,width=set_width,height=set_height)
    frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0,image=frame,anchor=tkinter.NW)

    # 4.wait for 1s
    time.sleep(2)
    # 5.display out/notout image
    if decision=="out":
        decisionImg=r"C:\Users\ROHIT\Desktop\python programms\python gui\out.png"
    else:
        decisionImg=r"C:\Users\ROHIT\Desktop\python programms\python gui\notout.png"   
    frame=cv2.cvtColor(cv2.imread(decisionImg),cv2.COLOR_BGR2RGB)
    frame=imutils.resize(frame,width=set_width,height=set_height)
    frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0,image=frame,anchor=tkinter.NW)

def play(speed):
    # print("you clicked",speed)
    flag=True
    frame1=stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES,frame1 + speed)
    grabbed,frame=stream.read()
    if not grabbed:
        exit()
    frame=imutils.resize(frame,width=set_width,height=set_height)
    frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0,image=frame,anchor=tkinter.NW)

    if flag:
        canvas.create_text(140,20,fill="red",font="lucida 20 bold",text="decision pending")
    flag=not flag

def out():
    thread=threading.Thread(target=pending,args=("out",))
    thread.daemon=1
    thread.start()
    print("out")

def not_out():
    thread=threading.Thread(target=pending,args=("not out",))
    thread.daemon=1
    thread.start()    
    print("not out")
# buttons to handle
btn=tkinter.Button(window,text="<< Previous (slow)",width=50,fg="red",command=partial(play,-2))
btn.pack()
btn=tkinter.Button(window,text="<< Previous (fast)",width=50,fg="red",command=partial(play,-25))
btn.pack()
btn=tkinter.Button(window,text=" Next (Slow)>>",width=50,fg="red",command=partial(play,2))
btn.pack()
btn=tkinter.Button(window,text=" Next (fast)>>",width=50,fg="red",command=partial(play,25))
btn.pack()

btn=tkinter.Button(window,text=" Give Out!",width=50,fg="red",command=out)
btn.pack()

btn=tkinter.Button(window,text=" Give Not Out!",width=50,fg="red",command=not_out)
btn.pack()
window.mainloop()
