from modelos.tarea import Tarea
import json

# Clase que contiene la lógica del sistema
class TareaServicio:
    def __init__(self):
        self.tareas = []            # Lista de tareas
        self.contador_id = 1        # Generador de IDs

        # Cargar tareas guardadas
        self.cargar_tareas()

    def agregar_tarea(self, descripcion):
        tarea = Tarea(self.contador_id, descripcion)
        self.tareas.append(tarea)
        self.contador_id += 1
        self.guardar_tareas()

    def obtener_tareas(self):
        return self.tareas

    def completar_tarea(self, id):
        for tarea in self.tareas:
            if tarea.id == id:
                tarea.marcar_completada()
        self.guardar_tareas()

    def eliminar_tarea(self, id):
        self.tareas = [t for t in self.tareas if t.id != id]
        self.guardar_tareas()

    # ---------------------------
    # GUARDAR EN ARCHIVO JSON
    # ---------------------------
    def guardar_tareas(self):
        data = []
        for t in self.tareas:
            data.append({
                "id": t.id,
                "descripcion": t.descripcion,
                "completado": t.completado
            })

        with open("tareas.json", "w") as f:
            json.dump(data, f)

    # ---------------------------
    # CARGAR DESDE JSON
    # ---------------------------
    def cargar_tareas(self):
        try:
            with open("tareas.json", "r") as f:
                data = json.load(f)
                for item in data:
                    tarea = Tarea(item["id"], item["descripcion"])
                    tarea.completado = item["completado"]
                    self.tareas.append(tarea)
                    self.contador_id = max(self.contador_id, tarea.id + 1)
        except:
            pass