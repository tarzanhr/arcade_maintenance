import pygame
import os

class Image: 
    """La classe Image est une classe qui permet de recuperer l'image voulue grâce au getter."""
    class Page:
        """La classe Page est une classe qui permet de recuperer l'image voulue grâce au getter."""
        # Get the directory of the current file to build absolute paths
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        
        PROFIL = pygame.image.load(os.path.join(BASE_DIR, "assets", "img", "page", "ACCUEIL.png")) if os.path.exists(os.path.join(BASE_DIR, "assets", "img", "page", "ACCUEIL.png")) else None
        FILTRER = pygame.image.load(os.path.join(BASE_DIR, "assets", "img", "page", "ACCUEIL.png")) if os.path.exists(os.path.join(BASE_DIR, "assets", "img", "page", "ACCUEIL.png")) else None
        AIDE = pygame.image.load(os.path.join(BASE_DIR, "assets", "img", "page", "ACCUEIL.png")) if os.path.exists(os.path.join(BASE_DIR, "assets", "img", "page", "ACCUEIL.png")) else None
        DETAIL = pygame.image.load(os.path.join(BASE_DIR, "assets", "img", "page", "ACCUEIL.png")) if os.path.exists(os.path.join(BASE_DIR, "assets", "img", "page", "ACCUEIL.png")) else None
        PLAY = pygame.image.load(os.path.join(BASE_DIR, "assets", "img", "page", "ACCUEIL.png")) if os.path.exists(os.path.join(BASE_DIR, "assets", "img", "page", "ACCUEIL.png")) else None
        ACCUEIL = pygame.image.load(os.path.join(BASE_DIR, "assets", "img", "page", "ACCUEIL.png")) if os.path.exists(os.path.join(BASE_DIR, "assets", "img", "page", "ACCUEIL.png")) else None
        MULTIJOUEUR = pygame.image.load(os.path.join(BASE_DIR, "assets", "img", "page", "ACCUEIL.png")) if os.path.exists(os.path.join(BASE_DIR, "assets", "img", "page", "ACCUEIL.png")) else None
        STATISTIQUE = pygame.image.load(os.path.join(BASE_DIR, "assets", "img", "page", "ACCUEIL.png")) if os.path.exists(os.path.join(BASE_DIR, "assets", "img", "page", "ACCUEIL.png")) else None
        QUITTER = pygame.image.load(os.path.join(BASE_DIR, "assets", "img", "page", "ACCUEIL.png")) if os.path.exists(os.path.join(BASE_DIR, "assets", "img", "page", "ACCUEIL.png")) else None
        
    class Cover:
        """La classe Cover est une classe qui permet de recuperer la cover d'un album d'une musique."""
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        
        BLINDINGLIGHTS = pygame.image.load(os.path.join(BASE_DIR, "assets", "img", "music", "blindinglights.png")) if os.path.exists(os.path.join(BASE_DIR, "assets", "img", "music", "blindinglights.png")) else None
        SUNFLOWER = pygame.image.load(os.path.join(BASE_DIR, "assets", "img", "music", "sunflower.png")) if os.path.exists(os.path.join(BASE_DIR, "assets", "img", "music", "sunflower.png")) else None
        SWEATERWEATHER = pygame.image.load(os.path.join(BASE_DIR, "assets", "img", "music", "sweaterweather.png")) if os.path.exists(os.path.join(BASE_DIR, "assets", "img", "music", "sweaterweather.png")) else None
        BELIEVER = pygame.image.load(os.path.join(BASE_DIR, "assets", "img", "music", "believer.png")) if os.path.exists(os.path.join(BASE_DIR, "assets", "img", "music", "believer.png")) else None