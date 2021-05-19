from tkinter import *
from tkinter import messagebox
from random import randint
global c
global b1
global b2
global b3
global b4
global b5
global b6
global b7
global b8
global b9
c='x'
def first():
    global c
    def second():
        def exiit():
            messagebox.showinfo('exit','you are going to exit')
            scr.destroy()
        def restart():
            scr.destroy()
            first()
        scr=Tk()
        scr.configure(background='light yellow')
        scr.title('TIC TAC TOE')
        scr.geometry('280x200')
        e=Button(scr,text='exit',fg='white',bg='red',command=lambda:exiit(),height=4,width=14,relief='sunken',state='active',cursor='clock')
        r=Button(scr,text='restart',fg='white',bg='green',command=lambda:restart(),height=4,width=14,relief='sunken',state='active',cursor='dotbox')
        l3=Label(scr,text='Match',fg='Red',bg='light yellow',font=('Time',38,'bold'))
        l4=Label(scr,text='Over',fg='Red',bg='light yellow',font=('Time',38,'bold'))
        l3.grid(row=1,column=0)
        l4.grid(row=1,column=1)
        e.grid(row=5,column=1)
        r.grid(row=5,column=0)
    def comp():
        p=randint(0,9)
        global c
        global b1
        global b2
        global b3
        global b4
        global b5
        global b6
        global b7
        global b8
        global b9
        if(p==0):
            if(b1['text']==' '):
                b1['text']='O'
                c='x'
            else:
                comp()
        elif(p==1):
            if(b2['text']==' '):
                b2['text']='O'
                c='x'
            else:
                comp()
        elif(p==2):
            if(b3['text']==' '):
                b3['text']='O'
                c='x'
            else:
                comp()
        elif(p==3):
            if(b4['text']==' '):
                b4['text']='O'
                c='x'
            else:
                comp()
        elif(p==4):
            if(b5['text']==' '):
                b5['text']='O'
                c='x'
            else:
                comp()
        elif(p==5):
            if(b6['text']==' '):
                b6['text']='O'
                c='x'
            else:
                comp()
        elif(p==6):
            if(b7['text']==' '):
                b7['text']='O'
                c='x'
            else:
                comp()
        elif(p==7):
            if(b8['text']==' '):
                b8['text']='O'
                c='x'
            else:
                comp()
        elif(p==8):
            if(b9['text']==' '):
                b9['text']='O'
                c='x'
            else:
                comp()
    def press(buttons):
        global c 
        if(buttons['text']==' ' and c=='x'):
            buttons['text']='X'
            c='o'
            comp()
        '''elif(buttons['text']==' ' and c=='o'):
            buttons['text']='O'
            c='x'''
        if(b1['text']=='X' and b2['text']=='X' and b3['text']=='X'):
            messagebox.showinfo('HURRAY','PLAYER 1 WINS')
            gui.destroy()
            second()
        elif(b4['text']=='X' and b5['text']=='X' and b6['text']=='X'):
            messagebox.showinfo('HURRAY','PLAYER 1 WINS')
            gui.destroy()
            second() 
        elif(b7['text']=='X' and b8['text']=='X' and b9['text']=='X'):
            messagebox.showinfo('HURRAY','PLAYER 1 WINS')
            gui.destroy()
            second()
        elif(b1['text']=='X' and b4['text']=='X' and b7['text']=='X'):
            messagebox.showinfo('HURRAY','PLAYER 1 WINS')
            gui.destroy()
            second()
        elif(b2['text']=='X' and b5['text']=='X' and b8['text']=='X'):
            messagebox.showinfo('HURRAY','PLAYER 1 WINS')
            gui.destroy()
            second()
        elif(b3['text']=='X' and b6['text']=='X' and b9['text']=='X'):
            messagebox.showinfo('HURRAY','PLAYER 1 WINS')
            gui.destroy()
            second()
        elif(b1['text']=='X' and b5['text']=='X' and b9['text']=='X'):
            messagebox.showinfo('HURRAY','PLAYER 1 WINS')
            gui.destroy()
            second()
        elif(b3['text']=='X' and b5['text']=='X' and b7['text']=='X'):
            messagebox.showinfo('HURRAY','PLAYER 2 WINS')
            gui.destroy()
            second()
        elif(b1['text']=='O' and b2['text']=='O' and b3['text']=='O'):
            messagebox.showinfo('HURRAY','PLAYER 2 WINS')
            gui.destroy()
            second()
        elif(b4['text']=='O' and b5['text']=='O' and b6['text']=='O'):
            messagebox.showinfo('HURRAY','PLAYER 2 WINS')
            gui.destroy()
            second()                    
        elif(b7['text']=='O' and b8['text']=='O' and b9['text']=='O'):
            messagebox.showinfo('HURRAY','PLAYER 2 WINS')
            gui.destroy()
            second()                    
        elif(b1['text']=='O' and b4['text']=='O' and b7['text']=='O'):
            messagebox.showinfo('HURRAY','PLAYER 2 WINS')
            gui.destroy()
            second()
        elif(b2['text']=='O' and b5['text']=='O' and b8['text']=='O'):
            messagebox.showinfo('HURRAY','PLAYER 2 WINS')
            gui.destroy()
            second()
        elif(b3['text']=='O' and b6['text']=='O' and b9['text']=='O'):
            messagebox.showinfo('HURRAY','PLAYER 2 WINS')
            gui.destroy()
            second()                    
        elif(b1['text']=='O' and b5['text']=='O' and b9['text']=='O'):
            messagebox.showinfo('HURRAY','PLAYER 2 WINS')
            gui.destroy()
            second()
        elif(b3['text']=='O' and b5['text']=='O' and b7['text']=='O'):
            messagebox.showinfo('HURRAY','PLAYER 2 WINS')
            gui.destroy()
            second()
        elif(b1['text']!=' ' and b2['text']!=' ' and b3['text']!=' ' and b4['text']!=' ' and b5['text']!=' ' and b6['text']!=' ' and b7['text']!=' ' and b8['text']!=' ' and b9['text']!=' '):
            messagebox.showinfo('OOPS','GAME DRAW')
            gui.destroy()
            second()
    global b1
    global b2
    global b3
    global b4
    global b5
    global b6
    global b7
    global b8
    global b9
    gui=Tk()
    gui.configure(background='white')
    gui.title('TIC TAC TOE')
    gui.geometry('340x280')
    b1=Button(gui,text=' ',fg='red',bg='light yellow',command=lambda:press(b1),height=4,width=14,relief='sunken',state='active',cursor='clock')
    b2=Button(gui,text=' ',fg='red',bg='light yellow',command=lambda:press(b2),height=4,width=14,relief='sunken',state='active',cursor='dotbox')
    b3=Button(gui,text=' ',fg='red',bg='light yellow',command=lambda:press(b3),height=4,width=14,relief='sunken',state='active',cursor='cross')
    b4=Button(gui,text=' ',fg='red',bg='light yellow',command=lambda:press(b4),height=4,width=14,relief='sunken',state='active',cursor='circle')
    b5=Button(gui,text=' ',fg='red',bg='light yellow',command=lambda:press(b5),height=4,width=14,relief='sunken',state='active',cursor='exchange')
    b6=Button(gui,text=' ',fg='red',bg='light yellow',command=lambda:press(b6),height=4,width=14,relief='sunken',state='active',cursor='fleur')
    b7=Button(gui,text=' ',fg='red',bg='light yellow',command=lambda:press(b7),height=4,width=14,relief='sunken',state='active',cursor='heart')
    b8=Button(gui,text=' ',fg='red',bg='light yellow',command=lambda:press(b8),height=4,width=14,relief='sunken',state='active',cursor='man')
    b9=Button(gui,text=' ',fg='red',bg='light yellow',command=lambda:press(b9),height=4,width=14,relief='sunken',state='active',cursor='man')
    l=Label(gui,text='TAC',fg='Red',bg='light yellow',font=('Time',38,'bold'))
    l1=Label(gui,text=' TIC ',fg='Red',bg='light yellow',font=('Time',38,'bold'))
    l2=Label(gui,text='TOE',fg='Red',bg='light yellow',font=('Time',38,'bold'))
    l.grid(row=1,column=1)
    l1.grid(row=1,column=0)
    l2.grid(row=1,column=2)
    b1.grid(row=2,column=0)
    b2.grid(row=2,column=1)
    b3.grid(row=2,column=2)
    b4.grid(row=3,column=0)
    b5.grid(row=3,column=1)
    b6.grid(row=3,column=2)
    b7.grid(row=4,column=0)
    b8.grid(row=4,column=1)
    b9.grid(row=4,column=2)
def fiirst():
    global c
    c="x"
    def second():
        def exiit():
            messagebox.showinfo('exit','you are going to exit')
            scr.destroy()
        def restart():
            scr.destroy()
            fiirst()
        scr=Tk()
        scr.configure(background='light yellow')
        scr.title('TIC TAC TOE')
        scr.geometry('280x200')
        e=Button(scr,text='exit',fg='white',bg='red',command=lambda:exiit(),height=4,width=14,relief='sunken',state='active',cursor='clock')
        r=Button(scr,text='restart',fg='white',bg='green',command=lambda:restart(),height=4,width=14,relief='sunken',state='active',cursor='dotbox')
        l3=Label(scr,text='Match',fg='Red',bg='light yellow',font=('Time',38,'bold'))
        l4=Label(scr,text='Over',fg='Red',bg='light yellow',font=('Time',38,'bold'))
        l3.grid(row=1,column=0)
        l4.grid(row=1,column=1)
        e.grid(row=5,column=1)
        r.grid(row=5,column=0)
    def press(buttons):
        global c 
        if(buttons['text']==' ' and c=='x'):
            buttons['text']='X'
            c='o'
        elif(buttons['text']==' ' and c=='o'):
            buttons['text']='O'
            c='x'
        if(b1['text']=='X' and b2['text']=='X' and b3['text']=='X'):
            messagebox.showinfo('HURRAY','PLAYER 1 WINS')
            gui.destroy()
            second()
        elif(b4['text']=='X' and b5['text']=='X' and b6['text']=='X'):
            messagebox.showinfo('HURRAY','PLAYER 1 WINS')
            gui.destroy()
            second()
        elif(b7['text']=='X' and b8['text']=='X' and b9['text']=='X'):
            messagebox.showinfo('HURRAY','PLAYER 1 WINS')
            gui.destroy()
            second()
        elif(b1['text']=='X' and b4['text']=='X' and b7['text']=='X'):
            messagebox.showinfo('HURRAY','PLAYER 1 WINS')
            gui.destroy()
            second()
        elif(b2['text']=='X' and b5['text']=='X' and b8['text']=='X'):
            messagebox.showinfo('HURRAY','PLAYER 1 WINS')
            gui.destroy()
            second()
        elif(b3['text']=='X' and b6['text']=='X' and b9['text']=='X'):
            messagebox.showinfo('HURRAY','PLAYER 1 WINS')
            gui.destroy()
            second()
        elif(b1['text']=='X' and b5['text']=='X' and b9['text']=='X'):
            messagebox.showinfo('HURRAY','PLAYER 1 WINS')
            gui.destroy()
            second()
        elif(b3['text']=='X' and b5['text']=='X' and b7['text']=='X'):
            messagebox.showinfo('HURRAY','PLAYER 2 WINS')
            gui.destroy()
            second()
        elif(b1['text']=='O' and b2['text']=='O' and b3['text']=='O'):
            messagebox.showinfo('HURRAY','PLAYER 2 WINS')
            gui.destroy()
            second()
        elif(b4['text']=='O' and b5['text']=='O' and b6['text']=='O'):
            messagebox.showinfo('HURRAY','PLAYER 2 WINS')
            gui.destroy()
            second()                    
        elif(b7['text']=='O' and b8['text']=='O' and b9['text']=='O'):
            messagebox.showinfo('HURRAY','PLAYER 2 WINS')
            gui.destroy()
            second()                    
        elif(b1['text']=='O' and b4['text']=='O' and b7['text']=='O'):
            messagebox.showinfo('HURRAY','PLAYER 2 WINS')
            gui.destroy()
            second()
        elif(b2['text']=='O' and b5['text']=='O' and b8['text']=='O'):
            messagebox.showinfo('HURRAY','PLAYER 2 WINS')
            gui.destroy()
            second()
        elif(b3['text']=='O' and b6['text']=='O' and b9['text']=='O'):
            messagebox.showinfo('HURRAY','PLAYER 2 WINS')
            gui.destroy()
            second()                    
        elif(b1['text']=='O' and b5['text']=='O' and b9['text']=='O'):
            messagebox.showinfo('HURRAY','PLAYER 2 WINS')
            gui.destroy()
            second()
        elif(b3['text']=='O' and b5['text']=='O' and b7['text']=='O'):
            messagebox.showinfo('HURRAY','PLAYER 2 WINS')
            gui.destroy()
            second()
        elif(b1['text']!=' ' and b2['text']!=' ' and b3['text']!=' ' and b4['text']!=' ' and b5['text']!=' ' and b6['text']!=' ' and b7['text']!=' ' and b8['text']!=' ' and b9['text']!=' '):
            messagebox.showinfo('OOPS','GAME DRAW')
            gui.destroy()
            second()                    
    gui=Tk()
    gui.configure(background='white')
    gui.title('TIC TAC TOE')
    gui.geometry('340x280')
    b1=Button(gui,text=' ',fg='red',bg='light yellow',command=lambda:press(b1),height=4,width=14,relief='sunken',state='active',cursor='clock')
    b2=Button(gui,text=' ',fg='red',bg='light yellow',command=lambda:press(b2),height=4,width=14,relief='sunken',state='active',cursor='dotbox')
    b3=Button(gui,text=' ',fg='red',bg='light yellow',command=lambda:press(b3),height=4,width=14,relief='sunken',state='active',cursor='cross')
    b4=Button(gui,text=' ',fg='red',bg='light yellow',command=lambda:press(b4),height=4,width=14,relief='sunken',state='active',cursor='circle')
    b5=Button(gui,text=' ',fg='red',bg='light yellow',command=lambda:press(b5),height=4,width=14,relief='sunken',state='active',cursor='exchange')
    b6=Button(gui,text=' ',fg='red',bg='light yellow',command=lambda:press(b6),height=4,width=14,relief='sunken',state='active',cursor='fleur')
    b7=Button(gui,text=' ',fg='red',bg='light yellow',command=lambda:press(b7),height=4,width=14,relief='sunken',state='active',cursor='heart')
    b8=Button(gui,text=' ',fg='red',bg='light yellow',command=lambda:press(b8),height=4,width=14,relief='sunken',state='active',cursor='man')
    b9=Button(gui,text=' ',fg='red',bg='light yellow',command=lambda:press(b9),height=4,width=14,relief='sunken',state='active',cursor='man')
    l=Label(gui,text='TAC',fg='Red',bg='light yellow',font=('Time',38,'bold'))
    l1=Label(gui,text=' TIC ',fg='Red',bg='light yellow',font=('Time',38,'bold'))
    l2=Label(gui,text='TOE',fg='Red',bg='light yellow',font=('Time',38,'bold'))
    l.grid(row=1,column=1)
    l1.grid(row=1,column=0)
    l2.grid(row=1,column=2)
    b1.grid(row=2,column=0)
    b2.grid(row=2,column=1)
    b3.grid(row=2,column=2)
    b4.grid(row=3,column=0)
    b5.grid(row=3,column=1)
    b6.grid(row=3,column=2)
    b7.grid(row=4,column=0)
    b8.grid(row=4,column=1)
    b9.grid(row=4,column=2)
def game():
    def exiit():
        sscr.destroy()
        fiirst()
    def restart():
        sscr.destroy()
        first()
    sscr=Tk()
    sscr.configure(background='light yellow')
    sscr.title('TIC TAC TOE')
    sscr.geometry('100x145')
    ee=Button(sscr,text='play with friend',fg='white',bg='red',command=lambda:exiit(),height=4,width=14,relief='sunken',state='active',cursor='clock')
    rr=Button(sscr,text='play with computer',fg='white',bg='green',command=lambda:restart(),height=4,width=14,relief='sunken',state='active',cursor='dotbox')
    #ll3=Label(sscr,text='Match',fg='Red',bg='light yellow',font=('Time',38,'bold'))
    #ll4=Label(sscr,text='Over',fg='Red',bg='light yellow',font=('Time',38,'bold'))
    #ll3.grid(row=1,column=0)
    #ll4.grid(row=1,column=1)
    ee.grid(row=2,column=0)
    rr.grid(row=5,column=0)
    
game()
