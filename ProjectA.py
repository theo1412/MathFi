import tkinter
from tkinter.ttk import *
from tkinter import *
import numpy as np
from random import *

import tkinter
from tkinter.ttk import *
from tkinter import *
import numpy as np

global fenetre1, fenetre2, covp



def covid1():
    global fenetre1, covidpage
    fenetre1.destroy()
    covidpage()


def backmainf1():
    global fenetre1, fenetre2
    fenetre2.destroy()
    fenetre1()


def quit():
    global fenetre1
    fenetre1.destroy()


def covid2():
    global fenetre2, covid
    fenetre2.destroy()
    covidpage()


def test():
    global fenetre1, fenetre2
    fenetre1.destroy()
    acceuil()


def back():
    global fenetre2, fenetre1
    fenetre2.destroy()
    fenetre()

def back3():
    global fenetre3, fenetre1
    fenetre3.destroy()
    fenetre()


def backcov():
    global covid
    covid.destroy()
    covidpage()



def show_about():
    about_window = tkinter.Toplevel(fenetre1)
    about_window.geometry("650x100")
    about_window.resizable(width=0, height=0)
    about_window.title("Infos très très utiles")
    lb = tkinter.Label(about_window, text="All my homies hate Louis \n wlh c'est vrai")
    lb.pack()


def show_useless():
    useless_window = tkinter.Toplevel(fenetre1)
    useless_window.geometry("800x125")
    useless_window.resizable(width=0, height=0)
    useless_window.title("Infos inutiles mdrr")
    lb = tkinter.Label(useless_window,
                       text="Un être humain possède environ 639 muscles alors qu’une chenille en posséderait près de 4000!\n Pour échapper à l’emprise des mâchoires d’un crocodile, poussez vos pouces dans ses yeux, il vous lâchera  immédiatement.\n Les chauves-souris tournent toujours à gauche lorsqu’elles sortent d’une grotte.\n Une personne passe en moyenne 6 mois de sa vie assis devant un feu rouge.\n Si vous mâchez un chewing-gum en épluchant des oignons, cela vous empêchera de pleurer.\n Il y a plus de personnes tuées chaque année par des noix de coco qui tombent de l’arbre que par des attaques de requins. \n Dans le règlement de Facebook, il est stipulé qu’on peut travailler en chaussettes.")
    lb.pack()


def fenetre():
    global fenetre1
    fenetre1 = Tk()

    fenetre1.title("Test Médical")
    fenetre1.geometry("1080x720")
    fenetre1.minsize(480, 360)
    fenetre1.iconbitmap("logo.ico")
    fenetre1.config(background='#3D40EC')
    frame = Frame(fenetre1, background='#3D40EC')
    label_title = Label(frame, text="Project A", font=("Arial", 50), background="#3D40EC", fg="white")
    label_title.pack()
    label_subtitle = Label(frame, text="Choose your type of exercise", font=("Arial", 20), bg="#3D40EC", fg="white")
    label_subtitle.pack()
    button = Button(frame, text="Simple Interest", font=("Arial", 25), bg="white", fg="#3D40EC", command=test)
    button.pack(pady=25, fill=X)
    button2 = Button(frame, text="Compounds Interest", font=("Arial", 25), bg="white", fg="#3D40EC", command=covid1)
    button2.pack(pady=25, fill=X)
    frame.pack(expand=YES)
    nomd = tkinter.Label(fenetre1, text='Exclusive possession and distribution of Dos Reis Théo ®', font=("Arial", 20),
                         bg="#3D40EC", fg="white")
    nomd.place(relx=1.0, rely=1.0, anchor=SE)
    versionshow = tkinter.Label(fenetre1, text='Version 1.1.1', font=("Arial", 20), bg="#3D40EC", fg="white")
    versionshow.place(relx=0, rely=1.0, anchor=SW)
    buttonquit = Button(frame, text="Quit", font=("Arial", 25), bg="white", fg="#3D40EC", command=quit)
    buttonquit.pack(pady=25, fill=X, anchor=S)

    mainmenu = tkinter.Menu(fenetre1)

    first_menu = tkinter.Menu(mainmenu, tearoff=0)
    first_menu.add_command(label="Compounds Interest", command=covid1)
    first_menu.add_command(label="Simple Interest", command=test)
    first_menu.add_separator()
    first_menu.add_command(label="Quitter", command=fenetre1.quit)
    second_menu = tkinter.Menu(mainmenu, tearoff=0)
    second_menu.add_command(label="Infos utiles", command=show_about)
    second_menu.add_command(label="Infos pas utiles mdrr", command=show_useless)

    mainmenu.add_cascade(label="Menu Principal", menu=first_menu)
    mainmenu.add_cascade(label="A Propos", menu=second_menu)

    fenetre1.config(menu=mainmenu)
    fenetre1.mainloop()


def acceuil():
    global fenetre2, fenetre1, covp
    fenetre2 = Tk()

    listeentreprise = ['AllahMourim', 'SuperBock', 'SUUUUUUUUUU', 'Trouel=on', 'VivaChouriça']
    listeerreur = ["That's wrong", "You're soo bad", "Even Louis would have done better", "NOOOOOOOOOOOOOOOOOOOOOOOO"]
    entreprise = choice(listeentreprise)
    PV = randint(1000, 50000)
    years = randint(1, 15)
    rate = (randint(1, 20) / 100)

    fenetre2.title("Simple Interest")
    fenetre2.geometry("1080x720")
    fenetre2.minsize(600, 400)
    fenetre2.iconbitmap("logo.ico")
    fenetre2.config(background='#1B65C4')
    mainframe = tkinter.LabelFrame(fenetre2, text="Exercice", width=500, height=450)
    mainframe.pack(expand=YES)

    test3 = tkinter.Label(mainframe, text="You have money lying around in your bank account and decide to make an investment.\n So you decide to call the bank " + str(
                        entreprise) + "\nThis company offers you an initial investment of " + str(
                        PV) + "$ at a rate of " + str(
                        rate * 100) + "%" + "\nHow much money will you have after " + str(years) + " years ?\n", font=("ARIAL_BLUR", 20))
    test3.pack()

    entry = tkinter.Entry(mainframe, width=30, justify=CENTER, font=("ARIAL_BLUR", 20))
    entry.pack()

    def checkresult():

        erreur = choice(listeerreur)
        if str(entry.get()) == str((PV * years * rate) + PV):
            resultshow = "That's the good anwser"
        else:
            resultshow = erreur
        print ((PV * years * rate)+PV)
        print (entry.get())
        resultlabel = tkinter.Label(mainframe, text=resultshow, font=("ARIAL_BLUR",20))
        resultlabel.pack_forget()
        resultlabel.pack()




    start_button = Button(mainframe, text="Démarrer", bg='white', fg='#1B65C4', command=checkresult)
    start_button.pack()

    refreshb = Button(fenetre2, text='Quitter', command=back)
    refreshb.pack()

    mainmenu = tkinter.Menu(fenetre2)

    first_menu = tkinter.Menu(mainmenu, tearoff=0)
    first_menu.add_command(label="Test Covid", command=covid2)
    first_menu.add_command(label="Test Maladies")
    first_menu.add_separator()
    first_menu.add_command(label="Quitter", command=fenetre2.quit)
    second_menu = tkinter.Menu(mainmenu, tearoff=0)
    second_menu.add_command(label="Infos utiles", command=show_about)
    second_menu.add_command(label="Infos pas utiles mdrr", command=show_useless)

    mainmenu.add_cascade(label="Menu Principal", menu=first_menu)
    mainmenu.add_cascade(label="A Propos", menu=second_menu)

    fenetre2.config(menu=mainmenu)


def covidpage():
    global fenetre2, fenetre1, covid, fenetre3
    fenetre3 = Tk()

    listeentreprise = ['AllahMourim', 'SuperBock', 'SUUUUUUUUUU', 'Trouel=on', 'VivaChouriça']
    listeerreur = ["That's wrong", "You're soo bad", "Even Louis would have done better", "NOOOOOOOOOOOOOOOOOOOOOOOO"]
    entreprise = choice(listeentreprise)
    PV = randint(1000, 50000)
    years = randint(2, 15)
    rate = (randint(1, 20) / 100)

    fenetre3.title("Compound Interest")
    fenetre3.geometry("1080x720")
    fenetre3.minsize(600, 400)
    fenetre3.iconbitmap("logo.ico")
    fenetre3.config(background='#F37D06')
    mainframe = tkinter.LabelFrame(fenetre3, text="Exercice", width=500, height=450)
    mainframe.pack(expand=YES)

    test3 = tkinter.Label(mainframe,
                          text="You have money lying around in your bank account and decide to make an investment.\n So you decide to call the bank " + str(
                              entreprise) + "\nThis company offers you an initial investment of " + str(
                              PV) + "$ at a rate of " + str(
                              rate * 100) + "%" + "\nHow much money will you have after " + str(years) + " years ?"+"\n\nRound to the hundredths\n",
                          font=("ARIAL_BLUR", 20))
    test3.pack()

    entry = tkinter.Entry(mainframe, width=30, justify=CENTER, font=("ARIAL_BLUR", 20))
    entry.pack()

    def checkresult():

        erreur = choice(listeerreur)
        check3 = round(PV*((1+rate)**years),2)
        if str(entry.get()) == str(check3):
            resultshow = "That's the good anwser"
        else:
            resultshow = erreur
        print(round(PV*((1+rate)**years),2))
        print(entry.get())
        resultlabel = tkinter.Label(mainframe, text=resultshow, font=("ARIAL_BLUR", 20))
        resultlabel.pack_forget()
        resultlabel.pack()

    start_button = Button(mainframe, text="Démarrer", bg='white', fg='#F37D06', command=checkresult)
    start_button.pack()

    refreshb = Button(fenetre3, text='Quitter', command=back3)
    refreshb.pack()

    mainmenu = tkinter.Menu(fenetre3)

    first_menu = tkinter.Menu(mainmenu, tearoff=0)
    first_menu.add_command(label="Test Covid", command=covid2)
    first_menu.add_command(label="Test Maladies")
    first_menu.add_separator()
    first_menu.add_command(label="Quitter", command=fenetre3.quit)
    second_menu = tkinter.Menu(mainmenu, tearoff=0)
    second_menu.add_command(label="Infos utiles", command=show_about)
    second_menu.add_command(label="Infos pas utiles mdrr", command=show_useless)

    mainmenu.add_cascade(label="Menu Principal", menu=first_menu)
    mainmenu.add_cascade(label="A Propos", menu=second_menu)

    fenetre3.config(menu=mainmenu)


if __name__ == '__main__':
    fenetre()


