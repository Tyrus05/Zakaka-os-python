import tkinter as tk

DOSSIER_CIBLE = "/Users/ton nom d'utilisateur/Desktop/ZAKAKA OS"


def ajouter_prefixe(event=None):
    # Récupère la ligne avant le prompt
    contenu = champ_texte.get("end-2l linestart", "end-1c").strip()

    # On enlève le prompt pour récupérer la commande seule
    if contenu.startswith("zakaka>"):
        commande = contenu[len("zakaka>"):].strip()
    else:
        commande = contenu

    if commande == "ls":
        fichiers = os.listdir(DOSSIER_CIBLE)
        for fichier in fichiers:
            champ_texte.insert(tk.END, f"\n{fichier}")

    elif commande.startswith('az="') and commande.endswith('"'):
        # Récupère le nom de fichier entre les guillemets
        nom_fichier = commande[4:-1]

        # Crée le dossier s'il n'existe pas
        os.makedirs(DOSSIER_CIBLE, exist_ok=True)

        chemin_fichier = os.path.join(DOSSIER_CIBLE, nom_fichier)

        try:
            # Crée un fichier vide
            with open(chemin_fichier, "w") as f:
                pass
            champ_texte.insert(tk.END, f'\nFichier "{nom_fichier}" créé avec succès.')
        except Exception as e:
            champ_texte.insert(tk.END, f"\nErreur lors de la création du fichier : {e}")

    else:
        champ_texte.insert(tk.END, "\nCommande inconnue")

    # Nouveau prompt
    champ_texte.insert(tk.END, "\nzakaka>")

    return "break"

fenetre = tk.Tk()
fenetre.title("Zakaka 2.0")
fenetre.geometry("600x400")
fenetre.configure(bg="black")

champ_texte = tk.Text(
    fenetre,
    bg="black",
    fg="green",
    insertbackground="green",  # curseur vert
    borderwidth=0,
    highlightthickness=0
)
champ_texte.pack(padx=10, pady=10)
champ_texte.place(relx=0, rely=0, relwidth=1, relheight=1)

champ_texte.insert(tk.END, "zakaka>")
champ_texte.bind("<Return>", ajouter_prefixe)

fenetre.mainloop()
