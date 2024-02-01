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
    global fenetre2
    fenetre2.destroy()
    acceuil()

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
    lb = tkinter.Label(useless_window, text="Un être humain possède environ 639 muscles alors qu’une chenille en posséderait près de 4000!\n Pour échapper à l’emprise des mâchoires d’un crocodile, poussez vos pouces dans ses yeux, il vous lâchera  immédiatement.\n Les chauves-souris tournent toujours à gauche lorsqu’elles sortent d’une grotte.\n Une personne passe en moyenne 6 mois de sa vie assis devant un feu rouge.\n Si vous mâchez un chewing-gum en épluchant des oignons, cela vous empêchera de pleurer.\n Il y a plus de personnes tuées chaque année par des noix de coco qui tombent de l’arbre que par des attaques de requins. \n Dans le règlement de Facebook, il est stipulé qu’on peut travailler en chaussettes.")
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
    label_title = Label(frame, text="Welcome to MathFi Exercises", font=("Arial", 50), background="#3D40EC", fg="white")
    label_title.pack()
    label_subtitle = Label(frame, text="Choose your type of exercise", font=("Arial", 20), bg="#3D40EC", fg="white")
    label_subtitle.pack()
    button = Button(frame, text="Simple Interest", font=("Arial", 25), bg="white", fg="#3D40EC", command=test)
    button.pack(pady=25, fill=X)
    button2 = Button(frame, text="Compounds Interest", font=("Arial", 25), bg="white", fg="#3D40EC", command=covid1)
    button2.pack(pady=25, fill=X)
    frame.pack(expand=YES)
    nomd = tkinter.Label(fenetre1, text='Exclusive possession and distribution of Dos Reis Théo ®', font=("Arial", 20), bg="#3D40EC", fg="white")
    nomd.place(relx=1.0, rely=1.0, anchor=SE)
    versionshow = tkinter.Label(fenetre1, text='Version 1.0.1', font=("Arial", 20), bg="#3D40EC", fg="white")
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

    def expmode():
        if (scale_exp['state'] == NORMAL):
            scale_exp['state'] = DISABLED
        else:
            scale_exp['state'] = NORMAL


    def start_prog():

        start_button['state'] = DISABLED
        b = var_sc1.get()
        c = var_sc2.get()
        d = var_sc3.get()
        e = var_sc4.get()
        f = var_yn.get()
        z = var_exp.get()
        x_entrer = np.array(([8, 0, 0, 6, 1], [6, 0, 9, 9, 0], [4, 10, 0, 2, 0], [8, 7, 6, 0, 0], [0, 0, 6, 0, 1],
                             [0, 4, 4, 0, 0], [0, 4, 9, 0, 0], [4, 10, 0, 0, 0], [b, c, d, e, f]), dtype=float)
        y = np.array(([0.1], [0.2], [0.3], [0.4], [0.5], [0.6], [0.6], [0.3]), dtype=float)
        x_entrer = x_entrer / np.amax(x_entrer, axis=0)
        X = np.split(x_entrer, [8])[0]
        xPrediction = np.split(x_entrer, [8])[1]

        class Neural_Network(object):
            def __init__(self):
                self.inputSize = 5  # synapse d'entrée
                self.outputSize = 1  # la valeur de sortie (on en veut que une)
                self.hiddenSize = 7  # les synapse cachées
                self.W1 = np.random.randn(self.inputSize, self.hiddenSize)
                self.W2 = np.random.randn(self.hiddenSize, self.outputSize)

            def forward(self, X):
                self.z = np.dot(X, self.W1)
                self.z2 = self.sigmoid(self.z)
                self.z3 = np.dot(self.z2, self.W2)
                o = self.sigmoid(self.z3)
                return o

            def sigmoid(self, s):
                return 1 / (1 + np.exp(-s))

            def sigmoidPrime(self, s):
                return s * (1 - s)

            def backward(self, X, y, o):
                self.o_error = y - o
                self.o_delta = self.o_error * self.sigmoidPrime(o)
                self.z2_error = self.o_delta.dot(self.W2.T)
                self.z2_delta = self.z2_error * self.sigmoidPrime(self.z2)
                self.W1 += X.T.dot(self.z2_delta)
                self.W2 += self.z2.T.dot(self.o_delta)

            def train(self, X, y):
                o = self.forward(X)
                self.backward(X, y, o)

            def predict(self):
                print("Donnée predite apres entrainement:")
                print("Entrée : \n" + str(xPrediction))
                print("Sortie : \n" + str(self.forward(xPrediction)))
                if (self.forward(xPrediction) < 0.13):
                     result = " Il s'agit de la Fièvre Jaune ! "
                elif (self.forward(xPrediction) < 0.23):
                    result = " Il s'agit du Typhus ! "
                elif (self.forward(xPrediction) < 0.33):
                    result= " Il s'agit du Palludisme ! "
                elif (self.forward(xPrediction) < 0.43):
                    result =  " Il s'agit de Ebolla ! "
                elif (self.forward(xPrediction) < 0.53):
                    result = " Il s'agit de la Cirrose ! "
                elif (self.forward(xPrediction) < 0.63):
                    result = " Il s'agit de la Psoriasis ! "
                else:
                    result = "Erreur valeurs, recommencez"
                test3 = tkinter.Label(mainframe, text=result, font=("ARIAL_BLUR", 25))
                test3.pack_forget()
                test3.pack()




        NN = Neural_Network()
        for i in range(z):
            print("#" + str(i) + "\n")
            print("Valeurs d'entrées: \n" + str(X))
            print("Sortie Actuelle: \n" + str(y))
            print("Sortie predite: \n" + str(np.matrix.round(NN.forward(X), 2)))
            print("\n")
            progress['value'] = ((1 * i) * 100 / 3000)
            fenetre2.update_idletasks()
            NN.train(X, y)
        NN.predict()



    # obs
    def updateyn_observer(*args):
        if var_yn.get():
            f = 1
        else:
            f = 0
        print(f)

    def updatesc1_observer(*args):
        if var_sc1.get():
            b = var_sc1.get()
        else:
            b = 0
        print(b)

    def updatesc2_observer(*args):
        if var_sc2.get():
            c = var_sc2.get()
        else:
            c = 0
        print(c)

    def updatesc3_observer(*args):
        if var_sc3.get():
            d = var_sc3.get()
        else:
            d = 0
        print(d)

    def updatesc4_observer(*args):
        if var_sc4.get():
            e = var_sc4.get()
        else:
            e = 0
        print(e)

    def exp_observer(*args):
        if var_exp.get():
            z = var_exp.get()
        else:
            z = 3000
        print(z)




    var_yn = tkinter.IntVar()
    var_yn.trace("w", updateyn_observer)
    var_sc1 = tkinter.IntVar()
    var_sc1.trace("w", updatesc1_observer)
    var_sc2 = tkinter.IntVar()
    var_sc2.trace("w", updatesc2_observer)
    var_sc3 = tkinter.IntVar()
    var_sc3.trace("w", updatesc3_observer)
    var_sc4 = tkinter.IntVar()
    var_sc4.trace("w", updatesc4_observer)
    var_exp = tkinter.IntVar()
    var_exp.trace("w", exp_observer)


    fenetre2.title("Test Médical")
    fenetre2.geometry("1080x720")
    fenetre2.minsize(480, 360)
    fenetre2.iconbitmap("logo.ico")
    fenetre2.config(background='#1B65C4')
    mainframe = tkinter.LabelFrame(fenetre2, text="Symptomes", width=500, height=450)
    mainframe.pack(expand=YES)

    scale_w = tkinter.Scale(mainframe, from_=0, to=10, variable=var_sc1, orient='horizontal', label='Fièvre:',tickinterval=5, length=300)
    scale_w.pack()
    scale_w2 = tkinter.Scale(mainframe, from_=0, to=10, variable=var_sc2, orient='horizontal', label='Douleurs:', tickinterval=5, length=300)
    scale_w2.pack()
    scale_w3 = tkinter.Scale(mainframe, from_=0, to=10, variable=var_sc3, orient='horizontal', label='Marques Cutanées:', tickinterval=5, length=300)
    scale_w3.pack()
    scale_w4 = tkinter.Scale(mainframe, from_=0, to=10, variable=var_sc4, orient='horizontal', label='Céphalées:', tickinterval=5, length=300)
    scale_w4.pack()

    jaunisse = tkinter.Label(mainframe, text="Souffrez vous de Jaunisse ?")
    jaunisse.pack()
    radio1 = tkinter.Radiobutton(mainframe, text="Oui", value=1, variable=var_yn)
    radio2 = tkinter.Radiobutton(mainframe, text="Non", value=0, variable=var_yn)
    radio1.pack()
    radio2.pack()
    scale_exp = tkinter.Scale(mainframe, from_=3000, to=10000, resolution=500, variable=var_exp, orient='horizontal', label="Nombre d'entrainements:", tickinterval=3500, length=300)
    scale_exp.pack()
    scale_exp['state'] = DISABLED
    start_button = Button(mainframe, text="Démarrer", bg='white', fg='#1B65C4', command=start_prog)
    start_button.pack()

    refreshb = Button(fenetre2, text='Refresh', command=back)
    refreshb.pack()
    checkexp = tkinter.Checkbutton(fenetre2, text='ExpertMode', command=expmode)
    checkexp.place(relx=1.0, rely=1.0, anchor=SE)
    progress = Progressbar(fenetre2, orient=HORIZONTAL, length=100, mode='determinate')
    progress.pack()



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
    global fenetre2, fenetre1, covid
    covid = Tk()
    covid.title("Test Covid")
    covid.geometry("1080x720")
    covid.minsize(480, 360)
    covid.iconbitmap("logo.ico")
    covid.config(background='#E97C00')



    def observer1(*args):
        if var1.get():
            b = var1.get()
        else:
            b = 0
        print(b)

    def observer2(*args):
        if var2.get():
            c = var2.get()
        else:
            c = 0
        print(c)

    def observer3(*args):
        if var3.get():
            d = var3.get()
        else:
            d = 0
        print(d)

    def observer4(*args):
        if var4.get():
            e = var4.get()
        else:
            e = 0
        print(e)

    def observer5(*args):
        if var5.get():
            f = var5.get()
        else:
            f = 0
        print(f)

    def start_cov():
        b = var1.get()
        c = var2.get()
        d = var3.get()
        e = var4.get()
        f = var5.get()
        x_entrer = np.array(([3, 4, 7, 2, 5], [8, 8, 9, 0, 4], [4, 5, 3, 9, 9], [6, 2, 2, 10, 8], [7, 6, 5, 4, 5],
                             [10, 8, 9, 0, 5], [3, 4, 7, 0, 8], [8, 2, 2, 8, 7], [b, c, d, e, f]), dtype=float)
        y = np.array(([0], [0], [1], [1], [0], [0], [0], [1]), dtype=float)
        x_entrer = x_entrer / np.amax(x_entrer, axis=0)
        X = np.split(x_entrer, [8])[0]
        xPrediction = np.split(x_entrer, [8])[1]

        class Neural_Network(object):
            def __init__(self):
                self.inputSize = 5  # synapse d'entrée
                self.outputSize = 1  # la valeur de sortie (on en veut que une)
                self.hiddenSize = 7  # les synapse cachées
                self.W1 = np.random.randn(self.inputSize, self.hiddenSize)
                self.W2 = np.random.randn(self.hiddenSize, self.outputSize)

            def forward(self, X):
                self.z = np.dot(X, self.W1)
                self.z2 = self.sigmoid(self.z)
                self.z3 = np.dot(self.z2, self.W2)
                o = self.sigmoid(self.z3)
                return o

            def sigmoid(self, s):
                return 1 / (1 + np.exp(-s))

            def sigmoidPrime(self, s):
                return s * (1 - s)

            def backward(self, X, y, o):
                self.o_error = y - o
                self.o_delta = self.o_error * self.sigmoidPrime(o)
                self.z2_error = self.o_delta.dot(self.W2.T)
                self.z2_delta = self.z2_error * self.sigmoidPrime(self.z2)
                self.W1 += X.T.dot(self.z2_delta)
                self.W2 += self.z2.T.dot(self.o_delta)

            def train(self, X, y):
                o = self.forward(X)
                self.backward(X, y, o)

            def predict(self):
                print("Donnée predite apres entrainement:")
                print("Entrée : \n" + str(xPrediction))
                print("Sortie : \n" + str(self.forward(xPrediction)))
                if (self.forward(xPrediction) < 0.5):
                    result = "Il ne s'agit pas du Covid 19 !"
                else:
                    result = "Il s'agit du Covid 19 !"

                test3 = tkinter.Label(mainframecov, text=result, font=("ARIAL_BLUR", 25))
                test3.pack_forget()
                test3.pack()
        NN = Neural_Network()
        for i in range(3000):
            print("#" + str(i) + "\n")
            print("Valeurs d'entrées: \n" + str(X))
            print("Sortie Actuelle: \n" + str(y))
            print("Sortie predite: \n" + str(np.matrix.round(NN.forward(X), 2)))
            print("\n")
            NN.train(X, y)
        NN.predict()

    var1 = tkinter.IntVar()
    var1.trace("w", observer1)
    var2 = tkinter.IntVar()
    var2.trace("w", observer2)
    var3 = tkinter.IntVar()
    var3.trace("w", observer3)
    var4 = tkinter.IntVar()
    var4.trace("w", observer4)
    var5 = tkinter.IntVar()
    var5.trace("w", observer5)

    mainframecov = tkinter.LabelFrame(covid, text="Symptomes", width=500, height=450)
    mainframecov.pack(expand=YES)
    spintoux = tkinter.Scale(mainframecov, label='Toux:', from_=0, to=10, length=300, orient='horizontal')
    spintoux.pack()
    spinmv = tkinter.Scale(mainframecov, label='Mal de ventre:', from_=0, to=10, length=300, orient='horizontal')
    spinmv.pack()
    spinnc = tkinter.Scale(mainframecov, label='Nez qui coule:', from_=0, to=10, length=300, orient='horizontal')
    spinnc.pack()
    spindr = tkinter.Scale(mainframecov, label='Difficultés respiratoires:', from_=0, to=10, length=300, orient='horizontal')
    spindr.pack()
    spinf = tkinter.Scale(mainframecov, label='Fièvre:', from_=0, to=10, length=300, orient='horizontal')
    spinf.pack()
    start_button = Button(mainframecov, text="Démarrer", bg='white', fg='#E97C00', command=start_cov)
    start_button.pack()
    refreshb = Button(covid, text='Refresh', command=backcov)
    refreshb.pack()

    mainmenu = tkinter.Menu(covid)

    first_menu = tkinter.Menu(mainmenu, tearoff=0)
    first_menu.add_command(label="Test Covid")
    first_menu.add_command(label="Test Maladies", command=test)
    first_menu.add_separator()
    first_menu.add_command(label="Quitter", command=covid.quit)
    second_menu = tkinter.Menu(mainmenu, tearoff=0)
    second_menu.add_command(label="Infos utiles", command=show_about)
    second_menu.add_command(label="Infos pas utiles mdrr", command=show_useless)

    mainmenu.add_cascade(label="Menu Principal", menu=first_menu)
    mainmenu.add_cascade(label="A Propos", menu=second_menu)

    covid.config(menu=mainmenu)
    covid.mainloop()

if __name__ == '__main__':
    fenetre()