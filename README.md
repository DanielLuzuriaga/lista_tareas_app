# 📝 Lista de Tareas - Aplicación GUI con Tkinter

## 📌 Descripción del Proyecto
Mi proyecto consiste en el desarrollo de una aplicación de escritorio para la gestión de tareas (To-Do List), implementada en Python utilizando la biblioteca Tkinter. La aplicación permite al usuario interactuar de forma sencilla para organizar sus actividades diarias mediante una interfaz gráfica intuitiva.

## 🎯 Objetivo
Desarrollar una aplicación GUI que implemente arquitectura modular por capas, manejo de eventos de teclado y ratón, separación entre lógica de negocio e interfaz, y generación de un ejecutable con PyInstaller.

## 🧠 Arquitectura del Sistema
El proyecto sigue una estructura modular organizada en capas:

lista_tareas_app/
├── main.py  
├── modelos/  
│   └── tarea.py  
├── servicios/  
│   └── tarea_servicio.py  
└── ui/  
    └── app_tkinter.py  

### 🔹 Descripción de capas
- Modelos: Representa la estructura de los datos  
- Servicios: Contiene la lógica del sistema  
- UI: Maneja la interfaz gráfica  
- Main: Punto de entrada del programa  

## ⚙️ Funcionalidades
- Agregar tareas  
- Visualizar tareas  
- Marcar tareas como completadas  
- Eliminar tareas  
- Actualización visual del estado  

## 🖱️ Manejo de Eventos
- Enter → Añadir tarea  
- Doble clic → Marcar como completada  
- Delete → Eliminar tarea  

## 🎨 Interfaz Gráfica
La interfaz fue desarrollada con Tkinter e incluye un campo de entrada, botones de acción y una lista de tareas. Además, presenta cambios visuales cuando una tarea es completada.

## ▶️ Ejecución del Proyecto
Abrir terminal en la carpeta del proyecto y ejecutar:

python main.py

## 📦 Generación del Ejecutable
El ejecutable se generó utilizando PyInstaller con el siguiente comando:

pyinstaller --noconsole --onefile --name ListaTareas main.py

Esto genera el archivo:

dist/ListaTareas.exe

## ⚠️ Consideraciones
El ejecutable puede ser detectado como falso positivo por algunos antivirus debido al empaquetado con PyInstaller.

## 📸 Evidencia
Se incluyen capturas de la aplicación en ejecución, del código fuente y del archivo ejecutable.

## 👨‍💻 Autor
Daniel Luzuriaga

## 🚀 Tecnologías Utilizadas
Python 3  
Tkinter  
PyInstaller  
Git  
GitHub  

## 📚 Conclusión
Este proyecto demuestra la aplicación de buenas prácticas en el desarrollo de software, incluyendo la separación de responsabilidades, el uso de eventos en interfaces gráficas y la generación de ejecutables para distribución.