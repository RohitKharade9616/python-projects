from tkinter import *
root=Tk()
root.geometry("500x500")

def click(event):
    global scvalue
    text=event.widget.cget("text")
    
    if text=="=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            value=eval(e.get())
        scvalue.set(value)
        e.update()
    elif text=="c":
        scvalue.set("")
        e.update()
    else:
        scvalue.set(scvalue.get()+text)
        e.update()

scvalue=StringVar()
scvalue.set("")
e=Entry(root,textvar=scvalue,font="lucida 30 bold")
e.pack(fill=X,ipadx=8,pady=10,padx=10)

f=Frame(root,bg="red")
nine=Button(f,text="9",font="lucida 20 bold",padx=10)
nine.pack(side=LEFT,padx=21,pady=10)
nine.bind("<Button-1>",click)

eight=Button(f,text="8",font="lucida 20 bold",padx=10)
eight.pack(side=LEFT,padx=21,pady=10)
eight.bind("<Button-1>",click)

seven=Button(f,text="7",font="lucida 20 bold",padx=10)
seven.pack(side=LEFT,padx=21,pady=10)
seven.bind("<Button-1>",click)

mul=Button(f,text="*",font="lucida 20 bold",padx=10)
mul.pack(side=LEFT,padx=21,pady=10)
mul.bind("<Button-1>",click)

f.pack()

f=Frame(root,bg="red")
four=Button(f,text="4",font="lucida 20 bold",padx=10)
four.pack(side=LEFT,padx=21,pady=10)
four.bind("<Button-1>",click)

five=Button(f,text="5",font="lucida 20 bold",padx=10)
five.pack(side=LEFT,padx=21,pady=10)
five.bind("<Button-1>",click)

six=Button(f,text="6",font="lucida 20 bold",padx=10)
six.pack(side=LEFT,padx=21,pady=10)
six.bind("<Button-1>",click)

sub=Button(f,text="-",font="lucida 20 bold",padx=10)
sub.pack(side=LEFT,padx=21,pady=10)
sub.bind("<Button-1>",click)
f.pack()

f=Frame(root,bg="red")

one=Button(f,text="1",font="lucida 20 bold",padx=10)
one.pack(side=LEFT,padx=20,pady=10)
one.bind("<Button-1>",click)

two=Button(f,text="2",font="lucida 20 bold",padx=10)
two.pack(side=LEFT,padx=20,pady=10)
two.bind("<Button-1>",click)

three=Button(f,text="3",font="lucida 20 bold",padx=10)
three.pack(side=LEFT,padx=20,pady=10)
three.bind("<Button-1>",click)

add=Button(f,text="+",font="lucida 20 bold",padx=10)
add.pack(side=LEFT,padx=20,pady=10)
add.bind("<Button-1>",click)

f.pack()

f=Frame(root,bg="red")

c=Button(f,text="c",font="lucida 20 bold",padx=10)
c.pack(side=LEFT,padx=20,pady=10)
c.bind("<Button-1>",click)

zero=Button(f,text="0",font="lucida 20 bold",padx=10)
zero.pack(side=LEFT,padx=20,pady=10)
zero.bind("<Button-1>",click)

dec=Button(f,text=".",font="lucida 20 bold",padx=10)
dec.pack(side=LEFT,padx=20,pady=10)
dec.bind("<Button-1>",click)

equal=Button(f,text="=",font="lucida 20 bold",padx=10)
equal.pack(side=LEFT,padx=20,pady=10)
equal.bind("<Button-1>",click)

f.pack()
f.pack()
root.mainloop()