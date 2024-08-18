import streamlit as st
from math import pi
import matplotlib.pyplot as plt
import numpy as np

# Utiliser des onglets pour la navigation
tab1, tab2, tab3 = st.tabs(["CV", "Projets", "Python"])

#######################
# PAGE CV

with tab1:
    st.write("")
    st.write("")
    st.title("HUGO DE COSTER")
    st.write("Mail : hugodecoster.hdc@gmail.com               Tel : 0470/56.39.60 ")
    st.write("")
    st.header("Profil")

    st.markdown(
    """
    Ingénieur civil architecte avec une expérience en bureaux d'études et une riche expértise sur le terrain en tant que charpentier et ferronnier. J'ai suivi un parcours atypique où mes intérêts privés nourrissent ma carrière. Du dévelloppement informatique à l'invention de structures innovantes en passant par l'enseignement, j'ai transformé chaque passion en compétence professionnelle. Je m'efforce d'apporter une valeur ajoutée à chaque mission en combinant expertise, créativité et engagement indéfectible.  <br><br>

    """,
    unsafe_allow_html=True
)
    
    col1, col2 = st.columns([2,4])

    # Contenu pour la colonne de gauche
    with col1:
            st.markdown(
    """
    <div style="text-align: left; font-weight: bold;">
        <u>COMPETENCES CLES </u> <br><br>
    </div>
    <div style="text-align: left; font-weight: bold;">
        • Création et enseignement de contenus techniques :
    </div>
     Développement de matériel pédagogique et enseignement. 

    <div style="text-align: left; font-weight: bold;">
        • Conception et calcul des structures :
    </div>
     Acord bat, Karamba 3D, Ancrage Profis Engineering Hilti, CLT designer
    
    <div style="text-align: left; font-weight: bold;">
       • Dessin :
    </div>
     AutoCAD, Rhino, Cadwork, Grasshopper (conception paramétrique) 
    <div style="text-align: left; font-weight: bold;">
        • Codage :
    </div>
       Python (programmation élémentaire pour le calcul et le traitement de données) <br><br>


    <div style="text-align: left; font-weight: bold;">
        <u>LANGUES </u> <br>
    </div>
        <br>• Français : Courant 
        <br>• Anglais : Niveau élémentaire, Lecture scientifique
        <br>• Néerlandais :  Niveau scolaire, en progression avec un focus sur l'acquisition du vocabulaire professionnel <br><br>

    <div style="text-align: left; font-weight: bold;">
        <u>INTERETS & PROJETS PERSONNELS </u> <br>
    </div>
        <br>• Calcul et modélisation relatif à l’énergétique du bâtiment, avec Grasshopper et python
        <br>• Gestion immobilière
        <br>• Organisation et gestion de projets 
        <br>• Organisation de cours de calcul des structures pour l'Association belge de charpente
        <br>• Réalisation d’une station de biométhanisation
        <br>• Conceptions paramétrique et réalisation de structure réciproque en bois rond 

 
    
    """,
    unsafe_allow_html=True
)
    with col2:


            # Ligne de séparation pour distinguer les colonnes
            #st.markdown("<hr style='border: 1px solid #e0e0e0;' />", unsafe_allow_html=True)
            st.markdown(
    """
    <div style="text-align: left; font-weight: bold;">
        <u>EXPERIENCES PROFESSIONNELLES</u>
    </div>
    <div style="text-align: left; font-weight: bold;">
         <br> Ingénieur structure :
    </div>
    Cambium| Bruxelles, Belgique |2023 – Présent <br>
    <br>• Bâtiment public : École Van Asbroeck, Bruxelles. Complexe scolaire Pablo Picasso, France (Multi étages et calcul au feu) 
    <br>• Maison unifamiliale : Dimensionnement et assemblages (CLT, ossature bois, acier) 
    <br>• Patrimoine : Château de Monceau sur Sambre (plans par nuage de points, diagnostic sanitaire et pré-étude stabilité) 
    <br>• Bâtiment hors norme : Structure sur pilotis (Walibi) 
    <br>• Concours avec architectes : Réflexion structurelle et prédimensionnement (marché publique)<br><br>

    <div style="text-align: left; font-weight: bold;">
         Enseignant :
    </div>
    Association Belge de Charpente | Brabant Wallon |2020 – 2021 <br>
    <br>• Conception et calcul des structures bois (cours du soir) 
    <br>• Traits de charpente (patrimoine culturel immatériel de l'humanité UNESCO) <br><br>

    <div style="text-align: left; font-weight: bold;">
         Ouvrier charpentier :
    </div>
    Elan Bois | Haute Savoie |2013 - 2014 <br>
    <br>• Extensions, constructions neuves et rénovations 
    <br>• Chef d’équipe <br><br>

    <div style="text-align: left; font-weight: bold;">
         Apprenti charpentier :
    </div>
    Gauthier Cargo | Saône et Loire | 2011 - 2012 <br>
    <br>• Construction neuve, rénovations de patrimoine et bâtiments publics <br><br>

    <div style="text-align: left; font-weight: bold;">
        <u>EDUCATION</u>
    </div>
    <div style="text-align: left; font-weight: bold;">
         <br> Diplôme d'Ingénieur civil architecte :
    </div>
    UCLouvain | 2018 - 2023 Mention : <br> Grande Distinction  <br>
    <div style="text-align: left; font-weight: bold;">
         <br> CAP Charpentier :
    </div>
    Compagnons du Devoir | 2012 - 2013: <br> 
    <div style="text-align: left; font-weight: bold;">
         <br> Autres formations :
    </div>
    <br>Monteur échafaudage : Alpes Contrôle |2013 
    <br>Ferronnerie : École de Maréchalerie, Bruxelles |2017-2018 
    <br>Agent immobilier (1ère année cours du soir) : IFAPME |2017-2018 
    <br>Gestion : IFAPME |2017 
 

    """,
    unsafe_allow_html=True
)

#######################
# PAGE PROJETS

with tab2:



    # Données pour les projets
    projets = [
        {
            "titre": "Projets stabilité",
            "photos": [
                {"path": "STR1.jpg", "description": "Complexe scolaire Pablo Picasso (France) : en cours."},
                {"path": "STR2.jpg", "description": "Château de Monceau sur Sambre : diagnostic sanitaire [nuage de points, analyse stabilité, mesures conservatoires]."},
                {"path": "STR3.jpg", "description": "Château de Monceau sur Sambre : diagnostic sanitaire [nuage de points, analyse stabilité, mesures conservatoires]."},
                {"path": "STR4.jpg", "description": "Dockworld Walibi : structures sur pilotis, conception et calcul des assemblages."},
                {"path": "STR5.jpg", "description": "Maisons unifamiliales : sections, assemblages, dessin."}
            ],
            "description": "En poste comme ingénieur stabilité chez CAMBIUM, voici quelques projets réalisés ou en cours."
        },
        {
            "titre": "Projets personnels",
            "photos": [
                {"path": "Perso1.jpg", "description": "Station de méthanisation: conception pratique avec étude des phénomènes et calcul de rendement."},
                {"path": "Perso2.jpg", "description": "Conception paramétrique pour structure réciproque en bois rond: création de gabarits pour tronçonneuses."},
                {"path": "Perso3.jpg", "description": "Exposition -Le bois dans la construction d'aujourd'hui et de demain- : L'exposition explique certains concepts  élémentaires et puis pose des questions sans réponses pour animer des discussions chez les visiteurs."},
                {"path": "Cours1.jpg", "description": "Cours de calcul des structures bois :développement de matériel pédagogique et enseignement."},
                {"path": "Cours2.jpg", "description": "Cours de trait de charpente : développement de matériel pédagogique et enseignement."},
                {"path": "Perso4.jpg", "description": "Aide à la conception et calcul de dimensionnement pour entreprise de charpente."},
                {"path": "Perso5.jpg", "description": "Aide à la conception et calcul de dimensionnement pour entreprise de charpente."}
                
            ],
            "description": "Les projets suivant ont été mennées en complément de mes études."
        },
        {
            "titre": "Projets scolaires",
            "photos": [
                {"path": "UCL1.jpg", "description": "Cours à options : sylviculture, anatomies du bois, architecture avec le bois et rénovation"},
                {"path": "UCL6.JPG", "description": "Structures arch, bois, acier et béton : Ces cours ont suscité un vif intérêt et un investissement personnel important."},
                {"path": "UCL2.jpg", "description": "Approche créative et technique pour chaque projet d'architecture : maquette de forme-finding"},
                {"path": "UCL7.JPG", "description": "Edification soutenable et parametrique designe : Ces cours ont suscité un vif intérêt et un investissement personnel important."},
                {"path": "UCL3.jpg", "description": "Approche créative et technique pour chaque projet d'architecture : Construction d'un Elliodome et analyse numérique"},
                {"path": "UCL4.jpg", "description": "Mémoire: disponible sur demande"},
                {"path": "UCL5.jpg", "description": "Aménagement d'un camion en habitation pour commencer mes études avec famille et enfants, permettant de vivre à moindre coût."}
            ],
            "description": "Quelques éléments particuliers de mon parcours étudiant."
        },

        {
            "titre": "Projets charpente - ferronnerie",
            "photos": [
                {"path": "Construction1.jpg", "description": "Gestion de chantier et chef d'équipe pour des projets d'extensions ou de maisons unifamiliales."},
                {"path": "Construction2.jpg", "description": "Réalisation d'outillages, escaliers, mains courantes...[TIG, MAG, ARC]"}
            ],
            "description": "Expériences de terrain."
        }
    ]

    # Afficher tous les projets
    for projet in projets:
        with st.expander(projet["titre"], expanded=False):
            st.write(projet["description"])
            for photo in projet["photos"]:
                st.image(photo["path"], caption=photo["description"],use_column_width=True)# width=300)






#######################
# PAGE PYHTON

with tab3:
    st.write("")
    # Créer une liste déroulante pour sélectionner la langue
    langue = st.selectbox('Choos a language', ['FR', 'NL', 'EN'])

    # Afficher la salutation dans la langue sélectionnée
    #st.title(salutations[langue])

    #st.header("Optimisation et analyse avec Python:")

    TitreP = {
        'FR': "Optimisation et analyse avec Python:",
        'NL': 'Optimalisatie en analyse met Python: ',
        'EN': 'Optimization and analysis with Python:'
    }
    # Titre de l'application
    Sous_Titre = {
        'FR': "Python est un langage puissant que j'utilise pour traiter des données, exécuter des tâches variées et créer des outils interactifs. Dans cet exemple, je montre comment il est possible d'expliquer un concept scientifique de manière vulgarisée avec python en posant la question :",
        'NL': 'Python is een krachtige taal die ik gebruik om gegevens te verwerken, diverse taken uit te voeren en interactieve tools te creëren. In dit voorbeeld laat ik zien hoe je met Python een wetenschappelijk concept op een toegankelijke manier kunt uitleggen door de vraag te stellen:',
        'EN': 'Python is a powerful language that I use to process data, perform various tasks, and create interactive tools. In this example, I demonstrate how Python can be used to explain a scientific concept in a simplified way by asking the question:'
    }

    Question = {
        'FR': " - Pourquoi l'épaisseur d'un isolant doit-elle prendre en compte l'ACV (Analyse de Cycle de Vie) pour minimiser la consommation d'énergie ? - ",
        'NL': '- Waarom moet de dikte van een isolatiemateriaal rekening houden met de levenscyclusanalyse (LCA) om het energieverbruik te minimaliseren? -',
        'EN': '- Why should the thickness of an insulation material consider Life Cycle Assessment (LCA) to minimize energy consumption? -'
    }
    #st.write(Sous_Titre [langue])
    # Récupérer le sous-titre dans la langue sélectionnée
    sous_titre_texte = Sous_Titre[langue]
    Question_texte = Question[langue]
    TitreP_texte = TitreP[langue]

    # Afficher le sous-titre en jaune ocre
    st.markdown(f'<p style="color:#666666; font-size: 35px; ">{TitreP_texte}</p>', unsafe_allow_html=True)#font-weight: bold;
    #st.markdown(f'<p style="color:#D4A017;">{TitreP_texte}</p>', unsafe_allow_html=True)    
    st.markdown(f'<p style="color:#D4A017;">{sous_titre_texte}</p>', unsafe_allow_html=True)
    st.markdown(f'<p style="text-align: center; font-weight: bold; color: #D4A017;">{Question_texte}</p>', unsafe_allow_html=True)

    #st.markdown('<p style="color:#D4A017;">Ce texte est en jaune ocre.</p>', unsafe_allow_html=True)

    # Ligne de séparation pour distinguer les colonnes
    st.markdown("<hr style='border: 1px solid #e0e0e0;' />", unsafe_allow_html=True)


    st.markdown(
    """

    <div style="text-align: center; font-weight: bold;">
        Exemple de déperdition thermique journalière à travers un isolant. <br><br>
    </div>
    """,
    unsafe_allow_html=True
)
    

    
    st.image("DeperditionJournaliere.jpg", caption="Schema de deperdition thermique", width=500 ) #use_column_width=True)

    st.write("En définissant un type d'isolant et une épaisseur, nous pouvons lire sur le graphique la déperdition thermique journalière en kWh/m² (couleur) pour une température intérieur (axe : X) et extérieure (axe : Y) connue.") 

    # Dictionnaire pour associer une valeur a isolant choisit par l utilisateur
    lbd = {
        'Laine de bois': 0.04,
        'Laine minerale': 0.035,
        'styrodure': 0.025
    }
#Densité kg/m³
    densite = {
        'Laine de bois': 75,
        'Laine minerale': 100,
        'styrodure': 40
    }
#Energie grise Mj/kg
    engG = {
        'Laine de bois': 26,
        'Laine minerale': 23,
        'styrodure': 100
    }


        # Créer deux colonnes
    col1, col2 = st.columns(2)

    # Contenu pour la colonne de gauche
    with col1:

        # Créer une liste déroulante pour sélectionner 
        isolant = st.selectbox('Choisir isolant', ['Laine de bois', 'Laine minerale', 'styrodure'])
        #saisie d'un nombre stocké dans la variable nb_input
        epaisseur = st.number_input("Saisissez l'épaisseur d'isolant en cm", value=5)
        st.write("Exemple")
        #Repérer un point 
        Temp_ext = st.number_input("Repérez une température extérieur", value=0, min_value=-10, max_value=15)
        Temp_int = st.number_input("Repérez une température intérieur", value=20, min_value=15, max_value=25)

    R = (1/8)+ (epaisseur/100)/lbd[isolant] + (1/23)
    #st.write ("R =", R)
    U = 1/R

    
    # Calculer les valeurs de energie journalière
    def calculXA1(Tint, Text):
        q = (1/R * (Tint-Text))/1000 #Flux kW/m²
        X = q * 24 # (kWH/m²/j) #######U*(Tint-Text)*24/10
        return X
    

    # Calculer les grilles de Spl et D en fonction de isolant selectionne
    Tint = np.arange(15, 25 , 1)
    Text = np.arange(-10, 16, 1)
    Tint, Text = np.meshgrid(Tint, Text)

    # Calculer X
    X = calculXA1(Tint, Text)
    Xi = calculXA1(Temp_int, Temp_ext)
    Xa = calculXA1(Temp_int, Temp_ext)

    # Créer le graphique
    fig, ax = plt.subplots()
    contour = ax.contourf(Tint, Text, X, cmap='coolwarm')#'coolwarm_r' pour inverser la palette de couleur
    fig.colorbar(contour, ax=ax)
    ax.set_xlabel('T int °C')
    ax.set_ylabel('T ext °C')
    ax.set_title('kWh/m² Journalier , \n(10 kWh = 1L de fuel)')
    plt.scatter(Temp_int, Temp_ext, color='red')  # Point rouge
    plt.text(Temp_int +0.5 , Temp_ext +0.5 , "Exemple", color='black', fontsize=12, verticalalignment='bottom')
    # Ajouter des lignes jusqu'au point, depuis les axes
    ax.plot([Temp_int, Temp_int], [ax.get_ylim()[0], Temp_ext], color='gray', linestyle='--')  # Ligne verticale grise
    ax.plot([ax.get_xlim()[0], Temp_int], [Temp_ext, Temp_ext], color='gray', linestyle='--')  # Ligne horizontale grise

    ax.contour(Tint, Text, X, levels=[0], colors='black')
    ax.contour(Tint, Text, X, levels=[1], colors='black')





    # Contenu pour la colonne de droite
    with col2:
    # Afficher le graphique dans Streamlit
        st.pyplot(fig)

        # Contrôler le nombre de chiffres après la virgule
        Temp_int_str = f"{Temp_int:.1f}"  # 1 chiffre après la virgule
        Temp_ext_str = f"{Temp_ext:.1f}"  # 1 chiffre après la virgule
        Xi_str = f"{Xi:.2f}"  # 2 chiffres après la virgule
        Fuel_str = f"{Xi * 10:.1f}"  #

        #st.write("Exemple")
        st.write("Exemple : Pour les températures données, l énergie qui s'échappe chaque jour à travers 1m² de parois  est de ", Xi_str, "kWH soit", Fuel_str , "cl de fuel ")

    # Ligne de séparation pour distinguer les colonnes
    st.markdown("<hr style='border: 1px solid #e0e0e0;' />", unsafe_allow_html=True)

    st.markdown(
    """

    <div style="text-align: center; font-weight: bold;">
        Exemple de déperdition thermique annuelle à travers un isolant. <br><br>
    </div>
    """,
    unsafe_allow_html=True
)

    st.image("DeperditionAnnuelle.jpg", caption="Schema de deperdition thermique", width=500 ) #use_column_width=True)
    st.write("Avec les moyennes de températures météorologique il est possible de définir une saison de chauffe type pour calculer les déperdidtions annuelle.")

    # Ligne de séparation pour distinguer les colonnes
    st.markdown("<hr style='border: 1px solid #e0e0e0;' />", unsafe_allow_html=True)

    st.markdown(
    """

    <div style="text-align: center; font-weight: bold;">
        Energie liée à l'ACV de l'isolant. <br><br>
    </div>
    """,
    unsafe_allow_html=True
)
    st.write ("L'énergie grise désigne la quantité totale d'énergie consommée lors des étapes du cycle de vie d'un produit. Il est possible d'estimer approximativement l energie necessaire pour produire et mettre en oeuvre 1m³ d'isolant.")       
        # Créer deux colonnes
    st.image("EnergieGrise.jpg", caption="Schema de deperdition thermique", width=500 ) #use_column_width=True)

    #Ligne de séparation 
    st.markdown("<hr style='border: 1px solid #e0e0e0;' />", unsafe_allow_html=True)
    st.markdown(
    """
    
    <div style="text-align: center; font-weight: bold;">
        Optimisation: <br><br>
        Énergie consommée = déperdition thermique annuelle x n° d'année + Énergie grise. <br><br>
    </div>
    """,
    unsafe_allow_html=True
)
    col1, col2 = st.columns(2)
    # Contenu pour la colonne de gauche
    with col1:

        # Créer une liste déroulante pour sélectionner 
        isolant2 = st.selectbox('Choisir isolant ', ['Laine de bois', 'Laine minerale', 'styrodure'])
        #saisie d'un nombre stocké dans la variable nb_input
        NbAnnee2 = st.number_input("Saisissez la durer de vie estimée de l'isolant en année", value=50)
        st.write("Exemple")
        epaisseur2 = st.slider("Saisissez l'épaisseur d'isolant en cm", min_value=1, max_value=50, value=15)#st.number_input("Saisissez l'épaisseur d'isolant en cm ", value=5)

    with col2: 

        # Générer des données pour le graphique
        engG1m2= densite[isolant2]* (epaisseur2/100)*engG[isolant2]/0.2778 # kg/m³ * m (*1m²) * Mj/kg = Mj = 0.2778 kWH
        x = np.linspace(3, 50, 100)
        y1 = densite[isolant2]* (x/100)*engG[isolant2]/0.2778 
        R1 = (1/8)+ (x/100)/lbd[isolant2] + (1/23)
        y2 = ((1/R1 * (20-6))/1000*24)*240*NbAnnee2 # energie journalière*nb année
        y = y1+y2
        
        #Point
        y1point = densite[isolant2]* (epaisseur2/100)*engG[isolant2]/0.2778 
        R1point = (1/8)+ (epaisseur2/100)/lbd[isolant2] + (1/23)
        y2point = ((1/R1point * (20-6))/1000*24)*240*NbAnnee2 # energie journalière*nb année
        ypoint=y1point+y2point
        xpoint=epaisseur2

        # Créer le graphique avec Matplotlib
        fig, ax = plt.subplots()
        ax.plot(x, y)
        ax.set_title(f"Energie total consomée sur {NbAnnee2:.0f} ans")
        ax.set_xlabel("Epaisseur d'isolant cm")
        ax.set_ylabel("Energie grise + déperdition kWh")
        plt.scatter(xpoint, ypoint, color='red')  # Point rouge
        plt.text(xpoint +0.5 , ypoint +0.5 , "Exemple", color='black', fontsize=12, verticalalignment='bottom')
        ax.plot([epaisseur2, epaisseur2 ], [0, y1point], color='gray', linestyle='-', linewidth=5, label="Portion d'énergie grise")
        ax.plot([epaisseur2, epaisseur2 ], [y1point, ypoint], color='orange', linestyle='-',linewidth=5, label="Portion d'energie de déperdition")
        ax.legend(loc='lower left')
        st.pyplot(fig)
        

######

    
    xpoint_str = f"{xpoint :.0f}"  #
    ypoint_str = f"{ypoint :.0f}"  #
    y1point_str = f"{y1point :.0f}"  #
    y2point_str = f"{y2point :.0f}"  #
    NbAnnee2_str = f"{NbAnnee2 :.0f}"  #

    st.write("Exemple : Pour l'isolant choisit d'épaisseur ", xpoint_str, "cm, et une durée de vie supposée de", NbAnnee2_str," ans, l'énergie total consommée se compose de", y1point_str , "kWh d'energie grise et de ", y2point_str,"kWh d'énergie de déperdition" )



