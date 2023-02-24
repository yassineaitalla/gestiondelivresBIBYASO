from ast import excepthandler
from cProfile import label
from email.mime import image
from logging import root            # pour importer la bibliotheque tkinter
from re import L
from tkinter import * 
from subprocess import call

 


from tkinter import ttk, messagebox
from turtle import bgcolor, title #permetre de gerer les selcetions et les message derrueeur  afficher ou de securite
  
import pymysql 
      
                    
class adherents:  #classe formulaire:
    def __init__(self,root):                   
        self.PageAdherents = root
        self.PageAdherents.title("Adherents")
        self.PageAdherents.geometry("1040x560+400+200")
        self.PageAdherents.resizable(width=False, height=False)
        self.PageAdherents.iconbitmap("Images/bib.ico") 
        
        self.idAdherent = StringVar()
        self.nom = StringVar()
        self.prenom = StringVar()
        self.codepostal= StringVar()
        self.ville = StringVar()
        self.recherche_par = StringVar()
        self.recherche = StringVar()


        self.Paneauvertdegestionlivres = Frame(self.PageAdherents, bg="#bedb0d")
        self.Paneauvertdegestionlivres.place(x=190, y=0, width=1100, height=1000)

        Paneauorangedegestionlivres = Frame(self.PageAdherents, bg="#ff7f00")
        Paneauorangedegestionlivres.place(x=0, y=0, width=190, height=1000)

        self.ImageGestionlivres = PhotoImage(file="Images/Gestionlivre.png")
        self.BoutonGestionLivres = Button(self.PageAdherents, command=self.VersGestionsLivres,text="",image=self.ImageGestionlivres, width=184,height=90, bg="#ff7f00",font="arial 12 bold")
        self.BoutonGestionLivres.place(x=0 , y=0) 
        
        self.ImageAdherents = PhotoImage(file="Images/Adherents.png")
        self.BoutonImageAdherent = Button(self.PageAdherents, text="",image=self.ImageAdherents, width=184, height=90, bg="#ff7f00",font="arial 12 bold")
        self.BoutonImageAdherent.place(x=0 , y=140) 

        self.ImageGestionDesPrets = PhotoImage(file="Images/Emprunter.png") 
        self.BoutonImageGestionDesPrets = Button(self.PageAdherents, command=self.VersGestionsdesPrets,text="",image=self.ImageGestionDesPrets, width=184, height=90, bg="#ff7f00",font="arial 12 bold")
        self.BoutonImageGestionDesPrets.place(x=0 , y=280) 

        self.ImageSedeconnecter = PhotoImage(file="Images/Sedeconnecter.png")
        self.BoutonImageSedeconnecter = Button(self.PageAdherents, text="",command=self.PourSeDeconnecter,image=self.ImageSedeconnecter, width=184, height=90, bg="#ff7f00",font="arial 12 bold")
        self.BoutonImageSedeconnecter.place(x=0 , y=420)

        # command  ------> Réecuperer la fontion qu'oncrée
         

        #Titres
        titreGestionAdherentsDeLaPageAdherents = Label(self.PageAdherents, text=" Gestion Adhérents ",font =("algarian", 20,"bold"), bg="#bedb0d", fg="black")
        titreGestionAdherentsDeLaPageAdherents.place(x=350, y=20,width=500)
        
        titreGestionlivres = Label(self.PageAdherents, text=" Livres ",font =("algarian", 15,"bold"), bg="#ff7f00", fg="black")
        titreGestionlivres.place(x=0, y=100,width=190)

        titreGestionAdherentsDeLaPageAdherents = Label(self.PageAdherents, text=" Adhérents ",font =("algarian", 15,"bold"), bg="#ff7f00", fg="black")
        titreGestionAdherentsDeLaPageAdherents.place(x=0, y=240,width=190)

        titreGestionDesPretsDeLaPageAdherents = Label(self.PageAdherents, text=" Prêts",font =("algarian", 15,"bold"), bg="#ff7f00", fg="black")
        titreGestionDesPretsDeLaPageAdherents.place(x=0, y=380,width=190)

        titreSedeconnecterDeLaPageAdherents = Label(self.PageAdherents, text=" Se déconnecter",font =("algarian", 15,"bold"), bg="#ff7f00", fg="black")
        titreSedeconnecterDeLaPageAdherents.place(x=0, y=520,width=190)

        titreRechercherlesadherentspar = Label(self.PageAdherents, text=" Rechercher les adhérents par :",font =("algarian", 12,"bold"), bg="#bedb0d", fg="black")
        titreRechercherlesadherentspar.place(x=210, y=90,width=250)

        #Boutons
        BoutonAjouterunAdherentDeLaPageAdherents = Button(self.PageAdherents, text="Ajouter un adhérent",command=self.AllerVersLaPagePourAjouterdesadherents,cursor="hand2", font=("times new roman",11), bd=0,bg="white",fg="black")
        BoutonAjouterunAdherentDeLaPageAdherents.place(x=215, y=500)

        BoutonSupprimerAdherentDeLaPageAdherents = Button(self.PageAdherents, command=self.SupprimerunAdherent,text="Supprimer un adhérent",cursor="hand2", font=("times new roman",11), bd=0,bg="white",fg="black")
        BoutonSupprimerAdherentDeLaPageAdherents.place(x=890, y=500)

        BoutonPourRechercherUnLivre = Button(self.PageAdherents,command=self.ClickBoutonRechercher, text=" Rechercher  ",cursor="hand2", font=("times new roman",11), bd=0,bg="white",fg="black")
        BoutonPourRechercherUnLivre.place(x=730, y=90) # command est attribuer a un bouton pour pouvoir l'executer

        BoutonActualiser = Button(self.PageAdherents,command=self.ClickBoutonActualiser, text="Actualiser ",cursor="hand2", font=("times new roman",11), bd=0,bg="white",fg="black")
        BoutonActualiser.place(x=830, y=90) # command est attribuer a un bouton pour pouvoir l'executer  

        #Champs de saisie
        self.ChampsDesaisiePourRechercherDesadherents= Entry(self.PageAdherents,textvariable=self.recherche ,font= (5), bg="white")
        self.ChampsDesaisiePourRechercherDesadherents.place(x=570, y=90,width=150)

        
        Listeadherent = ttk.Combobox(self.PageAdherents,textvariable=self.recherche_par, font=("times new roman", 15), state="readonly")
        Listeadherent["values"]=("idAdherent", "nomAdherent") # on recupere le soit l'idEmprunt ou soit le numAdheren
        Listeadherent.place(x=455, y=87, width=110) #.place pour la position du ttk.combobox 
        Listeadherent.current(0)



        #Cadre

        CadretableauGestionAdherents = Frame(self.PageAdherents, bd=5,relief=GROOVE,bg="white")
        CadretableauGestionAdherents.place(x=215, y=130,width=800, height=350)

        barededefilementX = Scrollbar(CadretableauGestionAdherents,orient=HORIZONTAL)
        barededefilemenyY = Scrollbar(CadretableauGestionAdherents, orient=VERTICAL)
        
        self.tableauGestionAdherents = ttk.Treeview(CadretableauGestionAdherents,columns=("idadherent","nomadherent", "prenomadherent", "codepostaladherent","villeadherent"),xscrollcommand=barededefilementX.set, yscrollcommand=barededefilemenyY.set)
        barededefilementX.pack(side=BOTTOM, fill=X)
        barededefilemenyY.pack(side=RIGHT, fill=Y) 
        self.tableauGestionAdherents.selection
        
        self.tableauGestionAdherents.heading("idadherent", text="idAdherent")
        self.tableauGestionAdherents.heading("nomadherent", text="nomAdherent")
        self.tableauGestionAdherents.heading("prenomadherent", text="prenomAdherent")
        
        self.tableauGestionAdherents.heading("codepostaladherent", text="codepostalAdherent")
        self.tableauGestionAdherents.heading("villeadherent", text="villeAdherent")

        self.tableauGestionAdherents["show"]="headings"

        self.tableauGestionAdherents.column("idadherent",width=80)
        self.tableauGestionAdherents.column("nomadherent",width=80)
        self.tableauGestionAdherents.column("prenomadherent",width=80)
        self.tableauGestionAdherents.column("codepostaladherent",width=80)
        self.tableauGestionAdherents.column("villeadherent", width=80)

        self.tableauGestionAdherents.pack(side=TOP, fill=X,)
        self.tableauGestionAdherents.pack(fill=BOTH, expand=1)
        
        
        self.tableauGestionAdherents.bind("<ButtonRelease-1>",self.information) # le self information est important si on souhaite faire la meme vhose ailleurs
        self.ClickBoutonActualiser()
    
    def AllerVersLaPagePourAjouterdesadherents(self):
        self.PageAdherents.destroy()
        call(["python", "ajouterdesadherents.py"]) 
    
    
    def ClickBoutonRechercher(self):
        connectionbdd= pymysql.connect(host="localhost", user="root", password="", database="bddcomptes") # connexion a la base de donnes
        execut=connectionbdd.cursor()        
        execut.execute("select * from adherent  where "+str(self.recherche_par.get())+" LIKE '%"+str(self.recherche.get())+"%'")
        ligne = execut.fetchall()
        if len(ligne)!=0:
           self.tableauGestionAdherents.delete(*self.tableauGestionAdherents.get_children())
           for row in ligne:
            self.tableauGestionAdherents.insert('', END, values=row)
        connectionbdd.commit()
        connectionbdd.close()

        

    def VersGestionsLivres(self):
        self.PageAdherents.destroy()
        call(["python", "Gestionlivres.py"]) 

    
    def VersGestionsdesPrets(self):
        self.PageAdherents.destroy()
        call(["python", "GestionDesprets.py"]) 

    
    def PourSeDeconnecter(self):
        
        lemessagebox = messagebox.askyesno("Déconnexion","Voulez-vous vous déconnecter", parent=self.PageAdherents)
        if lemessagebox == YES:
         self.PageAdherents.destroy()                           
         call(["python", "Connexion.py"])
        
        
      

    def information(self,ev):
        cursor_row = self.tableauGestionAdherents.focus()
        contents = self.tableauGestionAdherents.item(cursor_row)
        row = contents["values"]
        
        self.idAdherent.set(row[0]),
        self.nom.set(row[1]),
        self.prenom.set(row[2]),
        self.codepostal.set(row[3]),
        self.ville.set(row[4]),
    
    def ClickBoutonActualiser(self):
        connectionbdd =  pymysql.connect(host="localhost", user="root", password="", database="bddcomptes")
        execut=connectionbdd.cursor() #Cursor permet d'éxecuter une operation SQL   
        execut.execute("select * from adherent") #requette sql pour récuperer les adherents
        
        ligne= execut.fetchall() #fetchall récupère toutes les lignes d'un résultat de requête
        if len(ligne)!=0:
            self.tableauGestionAdherents.delete(*self.tableauGestionAdherents.get_children())
            for ligne in ligne:
                self.tableauGestionAdherents.insert("", END, values=ligne)
                
        connectionbdd.commit() #valide la transaction
        connectionbdd.close() #ferme la connexion a la bdd



        
    def SupprimerunAdherent(self):

        if self.idAdherent.get()=="":
         messagebox.showerror("Erreur", "Veuillez, sélectionner un adhérent", parent=self.PageAdherents) #si tout les champs ne sont pas rempli alors affiche un message box pour dire que les champs ne sont pas rempli 
                
        else:
            connectionbdd= pymysql.connect(host="localhost", user="root", password="", database="bddcomptes")
            execut=connectionbdd.cursor()
            execut.execute("delete from adherent where idAdherent = %s", self.idAdherent.get())
           
            
            connectionbdd.commit()
            messagebox.showinfo("Succés", "L'adhérent à bien était supprimer ", parent=self.PageAdherents)
            self.ClickBoutonActualiser()
                    
            connectionbdd.close()

          

root =Tk()
obj = adherents(root)
root.mainloop() #root est la fenetre racine