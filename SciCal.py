# By Arpan Srijita Priyanka Sucheta Adrita

import math
from tkinter import *
import gspread
from oauth2client.service_account import ServiceAccountCredentials
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_name('connection.json',scope)
client = gspread.authorize(credentials)
sheet = client.open("yahoo").sheet1
data = sheet.get_all_records()
expr=""
def btnclk(n):
    global expr
    expr=expr+str(n)
    v.set(expr)
def calculate():
    try:
        global expr
        sheet.update_cell(2,1,expr)
        result=round(eval(expr),6)
        v.set(result)
    except ZeroDivisionError:
        v.set("Math Error")
    except :
        v.set("Syntax Error")
def lg(a):
    x=math.log(a)/math.log(10)
    return x
def npr(n,r):
    if(n<r):
        v.set("Error: n is less than r")
    else:
        ans_npr = (math.factorial(n))/(math.factorial(n-r))
        return ans_npr
def ncr(n,r):
    if(n<r):
        v.set("Error: n is less than r")
    else:
        ans_ncr = (math.factorial(n))/(math.factorial(r)*math.factorial(n-r))
        return ans_ncr
def sq(a):
    return a**2
def cu(a):
    return a**3
def md(a,b):
    return a%b
def cr(a):
    return a**0.3333333333333333333333
def blog(value,base):
    if(value==0 or base==0):
        v.set("Error")
    else:
        ans_log=math.log(value,base)
        return ans_log
def per(a,b):
    x = (a/b)*100
    return x
def sin(a):
    return (math.sin(math.radians(a)))
def cos(a):
    return (math.cos(math.radians(a)))
def tan(a):
    try: 
        if (a==90 or a==270 or a==450 or a==630 or a==810 or a==990 or a==1170):
            raise TanError
        return (math.tan(math.radians(a)))
    except TanError:
        v.set("Math error")
def sinh(a):
    return (math.sinh(math.radians(a)))
def cosh(a):
    return (math.cosh(math.radians(a)))
def tanh(a):
    try: 
        if (a==90 or a==270 or a==450 or a==630 or a==810 or a==990 or a==1170):
            raise TanhError
        return (math.tanh(math.radians(a)))
    except TanError:
        v.set("Math error")
def sqrt(a):
    return math.sqrt(a)
def exp(a):
    return math.exp(a)
def fact(a):
    return math.factorial(a)
def ln(a):
    return math.log(a)
def hist():
    global data
    data = sheet.get_all_records()
    da = str(data[0])
    da = da[5:len(da)-1]
    #daa=int(da)
    daa=da[1:len(da)-1]
    v.set(daa)


def back():
    global expr
    expr=expr[:len(expr)-1]
    v.set(expr)
    
def clear():
    global expr
    expr=""
    v.set(expr)
w=Tk()
w.title("SCIENTIFIC CALCULATOR")
w.iconbitmap(r'l33.ico')
v=StringVar()
###  create  all components
pi=math.pi
E= Entry(w, font=('sans-serif', 20, 'bold'), textvariable=v,relief=RIDGE,
                    bd=5,bg='#EBEBEB', justify='right')


B1=Button(w,text="1",font=("arial",15,"bold"),bg='grey',fg='white',width=4,command=lambda:btnclk(1))
B2=Button(w,text="2",font=("arial",15,"bold"),bg='grey',fg='white',width=4,command=lambda:btnclk(2))
B3=Button(w,text="3",font=("arial",15,"bold"),bg='grey',fg='white',width=4,command=lambda:btnclk(3))
B4=Button(w,text="4",font=("arial",15,"bold"),bg='grey',fg='white',width=4,command=lambda:btnclk(4))
B5=Button(w,text="5",font=("arial",15,"bold"),bg='grey',fg='white',width=4,command=lambda:btnclk(5))
B6=Button(w,text="6",font=("arial",15,"bold"),bg='grey',fg='white',width=4,command=lambda:btnclk(6))
B7=Button(w,text="7",font=("arial",15,"bold"),bg='grey',fg='white',width=4,command=lambda:btnclk(7))
B8=Button(w,text="8",font=("arial",15,"bold"),bg='grey',fg='white',width=4,command=lambda:btnclk(8))
B9=Button(w,text="9",font=("arial",15,"bold"),bg='grey',fg='white',width=4,command=lambda:btnclk(9))
B0=Button(w,text="0",font=("arial",15,"bold"),bg='grey',fg='white',width=4,command=lambda:btnclk(0))
Bequal=Button(w,text="=",font=("arial",15,"bold"),bg='#464646',fg='#FF8200',height=2,width=8,command=lambda:calculate())
Bclear=Button(w,text="C",font=("arial",15,"bold"),bg='red',fg='white',width=8,command=lambda:clear())
Bplus=Button(w,text="+",font=("arial",15,"bold"),bg='#FF8200',fg='white',width=4,command=lambda:btnclk('+'))
Bminus=Button(w,text="-",font=("arial",15,"bold"),bg='#FF8200',fg='white',width=4,command=lambda:btnclk('-'))
Bmul=Button(w,text="X",font=("arial",15,"bold"),bg='#FF8200',fg='white',width=4,command=lambda:btnclk('*'))
Bdiv=Button(w,text="÷",font=("arial",15,"bold"),bg='#FF8200',fg='white',width=4,command=lambda:btnclk('/'))
Bsin=Button(w,text="sin",font=("arial",15,"bold"),bg='black',fg='white',width=4,command=lambda:btnclk('sin('))
Bcos=Button(w,text="cos",font=("arial",15,"bold"),bg='black',fg='white',width=4,command=lambda:btnclk('cos('))
Btan=Button(w,text="tan",font=("arial",15,"bold"),bg='black',fg='white',width=4,command=lambda:btnclk('tan('))
Blog=Button(w,text="log",font=("arial",15,"bold"),bg='black',fg='white',width=4,command=lambda:btnclk('lg('))
Bdel=Button(w,text="del",font=("arial",15,"bold"),bg='#FF8200',fg='white',width=4,command=lambda:back())
Bsqrt=Button(w,text="√ ",font=("arial",15,"bold"),bg='black',fg='white',width=4,command=lambda:btnclk('sqrt('))
Bob=Button(w,text="(",font=("arial",15,"bold"),bg='black',fg='white',width=4,command=lambda:btnclk('('))
Bcb=Button(w,text=")",font=("arial",15,"bold"),bg='black',fg='white',width=4,command=lambda:btnclk(')'))
Bpow=Button(w,text="^",font=("arial",15,"bold"),bg='black',fg='white',width=4,command=lambda:btnclk('**'))
Bncr=Button(w,text="nCr",font=("arial",15,"bold"),bg='black',fg='white',width=4,command=lambda:btnclk('ncr('))
Bnpr=Button(w,text="nPr",font=("arial",15,"bold"),bg='black',fg='white',width=4,command=lambda:btnclk('npr('))
Bfact=Button(w,text="!",font=("arial",15,"bold"),bg='black',fg='white',width=4,command=lambda:btnclk('fact('))
Be=Button(w,text="e",font=("arial",15,"bold"),bg='black',fg='white',width=4,command=lambda:btnclk('exp('))
Bsq=Button(w,text="x²",font=("arial",15,"bold"),bg='black',fg='white',width=4,command=lambda:btnclk('sq('))
Bdec=Button(w,text=".",font=("arial",15,"bold"),bg='black',fg='white',width=4,command=lambda:btnclk('.'))
Bln=Button(w,text="ln",font=("arial",15,"bold"),bg='black',fg='white',width=4,command=lambda:btnclk('ln('))
Bneg=Button(w,text="(-)",font=("arial",15,"bold"),bg='black',fg='white',width=4,command=lambda:btnclk('-1*'))
Bhist=Button(w,text="hist",font=("arial",15,"bold"),bg='#FF8200',fg='white',width=4,command=lambda:hist())
Bmod=Button(w,text="mod",font=("arial",15,"bold"),bg='black',fg='white',width=4,command=lambda:btnclk('md('))
Bpi=Button(w,text="π",font=("arial",15,"bold"),bg='black',fg='white',width=4,command=lambda:btnclk('pi'))
Binv=Button(w,text="inv",font=("arial",15,"bold"),bg='black',fg='white',width=4,command=lambda:btnclk('1/'))
Bblog=Button(w,text="blog",font=("arial",15,"bold"),bg='black',fg='white',width=4,command=lambda:btnclk('blog('))
Bcube=Button(w,text="x³",font=("arial",15,"bold"),bg='black',fg='white',width=4,command=lambda:btnclk('cu('))
Bcroot=Button(w,text="3√ ",font=("arial",15,"bold"),bg='black',fg='white',width=4,command=lambda:btnclk('cr('))
Bper=Button(w,text="%",font=("arial",15,"bold"),bg='black',fg='white',width=4,command=lambda:btnclk('per('))
Bcomma=Button(w,text=",",font=("arial",15,"bold"),bg='black',fg='white',width=4,command=lambda:btnclk(','))
Bsinh=Button(w,text="sinh",font=("arial",15,"bold"),bg='black',fg='white',width=4,command=lambda:btnclk('sinh('))
Bcosh=Button(w,text="cosh",font=("arial",15,"bold"),bg='black',fg='white',width=4,command=lambda:btnclk('cosh('))
Btanh=Button(w,text="tanh",font=("arial",15,"bold"),bg='black',fg='white',width=4,command=lambda:btnclk('tanh('))
B10x=Button(w,text="10^x",font=("arial",15,"bold"),bg='black',fg='white',width=4,command=lambda:btnclk('10**'))
########################################################
##palce the components at proper position
E.grid(row=1,column=1,columnspan=10,sticky='news')
## row 2
Bclear.grid(row=2,column=1,columnspan=2,sticky='news')
Bdel.grid(row=2,column=3,sticky='news')
Bhist.grid(row=2,column=4,sticky='news')
Bsqrt.grid(row=2,column=5,sticky='news')
Bcroot.grid(row=2,column=6,sticky='news')
Bpi.grid(row=2,column=7,sticky='news')
Bob.grid(row=2,column=8,sticky='news')
Bcb.grid(row=2,column=9,sticky='news')
Bpow.grid(row=2,column=10,sticky='news')
## row 3
B7.grid(row=3,column=1,sticky='news')
B8.grid(row=3,column=2,sticky='news')
B9.grid(row=3,column=3,sticky='news')
Bdiv.grid(row=3,column=4,sticky='news')
Bsq.grid(row=3,column=5,sticky='news')
Bcube.grid(row=3,column=6,sticky='news')
B10x.grid(row=3,column=7,sticky='news')
Bsin.grid(row=3,column=8,sticky='news')
Bcos.grid(row=3,column=9,sticky='news')
Btan.grid(row=3,column=10,sticky='news')
## row 4
B4.grid(row=4,column=1,sticky='news')
B5.grid(row=4,column=2,sticky='news')
B6.grid(row=4,column=3,sticky='news')
Bmul.grid(row=4,column=4,sticky='news')
Bmod.grid(row=4,column=5,sticky='news')
Bblog.grid(row=4,column=6,sticky='news')
Bfact.grid(row=4,column=7,sticky='news')
Bsinh.grid(row=4,column=8,sticky='news')
Bcosh.grid(row=4,column=9,sticky='news')
Btanh.grid(row=4,column=10,sticky='news')
## row 5
B1.grid(row=5,column=1,sticky='news')
B2.grid(row=5,column=2,sticky='news')
B3.grid(row=5,column=3,sticky='news')
Bminus.grid(row=5,column=4,sticky='news')
Bnpr.grid(row=5,column=5,sticky='news')
Bncr.grid(row=5,column=6,sticky='news')
Binv.grid(row=5,column=7,sticky='news')
Bper.grid(row=5,column=8,sticky='news')
Bequal.grid(row=5,column=9,columnspan=2,rowspan=2,sticky='news')
## row 6
Bdec.grid(row=6,column=1,sticky='news')
B0.grid(row=6,column=2,sticky='news')
Bcomma.grid(row=6,column=3,sticky='news')
Bplus.grid(row=6,column=4,sticky='news')
Bneg.grid(row=6,column=5,sticky='news')
Be.grid(row=6,column=6,sticky='news')
Bln.grid(row=6,column=7,sticky='news')
Blog.grid(row=6,column=8,sticky='news')

w.rowconfigure(1,weight=2)
w.rowconfigure(2,weight=1)
w.rowconfigure(3,weight=1)
w.rowconfigure(4,weight=1)
w.rowconfigure(5,weight=1)
w.rowconfigure(6,weight=1)
w.columnconfigure(1,weight=1)
w.columnconfigure(2,weight=1)
w.columnconfigure(3,weight=1)
w.columnconfigure(4,weight=1)
w.columnconfigure(5,weight=1)
w.columnconfigure(6,weight=1)
w.columnconfigure(7,weight=1)
w.columnconfigure(8,weight=1)
w.columnconfigure(9,weight=1)
w.columnconfigure(10,weight=1)
w.mainloop()



