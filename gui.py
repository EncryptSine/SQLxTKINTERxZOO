import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from fonction import peupler_tables, afficher, supprimer_bis, remplacer

class AnimalApp:
    def __init__(self, root):
        """Innitialise l'application avec une fonction principale et établit une connexion à la base de données
        
        entrée principale: root
        sortie: none
        """
        self.root = root
        self.root.title("Mini PRojet") #On attribue à l'objet un titre

        self.conn = sqlite3.connect("animal_db") #on va connecté self.conn avec la base de données qu'on va modifier
        self.cur = self.conn.cursor()

        # Création des widgets: création contrôle d'onglet pour les différentes fonctionalités de l'application
        self.tab_control = ttk.Notebook(root)
        self.tab_peupler = ttk.Frame(self.tab_control)
        self.tab_afficher = ttk.Frame(self.tab_control)
        self.tab_modifier = ttk.Frame(self.tab_control)
        self.tab_supprimer = ttk.Frame(self.tab_control)

        #Ajoute les onglets au contrôle d'onglets
        self.tab_control.add(self.tab_peupler, text='Peupler')
        self.tab_control.add(self.tab_afficher, text='Afficher')
        self.tab_control.add(self.tab_modifier, text='Modifier')
        self.tab_control.add(self.tab_supprimer, text='Supprimer')
        self.tab_control.pack(expand=1, fill="both")

        #crée les widgets pour chaque onglet
        self.create_peupler_tab()
        self.create_afficher_tab()
        self.create_modifier_tab()
        self.create_supprimer_tab()

    def create_peupler_tab(self):
        """
        Crée l'onglet Peupler avec un menu déroulant pour sélectionner la table à peupler,
        un cadre pour afficher les champs correspondants et un bouton pour peupler la table.
        """
        # Crée un label et un menu déroulant pour sélectionner la table à peupler
        self.label_table_peupler = tk.Label(self.tab_peupler, text="Table:")
        self.label_table_peupler.grid(row=0, column=0, padx=5, pady=5)
        self.table_var = tk.StringVar()
        self.table_var.set("Sélectionner une table")
        self.table_dropdown = ttk.Combobox(self.tab_peupler, textvariable=self.table_var, values=[
                                        "animal", "enclos", "espece", "soin_animaux"])
        self.table_dropdown.grid(row=0, column=1, padx=5, pady=5)
        self.table_dropdown.bind("<<ComboboxSelected>>", self.show_fields)

        # Crée un cadre pour afficher les champs
        self.fields_frame = tk.Frame(self.tab_peupler)
        self.fields_frame.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        # Dictionnaire pour stocker les labels des champs
        self.label_fields = {}

        # Crée un bouton pour peupler la table
        self.btn_peupler = tk.Button(
            self.tab_peupler, text="Peupler", command=self.peupler_animal)
        self.btn_peupler.grid(row=3, column=0, columnspan=2, padx=5, pady=5)


    def show_fields(self, event):
        """
        Affiche les champs de modification en fonction de la table sélectionnée.

        Args:
            event: Événement déclenché par le changement de sélection dans la liste déroulante.
        """
        
        # Récupère la table sélectionnée
        table = self.table_var.get()
        
        # Détruit le cadre des champs de modification précédemment affiché
        self.fields_frame.destroy()
        self.fields_frame = tk.Frame(self.tab_peupler)
        self.fields_frame.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        # Affiche les champs de modification spécifiques à la table sélectionnée
        if table == "animal":
            self.label_id_animal = tk.Label(
                self.fields_frame, text="ID animal:")
            self.label_id_animal.grid(row=0, column=0, padx=5, pady=5)
            self.entry_id_animal = tk.Entry(self.fields_frame)
            self.entry_id_animal.grid(row=0, column=1, padx=5, pady=5)

            self.label_nom = tk.Label(self.fields_frame, text="Nom:")
            self.label_nom.grid(row=1, column=0, padx=5, pady=5)
            self.entry_nom = tk.Entry(self.fields_frame)
            self.entry_nom.grid(row=1, column=1, padx=5, pady=5)

            self.label_age = tk.Label(self.fields_frame, text="Age:")
            self.label_age.grid(row=2, column=0, padx=5, pady=5)
            self.entry_age = tk.Entry(self.fields_frame)
            self.entry_age.grid(row=2, column=1, padx=5, pady=5)

            self.label_taille = tk.Label(self.fields_frame, text="Taille:")
            self.label_taille.grid(row=3, column=0, padx=5, pady=5)
            self.entry_taille = tk.Entry(self.fields_frame)
            self.entry_taille.grid(row=3, column=1, padx=5, pady=5)

            self.label_masse = tk.Label(self.fields_frame, text="Masse:")
            self.label_masse.grid(row=4, column=0, padx=5, pady=5)
            self.entry_masse = tk.Entry(self.fields_frame)
            self.entry_masse.grid(row=4, column=1, padx=5, pady=5)

            self.label_nom_espece = tk.Label(
                self.fields_frame, text="Nom espèce:")
            self.label_nom_espece.grid(row=5, column=0, padx=5, pady=5)
            self.entry_nom_espece = tk.Entry(self.fields_frame)
            self.entry_nom_espece.grid(row=5, column=1, padx=5, pady=5)
            
            self.label_id_espece = tk.Label(
                self.fields_frame, text="ID espèce:")
            self.label_id_espece.grid(row=6, column=0, padx=5, pady=5)
            self.entry_id_espece = tk.Entry(self.fields_frame)
            self.entry_id_espece.grid(row=6, column=1, padx=5, pady=5)

        elif table == "enclos":
            self.label_id_enclos = tk.Label(
                self.fields_frame, text="ID enclos:")
            self.label_id_enclos.grid(row=0, column=0, padx=5, pady=5)
            self.entry_id_enclos = tk.Entry(self.fields_frame)
            self.entry_id_enclos.grid(row=0, column=1, padx=5, pady=5)

            self.label_numero_enclos = tk.Label(
                self.fields_frame, text="Numéro enclos:")
            self.label_numero_enclos.grid(row=1, column=0, padx=5, pady=5)
            self.entry_numero_enclos = tk.Entry(self.fields_frame)
            self.entry_numero_enclos.grid(row=1, column=1, padx=5, pady=5)

            self.label_ecosysteme = tk.Label(
                self.fields_frame, text="Ecosystème:")
            self.label_ecosysteme.grid(row=2, column=0, padx=5, pady=5)
            self.entry_ecosysteme = tk.Entry(self.fields_frame)
            self.entry_ecosysteme.grid(row=2, column=1, padx=5, pady=5)

            self.label_surface = tk.Label(self.fields_frame, text="Surface:")
            self.label_surface.grid(row=3, column=0, padx=5, pady=5)
            self.entry_surface = tk.Entry(self.fields_frame)
            self.entry_surface.grid(row=3, column=1, padx=5, pady=5)

            self.label_struct = tk.Label(self.fields_frame, text="Structure:")
            self.label_struct.grid(row=4, column=0, padx=5, pady=5)
            self.entry_struct = tk.Entry(self.fields_frame)
            self.entry_struct.grid(row=4, column=1, padx=5, pady=5)

            self.label_date_entretien = tk.Label(
                self.fields_frame, text="Date entretien:")
            self.label_date_entretien.grid(row=5, column=0, padx=5, pady=5)
            self.entry_date_entretien = tk.Entry(self.fields_frame)
            self.entry_date_entretien.grid(row=5, column=1, padx=5, pady=5)

        elif table == "espece":
            self.label_id_espece = tk.Label(
                self.fields_frame, text="ID espèce:")
            self.label_id_espece.grid(row=0, column=0, padx=5, pady=5)
            self.entry_id_espece = tk.Entry(self.fields_frame)
            self.entry_id_espece.grid(row=0, column=1, padx=5, pady=5)

            self.label_nom_espece = tk.Label(
                self.fields_frame, text="Nom espèce:")
            self.label_nom_espece.grid(row=1, column=0, padx=5, pady=5)
            self.entry_nom_espece = tk.Entry(self.fields_frame)
            self.entry_nom_espece.grid(row=1, column=1, padx=5, pady=5)

            self.label_classe = tk.Label(self.fields_frame, text="Classe:")
            self.label_classe.grid(row=2, column=0, padx=5, pady=5)
            self.entry_classe = tk.Entry(self.fields_frame)
            self.entry_classe.grid(row=2, column=1, padx=5, pady=5)

            self.label_alimentation = tk.Label(
                self.fields_frame, text="Alimentation:")
            self.label_alimentation.grid(row=3, column=0, padx=5, pady=5)
            self.entry_alimentation = tk.Entry(self.fields_frame)
            self.entry_alimentation.grid(row=3, column=1, padx=5, pady=5)

        elif table == "soin_animaux":

            self.label_id_animal_soin = tk.Label(
                self.fields_frame, text="ID animal:")
            self.label_id_animal_soin.grid(row=0, column=0, padx=5, pady=5)
            self.entry_id_animal_soin = tk.Entry(self.fields_frame)
            self.entry_id_animal_soin.grid(row=0, column=1, padx=5, pady=5)

            self.label_prise_temp = tk.Label(
                self.fields_frame, text="Prise température:")
            self.label_prise_temp.grid(row=1, column=0, padx=5, pady=5)
            self.entry_prise_temp = tk.Entry(self.fields_frame)
            self.entry_prise_temp.grid(row=1, column=1, padx=5, pady=5)

            self.label_type_vaccin = tk.Label(
                self.fields_frame, text="Type vaccin:")
            self.label_type_vaccin.grid(row=2, column=0, padx=5, pady=5)
            self.entry_type_vaccin = tk.Entry(self.fields_frame)
            self.entry_type_vaccin.grid(row=2, column=1, padx=5, pady=5)

            self.label_date_vaccin = tk.Label(
                self.fields_frame, text="Date vaccin:")
            self.label_date_vaccin.grid(row=3, column=0, padx=5, pady=5)
            self.entry_date_vaccin = tk.Entry(self.fields_frame)
            self.entry_date_vaccin.grid(row=3, column=1, padx=5, pady=5)

            self.label_nature_dernier_soins = tk.Label(
                self.fields_frame, text="Nature dernier soins:")
            self.label_nature_dernier_soins.grid(
                row=4, column=0, padx=5, pady=5)
            self.entry_nature_dernier_soins = tk.Entry(self.fields_frame)
            self.entry_nature_dernier_soins.grid(
                row=4, column=1, padx=5, pady=5)

            self.label_nature_soin_en_cours = tk.Label(
                self.fields_frame, text="Nature soin en cours:")
            self.label_nature_soin_en_cours.grid(
                row=5, column=0, padx=5, pady=5)
            self.entry_nature_soin_en_cours = tk.Entry(self.fields_frame)
            self.entry_nature_soin_en_cours.grid(
                row=5, column=1, padx=5, pady=5)

    def create_afficher_tab(self):
        """
        Crée l'onglet Afficher avec une entrée pour spécifier la table à afficher, un bouton pour afficher les données de la table
        et un widget Text pour afficher les données.
        """
        # Crée un label et une entrée pour spécifier la table à afficher
        self.label_table = tk.Label(self.tab_afficher, text="Table:")
        self.label_table.grid(row=0, column=0, padx=5, pady=5)
        self.entry_table = tk.Entry(self.tab_afficher)
        self.entry_table.grid(row=0, column=1, padx=5, pady=5)

        # Crée un bouton pour afficher les données de la table
        self.btn_afficher = tk.Button(
            self.tab_afficher, text="Afficher", command=self.afficher_table)
        self.btn_afficher.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        # Crée un widget Text pour afficher les données
        self.text_afficher = tk.Text(self.tab_afficher, height=10, width=50)
        self.text_afficher.grid(row=2, column=0, columnspan=2, padx=5, pady=5)


    def create_modifier_tab(self):
        """
        Crée l'onglet Modifier avec un menu déroulant pour sélectionner la table à modifier,
        un cadre pour afficher les champs de modification et un bouton pour déclencher la modification.
        """
        # Crée un label et un menu déroulant pour sélectionner la table à modifier
        self.label_table_modif = tk.Label(self.tab_modifier, text="Table:")
        self.label_table_modif.grid(row=0, column=0, padx=5, pady=5)
        self.table_var_modif = tk.StringVar()
        self.table_var_modif.set("Sélectionner une table")
        self.table_dropdown_modif = ttk.Combobox(self.tab_modifier, textvariable=self.table_var_modif, values=["animal", "enclos", "espece", "soin_animaux"])
        self.table_dropdown_modif.grid(row=0, column=1, padx=5, pady=5)
        self.table_dropdown_modif.bind("<<ComboboxSelected>>", self.show_modif_fields)

        # Crée un cadre pour afficher les champs à modifier
        self.modif_fields_frame = tk.Frame(self.tab_modifier)
        self.modif_fields_frame.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        # Crée un bouton pour déclencher la modification
        self.btn_modifier = tk.Button(self.tab_modifier, text="Modifier", command=self.modifier_table)
        self.btn_modifier.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    def show_modif_fields(self, event):
        """
        Affiche les champs de modification en fonction de la table sélectionnée.

        Args:
            event: Événement déclenché par le changement de sélection dans la liste déroulante.
        """
        # Récupère la table sélectionnée
        table = self.table_var_modif.get()
        
        # Détruit le cadre des champs de modification précédemment affiché
        self.modif_fields_frame.destroy()
        self.modif_fields_frame = tk.Frame(self.tab_modifier)
        self.modif_fields_frame.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        # Affiche les champs de modification spécifiques à la table sélectionnée
        if table == "animal":
            self.label_id_animal_modif = tk.Label(
                self.modif_fields_frame, text="ID animal:")
            self.label_id_animal_modif.grid(row=0, column=0, padx=5, pady=5)
            self.entry_id_animal_modif = tk.Entry(self.modif_fields_frame)
            self.entry_id_animal_modif.grid(row=0, column=1, padx=5, pady=5)
            
            self.label_nom_modif = tk.Label(
                self.modif_fields_frame, text="Nom:")
            self.label_nom_modif.grid(row=1, column=0, padx=5, pady=5)
            self.entry_nom_modif = tk.Entry(self.modif_fields_frame)
            self.entry_nom_modif.grid(row=1, column=1, padx=5, pady=5)
            
            self.label_age_modif = tk.Label(
                self.modif_fields_frame, text="Age:")
            self.label_age_modif.grid(row=2, column=0, padx=5, pady=5)
            self.entry_age_modif = tk.Entry(self.modif_fields_frame)
            self.entry_age_modif.grid(row=2, column=1, padx=5, pady=5)
            
            self.label_taille_modif = tk.Label(
                self.modif_fields_frame, text="Taille:")
            self.label_taille_modif.grid(row=3, column=0, padx=5, pady=5)
            self.entry_taille_modif = tk.Entry(self.modif_fields_frame)
            self.entry_taille_modif.grid(row=3, column=1, padx=5, pady=5)
            
            self.label_masse_modif = tk.Label(
                self.modif_fields_frame, text="Masse:")
            self.label_masse_modif.grid(row=4, column=0, padx=5, pady=5)
            self.entry_masse_modif = tk.Entry(self.modif_fields_frame)
            self.entry_masse_modif.grid(row=4, column=1, padx=5, pady=5)
            
            self.label_nom_espece_modif = tk.Label(
                self.modif_fields_frame, text="Nom espèce:")
            self.label_nom_espece_modif.grid(row=5, column=0, padx=5, pady=5)
            self.entry_nom_espece_modif = tk.Entry(self.modif_fields_frame)
            self.entry_nom_espece_modif.grid(row=5, column=1, padx=5, pady=5)
            
            self.label_id_espece_modif = tk.Label(
                self.modif_fields_frame, text="ID espèce:")
            self.label_id_espece_modif.grid(row=6, column=0, padx=5, pady=5)
            self.entry_id_espece_modif = tk.Entry(self.modif_fields_frame)
            self.entry_id_espece_modif.grid(row=6, column=1, padx=5, pady=5)

        elif table == "enclos":
            self.label_id_enclos_modif = tk.Label(
                self.modif_fields_frame, text="ID enclos:")
            self.label_id_enclos_modif.grid(row=0, column=0, padx=5, pady=5)
            self.entry_id_enclos_modif = tk.Entry(self.modif_fields_frame)
            self.entry_id_enclos_modif.grid(row=0, column=1, padx=5, pady=5)

            self.label_num_enclos_modif = tk.Label(
                self.modif_fields_frame, text="Numéro enclos:")
            self.label_num_enclos_modif.grid(row=1, column=0, padx=5, pady=5)
            self.entry_num_enclos_modif = tk.Entry(self.modif_fields_frame)
            self.entry_num_enclos_modif.grid(row=1, column=1, padx=5, pady=5)
            
            self.label_ecosysteme_modif = tk.Label(
                self.modif_fields_frame, text="Ecosystème:")
            self.label_ecosysteme_modif.grid(row=2, column=0, padx=5, pady=5)
            self.entry_ecosysteme_modif = tk.Entry(self.modif_fields_frame)
            self.entry_ecosysteme_modif.grid(row=2, column=1, padx=5, pady=5)
            
            self.label_surface_modif = tk.Label(
                self.modif_fields_frame, text="Surface:")
            self.label_surface_modif.grid(row=3, column=0, padx=5, pady=5)
            self.entry_surface_modif = tk.Entry(self.modif_fields_frame)
            self.entry_surface_modif.grid(row=3, column=1, padx=5, pady=5)
            
            self.label_struct_modif = tk.Label(
                self.modif_fields_frame, text="Structure:")
            self.label_struct_modif.grid(row=4, column=0, padx=5, pady=5)
            self.entry_struct_modif = tk.Entry(self.modif_fields_frame)
            self.entry_struct_modif.grid(row=4, column=1, padx=5, pady=5)
            
            self.label_date_entretien_modif = tk.Label(
                self.modif_fields_frame, text="Date entretien:")
            self.label_date_entretien_modif.grid(row=5, column=0, padx=5, pady=5)
            self.entry_date_entretien_modif = tk.Entry(self.modif_fields_frame)
            self.entry_date_entretien_modif.grid(row=5, column=1, padx=5, pady=5)

        elif table == "espece":
            self.label_id_espece_modif = tk.Label(
                self.modif_fields_frame, text="ID espèce:")
            self.label_id_espece_modif.grid(row=0, column=0, padx=5, pady=5)
            self.entry_id_espece_modif = tk.Entry(self.modif_fields_frame)
            self.entry_id_espece_modif.grid(row=0, column=1, padx=5, pady=5)

            self.label_nom_espece_modif = tk.Label(
                self.modif_fields_frame, text="Nom espèce:")
            self.label_nom_espece_modif.grid(row=1, column=0, padx=5, pady=5)
            self.entry_nom_espece_modif = tk.Entry(self.modif_fields_frame)
            self.entry_nom_espece_modif.grid(row=1, column=1, padx=5, pady=5)
            
            self.label_classe_modif = tk.Label(
                self.modif_fields_frame, text="Classe:")
            self.label_classe_modif.grid(row=2, column=0, padx=5, pady=5)
            self.entry_classe_modif = tk.Entry(self.modif_fields_frame)
            self.entry_classe_modif.grid(row=2, column=1, padx=5, pady=5)
            
            self.label_alimentation_modif = tk.Label(
                self.modif_fields_frame, text="Alimentation:")
            self.label_alimentation_modif.grid(row=3, column=0, padx=5, pady=5)
            self.entry_alimentation_modif = tk.Entry(self.modif_fields_frame)
            self.entry_alimentation_modif.grid(row=3, column=1, padx=5, pady=5)

        elif table == "soin_animaux":
            self.label_id_animal_modif = tk.Label(
                self.modif_fields_frame, text="ID animal:")
            self.label_id_animal_modif.grid(row=0, column=0, padx=5, pady=5)
            self.entry_id_animal_modif = tk.Entry(self.modif_fields_frame)
            self.entry_id_animal_modif.grid(row=0, column=1, padx=5, pady=5)
            
            self.label_prise_temp_modif = tk.Label(
                self.modif_fields_frame, text="Prise température:")
            self.label_prise_temp_modif.grid(row=1, column=0, padx=5, pady=5)
            self.entry_prise_temp_modif = tk.Entry(self.modif_fields_frame)
            self.entry_prise_temp_modif.grid(row=1, column=1, padx=5, pady=5)
            
            self.label_type_vaccin_modif = tk.Label(
                self.modif_fields_frame, text="Type vaccin:")
            self.label_type_vaccin_modif.grid(row=2, column=0, padx=5, pady=5)
            self.entry_type_vaccin_modif = tk.Entry(self.modif_fields_frame)
            self.entry_type_vaccin_modif.grid(row=2, column=1, padx=5, pady=5)
            
            self.label_date_vaccin_modif = tk.Label(
                self.modif_fields_frame, text="Date vaccin:")
            self.label_date_vaccin_modif.grid(row=3, column=0, padx=5, pady=5)
            self.entry_date_vaccin_modif = tk.Entry(self.modif_fields_frame)
            self.entry_date_vaccin_modif.grid(row=3, column=1, padx=5, pady=5)
            
            self.label_nature_dernier_soins_modif = tk.Label(
                self.modif_fields_frame, text="Nature dernier soins:")
            self.label_nature_dernier_soins_modif.grid(row=4, column=0, padx=5, pady=5)
            self.entry_nature_dernier_soins_modif = tk.Entry(self.modif_fields_frame)
            self.entry_nature_dernier_soins_modif.grid(row=4, column=1, padx=5, pady=5)
            
            self.label_nature_soin_en_cours_modif = tk.Label(
                self.modif_fields_frame, text="Nature soin en cours:")
            self.label_nature_soin_en_cours_modif.grid(row=5, column=0, padx=5, pady=5)
            self.entry_nature_soin_en_cours_modif = tk.Entry(self.modif_fields_frame)
            self.entry_nature_soin_en_cours_modif.grid(row=5, column=1, padx=5, pady=5)
            
    def create_supprimer_tab(self):
        """
        Crée l'onglet Supprimer avec des widgets pour spécifier la table et l'ID à supprimer.
        """
        # Crée un label et une entrée pour spécifier la table
        self.label_table_supp = tk.Label(self.tab_supprimer, text="Table:")
        self.label_table_supp.grid(row=0, column=0, padx=5, pady=5)
        self.entry_table_supp = tk.Entry(self.tab_supprimer)
        self.entry_table_supp.grid(row=0, column=1, padx=5, pady=5)

        # Crée un label et une entrée pour spécifier l'ID à supprimer
        self.label_id_supp = tk.Label(self.tab_supprimer, text="ID à supprimer:")
        self.label_id_supp.grid(row=1, column=0, padx=5, pady=5)
        self.entry_id_supp = tk.Entry(self.tab_supprimer)
        self.entry_id_supp.grid(row=1, column=1, padx=5, pady=5)

        # Crée un bouton pour déclencher la suppression
        self.btn_supprimer = tk.Button(
            self.tab_supprimer, text="Supprimer", command=self.supprimer_table)
        self.btn_supprimer.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    def peupler_animal(self):
        """
        La fonction permet de peupler les tables selon les informations données par l'utilisateur

        entrée: self (l'animal: l'objet)
        sortie: on ajoute enregistrement dans la table si l'id n'avait pas été pris, on retourne un message nous disant que l'enregistrement a été effectué.

        """
        table = self.table_var.get() #On obtient la table donnée
        
        #Selon la table donnée, si elle fait partie des propositions données, on récupère les attributs qu'on va placer dans la table. A la fin on obtient un message nous disant que l'enregistrement a bien été effectué
        if table == "animal":
            id_animal = self.entry_id_animal.get()
            nom = self.entry_nom.get()
            age = self.entry_age.get()
            taille = self.entry_taille.get()
            masse = self.entry_masse.get()
            nom_espece = self.entry_nom_espece.get()
            id_espece = self.entry_id_espece.get()

            peupler_tables(table, id_animal, nom, age, taille,
                           masse, nom_espece, id_espece)
        elif table == "enclos":
            id_enclos = self.entry_id_enclos.get()
            numero_enclos = self.entry_numero_enclos.get()
            ecosysteme = self.entry_ecosysteme.get()
            surface = self.entry_surface.get()
            struct = self.entry_struct.get()
            date_entretien = self.entry_date_entretien.get()

            peupler_tables(table, id_enclos, numero_enclos,
                           ecosysteme, surface, struct, date_entretien)
        elif table == "espece":
            id_espece = self.entry_id_espece.get()
            nom_espece = self.entry_nom_espece.get()
            classe = self.entry_classe.get()
            alimentation = self.entry_alimentation.get()

            peupler_tables(table, id_espece, nom_espece, classe, alimentation)
        elif table == "soin_animaux":
            id_animal = self.entry_id_animal_soin.get()
            prise_temp = self.entry_prise_temp.get()
            type_vaccin = self.entry_type_vaccin.get()
            date_vaccin = self.entry_date_vaccin.get()
            nature_dernier_soins = self.entry_nature_dernier_soins.get()
            nature_soin_en_cours = self.entry_nature_soin_en_cours.get()

            peupler_tables(table, id_animal, prise_temp, type_vaccin,
                           date_vaccin, nature_dernier_soins, nature_soin_en_cours)

        messagebox.showinfo("Succès", "Informations ajoutées avec succès")

    def afficher_table(self):
        """
        Fonction permettant d'afficher les tables voulues

        entrée: self: objet
        sortie: on affiche la table demandé grâce à la fonction afficher()
        """
        table = self.entry_table.get() #On obtient la table donnée par l'utilisateur

        results = afficher(table) #On affiche la table grâce à la fonction afficher()
        if results: #Présentation tkinter, comment on va présenter les tables
            self.text_afficher.delete('1.0', tk.END)
            for row in results:
                self.text_afficher.insert(tk.END, row)
                self.text_afficher.insert(tk.END, '\n')
        else:
            messagebox.showinfo("ALerte", "table vide") #Si la table est vide, on reçoit un message disant que celle-ci est vide

    def modifier_table(self):
        """Fonction permettant de modifier des enregistrement en fonction d'un id
            self: l'objet

            sortie: l'enregistrement est modifier en donnant son id grâce à la fonction remplacer
        """
        table = self.table_var_modif.get() #on obtient la table donné
        id_modif = self.entry_id_supp.get() #on obtient l'id dont l'enregistrement va être modifier
        
        # si la table est l'une des tables proposées, on recupère les attributs qu'on donne pour remplacer les données de l'enregistrement. A la fin on retourne que l'enregistrement a bien été modifié
        if table == "animal": 
            id_animal = self.entry_id_animal_modif.get()
            nom = self.entry_nom_modif.get()
            age = self.entry_age_modif.get()
            taile = self.entry_taille_modif.get()
            masse = self.entry_masse_modif.get()
            nom_espece = self.entry_nom_espece_modif.get()
            id_espece = self.entry_id_espece_modif.get()

            remplacer(table, id_animal, Id_animal=id_animal, nom=nom, age=age, taille=taile, masse=masse, nom_espece=nom_espece, Id_espece=id_espece)
            messagebox.showinfo("Succes", f"Données de l'enregistrement avec l'ID {id_modif} dans la table {table} mises à jour")

        elif table == "enclos":
            id_enclos = self.entry_id_enclos_modif.get()
            num_enclos = self.entry_num_enclos_modif.get()
            ecosysteme = self.entry_ecosysteme_modif.get()
            surface = self.entry_surface_modif.get()
            struct = self.entry_struct_modif.get()
            date_entretien = self.entry_date_entretien_modif.get()

            remplacer(table, id_enclos ,Id_enclos=id_enclos, num_enclos=num_enclos,
                    ecosysteme=ecosysteme, surface=surface, struct=struct, date_entretien=date_entretien)
            messagebox.showinfo(
                "Succes", f"Données de l'enregistrement avec l'ID {id_modif} dans la table {table} mises à jour")

        elif table == "espece":
            id_espece = self.entry_id_espece_modif.get()
            nom_espece = self.entry_nom_espece_modif.get()
            classe = self.entry_classe_modif.get()
            alimentation = self.entry_alimentation_modif.get()

            remplacer(table, id_espece, Id_espece=id_espece,
                    nom_espece=nom_espece, classe=classe, alimentation=alimentation)
            messagebox.showinfo(
                "Succes", f"Données de l'enregistrement avec l'ID {id_modif} dans la table {table} mises à jour")

        elif table == "soin_animaux":
            id_animal = self.entry_id_animal_modif.get()
            prise_temp = self.entry_prise_temp_modif.get()
            type_vaccin = self.entry_type_vaccin_modif.get()
            date_vaccin = self.entry_date_vaccin_modif.get()
            nature_dernier_soins = self.entry_nature_dernier_soins_modif.get()
            nature_soin_en_cours = self.entry_nature_soin_en_cours_modif.get()

            remplacer(table, id_animal, Id_animal=id_animal, prise_temp=prise_temp, type_vaccin=type_vaccin,
                    date_vaccin=date_vaccin, nature_dernier_soins=nature_dernier_soins, nature_soin_en_cours=nature_soin_en_cours)
            messagebox.showinfo(
                "Succes", f"Données de l'enregistrement avec l'ID {id_modif} dans la table {table} mises à jour")
    
    def supprimer_table(self):  
        """Fonction permettant de supprimer des enregistrement en fonction d'un id
            self: l'objet

            sortie: l'enregistrement est supprimé grâce à la fonction supprimer_bis, on affiche un message disant que l'enregistrement a bien été supprimé
        """
        table = self.entry_table_supp.get() #on obtient la table donnée, et l'id de l'enregistrement a supprimé
        id_supp = self.entry_id_supp.get()

        supprimer_bis(id_supp, table) #Pour supprimer l'élément, on utilise la fonction supprimer_bis
        messagebox.showinfo(
            "Succes", f"L'enregistrement avec l'ID {id_supp} dans la table {table} a été supprimé") #On affiche un message qui nous dit que l'enregistrement a bien été supprimé


if __name__ == "__main__":
    #On lance le tkinter
    root = tk.Tk() 
    app = AnimalApp(root)
    root.mainloop() 
