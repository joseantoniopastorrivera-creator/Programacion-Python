class PistaAudio:
#Constructor
    def __init__(self, titulo, artista, bpm, en_reproduccion):
        self.titulo=titulo
        self.artista=artista
        self.bpm=bpm
        self.en_reproduccion = False    
        
    #Método play    
    def play(self):
        self.en_reproduccion=True    
        print(f"Cargando el deck: {self.titulo} de {self.artista} a {self.bpm} BPM.")
        
#PRUEBAS
print("Iniciando software de mezclas..")

#Objetos de prueba
pista1 = PistaAudio("Bajo el Sol", "Kaiser", 138, False)
pista2 = PistaAudio("SUIT_99", "Carmen Electro", 142, False)

#LLamamos a los métodos
pista1.play()
pista2.play()        