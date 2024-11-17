# Lista de tareas

import flet as ft

def main(page: ft.Page):
    page.bgcolor = ft.colors.BLUE_GREY_900
    page.title = "Mi Lista de Tareas"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    titulo = ft.Text(value="Mi Lista de Tareas con Flet", size=30, weight=ft.FontWeight.BOLD)

    # Funciones:
    def agregar_tarea(e):
        if campo_tarea.value:   # valido si la entrada de texto esta llena (hay algo escrito en el)
            tarea = ft.ListTile(title=ft.Text(campo_tarea.value), leading=ft.Checkbox(on_change=seleccionar_tarea))
            tareas.append(tarea)    # se agrega tarea a lista de tareas
            campo_tarea.value = ""
            actualizar_lista()

    def seleccionar_tarea(e):
        seleccionadas = [t.title.value for t in tareas if t.leading.value]  # lista por comprension, que selecciona solo las tareas seleccionadas
        tareas_seleccionadas.value = "Tareas seleccionadas: " + ", ". join(seleccionadas)   # para que se unan todos los elementos de lista (seleccionadas) con una coma
        page.update()

    def actualizar_lista():
        lista_tareas.controls.clear()   # limpiamos todos los controles de la lista (para limpiar listview)
        lista_tareas.controls.extend(tareas)    # añadimos todos los elementos de la lista tareas al listview
        page.update()       # actualizamos la página

    campo_tarea = ft.TextField(hint_text="Escribe una nueva tareas")         # Campo de entrada de texto
    boton_agregar = ft.FilledButton(text="Agregar tarea", on_click=agregar_tarea)

    lista_tareas = ft.ListView(expand=1, spacing=3)     # lista tareas, expand 1 (que va a hacer al expandirse, ej el eje vertical), si le coloco 0 no se expandería estas lista y la lista de tareas seleccionadas aparecería seguido, pero con 1 aparece al final

    tareas = []     # Lista de tareas vacias (inicial)
    tareas_seleccionadas = ft.Text(value="", size=20, weight=ft.FontWeight.BOLD)    # Lista de tareas seleccionadas (inicial)


    page.add(titulo, campo_tarea, boton_agregar, lista_tareas, tareas_seleccionadas)

ft.app(target=main)
