import tkinter as tk
from tkinter import messagebox

# Función para añadir tarea
def add_task(event=None):
    task = task_entry.get()
    if task:
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "La tarea no puede estar vacía.")

# Función para marcar tarea como completada
def complete_task(event=None):
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        task_text = tasks_listbox.get(selected_task_index)
        if not task_text.startswith("[Completada]"):
            tasks_listbox.delete(selected_task_index)
            tasks_listbox.insert(selected_task_index, "[Completada] " + task_text)
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para marcar como completada.")

# Función para eliminar tarea
def delete_task(event=None):
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar.")

# Función para cerrar la aplicación
def close_app(event=None):
    root.quit()

# Configuración de la ventana principal
root = tk.Tk()
root.title("Gestor de Tareas Pendientes")
root.geometry("400x400")

# Campo de entrada para añadir nuevas tareas
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

# Botones
add_button = tk.Button(root, text="Añadir Tarea", command=add_task)
add_button.pack(pady=5)

complete_button = tk.Button(root, text="Marcar como Completada", command=complete_task)
complete_button.pack(pady=5)

delete_button = tk.Button(root, text="Eliminar Tarea", command=delete_task)
delete_button.pack(pady=5)

# Lista de tareas
tasks_listbox = tk.Listbox(root, width=50, height=15)
tasks_listbox.pack(pady=10)

# Asignación de atajos de teclado
root.bind('<Return>', add_task)  # Añadir tarea con "Enter"
root.bind('<c>', complete_task)   # Marcar tarea con "C"
root.bind('<d>', delete_task)     # Eliminar tarea con "D"
root.bind('<Delete>', delete_task) # También con "Delete"
root.bind('<Escape>', close_app)  # Cerrar aplicación con "Escape"

# Bucle principal de la aplicación
root.mainloop()