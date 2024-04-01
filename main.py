import tkinter as tk
from tkinter import ttk
from sug import prd

key = tk.Tk()  # key window name
key.title('Wscube Tech Keyboard')  # title Name

def file_write(a): # File to Store Data
    p = open("all_data.txt","a")
    a = " "+a
    p.write(a)
    p.close()


exp = ""
c = 0

def done():
    global  exp,c
    c = 0
    if exp == "":
        data = Dis_entry.get(1.0,tk.END)
    else:
        data = exp
        exp = ""

    file_write(data)
    Dis_entry.delete(1.0, tk.END)

sug_word = ("","","")

def press(num):
    global exp,c,sug_word
    Dis_entry.insert(tk.END,num)
    exp = exp + num
    if num == " ":
        l = exp.split(" ")
        get_word = prd(l[c])
        sug_word = get_word
        c = c + 1
        q1.config(text=get_word[0])
        w1.config(text=get_word[2])
        E1.config(text = get_word[1])


def clear():
    global exp
    exp = ""
    Dis_entry.delete(1.0,tk.END)



key.geometry('882x450')


key.configure(bg = 'green')


Dis_entry = tk.Text(key,font=(102))
Dis_entry.place(x=0,y=0,height=150,width=882)


# First Line Button
q1 = ttk.Button(key,text = '',command=lambda : press(sug_word[0]))
q1.place(x=0,y=150,height=50,width=250)

w1 = ttk.Button(key,text = '',command=lambda : press(sug_word[2]))
w1.place(x=250,y=150,height=50,width=250)

E1 = ttk.Button(key,text = '',command=lambda : press(sug_word[1]))
E1.place(x=500,y=150,height=50,width=250)

arraw_img = tk.PhotoImage(file="images.png")
R1 = ttk.Button(key,image=arraw_img,command=done)
R1.place(x=750,y=150,height=50,width=132)



q_ = ttk.Button(key,text = '`')
q_.place(x=0,y=200,height=50,width=63)

b1 = ttk.Button(key,text = '1' , command = lambda : press('1'))
b1.place(x=63,y=200,height=50,width=63)

b2 = ttk.Button(key,text = '2' , command = lambda : press('2'))
b2.place(x=126,y=200,height=50,width=63)

b3 = ttk.Button(key,text = '3' , command = lambda : press('3'))
b3.place(x=189,y=200,height=50,width=63)

b4 = ttk.Button(key,text = '4' , command = lambda : press('4'))
b4.place(x=252,y=200,height=50,width=63)

b5 = ttk.Button(key,text = '5' , command = lambda : press('5'))
b5.place(x=315,y=200,height=50,width=63)

b6 = ttk.Button(key,text = '6' , command = lambda : press('6'))
b6.place(x=378,y=200,height=50,width=63)

b7 = ttk.Button(key,text = '7', command = lambda : press('7'))
b7.place(x=441,y=200,height=50,width=63)

b8 = ttk.Button(key,text = '8' , command = lambda : press('8'))
b8.place(x=504,y=200,height=50,width=63)

b9 = ttk.Button(key,text = '9' , command = lambda : press('9'))
b9.place(x=567,y=200,height=50,width=63)

b0 = ttk.Button(key,text = '0' , command = lambda : press('0'))
b0.place(x=630,y=200,height=50,width=63)

bsub = ttk.Button(key,text = '-' , command = lambda : press('-'))
bsub.place(x=693,y=200,height=50,width=63)

bplus = ttk.Button(key,text = '+' , command = lambda : press('+'))
bplus.place(x=756,y=200,height=50,width=63)


clear = ttk.Button(key,text = 'Clear' , command = clear)
clear.place(x=819,y=200,height=50,width=63)

#_________________________________________

q = ttk.Button(key,text = 'Q', command = lambda : press('q'))
q.place(x=0,y=250,height=50,width=63)

w = ttk.Button(key,text = 'W' , command = lambda : press('w'))
w.place(x=63,y=250,height=50,width=63)

E = ttk.Button(key,text = 'E' , command = lambda : press('e'))
E.place(x=126,y=250,height=50,width=63)

R = ttk.Button(key,text = 'R' , command = lambda : press('r'))
R.place(x=189,y=250,height=50,width=63)

T = ttk.Button(key,text = 'T' , command = lambda : press('t'))
T.place(x=252,y=250,height=50,width=63)

Y = ttk.Button(key,text = 'Y', command = lambda : press('y'))
Y.place(x=315,y=250,height=50,width=63)

U = ttk.Button(key,text = 'U' , command = lambda : press('u'))
U.place(x=378,y=250,height=50,width=63)

I = ttk.Button(key,text = 'I' , command = lambda : press('i'))
I.place(x=441,y=250,height=50,width=63)

O = ttk.Button(key,text = 'O' , command = lambda : press('o'))
O.place(x=504,y=250,height=50,width=63)

P = ttk.Button(key,text = 'P' , command = lambda : press('p'))
P.place(x=567,y=250,height=50,width=63)

cur = ttk.Button(key,text = '{' , command = lambda : press('{'))
cur.place(x=630,y=250,height=50,width=63)

cur_c = ttk.Button(key,text = '}' , command = lambda : press('}'))
cur_c.place(x=693,y=250,height=50,width=63)

back_slash = ttk.Button(key,text = '\\', command = lambda : press('\\'))
back_slash.place(x=756,y=250,height=50,width=63)


clear = ttk.Button(key,text = 'caps lock' )
clear.place(x=819,y=250,height=50,width=63)

# Second Line Button



A = ttk.Button(key,text = 'A' , command = lambda : press('a'))
A.place(x=0,y=300,height=50,width=63)

S = ttk.Button(key,text = 'S' , command = lambda : press('s'))
S.place(x=63,y=300,height=50,width=63)

D = ttk.Button(key,text = 'D' , command = lambda : press('d'))
D.place(x=126,y=300,height=50,width=63)

F = ttk.Button(key,text = 'F' , command = lambda : press('f'))
F.place(x=189,y=300,height=50,width=63)

G = ttk.Button(key,text = 'G' , command = lambda : press('g'))
G.place(x=252,y=300,height=50,width=63)


H = ttk.Button(key,text = 'H' , command = lambda : press('h'))
H.place(x=315,y=300,height=50,width=63)


J = ttk.Button(key,text = 'J' , command = lambda : press('j'))
J.place(x=378,y=300,height=50,width=63)


K = ttk.Button(key,text = 'K' , command = lambda : press('k'))
K.place(x=441,y=300,height=50,width=63)

L = ttk.Button(key,text = 'L' , command = lambda : press('l'))
L.place(x=504,y=300,height=50,width=63)


semi_co = ttk.Button(key,text = ';' , command = lambda : press(';'))
semi_co.place(x=567,y=300,height=50,width=63)


d_colon = ttk.Button(key,text = '"' , command = lambda : press('"'))
d_colon.place(x=630,y=300,height=50,width=63)


enter = ttk.Button(key,text = 'Enter', command=lambda :press("\n"))
enter.place(x=693,y=300,height=50,width=189)


# # third line Button

Z = ttk.Button(key,text = 'Z' , command = lambda : press('z'))
Z.place(x=0,y=350,height=50,width=63)


X = ttk.Button(key,text = 'X' , command = lambda : press('x'))
X.place(x=63,y=350,height=50,width=63)


C = ttk.Button(key,text = 'C' , command = lambda : press('c'))
C.place(x=126,y=350,height=50,width=63)


V = ttk.Button(key,text = 'V' , command = lambda : press('v'))
V.place(x=189,y=350,height=50,width=63)

B = ttk.Button(key, text= 'B' , command = lambda : press('b'))
B.place(x=252,y=350,height=50,width=63)


N = ttk.Button(key,text = 'N' , command = lambda : press('n'))
N.place(x=315,y=350,height=50,width=63)


M = ttk.Button(key,text = 'M' , command = lambda : press('m'))
M.place(x=378,y=350,height=50,width=63)


left = ttk.Button(key,text = '<', command = lambda : press('<'))
left.place(x=441,y=350,height=50,width=63)


right = ttk.Button(key,text = '>' , command = lambda : press('>'))
right.place(x=504,y=350,height=50,width=63)


slas = ttk.Button(key,text = '/' , command = lambda : press('/'))
slas.place(x=567,y=350,height=50,width=63)


q_mark = ttk.Button(key,text = '?' , command = lambda : press('?'))
q_mark.place(x=567,y=350,height=50,width=63)


coma = ttk.Button(key,text = ',' , command = lambda : press(','))
coma.place(x=630,y=350,height=50,width=63)

dot = ttk.Button(key,text = '.' , command = lambda : press('.'))
dot.place(x=693,y=350,height=50,width=63)

shift = ttk.Button(key,text = 'Shift' , command = lambda : press('Shift'))
shift.place(x=756,y=350,height=50,width=126)

# #Fourth Line Button

ctrl = ttk.Button(key,text = 'Ctrl' , command = lambda : press('Ctrl'))
ctrl.place(x=0,y=400,height=50,width=63)


Fn = ttk.Button(key,text = 'Fn' , command = lambda : press('Fn'))
Fn.place(x=63,y=400,height=50,width=63)


window = ttk.Button(key,text = 'Window' , command = lambda : press('Window'))
window.place(x=126,y=400,height=50,width=63)

Alt = ttk.Button(key,text = 'Alt' , command = lambda : press('Alt'))
Alt.place(x=189,y=400,height=50,width=63)

space = ttk.Button(key,text = 'Space' , width = 6, command = lambda : press(' '))
space.place(x=252,y=400,height=50,width=378)

Alt_gr = ttk.Button(key,text = 'Alt Gr' , width = 6, command = lambda : press('Alt'))
Alt_gr.place(x=630,y=400,height=50,width=63)

open_b = ttk.Button(key,text = '(' , command = lambda : press('('))
open_b.place(x=693,y=400,height=50,width=63)

close_b = ttk.Button(key,text = ')' , command = lambda : press(')'))
close_b.place(x=756,y=400,height=50,width=63)


tap = ttk.Button(key,text = 'Tab' , command = lambda : press('  '))
tap.place(x=819,y=400,height=50,width=63)



key.mainloop()  # using ending point