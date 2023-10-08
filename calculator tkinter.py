from tkinter import *
from tkinter import messagebox
root=Tk()
root.geometry("300x400")
root.resizable(0,0)
root.title("calculator")
val=""
a=0
operator=""
def btn1():
    global val
    val=val+'1'
    data.set(val)
def btn2():
    global val
    val=val+'2'
    data.set(val)
def btn3():
    global val
    val=val+'3'
    data.set(val)
def btn4():
    global val
    val=val+'4'
    data.set(val)
def btn5():
    global val
    val=val+'5'
    data.set(val)
def btn6():
    global val
    val=val+'6'
    data.set(val)
def btn7():
    global val
    val=val+'7'
    data.set(val)
def btn8():
    global val
    val=val+'8'
    data.set(val)
def btn9():
    global val
    val=val+'9'
    data.set(val)
def btn0():
    global val
    val=val+'0'
    data.set(val)
def btnplus():
    global a
    global operator
    global val
    a=int(val)
    operator="+"
    val=val+"+"
    data.set(val)
def btnminus():
    global a
    global operator
    global val
    a=int(val)
    operator="-"
    val=val+"-"
    data.set(val)
def btnmultiply():
    global a
    global operator
    global val
    a=int(val)
    operator="*"
    val=val+"*"
    data.set(val)
def btndivide():
    global a
    global operator
    global val
    a=int(val)
    operator="/"
    val=val+"/"
    data.set(val)
def btnclear():
    global a
    global operator
    global val
    val=""
    operator=""
    data.set(val)
def result():
    global a
    global operator
    global val
    if operator=='+':
        val2=val
        x=int((val2.split("+")[1]))
        c=a+x
        data.set(c)
        val=str(c)
    elif operator=='-':
        val2=val
        x=int((val2.split("-")[1]))
        c=a-x
        data.set(c)
        val=str(c)
    elif operator=='*':
        val2=val
        x=int((val2.split("*")[1]))
        c=a*x
        data.set(c)
        val=str(c)
    elif operator=="/":
        val2=val
        x=int((val2.split("/")[1]))
        if x==0:
            messagebox.showerror("Error,division by 0 is not defined")
            a=""
            val=""
            data.set(val)
        else:
            c=a/x
            c=(round(c,5))
            data.set(c)
            val=str(c)
    
data=StringVar()
l1=Label(root,text="Enter",anchor=E,font=("Arial",30),textvariable=data)
l1.pack(expand=True,fill="both")
btnrow1=Frame(root,bg='black')
btnrow1.pack(expand=True,fill="both",)
btnrow2=Frame(root)
btnrow2.pack(expand=True,fill="both",)
btnrow3=Frame(root)
btnrow3.pack(expand=True,fill="both",)
btnrow4=Frame(root)
btnrow4.pack(expand=True,fill="both",)

b1=Button(btnrow1,text="AC",font=("Arial",20),relief=GROOVE,border=0,command=btnclear)
b1.pack(side=LEFT,expand=True,fill="both")
b2=Button(btnrow1,text="/",font=("Arial",20),relief=GROOVE,border=0,command=btndivide)
b2.pack(side=LEFT,expand=True,fill="both")
b3=Button(btnrow1,text="0",font=("Arial",20),relief=GROOVE,border=0,command=btn0)
b3.pack(side=LEFT,expand=True,fill="both")
b4=Button(btnrow1,text="=",font=("Arial",20),relief=GROOVE,border=0,command=result)
b4.pack(side=LEFT,expand=True,fill="both")
b5=Button(btnrow2,text="7",font=("Arial",20),relief=GROOVE,border=0,command=btn7)
b5.pack(side=LEFT,expand=True,fill="both")
b6=Button(btnrow2,text="8",font=("Arial",20),relief=GROOVE,border=0,command=btn8)
b6.pack(side=LEFT,expand=True,fill="both")
b7=Button(btnrow2,text="9",font=("Arial",20),relief=GROOVE,border=0,command=btn9)
b7.pack(side=LEFT,expand=True,fill="both")
b8=Button(btnrow2,text="x",font=("Arial",20),relief=GROOVE,border=0,command=btnmultiply)
b8.pack(side=LEFT,expand=True,fill="both")
b9=Button(btnrow3,text="4",font=("Arial",20),relief=GROOVE,border=0,command=btn4)
b9.pack(side=LEFT,expand=True,fill="both")
b10=Button(btnrow3,text="5",font=("Arial",20),relief=GROOVE,border=0,command=btn5)
b10.pack(side=LEFT,expand=True,fill="both")
b11=Button(btnrow3,text="6",font=("Arial",20),relief=GROOVE,border=0,command=btn6)
b11.pack(side=LEFT,expand=True,fill="both")
b12=Button(btnrow3,text="-",font=("Arial",20),relief=GROOVE,border=0,command=btnminus)
b12.pack(side=LEFT,expand=True,fill="both")
b13=Button(btnrow4,text="1",font=("Arial",20),relief=GROOVE,border=0,command=btn1)
b13.pack(side=LEFT,expand=True,fill="both")
b14=Button(btnrow4,text="2",font=("Arial",20),relief=GROOVE,border=0,command=btn2)
b14.pack(side=LEFT,expand=True,fill="both")
b15=Button(btnrow4,text="3",font=("Arial",20),relief=GROOVE,border=0,command=btn3)
b15.pack(side=LEFT,expand=True,fill="both")
b16=Button(btnrow4,text="+",font=("Arial",20),relief=GROOVE,border=0,command=btnplus)
b16.pack(side=LEFT,expand=True,fill="both")

