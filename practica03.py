# Ejemplo inicio de lista de tareas

import flet as ft


def main(page: ft.Page):
    page.bgcolor = ft.colors.BLUE_GREY_700
    def add_clicked(e):
        if (new_task.value):
            page.add(ft.Checkbox(label=new_task.value))
            new_task.value = ""
            new_task.focus()
            new_task.update()
        else:
            new_task.error_text = "Por favor inserte tarea"
            page.update()
    
    def muta(e):
        if texto.value == "Cambio el Pivote":
            texto.value = "Texto pivote"
        else:
            texto.value = "Cambio el Pivote"
        page.update()

    def visible(e):
        if texto.color == ft.colors.BLUE_400:
            texto.color = ft.colors.RED_300
        else:
            texto.color = ft.colors.BLUE_400
        page.update()

    new_task = ft.TextField(label="Que estas necesitando?", width=300)  # el hint_text es como un place_holder
    page.add(ft.Row([new_task, ft.ElevatedButton("Add", on_click=add_clicked), ft.ElevatedButton("Pivote", on_click=muta), ft.ElevatedButton("Cambia el color Pivote", on_click=visible)]))
    texto = ft.Text(value="Texto pivote", size=22)
    page.add(texto)


ft.app(main)
