from tkinter import *

def click(event):
    global scvalue
    text= event.widget.cget("text")
    if text  == "C":
        scvalue.set("")
        screen.update()
    elif text  == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                value= "Error"
                
            
        scvalue.set(value)
        screen.update()
        
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()
    
    
    
window = Tk()
window.geometry('255x180') 
window.title('Calculator')

scvalue = StringVar()
scvalue.set("")
screen = Entry(window, textvar=scvalue, font= 16 )
#screen.grid(columnspan=4, ipadx=70) 
screen.pack(fill= X, ipadx=5, pady=5,padx=8)

f= Frame (window, bg= 'grey')
b1=Button(f, text ='(', height=1, width=7)
b1.grid(row=2, column=0)
#b1.pack(side=LEFT)
b1.bind("<Button-1>",click)

b2=Button(f, text =')', height=1, width=7)
#b2.pack(side=LEFT)
b2.grid(row=2, column=1)
b2.bind("<Button-1>",click)

b3=Button(f, text ='%', height=1, width=7)
#b3.pack(side=LEFT)
b3.grid(row=2, column=2)
b3.bind("<Button-1>",click)

b4=Button(f, text ='C', height=1, width=7)
#b4.pack(side=LEFT)
b4.grid(row=2, column=3)
b4.bind("<Button-1>",click)
f.pack()
f= Frame (window, bg= 'grey')
b1=Button(f, text ='7', height=1, width=7)
#b1.pack(side=LEFT)
b1.grid(row=3, column=0)
b1.bind("<Button-1>",click)

b2=Button(f, text ='8', height=1, width=7)
#b2.pack(side=LEFT)
b2.grid(row=3, column=1)
b2.bind("<Button-1>",click)

b3=Button(f, text ='9', height=1, width=7)
#b3.pack(side=LEFT)
b3.grid(row=3, column=2)
b3.bind("<Button-1>",click)

b4=Button(f, text ='*', height=1, width=7)
#b4.pack(side=LEFT)
b4.grid(row=3, column=3)
b4.bind("<Button-1>",click)
f.pack()

f= Frame (window, bg= 'grey')
b1=Button(f, text ='4', height=1, width=7)
b1.pack(side=LEFT)
b1.bind("<Button-1>",click)

b2=Button(f, text ='5', height=1, width=7)
b2.pack(side=LEFT)
b2.bind("<Button-1>",click)

b3=Button(f, text ='6', height=1, width=7)
b3.pack(side=LEFT)
b3.bind("<Button-1>",click)

b4=Button(f, text ='-', height=1, width=7)
b4.pack(side=LEFT)
b4.bind("<Button-1>",click)
f.pack()

f= Frame (window, bg= 'grey')
b1=Button(f, text ='1', height=1, width=7)
b1.pack(side=LEFT)
b1.bind("<Button-1>",click)

b2=Button(f, text ='2',height=1, width=7)
b2.pack(side=LEFT)
b2.bind("<Button-1>",click)

b3=Button(f, text ='3', height=1, width=7)
b3.pack(side=LEFT)
b3.bind("<Button-1>",click)

b4=Button(f, text ='+', height=1, width=7)
b4.pack(side=LEFT)
b4.bind("<Button-1>",click)
f.pack()

f= Frame (window, bg= 'grey')
b1=Button(f, text ='0', height=1, width=7)
b1.pack(side=LEFT)
b1.bind("<Button-1>",click)

b2=Button(f, text ='.', height=1, width=7)
b2.pack(side=LEFT)
b2.bind("<Button-1>",click)

b3=Button(f, text ='=', height=1, width=7)
b3.pack(side=LEFT)
b3.bind("<Button-1>",click)

b4=Button(f, text ='+',height=1, width=7)
b4.pack(side=LEFT)
b4.bind("<Button-1>",click)
f.pack()

window.mainloop()
