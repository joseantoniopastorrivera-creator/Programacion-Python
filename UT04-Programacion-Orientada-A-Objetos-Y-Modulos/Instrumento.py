from abc import ABC, abstractmethod


class Instrumento(ABC):

    @abstractmethod
    def afinar(self):
        pass

    @abstractmethod
    def tocar(self):
        pass


class Guitarra(Instrumento):
    def afinar(self):
        print("Tensando las cuerdas de la guitarra...")

    def tocar(self):
        print("Tocando las cuerdas de la guitarra...")


class Piano(Instrumento):
    def afinar(self):
        print("Afinando el piano con mucho cuidado...")

    def tocar(self):
        print("Tocando las teclas del piano...")


guitarra1 = Guitarra()
piano1 = Piano()

guitarra1.afinar()
guitarra1.tocar()
piano1.afinar()
piano1.tocar()

print("\n¡Que empiece el show!")
banda = [guitarra1, piano1]
for instrumento in banda:
    instrumento.afinar()
    instrumento.tocar()
    print("-" * 20)
