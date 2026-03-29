import tkinter as tk
from tkinter import messagebox
from servicios.tarea_servicio import TareaServicio

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas PRO")
        self.root.geometry("400x500")
        self.root.configure(bg="#f0f4f7")

        # Servicio (lógica)
        self.servicio = TareaServicio()

        # ---------------------------
        # ENTRY
        # ---------------------------
        self.entry = tk.Entry(root, width=30, font=("Arial", 12))
        self.entry.pack(pady=10)

        # Evento ENTER
        self.entry.bind("<Return>", self.agregar_evento)

        # ---------------------------
        # BOTONES
        # ---------------------------
        tk.Button(root, text="Añadir", bg="#4CAF50", fg="white",
                  command=self.agregar_tarea).pack(pady=5)

        tk.Button(root, text="Completar", bg="#2196F3", fg="white",
                  command=self.completar_tarea).pack(pady=5)

        tk.Button(root, text="Eliminar", bg="#f44336", fg="white",
                  command=self.eliminar_tarea).pack(pady=5)

        # ---------------------------
        # LISTA
        # ---------------------------
        self.lista = tk.Listbox(root, width=40, height=15)
        self.lista.pack(pady=10)

        # Evento doble clic
        self.lista.bind("<Double-1>", self.completar_evento)

        # Evento tecla DELETE
        self.root.bind("<Delete>", self.eliminar_evento)

        self.actualizar_lista()

    # ---------------------------
    def agregar_tarea(self):
        texto = self.entry.get()

        if texto:
            self.servicio.agregar_tarea(texto)
            self.entry.delete(0, tk.END)
            self.actualizar_lista()
            messagebox.showinfo("Info", "Tarea agregada")

    def agregar_evento(self, event):
        self.agregar_tarea()

    # ---------------------------
    def actualizar_lista(self):
        self.lista.delete(0, tk.END)

        for tarea in self.servicio.obtener_tareas():
            estado = "✔" if tarea.completado else "✗"
            self.lista.insert(tk.END, f"{estado} {tarea.id}. {tarea.descripcion}")

            if tarea.completado:
                self.lista.itemconfig(tk.END, fg="gray")

    # ---------------------------
    def obtener_id(self):
        seleccion = self.lista.curselection()
        if seleccion:
            texto = self.lista.get(seleccion[0])
            return int(texto.split(".")[0].split()[-1])
        return None

    # ---------------------------
    def completar_tarea(self):
        id_tarea = self.obtener_id()
        if id_tarea:
            self.servicio.completar_tarea(id_tarea)
            self.actualizar_lista()

    def completar_evento(self, event):
        self.completar_tarea()

    # ---------------------------
    def eliminar_tarea(self):
        id_tarea = self.obtener_id()
        if id_tarea:
            self.servicio.eliminar_tarea(id_tarea)
            self.actualizar_lista()

    def eliminar_evento(self, event):
        self.eliminar_tarea()