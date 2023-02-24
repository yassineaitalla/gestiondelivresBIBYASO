from ast import Delete, excepthandler
from cProfile import label
from email.mime import image
from logging import root
from re import L
from tkinter import * #pour importer la bibliotheque tkinter
from subprocess import call #Bibliotheque qui permet de faire appel au page sur les quelles on clique
from tkinter import ttk, messagebox #permetre de gerer les selcetions et les message derrueeur  afficher ou de securite
from turtle import bgcolor, title #permet d'importer les background et les titres
import pymysql #bibliotheque pour faire des requettes vers la base de donnes
     

class AjoutLivres:  # 
    def __init__(self,root):                   
        self.PageAjouterDesLivres = root
        self.PageAjouterDesLivres.title("Ajouter un livre") #titre Ajouter un livre
        self.PageAjouterDesLivres.geometry("1040x560+400+200") #taille de l'application
        self.PageAjouterDesLivres.resizable(width=False, height=False)# eviter d'agrandir la fenetre
        self.PageAjouterDesLivres.iconbitmap("Images/bib.ico") 



        #On déclare des variables pour ensuite les récuperer
        self.TitreLivre = StringVar()
        self.Auteurs = StringVar()
        self.Collections = StringVar()
        self.Etat = StringVar()
        
        #Panneau vert gestion livres
        self.Paneauvertdegestionlivres = Frame(self.PageAjouterDesLivres, bg="#bedb0d")
        self.Paneauvertdegestionlivres.place(x=190, y=0, width=1100, height=1000)

        #Panneau orange gestion livres
        Paneauorangedegestionlivres = Frame(self.PageAjouterDesLivres, bg="#ff7f00")
        Paneauorangedegestionlivres.place(x=0, y=0, width=190, height=1000)

        #PhotoBoutons
        self.ImageGestionlivres = PhotoImage(file="Images/Gestionlivre.png")
        self.BoutonImagesGestionlivre = Button(self.PageAjouterDesLivres,command=self.VersGestionlivres, text="",image=self.ImageGestionlivres, width=184,height=90, bg="#ff7f00",font="arial 12 bold")
        self.BoutonImagesGestionlivre.place(x=0 , y=0) 
        
        self.ImageAdherents = PhotoImage(file="Images/Adherents.png")
        self.BoutonImageAdherents = Button(self.PageAjouterDesLivres,command=self.VersAdherents ,text="",image=self.ImageAdherents, width=184, height=90, bg="#ff7f00",font="arial 12 bold")
        self.BoutonImageAdherents.place(x=0 , y=140) 

        self.ImageEmprunter = PhotoImage(file="Images/Emprunter.png")
        self.BoutonImageEmprunter = Button(self.PageAjouterDesLivres,command=self.VersGestiondesprets, text="",image=self.ImageEmprunter, width=184, height=90, bg="#ff7f00",font="arial 12 bold")
        self.BoutonImageEmprunter.place(x=0 , y=280) 

        self.ImageSedeconnecter = PhotoImage(file="Images/Sedeconnecter.png")
        self.BoutonImageSedeconnecter = Button(self.PageAjouterDesLivres, text="",command=self.PourSedeconnecter,image=self.ImageSedeconnecter, width=184, height=90, bg="#ff7f00",font="arial 12 bold")
        self.BoutonImageSedeconnecter.place(x=0 , y=420)


        #Titres
        titregestionlivres = Label(self.PageAjouterDesLivres, text=" Livres ",font =("algarian", 15,"bold"), bg="#ff7f00", fg="black")
        titregestionlivres.place(x=0, y=100,width=190)

        titreadherents = Label(self.PageAjouterDesLivres, text=" Adhérents ",font =("algarian", 15,"bold"), bg="#ff7f00", fg="black")
        titreadherents.place(x=0, y=240,width=190)

        titregestionprets = Label(self.PageAjouterDesLivres, text=" Prêts",font =("algarian", 15,"bold"), bg="#ff7f00", fg="black")
        titregestionprets.place(x=0, y=380,width=190)

        titresedeconnecter = Label(self.PageAjouterDesLivres, text=" Se déconnecter",font =("algarian", 15,"bold"), bg="#ff7f00", fg="black")
        titresedeconnecter.place(x=0, y=520,width=190) 

        titregestionlivretitre = Label(self.PageAjouterDesLivres, text=" Ajout de livres ",font =("algarian", 20,"bold"), bg="#bedb0d", fg="black")
        titregestionlivretitre.place(x=350, y=20,width=500)

        titre = Label(self.PageAjouterDesLivres, text=" titreLivre ",font =("algarian", 12,"bold"), bg="#bedb0d", fg="black")
        titre.place(x=300, y=150,width=100)

        auteur = Label(self.PageAjouterDesLivres, text=" idAuteur ",font =("algarian", 12,"bold"), bg="#bedb0d", fg="black")
        auteur.place(x=310, y=200,width=100)

        collections = Label(self.PageAjouterDesLivres, text=" idCollection ",font =("algarian", 12,"bold"), bg="#bedb0d", fg="black")
        collections.place(x=322, y=240,width=100)

        etat = Label(self.PageAjouterDesLivres, text=" Etat ",font =("algarian", 12,"bold"), bg="#bedb0d", fg="black")
        etat.place(x=300, y=280,width=100)

        
        #Bouton "Ajouter un livre"
        BoutonAjouterUnlivre = Button(self.PageAjouterDesLivres,command=self.ClickAjouterUnLivre, text="Ajouter un livre",cursor="hand2", font=("times new roman",11), bd=0,bg="white",fg="black")
        BoutonAjouterUnlivre.place(x=600, y=330)

        
        #Champs de saisie
        self.champsdesaisietitreLivre= Entry(self.PageAjouterDesLivres,textvariable=self.TitreLivre, font= (5), bg="white")
        self.champsdesaisietitreLivre.place(x=500, y=150,width=150)

        self.champsdesaisieauteurs= Entry(self.PageAjouterDesLivres, textvariable=self.Auteurs,font= (5), bg="white")
        self.champsdesaisieauteurs.place(x=500, y=200,width=150)

        self.champsdesaisiecollections= Entry(self.PageAjouterDesLivres,textvariable=self.Collections, font= (5), bg="white")
        self.champsdesaisiecollections.place(x=500, y=240,width=150)

        self.champsdesaisietat= Entry(self.PageAjouterDesLivres,textvariable=self.Etat, font= (5), bg="white")
        self.champsdesaisietat.place(x=500, y=280,width=150)


    #Fonction Supprimer les champs de saisie
    def SupprimerChampsDeSaisieAjouterDesLivres(self): #On déclare la fonction pour effacer les champs de saisie apres avoir saisie un livre
        self.champsdesaisietitreLivre.delete(0, END)
        self.champsdesaisieauteurs.delete(0, END)
        self.champsdesaisiecollections.delete(0, END)
        self.champsdesaisietat.delete(0, END)


    #Fonction ClickAjouterUnLivre pour inserer une livre dans la bse de données
    def ClickAjouterUnLivre(self):
        if self.TitreLivre.get()=="" or self.Auteurs.get()=="" or self.Collections.get()=="" or self.Etat.get()=="":
         messagebox.showerror("Erreur", "Veuillez remplir tout les champs", parent=self.PageAjouterDesLivres) #si tout les champs ne sont pas rempli alors affiche un message box pour dire que les champs ne sont pas rempli 
        else:
            try:
                    connectionbdd= pymysql.connect(host="localhost", user="root", password="", database="bddcomptes")
                    execut=connectionbdd.cursor()
                    execut.execute("select * from livre where titreLivre=%s",self.TitreLivre.get())
                    ligne= execut.fetchone()

                    if ligne != None:
                        messagebox.showerror("Erreur", "Ce livre existe deja", parent=self.PageAjouterDesLivres)
                    else:
                        execut.execute("insert into livre (titreLivre, idAuteur, idCollection,etatLivre) values (%s,%s,%s,%s)",
                        (
                            
                            self.TitreLivre.get(),
                            self.Auteurs.get(),
                            
                            self.Collections.get(),
                            self.Etat.get()
                            ))
                        messagebox.showinfo("Succes", "Le livre à bien était ajouté", parent=self.PageAjouterDesLivres) 
                        self.SupprimerChampsDeSaisieAjouterDesLivres 
                    connectionbdd.commit()
                    connectionbdd.close
                    
                
            except Exception as es :
                    messagebox.showerror("erreur",f"Erreur de connexion{str(es)}",parent=self.PageAjouterDesLivres)


        

    
    #Fonctions VersAdherents pour aller vers la page adhérent
    def VersAdherents(self):
        self.PageAjouterDesLivres.destroy() 
        call(["python", "Adherents.py"])

    #Fonctions VersGestiondesprets pour aller vers la page gestiondesprets
    def VersGestiondesprets(self):
        self.PageAjouterDesLivres.destroy()
        call(["python", "Gestiondesprets.py"])

    #Fonctions VersGestionLivres pour aller vers la page gestonLivres    
    def VersGestionlivres(self):
        self.PageAjouterDesLivres.destroy()
        call(["python", "Gestionlivres.py"])

    #Fonctions PourSedeconnecter 
    def PourSedeconnecter(self):
        lemessagebox = messagebox.askyesno("Déconnexion","Voulez-vous vous déconnecter", parent=self.PageAjouterDesLivres)
        if lemessagebox == YES:
         self.PageAjouterDesLivres.destroy()
         call(["python", "Connexion.py"])

    
    

root =Tk()
obj = AjoutLivres(root)
root.mainloop()