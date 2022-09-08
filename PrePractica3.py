from __future__ import annotations

class vehiculo:
    def __init__(self, marca: str, ruedas: int, color: str, enmarcha: bool, ) -> None:
        self.marca: str = marca
        self.ruedas: int= ruedas
        self.color: str= color
        self.enmarcha: bool= enmarcha
    
    
    def arrancar(self) -> bool:
        return self.enmarcha == True
    
    def tipovehiculo(self) -> str:
        if self.ruedas == 4:
            return "Automovil"
        elif self.ruedas==2:
            return "Motocicleta"
    
    
    def mostrar(self) -> None:
        return print(self.marca, self.ruedas, self.color, self.enmarcha)
