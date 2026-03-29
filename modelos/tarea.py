# Modelo que representa una tarea

class Tarea:
    def __init__(self, id, descripcion):
        # ID único de la tarea
        self.id = id

        # Descripción escrita por el usuario
        self.descripcion = descripcion

        # Estado de la tarea (False = pendiente, True = completada)
        self.completado = False

    # Método para marcar la tarea como completada
    def marcar_completada(self):
        self.completado = True