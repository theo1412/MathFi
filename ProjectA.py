from random import *
import tkinter
from tkinter.ttk import *
from tkinter import *



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


def yearsimpleswitch():
    global yearsimple, fenetre2
    fenetre2.destroy()
    yearsimple()


def yearcompoundswitch():
    global yearcompound, fenetre3
    fenetre3.destroy()
    yearcompound()


def ratecompoundswitch():
    global fenetre3, ratecompound
    fenetre3.destroy()
    ratecompound()


def ratesimpleswitch1():
    global fenetre2, ratesimple
    fenetre2.destroy()
    ratesimple()


def yearsimpleback():
    global yearsimple, fenetre2, fenetre1
    yearsimple.destroy()
    fenetre()


def yearcompoundback():
    global yearcompound, fenetre2, fenetre1, covidpage
    yearcompound.destroy()
    covidpage()


def ratecompoundback():
    global yearcompound, fenetre2, fenetre1, covidpage, ratecompound
    ratecompound.destroy()
    covidpage()


def ratesimpleback():
    global yearcompound, fenetre2, fenetre1, covidpage, ratesimple
    ratesimple.destroy()
    fenetre()






def fenetre():
    global fenetre2, fenetre1, covid, fenetre3, yearsimple, yearcompound, ratecompound, ratesimple, rateacturial
    fenetre1 = Tk()

    fenetre1.title("Project A")
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
    button = Button(frame, text="Acturial Rate", font=("Arial", 25), bg="white", fg="#3D40EC", command=rateacturial)
    button.pack(pady=25, fill=X)
    frame.pack(expand=YES)
    nomd = tkinter.Label(fenetre1, text='Exclusive possession and distribution of\nDos Reis Théo®', font=("Arial", 15),
                         bg="#3D40EC", fg="white")
    nomd.place(relx=1.0, rely=1.0, anchor=SE)
    versionshow = tkinter.Label(fenetre1, text='Version 1.2.2', font=("Arial", 20), bg="#3D40EC", fg="white")
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
    global fenetre2, fenetre1, covid, fenetre3, yearsimple, yearcompound, ratecompound, ratesimple, rateacturial, covp
    fenetre2 = Tk()

    listeentreprise = ['AllahMourim', 'SuperBock', 'SUUUUUUUUUU', 'Trouel=on', 'VivaChouriça', 'AllMyHomiesHatelouis']
    listeerreur = ["That's wrong", "You're soo bad", "Even Louis would have done better", "NOOOOOOOOOOOOOOOOOOOOOOOO"]
    entreprise = choice(listeentreprise)
    PV = randint(1000, 50000)
    years = randint(1, 15)
    rate = (round(randint(1, 20)) / 100)

    fenetre2.title("Simple Interest")
    fenetre2.geometry("1080x720")
    fenetre2.minsize(600, 400)
    fenetre2.iconbitmap("logo.ico")
    fenetre2.config(background='#1B65C4')
    mainframe = tkinter.LabelFrame(fenetre2, text="Exercice", width=500, height=450)
    mainframe.pack(expand=YES)

    test3 = tkinter.Label(mainframe,
                          text="You have money lying around in your bank account and decide to make an investment.\n So you decide to call the bank " + str(
                              entreprise) + "\nThis company offers you an initial investment of " + str(
                              PV) + " $ at a rate of " + str(
                              rate * 100) + "%" + "\nHow much money will you have after " + str(
                              years) + " years ?\n" + "\n\nRound to the hundredths\n", font=("ARIAL_BLUR", 20))
    test3.pack()

    entry = tkinter.Entry(mainframe, width=30, justify=CENTER, font=("ARIAL_BLUR", 20))
    entry.pack()

    def checkresult():

        check3 = round((PV * (1 + years + rate)), 2)
        erreur = choice(listeerreur)
        if str(entry.get()) == str(check3):
            resultshow = "That's the good anwser"
        else:
            resultshow = erreur
        print(round((PV * years * rate) + PV), 2)
        print(entry.get())
        resultlabel = tkinter.Label(mainframe, text=resultshow, font=("ARIAL_BLUR", 20))
        resultlabel.pack_forget()
        resultlabel.pack()

    skiptext = tkinter.Label(mainframe, text="", font=("ARIAL_BLUR", 20))
    skiptext.pack()
    start_button = Button(mainframe, text="Démarrer", bg='white', fg='#1B65C4', command=checkresult,
                          font=("ARIAL_BLUR", 15))
    start_button.pack()
    year_button = Button(mainframe, text="Year Exercise", bg='white', fg='#1B65C4', font=("ARIAL_BLUR", 15),
                         command=yearsimple)
    year_button.place(relx=1.0, rely=1.0, anchor=SE)
    rate_button = Button(mainframe, text="Rate Exercise", bg='white', fg='#1B65C4', font=("ARIAL_BLUR", 15),
                         command=ratesimple)
    rate_button.place(relx=0, rely=1.0, anchor=SW)

    refreshb = Button(fenetre2, text='Quitter', command=back)
    refreshb.pack()

    mainmenu = tkinter.Menu(fenetre2)

    first_menu = tkinter.Menu(mainmenu, tearoff=0)
    first_menu.add_command(label="Compound Interest", command=covid2)
    first_menu.add_command(label="Simple Interest")
    first_menu.add_separator()
    first_menu.add_command(label="Quitter", command=fenetre2.quit)
    second_menu = tkinter.Menu(mainmenu, tearoff=0)
    second_menu.add_command(label="Infos utiles", command=show_about)
    second_menu.add_command(label="Infos pas utiles mdrr", command=show_useless)

    mainmenu.add_cascade(label="Menu Principal", menu=first_menu)
    mainmenu.add_cascade(label="A Propos", menu=second_menu)

    fenetre2.config(menu=mainmenu)
    fenetre2.mainloop()


def covidpage():
    global fenetre2, fenetre1, covid, fenetre3
    fenetre3 = Tk()

    listeentreprise = ['AllahMourim', 'SuperBock', 'SUUUUUUUUUU', 'Trouel=on', 'VivaChouriça', 'AllMyHomiesHatelouis']
    listeerreur = ["That's wrong", "You're soo bad", "Even Louis would have done better", "NOOOOOOOOOOOOOOOOOOOOOOOO"]
    entreprise = choice(listeentreprise)
    PV = randint(1000, 50000)
    years = randint(2, 15)
    rate = (round(randint(1, 20)) / 100)

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
                              PV) + " $ at a rate of " + str(
                              rate * 100) + "%" + "\nHow much money will you have after " + str(
                              years) + " years ?" + "\n\nRound to the hundredths\n",
                          font=("ARIAL_BLUR", 20))
    test3.pack()

    entry = tkinter.Entry(mainframe, width=30, justify=CENTER, font=("ARIAL_BLUR", 20))
    entry.pack()

    def checkresult():

        erreur = choice(listeerreur)
        check3 = round(PV * ((1 + rate) ** years), 2)
        if str(entry.get()) == str(check3):
            resultshow = "That's the good anwser"
        else:
            resultshow = erreur
        print(round(PV * ((1 + rate) ** years), 2))
        print(entry.get())
        resultlabel = tkinter.Label(mainframe, text=resultshow, font=("ARIAL_BLUR", 20))
        resultlabel.pack()

    skiptext = tkinter.Label(mainframe, text="", font=("ARIAL_BLUR", 20))
    skiptext.pack()
    start_button = Button(mainframe, text="Démarrer", bg='white', fg='#F37D06', command=checkresult,
                          font=("ARIAL_BLUR", 15))
    start_button.pack()
    year_button = Button(mainframe, text="Year Exercise", bg='white', fg='#F37D06', font=("ARIAL_BLUR", 15),
                         command=yearcompound)
    year_button.place(relx=1.0, rely=1.0, anchor=SE)
    rate_button = Button(mainframe, text="Rate Exercise", bg='white', fg='#F37D06', font=("ARIAL_BLUR", 15),
                         command=ratecompound)
    rate_button.place(relx=0, rely=1.0, anchor=SW)

    refreshb = Button(fenetre3, text='Quitter', command=back3)
    refreshb.pack()

    mainmenu = tkinter.Menu(fenetre3)

    first_menu = tkinter.Menu(mainmenu, tearoff=0)
    first_menu.add_command(label="Compound Interest")
    first_menu.add_command(label="Simple Interest", command=backmainf1)
    first_menu.add_separator()
    first_menu.add_command(label="Quitter", command=fenetre3.quit)
    second_menu = tkinter.Menu(mainmenu, tearoff=0)
    second_menu.add_command(label="Infos utiles", command=show_about)
    second_menu.add_command(label="Infos pas utiles mdrr", command=show_useless)

    mainmenu.add_cascade(label="Menu Principal", menu=first_menu)
    mainmenu.add_cascade(label="A Propos", menu=second_menu)

    fenetre3.config(menu=mainmenu)
    fenetre3.mainloop()


def yearsimple():
    global fenetre2, fenetre1, covid, fenetre3, yearsimple
    yearsimple = Tk()

    listeentreprise = ['AllahMourim', 'SuperBock', 'SUUUUUUUUUU', 'Trouel=on', 'VivaChouriça', 'AllMyHomiesHatelouis']
    listeerreur = ["That's wrong", "You're soo bad", "Even Louis would have done better", "NOOOOOOOOOOOOOOOOOOOOOOOO"]
    entreprise = choice(listeentreprise)
    PV = randint(1000, 50000)
    years = randint(2, 15)
    rate = (round(randint(1, 20)) / 100)
    check3 = round((PV * (1 + years + rate)), 2)

    yearsimple.title("Simple Interest Years")
    yearsimple.geometry("1080x720")
    yearsimple.minsize(600, 400)
    yearsimple.iconbitmap("logo.ico")
    yearsimple.config(background='#80F306')
    mainframe = tkinter.LabelFrame(yearsimple, text="Exercice", width=500, height=450)
    mainframe.pack(expand=YES)

    test3 = tkinter.Label(mainframe,
                          text="You have money lying around in your bank account and decide to make an investment.\n So you decide to call the bank " + str(
                              entreprise) + "\nThis company offers you an initial investment of " + str(
                              PV) + " $ at a rate of " + str(
                              rate * 100) + "%" + "\nAt the end of the investment you will have " + str(
                              check3) + " $\n How many years will you have to invest to obtain this return ?\nRound to the nearest unit\n",
                          font=("ARIAL_BLUR", 20))
    test3.pack()

    entry = tkinter.Entry(mainframe, width=30, justify=CENTER, font=("ARIAL_BLUR", 20))
    entry.pack()

    def checkresult():

        erreur = choice(listeerreur)
        if str(entry.get()) == str(round(years)):
            resultshow = "That's the good anwser"
        else:
            resultshow = erreur
        print(round(years))
        print(entry.get())
        resultlabel = tkinter.Label(mainframe, text=resultshow, font=("ARIAL_BLUR", 20))
        resultlabel.pack()

    skiptext = tkinter.Label(mainframe, text="", font=("ARIAL_BLUR", 20))
    skiptext.pack()
    start_button = Button(mainframe, text="Démarrer", bg='white', fg='#80F306', command=checkresult,
                          font=("ARIAL_BLUR", 15))
    start_button.pack()


    mainmenu = tkinter.Menu(yearsimple)

    first_menu = tkinter.Menu(mainmenu, tearoff=0)
    first_menu.add_command(label="Compound Interest")
    first_menu.add_command(label="Simple Interest", command=backmainf1)
    first_menu.add_separator()
    first_menu.add_command(label="Quitter", command=yearsimple.quit)
    second_menu = tkinter.Menu(mainmenu, tearoff=0)
    second_menu.add_command(label="Infos utiles", command=show_about)
    second_menu.add_command(label="Infos pas utiles mdrr", command=show_useless)

    mainmenu.add_cascade(label="Menu Principal", menu=first_menu)
    mainmenu.add_cascade(label="A Propos", menu=second_menu)

    yearsimple.config(menu=mainmenu)
    yearsimple.mainloop()


def yearcompound():
    global fenetre2, fenetre1, covid, fenetre3, yearsimple, yearcompound
    yearcompound = Tk()

    listeentreprise = ['AllahMourim', 'SuperBock', 'SUUUUUUUUUU', 'Trouel=on', 'VivaChouriça', 'AllMyHomiesHatelouis']
    listeerreur = ["That's wrong", "You're soo bad", "Even Louis would have done better", "NOOOOOOOOOOOOOOOOOOOOOOOO"]
    entreprise = choice(listeentreprise)
    PV = randint(1000, 50000)
    years = randint(2, 15)
    rate = (round(randint(1, 20)) / 100)
    check3 = round((PV * (1 + years + rate)), 2)

    yearcompound.title("Compound Interest Years")
    yearcompound.geometry("1080x720")
    yearcompound.minsize(600, 400)
    yearcompound.iconbitmap("logo.ico")
    yearcompound.config(background='#F306EF')
    mainframe = tkinter.LabelFrame(yearcompound, text="Exercice", width=500, height=450)
    mainframe.pack(expand=YES)

    test3 = tkinter.Label(mainframe,
                          text="You have money lying around in your bank account and decide to make an investment.\n So you decide to call the bank " + str(
                              entreprise) + "\nThis company offers you an initial investment of " + str(
                              PV) + " $ at a rate of " + str(
                              rate * 100) + "%" + "\nAt the end of the investment you will have " + str(
                              check3) + " $\n How many years will you have to invest to obtain this return ?\nRound to the nearest unit\n",
                          font=("ARIAL_BLUR", 20))
    test3.pack()

    entry = tkinter.Entry(mainframe, width=30, justify=CENTER, font=("ARIAL_BLUR", 20))
    entry.pack()

    def checkresult():

        erreur = choice(listeerreur)
        if str(entry.get()) == str(round(years)):
            resultshow = "That's the good anwser"
        else:
            resultshow = erreur
        print(round(years))
        print(entry.get())
        resultlabel = tkinter.Label(mainframe, text=resultshow, font=("ARIAL_BLUR", 20))
        resultlabel.pack()

    skiptext = tkinter.Label(mainframe, text="", font=("ARIAL_BLUR", 20))
    skiptext.pack()
    start_button = Button(mainframe, text="Démarrer", bg='white', fg='#F306EF', command=checkresult,
                          font=("ARIAL_BLUR", 15))
    start_button.pack()


    mainmenu = tkinter.Menu(yearcompound)

    first_menu = tkinter.Menu(mainmenu, tearoff=0)
    first_menu.add_command(label="Compound Interest")
    first_menu.add_command(label="Simple Interest", command=backmainf1)
    first_menu.add_separator()
    first_menu.add_command(label="Quitter", command=yearcompound.quit)
    second_menu = tkinter.Menu(mainmenu, tearoff=0)
    second_menu.add_command(label="Infos utiles", command=show_about)
    second_menu.add_command(label="Infos pas utiles mdrr", command=show_useless)

    mainmenu.add_cascade(label="Menu Principal", menu=first_menu)
    mainmenu.add_cascade(label="A Propos", menu=second_menu)

    yearcompound.config(menu=mainmenu)
    yearcompound.mainloop()


def ratecompound():
    global fenetre2, fenetre1, covid, fenetre3, yearsimple, yearcompound, ratecompound
    ratecompound = Tk()

    listeentreprise = ['AllahMourim', 'SuperBock', 'SUUUUUUUUUU', 'Trouel=on', 'VivaChouriça', 'AllMyHomiesHatelouis']
    listeerreur = ["That's wrong", "You're soo bad", "Even Louis would have done better", "NOOOOOOOOOOOOOOOOOOOOOOOO"]
    entreprise = choice(listeentreprise)
    PV = randint(1000, 50000)
    years = randint(2, 15)
    rate = (round(randint(1, 20)) / 100)
    check3 = round(PV * ((1 + rate) ** years), 2)

    ratecompound.title("Compound Interest Years")
    ratecompound.geometry("1080x720")
    ratecompound.minsize(600, 400)
    ratecompound.iconbitmap("logo.ico")
    ratecompound.config(background='#F30606')
    mainframe = tkinter.LabelFrame(ratecompound, text="Exercice", width=500, height=450)
    mainframe.pack(expand=YES)

    test3 = tkinter.Label(mainframe,
                          text="You have money lying around in your bank account and decide to make an investment.\n So you decide to call the bank " + str(
                              entreprise) + "\nThis company offers you an initial investment of " + str(
                              PV) + " $ for " + str(
                              years) + " years" + "\nAt the end of the investment you will have " + str(
                              check3) + " $\n What was the interest rate of the investment ?\nRound to the nearest unit\n",
                          font=("ARIAL_BLUR", 20))
    test3.pack()

    entry = tkinter.Entry(mainframe, width=30, justify=CENTER, font=("ARIAL_BLUR", 20))
    entry.pack()

    def checkresult():

        erreur = choice(listeerreur)
        if str(entry.get()) == str(round(rate * 100)):
            resultshow = "That's the good anwser"
        else:
            resultshow = erreur
        print(round(rate * 100))
        print(entry.get())
        resultlabel = tkinter.Label(mainframe, text=resultshow, font=("ARIAL_BLUR", 20))
        resultlabel.pack()

    skiptext = tkinter.Label(mainframe, text="", font=("ARIAL_BLUR", 20))
    skiptext.pack()
    start_button = Button(mainframe, text="Démarrer", bg='white', fg='#F30606', command=checkresult,
                          font=("ARIAL_BLUR", 15))
    start_button.pack()

    mainmenu = tkinter.Menu(ratecompound)

    first_menu = tkinter.Menu(mainmenu, tearoff=0)
    first_menu.add_command(label="Compound Interest")
    first_menu.add_command(label="Simple Interest", command=backmainf1)
    first_menu.add_separator()
    first_menu.add_command(label="Quitter", command=ratecompound.quit)
    second_menu = tkinter.Menu(mainmenu, tearoff=0)
    second_menu.add_command(label="Infos utiles", command=show_about)
    second_menu.add_command(label="Infos pas utiles mdrr", command=show_useless)

    mainmenu.add_cascade(label="Menu Principal", menu=first_menu)
    mainmenu.add_cascade(label="A Propos", menu=second_menu)

    ratecompound.config(menu=mainmenu)
    ratecompound.mainloop()


def ratesimple():
    global fenetre2, fenetre1, covid, fenetre3, yearsimple, yearcompound, ratecompound, ratesimple
    ratesimple = Tk()

    listeentreprise = ['AllahMourim', 'SuperBock', 'SUUUUUUUUUU', 'Trouel=on', 'VivaChouriça', 'AllMyHomiesHatelouis']
    listeerreur = ["That's wrong", "You're soo bad", "Even Louis would have done better", "NOOOOOOOOOOOOOOOOOOOOOOOO"]
    entreprise = choice(listeentreprise)
    PV = randint(1000, 50000)
    years = randint(2, 15)
    rate = (round(randint(1, 20)) / 100)
    check3 = round((PV * (1 + years + rate)), 2)

    ratesimple.title("Simple Interest Years")
    ratesimple.geometry("1080x720")
    ratesimple.minsize(600, 400)
    ratesimple.iconbitmap("logo.ico")
    ratesimple.config(background='#06F3B6')
    mainframe = tkinter.LabelFrame(ratesimple, text="Exercice", width=500, height=450)
    mainframe.pack(expand=YES)

    test3 = tkinter.Label(mainframe,
                          text="You have money lying around in your bank account and decide to make an investment.\n So you decide to call the bank " + str(
                              entreprise) + "\nThis company offers you an initial investment of " + str(
                              PV) + " $ for " + str(
                              years) + " years" + "\nAt the end of the investment you will have " + str(
                              check3) + " $\n What was the interest rate of the investment ?\nRound to the nearest unit\n",
                          font=("ARIAL_BLUR", 20))
    test3.pack()

    entry = tkinter.Entry(mainframe, width=30, justify=CENTER, font=("ARIAL_BLUR", 20))
    entry.pack()

    def checkresult():

        erreur = choice(listeerreur)
        if str(entry.get()) == str(round(rate * 100)):
            resultshow = "That's the good anwser"
        else:
            resultshow = erreur
        print(round(rate * 100))
        print(entry.get())
        resultlabel = tkinter.Label(mainframe, text=resultshow, font=("ARIAL_BLUR", 20))
        resultlabel.pack()

    skiptext = tkinter.Label(mainframe, text="", font=("ARIAL_BLUR", 20))
    skiptext.pack()
    start_button = Button(mainframe, text="Démarrer", bg='white', fg='#06F3B6', command=checkresult,
                          font=("ARIAL_BLUR", 15))
    start_button.pack()

    refreshb = Button(ratesimple, text='Quitter', command=ratesimpleback)
    refreshb.pack()

    mainmenu = tkinter.Menu(ratesimple)

    first_menu = tkinter.Menu(mainmenu, tearoff=0)
    first_menu.add_command(label="Compound Interest")
    first_menu.add_command(label="Simple Interest", command=backmainf1)
    first_menu.add_separator()
    first_menu.add_command(label="Quitter", command=ratesimple.quit)
    second_menu = tkinter.Menu(mainmenu, tearoff=0)
    second_menu.add_command(label="Infos utiles", command=show_about)
    second_menu.add_command(label="Infos pas utiles mdrr", command=show_useless)

    mainmenu.add_cascade(label="Menu Principal", menu=first_menu)
    mainmenu.add_cascade(label="A Propos", menu=second_menu)

    ratesimple.config(menu=mainmenu)
    ratesimple.mainloop()


def rateacturial():
    global fenetre2, fenetre1, covid, fenetre3, yearsimple, yearcompound, ratecompound, ratesimple, rateacturial
    rateacturial = Tk()

    listeentreprise = ['AllahMourim', 'SuperBock', 'SUUUUUUUUUU', 'Trouel=on', 'VivaChouriça', 'AllMyHomiesHatelouis']
    listeerreur = ["That's wrong", "You're soo bad", "Even Louis would have done better", "NOOOOOOOOOOOOOOOOOOOOOOOO"]
    entreprise = choice(listeentreprise)
    PV = randint(1000, 50000)
    years = randint(2, 15)
    rate = (round(randint(1, 20)) / 100)
    check3 = round((PV * (1 + years + rate)), 2)

    rateacturial.title("Rate Acturial")
    rateacturial.geometry("1080x720")
    rateacturial.minsize(600, 400)
    rateacturial.iconbitmap("logo.ico")
    rateacturial.config(background='#5873D0')
    mainframe = tkinter.LabelFrame(rateacturial, text="Exercice", width=500, height=450)
    mainframe.pack(expand=YES)

    test3 = tkinter.Label(mainframe,
                          text="You have money lying around in your bank account and decide to make an investment.\n So you decide to call the bank " + str(
                              entreprise) + "\nThis company offers you an initial investment of " + str(
                              PV) + " $ for " + str(
                              years) + " years" + "\nAt the end of the investment you will have " + str(
                              check3) + " $\n What was the interest rate of the investment ?\nRound to the nearest unit\n",
                          font=("ARIAL_BLUR", 20))
    test3.pack()

    entry = tkinter.Entry(mainframe, width=30, justify=CENTER, font=("ARIAL_BLUR", 20))
    entry.pack()

    def checkresult():

        erreur = choice(listeerreur)
        if str(entry.get()) == str(round(rate * 100)):
            resultshow = "That's the good anwser"
        else:
            resultshow = erreur
        print(round(rate * 100))
        print(entry.get())
        resultlabel = tkinter.Label(mainframe, text=resultshow, font=("ARIAL_BLUR", 20))
        resultlabel.pack()

    skiptext = tkinter.Label(mainframe, text="", font=("ARIAL_BLUR", 20))
    skiptext.pack()
    start_button = Button(mainframe, text="Démarrer", bg='white', fg='#5873D0', command=checkresult,
                          font=("ARIAL_BLUR", 15))
    start_button.pack()


    mainmenu = tkinter.Menu(rateacturial)

    first_menu = tkinter.Menu(mainmenu, tearoff=0)
    first_menu.add_command(label="Compound Interest")
    first_menu.add_command(label="Simple Interest", command=backmainf1)
    first_menu.add_separator()
    first_menu.add_command(label="Quitter", command=rateacturial.quit)
    second_menu = tkinter.Menu(mainmenu, tearoff=0)
    second_menu.add_command(label="Infos utiles", command=show_about)
    second_menu.add_command(label="Infos pas utiles mdrr", command=show_useless)

    mainmenu.add_cascade(label="Menu Principal", menu=first_menu)
    mainmenu.add_cascade(label="A Propos", menu=second_menu)

    rateacturial.config(menu=mainmenu)
    rateacturial.mainloop()


if __name__ == '__main__':
    fenetre()
