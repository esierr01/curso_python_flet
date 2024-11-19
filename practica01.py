# Controles básicos, estructura inicial

import time
import flet as ft


def main(page: ft.Page):
    page.window_icon = "./assets/python.ico"
    # aqui muestro dos etiquetas
    t1 = ft.SafeArea(ft.Text("Hello, Flet!"))   # Control de Texto Básico, sin consideraciones de diseño
    t2 = ft.Text(value="Hello, world!", color="green")  # Texto Dentro de SafeArea, el texto se ajustara a la pantalla
    page.add(t1, t2)

    # se crea una etiqueta, que va contando
    t = ft.Text()   # elemento etiqueta vacia
    page.add(t) # agrega la etiqueta vacia en pantalla
    for i in range(3):     # ciclo for
        t.value = f"Step {i}"   # llena el valor del elemento con f-string Step #
        page.update()       # actualiza página
        time.sleep(1)       # detiene todo 1 segundo

    # control contenedor
    page.add(
        ft.Column(controls=[    # si coloca Column, coloca los textos en columna, si coloca Row, los coloca en fila
            ft.Text("A"),
            ft.Text("B"),
            ft.Text("C")
        ])
    )

    # TextField y ElevatedButton
    page.add(
        ft.Row(controls=[
            ft.TextField(label="Your name"),
            ft.ElevatedButton(text="Say my name!")
        ])
    )

    for i in range(5):
        page.controls.append(ft.Text(f"Line {i}"))
        if i > 2:
            page.controls.pop(0)
        page.update()
        time.sleep(0.3)

    # uso de boton, llamando a función
    def button_clicked(e):
        page.add(ft.Text("Presiono el botón!"))

    page.add(ft.ElevatedButton(text="Click me", on_click=button_clicked))


ft.app(main)
