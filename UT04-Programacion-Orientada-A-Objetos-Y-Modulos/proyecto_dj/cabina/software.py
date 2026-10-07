class TraktorPRO:
    def __init__(self, salida_audio):
        self.salida_audio=salida_audio
        
    def mezclar (self, pista):
        self.pista=pista
        print(f"TraktorPRO procesando la pista: {self.pista}.")
        self.salida_audio.reproducir(pista)    