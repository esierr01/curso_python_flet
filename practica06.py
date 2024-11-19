# Uso de Dropdown

import flet as ft


def main(page: ft.Page): 
    def button_clicked(e):
        output_text.value = f"El valor del Dropdown es: {color_dropdown.value}"
        page.update()


    output_text = ft.Text()
    submit_btn = ft.ElevatedButton(text="Submit", on_click=button_clicked)
    color_dropdown = ft.Dropdown(
        width=100,
        options=[
            ft.dropdown.Option("Rojo"),
            ft.dropdown.Option("Verde"),
            ft.dropdown.Option("Azul"),
        ],
    )
    page.add(color_dropdown, submit_btn, output_text)


ft.app(main)
