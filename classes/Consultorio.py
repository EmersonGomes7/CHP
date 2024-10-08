from classes.Floresta import Floresta

class Consultorio:
    def __init__(self, id):
        self.id = id
        self.filas = [ None, None]
    

    def adicionar_paciente(self, paciente):
        if paciente.prioritario:
            if self.filas[0] == None:
                self.filas[0] = Floresta(paciente)
            else:
                self.filas[0].adicionar(paciente)
        else:
            if self.filas[1] == None:
                self.filas[1] = Floresta(paciente)
            else:
                self.filas[1].adicionar(paciente)


    def fechar_consultorio(self, consultorio):
        if self.filas[0] is not None:
            consultorio.filas[0].unir(self.filas[0].floresta)
        if self.filas[1] is not None:
            consultorio.filas[1].unir(self.filas[1].floresta)


    def atender(self):
        if len(self.filas[0].floresta) == None or len(self.filas[0].floresta) == 0 and (len(self.filas[1].floresta) != 0 or self.filas[1] is not None):
            return self.filas[1].atender()
        elif self.filas[0] != None and len(self.filas[0].floresta) != 0:
            return self.filas[0].atender()
    

    def imprimir(self):
            if self.filas[0] is not None or self.filas[1] is not None:
                for fila in self.filas:
                    if fila is not None:
                        fila.imprimirPacientes(self)
            else:
                print(f"Consultorio {self.id}:")


    def tamanho(self):
            if self.filas[0] is not None and self.filas[1] is not None:
                return self.filas[0].somatorio() + self.filas[1].somatorio()  
            elif self.filas[0] is not None:
                return self.filas[0].somatorio()
            elif self.filas[1] is not None:
                return self.filas[1].somatorio()
            
            return 0
        