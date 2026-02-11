import pygame, librosa, random, os
from ui.utils.note import Note

class Piano:
    def __init__(self, gameview):
        self.__gameView = gameview
        self.__filepath = "./assets/music/" + self.__gameView.getWindowManager().getMusicSelect().lower().replace('play musique ', '').replace(' ', '').replace("'", '').replace(',', '') + ".mp3"
        self.__difficulty = 1
        
        # Check if file exists before trying to load
        if not os.path.exists(self.__filepath):
            print(f"Fichier musical non trouvé: {self.__filepath}")
            # Use a default fallback
            self.__filepath = "./assets/music/sunflower.mp3"
            if not os.path.exists(self.__filepath):
                print("Aucun fichier musical trouvé, utilisation de notes aléatoires")
                self.__notes = self.generate_random_notes()
                return
        
        try:
            self.__notes = self.generate_notes()
        except Exception as e:
            print(f"Erreur lors de la génération des notes: {e}")
            print("Utilisation de notes aléatoires à la place")
            self.__notes = self.generate_random_notes()

    def getNotes(self):
        return self.__notes

    def increaseDifficulty(self):
        self.__difficulty += 1

    def play(self):
        pygame.mixer.init()
        pygame.mixer.music.load(self.__filepath)
        pygame.mixer.music.play()

    def pause(self):
        pygame.mixer.music.pause()

    def generate_notes(self):
        print("Génération des notes à partir du fichier :", self.__filepath)
        notes = []

        try:
            # Charger le fichier en mono, à faible sample rate (optimisation mémoire)
            # Limiter la durée pour éviter les problèmes de mémoire
            y, sr = librosa.load(self.__filepath, sr=11025, mono=True, duration=30.0)  # Réduit à 11025 Hz et 30 secondes

            # Analyse du rythme
            tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
            beat_times = librosa.frames_to_time(beat_frames, sr=sr)

            for time in beat_times:
                nb_notes = min(self.__difficulty, random.randint(1, 4))
                for _ in range(nb_notes):
                    position = random.choice(["left", "middle", "right", "top"])
                    note = Note(gameview=self.__gameView, position=position, timestamp=time)
                    notes.append(note)

            print(f"{len(notes)} notes générées.")
            return notes
            
        except Exception as e:
            print(f"Erreur lors de l'analyse audio: {e}")
            raise e

    def generate_random_notes(self):
        """Génère des notes aléatoires quand l'analyse audio échoue"""
        print("Génération de notes aléatoires")
        notes = []
        
        # Générer environ 60 notes sur 30 secondes (une note toutes les 0.5 secondes)
        for i in range(60):
            time = i * 0.5  # Une note toutes les 0.5 secondes
            nb_notes = min(self.__difficulty, random.randint(1, 2))  # Moins de notes aléatoires
            
            for _ in range(nb_notes):
                position = random.choice(["left", "middle", "right", "top"])
                note = Note(gameview=self.__gameView, position=position, timestamp=time)
                notes.append(note)
        
        print(f"{len(notes)} notes aléatoires générées.")
        return notes

    def getCurrentTime(self):
        return pygame.mixer.music.get_pos() / 1000.0
